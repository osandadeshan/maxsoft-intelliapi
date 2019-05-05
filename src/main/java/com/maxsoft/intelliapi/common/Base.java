package com.maxsoft.intelliapi.common;

/**
 * Project Name : MaxSoft-IntelliAPI
 * Developer    : Osanda Deshan
 * Version      : 1.0.0
 * Date         : 6/30/2018
 * Time         : 3:51 PM
 * Description  :
 **/

import com.jayway.jsonpath.Configuration;
import com.jayway.jsonpath.JsonPath;
import com.jayway.jsonpath.PathNotFoundException;
import com.maxsoft.intelliapi.api.Endpoints;
import com.maxsoft.intelliapi.util.fileoperator.Csv;
import com.maxsoft.intelliapi.util.fileoperator.TextFile;
import com.maxsoft.intelliapi.util.reader.ApiDocument;
import com.maxsoft.intelliapi.util.table.Board;
import com.maxsoft.intelliapi.util.table.StringTable;
import com.maxsoft.intelliapi.util.datetime.EpochTime;
import com.opencsv.CSVWriter;
import com.thoughtworks.gauge.Gauge;
import com.thoughtworks.gauge.datastore.DataStore;
import com.thoughtworks.gauge.datastore.DataStoreFactory;
import io.restassured.RestAssured;
import io.restassured.http.ContentType;
import io.restassured.http.Header;
import io.restassured.http.Headers;
import io.restassured.response.Response;
import io.restassured.specification.RequestSpecification;
import org.json.JSONException;
import org.json.simple.JSONArray;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;
import org.testng.Assert;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.concurrent.TimeUnit;
import java.util.logging.FileHandler;
import java.util.logging.Logger;
import java.util.logging.SimpleFormatter;
import static com.maxsoft.intelliapi.common.Base.BodyType.JSON;
import static io.restassured.RestAssured.given;
import static io.restassured.config.EncoderConfig.encoderConfig;


public class Base {

    private static final String DEV = "dev";
    private static final String QA = "qa";
    private static final String UAT = "uat";
    private static final String PROD = "prod";

    public String AUTHORIZATION_HEADER_NAME = System.getenv("header_name_for_authorization");
    public String AUTHENTICATION_FIRST_VALUE = System.getenv("authentication_first_value");
    public static String CURRENT_DIRECTORY = System.getProperty("user.dir");
    public String ACCESS_TOKEN_FILE_PATH = CURRENT_DIRECTORY + File.separator + System.getenv("access_token_file_path");
    public static String INTELLIAPI_LOGS_FILE_PATH = CURRENT_DIRECTORY + File.separator + "logs" + File.separator + "intelliapi.log";
    public static String ENVIRONMENT = System.getenv("environment");
    public static String OS = System.getProperty("os.name");
    public String baseUrl = setBaseUrl();

    private Response response;
    private RequestSpecification request = getRequestSpecification();
    private static Csv csv = new Csv();
    Map<String, String> formParams = new HashMap<>();

    private static Logger logger = Logger.getLogger(Base.class.getName());
    private static FileHandler fileHandler;
    private static SimpleFormatter formatter = new SimpleFormatter();

    static {
        try {
            fileHandler = new FileHandler(INTELLIAPI_LOGS_FILE_PATH, true);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }


    public static String getFirstCharacter(String string){
        return string.substring(0, 1);
    }

    public static String getLastCharacter(String string){
        return string.substring(string.length() - 1);
    }

    public static String setStringLastCharInverseToFirstChar(String string){
        if (!(string.equals(""))) {
            String firstChart = "";
            String inverseOfLastChart = "";
            if (getLastCharacter(string).equals("}")) {
                inverseOfLastChart = "{";
                firstChart = "{\n";
                if (!(inverseOfLastChart.equals(getFirstCharacter(string)))) {
                    return firstChart + string;
                }
            } else if (getLastCharacter(string).equals("]")) {
                inverseOfLastChart = "[";
                firstChart = "[\n";
                if (!(inverseOfLastChart.equals(getFirstCharacter(string)))) {
                    return firstChart + string;
                }
            }
            return string;
        } else {
            return string;
        }
    }

    public static void printInfo(String text){
        logger.addHandler(fileHandler);
        fileHandler.setFormatter(formatter);
        logger.info(text +"\n");
        Gauge.writeMessage(text);
    }

    public static void printWarning(String text){
        logger.addHandler(fileHandler);
        fileHandler.setFormatter(formatter);
        logger.warning(text +"\n");
        Gauge.writeMessage(text);
    }

    public static void printRequest(String request) {
        printInfo("Request is: " + "\n" + request);
    }

    public String setBaseUrl() {
        String baseUrl = "";
        if (ENVIRONMENT == null) {
            Assert.fail("Please add \"environment\" in the environment property file and assign an environment QA|DEV|UAT|PROD");
        }
        switch (ENVIRONMENT.toLowerCase()) {
            case DEV:
                baseUrl = System.getenv("dev_environment_base_url");
                break;
            case QA:
                baseUrl = System.getenv("qa_environment_base_url");
                break;
            case UAT:
                baseUrl = System.getenv("uat_environment_base_url");
                break;
            case PROD:
                baseUrl = System.getenv("prod_environment_base_url");
                break;
            default:
                Assert.fail("Please assign an valid environment QA|DEV|UAT|PROD for \"environment\" in the environment property file");
                break;
        }
        if (baseUrl == null) {
            baseUrl = "";
        }
        return baseUrl;
    }

    public String getAPIDocumentFilePath() {
        String apiDocPath = "";
        if (ENVIRONMENT == null) {
            Assert.fail("Please add \"environment\" in the property file and assign an environment QA|DEV|UAT|PROD");
        }
        switch (ENVIRONMENT.toLowerCase()) {
            case DEV:
                apiDocPath = System.getenv("dev_api_document_path");
                break;
            case QA:
                apiDocPath = System.getenv("qa_api_document_path");
                break;
            case UAT:
                apiDocPath = System.getenv("uat_api_document_path");
                break;
            case PROD:
                apiDocPath = System.getenv("prod_api_document_path");
                break;
            default:
                Assert.fail("Please assign an valid environment QA|DEV|UAT|PROD for \"environment\" in the property file");
                break;
        }
        if (apiDocPath == null) {
            apiDocPath = "";
        }
        return CURRENT_DIRECTORY + File.separator + apiDocPath;
    }

    public String getCurrentTimestamp(String timestampPattern){
        return new SimpleDateFormat(timestampPattern).format(new Date());
    }

    public void replaceAllColumnValuesToTimestamps(String filePath, String columnName, String timestampPattern) throws IOException {
        for(int i = 1; i<= csv.getLinesCount(filePath); i++){
            csv.updateCSVByRowIndexAndColumnIndex(filePath, getCurrentTimestamp(timestampPattern), i,
                    csv.getColumnIndexByColumnName(filePath, columnName));
        }
    }

    public static String getSavedValueForScenario(String variableNameOfValueStoredInDataStore) {
        try {
            // Fetching Value from the Data Store
            DataStore scenarioStore = DataStoreFactory.getScenarioDataStore();
            String value = (String) scenarioStore.get(variableNameOfValueStoredInDataStore);
            return value;
        } catch (Exception ex) {
            printWarning("Failed to read the text inside Scenario Data Store [" + variableNameOfValueStoredInDataStore + "]\n" + ex.getMessage());
            return "";
        }
    }

    public static String getSavedValueForSpecification(String variableNameOfValueStoredInDataStore) {
        try {
            // Fetching Value from the Data Store
            DataStore specDataStore = DataStoreFactory.getSpecDataStore();
            String value = (String) specDataStore.get(variableNameOfValueStoredInDataStore);
            return value;
        } catch (Exception ex) {
            printWarning("Failed to read the text inside Specification Data Store [" + variableNameOfValueStoredInDataStore + "]\n" + ex.getMessage());
            return "";
        }
    }

    public static void saveValueForScenario(String variableNameOfValueToBeStoredInDataStore, String valueToBeStoredInDataStore) {
        try {
            // Adding value to the Data Store
            DataStore scenarioStore = DataStoreFactory.getScenarioDataStore();
            scenarioStore.put(variableNameOfValueToBeStoredInDataStore, valueToBeStoredInDataStore);
        } catch (Exception ex) {
            printWarning("\"" + valueToBeStoredInDataStore + "\" is failed to save as a text in Scenario Data Store [" + variableNameOfValueToBeStoredInDataStore + "]\n" + ex.getMessage());
        }
    }

    public static void saveValueForSpecification(String variableNameOfValueToBeStoredInDataStore, String valueToBeStoredInDataStore) {
        try {
            // Adding value to the Data Store
            DataStore specDataStore = DataStoreFactory.getSpecDataStore();
            specDataStore.put(variableNameOfValueToBeStoredInDataStore, valueToBeStoredInDataStore);
        } catch (Exception ex) {
            printWarning("\"" + valueToBeStoredInDataStore + "\" is failed to save as a text in Specification Data Store [" + variableNameOfValueToBeStoredInDataStore + "]\n" + ex.getMessage());
        }
    }

    public static String getScenarioDataStoreValue(String variableNameOfValueStoredInDataStore) {
        try {
            // Fetching Value from the Data Store
            DataStore scenarioStore = DataStoreFactory.getScenarioDataStore();
            String value = (String) scenarioStore.get(variableNameOfValueStoredInDataStore);
            printInfo("Text inside Scenario Data Store [" + variableNameOfValueStoredInDataStore + "] is: \"" + value + "\"" + "\n\n");
            return value;
        } catch (Exception ex) {
            printWarning("Failed to read the text inside Scenario Data Store [" + variableNameOfValueStoredInDataStore + "]" + "\n\n");
            return "";
        }
    }

    public static String getSpecificationDataStoreValue(String variableNameOfValueStoredInDataStore) {
        try {
            // Fetching Value from the Data Store
            DataStore specDataStore = DataStoreFactory.getSpecDataStore();
            String value = (String) specDataStore.get(variableNameOfValueStoredInDataStore);
            printInfo("Text inside Specification Data Store [" + variableNameOfValueStoredInDataStore + "] is: \"" + value + "\"" + "\n\n");
            return value;
        } catch (Exception ex) {
            printWarning("Failed to read the text inside Specification Data Store [" + variableNameOfValueStoredInDataStore + "]" + "\n\n");
            return "";
        }
    }

    public static String getSuiteDataStoreValue(String variableNameOfValueStoredInDataStore) {
        try {
            // Fetching Value from the Data Store
            DataStore suiteStore = DataStoreFactory.getSuiteDataStore();
            String value = (String) suiteStore.get(variableNameOfValueStoredInDataStore);
            printInfo("Text inside Suite Data Store [" + variableNameOfValueStoredInDataStore + "] is: \"" + value + "\"" + "\n\n");
            return value;
        } catch (Exception ex) {
            printWarning("Failed to read the text inside Suite Data Store [" + variableNameOfValueStoredInDataStore + "]" + "\n\n");
            return "";
        }
    }

    public static void saveToScenarioDataStore(String variableNameOfValueToBeStoredInDataStore, String valueToBeStoredInDataStore) {
        try {
            // Adding value to the Data Store
            DataStore scenarioStore = DataStoreFactory.getScenarioDataStore();
            scenarioStore.put(variableNameOfValueToBeStoredInDataStore, valueToBeStoredInDataStore);
            printInfo("\"" + valueToBeStoredInDataStore + "\" is successfully saved as a text in Scenario Data Store [" + variableNameOfValueToBeStoredInDataStore + "]");
        } catch (Exception ex) {
            printWarning("\"" + valueToBeStoredInDataStore + "\" is failed to save as a text in Scenario Data Store [" + variableNameOfValueToBeStoredInDataStore + "]");
        }
    }

    public static void saveToSpecificationDataStore(String variableNameOfValueToBeStoredInDataStore, String valueToBeStoredInDataStore) {
        try {
            // Adding value to the Data Store
            DataStore specDataStore = DataStoreFactory.getSpecDataStore();
            specDataStore.put(variableNameOfValueToBeStoredInDataStore, valueToBeStoredInDataStore);
            printInfo("\"" + valueToBeStoredInDataStore + "\" is successfully saved as a text in Specification Data Store [" + variableNameOfValueToBeStoredInDataStore + "]");
        } catch (Exception ex) {
            printWarning("\"" + valueToBeStoredInDataStore + "\" is failed to save as a text in Specification Data Store [" + variableNameOfValueToBeStoredInDataStore + "]");
        }
    }

    public static void saveToSuiteDataStore(String variableNameOfValueToBeStoredInDataStore, String valueToBeStoredInDataStore) {
        try {
            // Adding value to the Data Store
            DataStore suiteStore = DataStoreFactory.getSuiteDataStore();
            suiteStore.put(variableNameOfValueToBeStoredInDataStore, valueToBeStoredInDataStore);
            printInfo("\"" + valueToBeStoredInDataStore + "\" is successfully saved as a text in Suite Data Store [" + variableNameOfValueToBeStoredInDataStore + "]");
        } catch (Exception ex) {
            printWarning("\"" + valueToBeStoredInDataStore + "\" is failed to save as a text in Suite Data Store [" + variableNameOfValueToBeStoredInDataStore + "]");
        }
    }

    public void saveToDataStore(String dataStoreType, String variableName, String valueToBeStored){
        switch (dataStoreType.toLowerCase()){
            case "spec":
                saveToSpecificationDataStore(variableName, valueToBeStored);
                break;
            case "specification":
                saveToSpecificationDataStore(variableName, valueToBeStored);
                break;
            case "scenario":
                saveToScenarioDataStore(variableName, valueToBeStored);
                break;
            case "suite":
                saveToSuiteDataStore(variableName, valueToBeStored);
                break;
            default:
                Assert.fail("Please provide a valid data store type");
        }
    }

    public String readFromDataStore(String dataStoreType, String variableName){
        String value = "";
        switch (dataStoreType.toLowerCase()){
            case "spec":
                value = getSpecificationDataStoreValue(variableName);
                break;
            case "specification":
                value = getSpecificationDataStoreValue(variableName);
                break;
            case "scenario":
                value = getScenarioDataStoreValue(variableName);
                break;
            case "suite":
                value = getSuiteDataStoreValue(variableName);
                break;
            default:
                Assert.fail("Please provide a valid data store type");
        }
        return value;
    }

    public RequestSpecification getRequestSpecification() {
        return RestAssured.given().contentType(ContentType.JSON);
    }

    public void printTestingEnvironmentName() {
        printInfo("Environment: " + ENVIRONMENT.toUpperCase());
    }

    public void printTestingEnvironmentURL() {
        printInfo("Base URL: " + baseUrl);
    }

    public void printTestingEnvironmentOS() {
        printInfo("Operating System: " + OS);
    }

    public void testingEnvDetails() {
        printInfo("Configurations of Test Execution Environment\n\n");
        printTestingEnvironmentOS();
        printTestingEnvironmentName();
        printTestingEnvironmentURL();
    }

    public void printApiEndpoint(String apiEndpoint) {
        printInfo("API Endpoint is: " + "\n" + apiEndpoint + "\n\n");
    }

    public void printHttpMethod(String apiEndpoint) throws IOException {
        printInfo("HTTP Method is: " + ApiDocument.getHttpMethod(apiEndpoint) + "\n\n");
    }

    public void printResponse() {
        String response = setStringLastCharInverseToFirstChar(getSavedValueForScenario("response"));
        if (response.equals("")) {
            printInfo("Response is Empty" + "\n\n");
        } else {
            printInfo("Response is: " + "\n" + response + "\n\n");
        }
    }

    public void printResponseTime(){
        printInfo("Response Time is: " + response.getTimeIn(TimeUnit.MILLISECONDS) + "ms" + "\n\n");
    }

    public void printResponseHeaders() {
        printInfo("Response Headers are: \n" + response.getHeaders().toString());
    }

    public void apiToBeInvoked(String apiEndpointName) throws IOException {
        saveValueForScenario("apiName", apiEndpointName);
        // Print API Endpoint
        printApiEndpoint(Endpoints.getApiEndpointByName(apiEndpointName));
        printHttpMethod(apiEndpointName);
    }

    public String getQueryParams() {
        String queryParams = String.valueOf(getSavedValueForScenario("queryParams"));
        if (queryParams.equals("") || queryParams.equals("null")) {
            queryParams = "";
        }
        return queryParams;
    }

    public String getPathParams() {
        String pathParams = String.valueOf(getSavedValueForScenario("pathParams"));
        if (pathParams.equals("") || pathParams.equals("null")) {
            pathParams = "";
        }
        return pathParams;
    }

    public String getApiEndpointToBeInvoked() throws IOException {
        String invokingEndpoint = getSavedValueForScenario("invokingEndpoint");
        String apiName = getSavedValueForScenario("apiName"); // Fetching Value from the Data Store
        if (invokingEndpoint == null || invokingEndpoint.equals("")){
            invokingEndpoint = baseUrl.concat(Endpoints.getApiEndpointByName(apiName)).
                    concat(getPathParams().concat(getQueryParams()));
        } else {
            invokingEndpoint = baseUrl.concat(invokingEndpoint)
                    .concat(getPathParams().concat(getQueryParams()));
        }
        printInfo("Invoked API Endpoint: \n" + invokingEndpoint + "\n\n");
        printHttpMethod(apiName);
        return invokingEndpoint;
    }

    public void setScenarioDataStoreEmpty(String dataStoreName){
        saveValueForScenario(dataStoreName, "");
    }

    public void setInvokingApiEndpointEmpty(){
        setScenarioDataStoreEmpty("apiName");
        setScenarioDataStoreEmpty("invokingEndpoint");
        setScenarioDataStoreEmpty("pathParams");
        setScenarioDataStoreEmpty("queryParams");
    }

    public void postAPIWithAuthMultipleHeaders(String jsonPayload, String accessToken, List<Header> headerList) throws IOException {
        String invokingEndpoint = getApiEndpointToBeInvoked();
        Headers headers = new Headers(headerList);
        // Executing API and getting the response
        if (accessToken == null) {
            response = given()
                    .contentType("application/json")
                    .headers(headers)
                    .body(jsonPayload)
                    .when()
                    .post(invokingEndpoint);
        } else {
            response = given()
                    .contentType("application/json")
                    .header(AUTHORIZATION_HEADER_NAME, accessToken) //Some API contains access token to run with the API
                    .headers(headers)
                    .body(jsonPayload)
                    .when()
                    .post(invokingEndpoint);
        }
        getStatusCode();
        getResponse();
        printResponseTime();
        printResponse();
        printResponseHeaders();
        setInvokingApiEndpointEmpty();
        headerList.clear();
    }

    public void getAPIWithAuthMultipleHeaders(String accessToken, List<Header> headerList) throws IOException {
        String invokingEndpoint = getApiEndpointToBeInvoked();
        Headers headers = new Headers(headerList);
        if (accessToken == null) {
            response = request
                    .given()
                    .headers(headers)
                    .when()
                    .get(invokingEndpoint);
        } else {
            response = request
                    .given()
                    .header(AUTHORIZATION_HEADER_NAME, accessToken) //Some API contains access token to run with the API
                    .headers(headers)
                    .when()
                    .get(invokingEndpoint);
        }
        getStatusCode();
        getResponse();
        printResponseTime();
        printResponse();
        printResponseHeaders();
        setInvokingApiEndpointEmpty();
        headerList.clear();
    }

    public void putAPIWithAuthMultipleHeaders(String jsonPayload, String accessToken, List<Header> headerList) throws IOException {
        String invokingEndpoint = getApiEndpointToBeInvoked();
        Headers headers = new Headers(headerList);
        // Executing API and getting the response
        if (accessToken == null) {
            response = given()
                    .contentType("application/json")
                    .headers(headers)
                    .body(jsonPayload)
                    .when()
                    .put(invokingEndpoint);
        } else {
            response = given()
                    .contentType("application/json")
                    .header(AUTHORIZATION_HEADER_NAME, accessToken) //Some API contains access token to run with the API
                    .headers(headers)
                    .body(jsonPayload)
                    .when()
                    .put(invokingEndpoint);
        }
        getStatusCode();
        getResponse();
        printResponseTime();
        printResponse();
        printResponseHeaders();
        setInvokingApiEndpointEmpty();
        headerList.clear();
    }

    public void deleteAPIWithAuthMultipleHeaders(String jsonPayload, String accessToken, List<Header> headerList) throws IOException {
        String invokingEndpoint = getApiEndpointToBeInvoked();
        Headers headers = new Headers(headerList);
        // Executing API and getting the response
        if (accessToken == null) {
            response = given()
                    .contentType("application/json")
                    .headers(headers)
                    .body(jsonPayload)
                    .when()
                    .delete(invokingEndpoint);
        } else {
            response = given()
                    .contentType("application/json")
                    .header(AUTHORIZATION_HEADER_NAME, accessToken) //Some API contains access token to run with the API
                    .headers(headers)
                    .body(jsonPayload)
                    .when()
                    .delete(invokingEndpoint);
        }
        getStatusCode();
        getResponse();
        printResponseTime();
        printResponse();
        printResponseHeaders();
        setInvokingApiEndpointEmpty();
        headerList.clear();
    }

    public Map<String, String> setFormParamsMap(String formKey, String formValue) {
        formParams.put(formKey, formValue);
        return formParams;
    }

    public void printFormParamsMap() {
        printInfo("Form Params Map: \n\n");
        for (Map.Entry entry : formParams.entrySet())
        {
            printInfo(entry.getKey() + " = " + entry.getValue());
        }
    }

    public void clearFormParamsMap() {
        formParams.clear();
    }

    public void clearMultipartFileInfo() {
        for(int i = 1; i <= 5; i++){
            saveValueForScenario("fileKey"+i, "");
            saveValueForScenario("filePath"+i, "");
            saveValueForScenario("mimeType"+i, "");
            saveValueForScenario("noOfRows", "");
        }
    }

    public void postFormDataAPIWithAuthMultipleHeaders(String accessToken, List<Header> headerList) throws IOException {
        String invokingEndpoint = getApiEndpointToBeInvoked();
        Headers headers = new Headers(headerList);

        // File Keys
        String fileKey1 = getSavedValueForScenario("fileKey1");
        String fileKey2 = getSavedValueForScenario("fileKey2");
        String fileKey3 = getSavedValueForScenario("fileKey3");
        String fileKey4 = getSavedValueForScenario("fileKey4");
        String fileKey5 = getSavedValueForScenario("fileKey5");

        // File Paths
        String filePath1 = CURRENT_DIRECTORY + getSavedValueForScenario("filePath1");
        String filePath2 = CURRENT_DIRECTORY + getSavedValueForScenario("filePath2");
        String filePath3 = CURRENT_DIRECTORY + getSavedValueForScenario("filePath3");
        String filePath4 = CURRENT_DIRECTORY + getSavedValueForScenario("filePath4");
        String filePath5 = CURRENT_DIRECTORY + getSavedValueForScenario("filePath5");

        // File Mime Types
        String mimeType1 = getSavedValueForScenario("mimeType1");
        String mimeType2 = getSavedValueForScenario("mimeType2");
        String mimeType3 = getSavedValueForScenario("mimeType3");
        String mimeType4 = getSavedValueForScenario("mimeType4");
        String mimeType5 = getSavedValueForScenario("mimeType5");

        int noOfMultipartFiles = 0;

        try {
            noOfMultipartFiles = Integer.valueOf(getSavedValueForScenario("noOfRows"));
        } catch (Exception e){
            noOfMultipartFiles = 0;
        }
        // Executing API and getting the response
        switch (noOfMultipartFiles) {

            case 1:
                if (accessToken == null) {
                    response = given()
                            .config(
                                    RestAssured.config()
                                            .encoderConfig(
                                                    encoderConfig()
                                                            .encodeContentTypeAs("multipart/form-data", ContentType.TEXT)))
                            .formParams(formParams)
                            .multiPart(fileKey1, new File(filePath1), mimeType1)
                            .headers(headers)
                            .when()
                            .post(invokingEndpoint);
                } else {
                    response = given()
                            .config(
                                    RestAssured.config()
                                            .encoderConfig(
                                                    encoderConfig()
                                                            .encodeContentTypeAs("multipart/form-data", ContentType.TEXT)))
                            .header(AUTHORIZATION_HEADER_NAME, accessToken) //Some API contains access token to run with the API
                            .headers(headers)
                            .formParams(formParams)
                            .multiPart(fileKey1, new File(filePath1), mimeType1)
                            .when()
                            .post(invokingEndpoint);
                }
                break;

            case 2:
                if (accessToken == null) {
                    response = given()
                            .config(
                                    RestAssured.config()
                                            .encoderConfig(
                                                    encoderConfig()
                                                            .encodeContentTypeAs("multipart/form-data", ContentType.TEXT)))
                            .formParams(formParams)
                            .multiPart(fileKey1, new File(filePath1), mimeType1)
                            .multiPart(fileKey2, new File(filePath2), mimeType2)
                            .headers(headers)
                            .when()
                            .post(invokingEndpoint);
                } else {
                    response = given()
                            .config(
                                    RestAssured.config()
                                            .encoderConfig(
                                                    encoderConfig()
                                                            .encodeContentTypeAs("multipart/form-data", ContentType.TEXT)))
                            .header(AUTHORIZATION_HEADER_NAME, accessToken) //Some API contains access token to run with the API
                            .headers(headers)
                            .formParams(formParams)
                            .multiPart(fileKey1, new File(filePath1), mimeType1)
                            .multiPart(fileKey2, new File(filePath2), mimeType2)
                            .when()
                            .post(invokingEndpoint);
                }
                break;

            case 3:
                if (accessToken == null) {
                    response = given()
                            .config(
                                    RestAssured.config()
                                            .encoderConfig(
                                                    encoderConfig()
                                                            .encodeContentTypeAs("multipart/form-data", ContentType.TEXT)))
                            .formParams(formParams)
                            .multiPart(fileKey1, new File(filePath1), mimeType1)
                            .multiPart(fileKey2, new File(filePath2), mimeType2)
                            .multiPart(fileKey3, new File(filePath3), mimeType3)
                            .headers(headers)
                            .when()
                            .post(invokingEndpoint);
                } else {
                    response = given()
                            .config(
                                    RestAssured.config()
                                            .encoderConfig(
                                                    encoderConfig()
                                                            .encodeContentTypeAs("multipart/form-data", ContentType.TEXT)))
                            .header(AUTHORIZATION_HEADER_NAME, accessToken) //Some API contains access token to run with the API
                            .headers(headers)
                            .formParams(formParams)
                            .multiPart(fileKey1, new File(filePath1), mimeType1)
                            .multiPart(fileKey2, new File(filePath2), mimeType2)
                            .multiPart(fileKey3, new File(filePath3), mimeType3)
                            .when()
                            .post(invokingEndpoint);
                }
                break;

            case 4:
                if (accessToken == null) {
                    response = given()
                            .config(
                                    RestAssured.config()
                                            .encoderConfig(
                                                    encoderConfig()
                                                            .encodeContentTypeAs("multipart/form-data", ContentType.TEXT)))
                            .formParams(formParams)
                            .multiPart(fileKey1, new File(filePath1), mimeType1)
                            .multiPart(fileKey2, new File(filePath2), mimeType2)
                            .multiPart(fileKey3, new File(filePath3), mimeType3)
                            .multiPart(fileKey4, new File(filePath4), mimeType4)
                            .headers(headers)
                            .when()
                            .post(invokingEndpoint);
                } else {
                    response = given()
                            .config(
                                    RestAssured.config()
                                            .encoderConfig(
                                                    encoderConfig()
                                                            .encodeContentTypeAs("multipart/form-data", ContentType.TEXT)))
                            .header(AUTHORIZATION_HEADER_NAME, accessToken) //Some API contains access token to run with the API
                            .headers(headers)
                            .formParams(formParams)
                            .multiPart(fileKey1, new File(filePath1), mimeType1)
                            .multiPart(fileKey2, new File(filePath2), mimeType2)
                            .multiPart(fileKey3, new File(filePath3), mimeType3)
                            .multiPart(fileKey4, new File(filePath4), mimeType4)
                            .when()
                            .post(invokingEndpoint);
                }
                break;

            case 5:
                if (accessToken == null) {
                    response = given()
                            .config(
                                    RestAssured.config()
                                            .encoderConfig(
                                                    encoderConfig()
                                                            .encodeContentTypeAs("multipart/form-data", ContentType.TEXT)))
                            .formParams(formParams)
                            .multiPart(fileKey1, new File(filePath1), mimeType1)
                            .multiPart(fileKey2, new File(filePath2), mimeType2)
                            .multiPart(fileKey3, new File(filePath3), mimeType3)
                            .multiPart(fileKey4, new File(filePath4), mimeType4)
                            .multiPart(fileKey5, new File(filePath5), mimeType5)
                            .headers(headers)
                            .when()
                            .post(invokingEndpoint);
                } else {
                    response = given()
                            .config(
                                    RestAssured.config()
                                            .encoderConfig(
                                                    encoderConfig()
                                                            .encodeContentTypeAs("multipart/form-data", ContentType.TEXT)))
                            .header(AUTHORIZATION_HEADER_NAME, accessToken) //Some API contains access token to run with the API
                            .headers(headers)
                            .formParams(formParams)
                            .multiPart(fileKey1, new File(filePath1), mimeType1)
                            .multiPart(fileKey2, new File(filePath2), mimeType2)
                            .multiPart(fileKey3, new File(filePath3), mimeType3)
                            .multiPart(fileKey4, new File(filePath4), mimeType4)
                            .multiPart(fileKey5, new File(filePath5), mimeType5)
                            .when()
                            .post(invokingEndpoint);
                }
                break;

            default:
                if (accessToken == null) {
                    response = given()
                            .config(
                                    RestAssured.config()
                                            .encoderConfig(
                                                    encoderConfig()
                                                            .encodeContentTypeAs("multipart/form-data", ContentType.TEXT)))
                            .formParams(formParams)
                            .headers(headers)
                            .when()
                            .post(invokingEndpoint);
                } else {
                    response = given()
                            .config(
                                    RestAssured.config()
                                            .encoderConfig(
                                                    encoderConfig()
                                                            .encodeContentTypeAs("multipart/form-data", ContentType.TEXT)))
                            .formParams(formParams)
                            .header(AUTHORIZATION_HEADER_NAME, accessToken) //Some API contains access token to run with the API
                            .headers(headers)
                            .when()
                            .post(invokingEndpoint);
                }
                break;
        }

        getStatusCode();
        getResponse();
        printResponseTime();
        printResponse();
        printResponseHeaders();
        setInvokingApiEndpointEmpty();
        clearFormParamsMap();
        clearMultipartFileInfo();
        headerList.clear();
    }

    public void putFormDataAPIWithAuthMultipleHeaders(String accessToken, List<Header> headerList) throws IOException {
        String invokingEndpoint = getApiEndpointToBeInvoked();
        Headers headers = new Headers(headerList);

        // File Keys
        String fileKey1 = getSavedValueForScenario("fileKey1");
        String fileKey2 = getSavedValueForScenario("fileKey2");
        String fileKey3 = getSavedValueForScenario("fileKey3");
        String fileKey4 = getSavedValueForScenario("fileKey4");
        String fileKey5 = getSavedValueForScenario("fileKey5");

        // File Paths
        String filePath1 = CURRENT_DIRECTORY + getSavedValueForScenario("filePath1");
        String filePath2 = CURRENT_DIRECTORY + getSavedValueForScenario("filePath2");
        String filePath3 = CURRENT_DIRECTORY + getSavedValueForScenario("filePath3");
        String filePath4 = CURRENT_DIRECTORY + getSavedValueForScenario("filePath4");
        String filePath5 = CURRENT_DIRECTORY + getSavedValueForScenario("filePath5");

        // File Mime Types
        String mimeType1 = getSavedValueForScenario("mimeType1");
        String mimeType2 = getSavedValueForScenario("mimeType2");
        String mimeType3 = getSavedValueForScenario("mimeType3");
        String mimeType4 = getSavedValueForScenario("mimeType4");
        String mimeType5 = getSavedValueForScenario("mimeType5");

        int noOfMultipartFiles = 0;

        try {
            noOfMultipartFiles = Integer.valueOf(getSavedValueForScenario("noOfRows"));
        } catch (Exception e){
            noOfMultipartFiles = 0;
        }
        // Executing API and getting the response
        switch (noOfMultipartFiles) {

            case 1:
                if (accessToken == null) {
                    response = given()
                            .config(
                                    RestAssured.config()
                                            .encoderConfig(
                                                    encoderConfig()
                                                            .encodeContentTypeAs("multipart/form-data", ContentType.TEXT)))
                            .formParams(formParams)
                            .multiPart(fileKey1, new File(filePath1), mimeType1)
                            .headers(headers)
                            .when()
                            .put(invokingEndpoint);
                } else {
                    response = given()
                            .config(
                                    RestAssured.config()
                                            .encoderConfig(
                                                    encoderConfig()
                                                            .encodeContentTypeAs("multipart/form-data", ContentType.TEXT)))
                            .header(AUTHORIZATION_HEADER_NAME, accessToken) //Some API contains access token to run with the API
                            .headers(headers)
                            .formParams(formParams)
                            .multiPart(fileKey1, new File(filePath1), mimeType1)
                            .when()
                            .put(invokingEndpoint);
                }
                break;

            case 2:
                if (accessToken == null) {
                    response = given()
                            .config(
                                    RestAssured.config()
                                            .encoderConfig(
                                                    encoderConfig()
                                                            .encodeContentTypeAs("multipart/form-data", ContentType.TEXT)))
                            .formParams(formParams)
                            .multiPart(fileKey1, new File(filePath1), mimeType1)
                            .multiPart(fileKey2, new File(filePath2), mimeType2)
                            .headers(headers)
                            .when()
                            .put(invokingEndpoint);
                } else {
                    response = given()
                            .config(
                                    RestAssured.config()
                                            .encoderConfig(
                                                    encoderConfig()
                                                            .encodeContentTypeAs("multipart/form-data", ContentType.TEXT)))
                            .header(AUTHORIZATION_HEADER_NAME, accessToken) //Some API contains access token to run with the API
                            .headers(headers)
                            .formParams(formParams)
                            .multiPart(fileKey1, new File(filePath1), mimeType1)
                            .multiPart(fileKey2, new File(filePath2), mimeType2)
                            .when()
                            .put(invokingEndpoint);
                }
                break;

            case 3:
                if (accessToken == null) {
                    response = given()
                            .config(
                                    RestAssured.config()
                                            .encoderConfig(
                                                    encoderConfig()
                                                            .encodeContentTypeAs("multipart/form-data", ContentType.TEXT)))
                            .formParams(formParams)
                            .multiPart(fileKey1, new File(filePath1), mimeType1)
                            .multiPart(fileKey2, new File(filePath2), mimeType2)
                            .multiPart(fileKey3, new File(filePath3), mimeType3)
                            .headers(headers)
                            .when()
                            .put(invokingEndpoint);
                } else {
                    response = given()
                            .config(
                                    RestAssured.config()
                                            .encoderConfig(
                                                    encoderConfig()
                                                            .encodeContentTypeAs("multipart/form-data", ContentType.TEXT)))
                            .header(AUTHORIZATION_HEADER_NAME, accessToken) //Some API contains access token to run with the API
                            .headers(headers)
                            .formParams(formParams)
                            .multiPart(fileKey1, new File(filePath1), mimeType1)
                            .multiPart(fileKey2, new File(filePath2), mimeType2)
                            .multiPart(fileKey3, new File(filePath3), mimeType3)
                            .when()
                            .put(invokingEndpoint);
                }
                break;

            case 4:
                if (accessToken == null) {
                    response = given()
                            .config(
                                    RestAssured.config()
                                            .encoderConfig(
                                                    encoderConfig()
                                                            .encodeContentTypeAs("multipart/form-data", ContentType.TEXT)))
                            .formParams(formParams)
                            .multiPart(fileKey1, new File(filePath1), mimeType1)
                            .multiPart(fileKey2, new File(filePath2), mimeType2)
                            .multiPart(fileKey3, new File(filePath3), mimeType3)
                            .multiPart(fileKey4, new File(filePath4), mimeType4)
                            .headers(headers)
                            .when()
                            .put(invokingEndpoint);
                } else {
                    response = given()
                            .config(
                                    RestAssured.config()
                                            .encoderConfig(
                                                    encoderConfig()
                                                            .encodeContentTypeAs("multipart/form-data", ContentType.TEXT)))
                            .header(AUTHORIZATION_HEADER_NAME, accessToken) //Some API contains access token to run with the API
                            .headers(headers)
                            .formParams(formParams)
                            .multiPart(fileKey1, new File(filePath1), mimeType1)
                            .multiPart(fileKey2, new File(filePath2), mimeType2)
                            .multiPart(fileKey3, new File(filePath3), mimeType3)
                            .multiPart(fileKey4, new File(filePath4), mimeType4)
                            .when()
                            .put(invokingEndpoint);
                }
                break;

            case 5:
                if (accessToken == null) {
                    response = given()
                            .config(
                                    RestAssured.config()
                                            .encoderConfig(
                                                    encoderConfig()
                                                            .encodeContentTypeAs("multipart/form-data", ContentType.TEXT)))
                            .formParams(formParams)
                            .multiPart(fileKey1, new File(filePath1), mimeType1)
                            .multiPart(fileKey2, new File(filePath2), mimeType2)
                            .multiPart(fileKey3, new File(filePath3), mimeType3)
                            .multiPart(fileKey4, new File(filePath4), mimeType4)
                            .multiPart(fileKey5, new File(filePath5), mimeType5)
                            .headers(headers)
                            .when()
                            .put(invokingEndpoint);
                } else {
                    response = given()
                            .config(
                                    RestAssured.config()
                                            .encoderConfig(
                                                    encoderConfig()
                                                            .encodeContentTypeAs("multipart/form-data", ContentType.TEXT)))
                            .header(AUTHORIZATION_HEADER_NAME, accessToken) //Some API contains access token to run with the API
                            .headers(headers)
                            .formParams(formParams)
                            .multiPart(fileKey1, new File(filePath1), mimeType1)
                            .multiPart(fileKey2, new File(filePath2), mimeType2)
                            .multiPart(fileKey3, new File(filePath3), mimeType3)
                            .multiPart(fileKey4, new File(filePath4), mimeType4)
                            .multiPart(fileKey5, new File(filePath5), mimeType5)
                            .when()
                            .put(invokingEndpoint);
                }
                break;

            default:
                if (accessToken == null) {
                    response = given()
                            .config(
                                    RestAssured.config()
                                            .encoderConfig(
                                                    encoderConfig()
                                                            .encodeContentTypeAs("multipart/form-data", ContentType.TEXT)))
                            .formParams(formParams)
                            .headers(headers)
                            .when()
                            .put(invokingEndpoint);
                } else {
                    response = given()
                            .config(
                                    RestAssured.config()
                                            .encoderConfig(
                                                    encoderConfig()
                                                            .encodeContentTypeAs("multipart/form-data", ContentType.TEXT)))
                            .formParams(formParams)
                            .header(AUTHORIZATION_HEADER_NAME, accessToken) //Some API contains access token to run with the API
                            .headers(headers)
                            .when()
                            .put(invokingEndpoint);
                }
                break;
        }

        getStatusCode();
        getResponse();
        printResponseTime();
        printResponse();
        printResponseHeaders();
        setInvokingApiEndpointEmpty();
        clearFormParamsMap();
        clearMultipartFileInfo();
        headerList.clear();
    }

    public enum HttpMethod {
        GET, POST, PUT, DELETE
    }

    public enum BodyType {
        JSON, FORM_DATA
    }

    public void invokeApi(String jsonPayload, List<Header> headerList) throws IOException {
        String apiName = getSavedValueForScenario("apiName"); // Fetching Value from the Data Store
        String accessTokenInFile = readAccessToken(); // Fetching token from the text file
        String accessToken = "";
        String isAuthenticationRequired = "";
        String isAccessTokenRetrievedFromTextFile = "";
        String accessTokenString = "";

        try {
            isAuthenticationRequired = String.valueOf(getSavedValueForScenario(
                    "Is authentication required?").toLowerCase());
            isAccessTokenRetrievedFromTextFile = String.valueOf(getSavedValueForScenario(
                    "Do you need to retrieve the access token from the text file?").toLowerCase());
            accessTokenString = String.valueOf(getSavedValueForScenario(
                    "Provide the access token if you need to authorize the API manually"));
        } catch (Exception ex){
            isAuthenticationRequired = "";
            isAccessTokenRetrievedFromTextFile = "";
            accessTokenString = "";
        }

        if (Boolean.valueOf(isAuthenticationRequired).equals(Boolean.TRUE) || isAuthenticationRequired.equals("yes") || isAuthenticationRequired.equals("y")) {
            if (Boolean.valueOf(isAccessTokenRetrievedFromTextFile).equals(Boolean.TRUE) || isAccessTokenRetrievedFromTextFile.equals("yes") || isAccessTokenRetrievedFromTextFile.equals("y")) {
                accessToken = accessTokenInFile;
            } else {
                accessToken = accessTokenString;
            }
        } else {
            accessToken = "";
        }

        HttpMethod httpMethod = HttpMethod.valueOf(ApiDocument.getHttpMethod(apiName).toUpperCase());

        String bodyTypeFromExcel = ApiDocument.getBodyType(apiName);

        if (bodyTypeFromExcel.equals("") || bodyTypeFromExcel == null){
            bodyTypeFromExcel = String.valueOf(JSON);
        }

        BodyType bodyType = BodyType.valueOf(bodyTypeFromExcel.toUpperCase());

        if (ApiDocument.getBodyType(apiName).equals("") || ApiDocument.getBodyType(apiName) == null){
            bodyType = JSON;
        }

        switch ((bodyType)){

            case JSON:

                switch (httpMethod) {
                    case GET:
                        getAPIWithAuthMultipleHeaders(accessToken, headerList);
                        break;
                    case POST:
                        postAPIWithAuthMultipleHeaders(jsonPayload, accessToken, headerList);
                        break;
                    case PUT:
                        putAPIWithAuthMultipleHeaders(jsonPayload, accessToken, headerList);
                        break;
                    case DELETE:
                        deleteAPIWithAuthMultipleHeaders(jsonPayload, accessToken, headerList);
                        break;
                    default:
                        Assert.fail("HTTP Method is not implemented");
                        break;
                }
                break;

            case FORM_DATA:

                switch (httpMethod) {
                    case GET:
                        getAPIWithAuthMultipleHeaders(accessToken, headerList);
                        break;
                    case POST:
                        postFormDataAPIWithAuthMultipleHeaders(accessToken, headerList);
                        break;
                    case PUT:
                        putFormDataAPIWithAuthMultipleHeaders(accessToken, headerList);
                        break;
                    case DELETE:
                        deleteAPIWithAuthMultipleHeaders(jsonPayload, accessToken, headerList);
                        break;
                    default:
                        Assert.fail("HTTP Method is not implemented");
                        break;
                }
                break;

            default:
                Assert.fail("Body Type is not implemented");
                break;
        }
    }

    public void isResponseStatusCodeEqualTo(String statusCode) {
        Assert.assertEquals(getSavedValueForScenario("statusCode"), statusCode, "The expected status code for the request is not equal to the actual status code\n");
    }

    public void getStatusCode() {
        int statusCode = response.statusCode();
        // Set the value of status code into a Data Store
        saveValueForScenario("statusCode", String.valueOf(statusCode));
    }

    public String getResponse() {
        String responseAsString = response.prettyPrint();
        // Set the value of response into a Data Store
        saveValueForScenario("response", responseAsString);
        return responseAsString;
    }

    public void saveResponseJsonPathValue(String dataStoreType, String variableName, String jsonPath) throws JSONException {
        String jsonData = getSavedValueForScenario("response");
        Object dataObject = JsonPath.parse(jsonData).read(jsonPath);
        String jsonPathValue = dataObject.toString();
        // Save the value of response into a Data Store
        saveToDataStore(dataStoreType, variableName, jsonPathValue);
    }

    public void saveAccessToken(String jsonPath) throws JSONException {
        String jsonData = getSavedValueForScenario("response");
        Object dataObject = JsonPath.parse(jsonData).read(jsonPath);
        String jsonPathValue = dataObject.toString();
        if (AUTHENTICATION_FIRST_VALUE == null || AUTHENTICATION_FIRST_VALUE.equals(" ") || AUTHENTICATION_FIRST_VALUE.equals("")) {
            AUTHENTICATION_FIRST_VALUE = "";
        }
        // Save the token into a file
        try {
            TextFile.write(AUTHENTICATION_FIRST_VALUE + jsonPathValue, ACCESS_TOKEN_FILE_PATH);
            printInfo("Successfully saved the access token into the text file in the directory of \"" + ACCESS_TOKEN_FILE_PATH + "\"");
        } catch (Exception ex) {
            printWarning("Failed to save the access token into the text file in the directory of \"" + ACCESS_TOKEN_FILE_PATH + "\"\n" + ex.getMessage());
        }
    }

    public String readAccessToken() {
        String accessToken = "";
        try {
            accessToken = TextFile.readAccessToken(ACCESS_TOKEN_FILE_PATH);
        } catch (Exception ex) {
        } finally {
            return accessToken;
        }
    }

    public void saveResponseData(String jsonPath, String filePath){
        String jsonData = getSavedValueForScenario("response");
        Object dataObject = JsonPath.parse(jsonData).read(jsonPath);
        String jsonPathValue = dataObject.toString();
        // Save the token into a file
        try {
            File file = new File(CURRENT_DIRECTORY + filePath);
            if(!file.exists()){
                file.createNewFile();
            }
            TextFile.write(jsonPathValue, CURRENT_DIRECTORY + filePath);
            printInfo("Successfully saved the value inside \"" +jsonPath+ "\" into the text file in the directory of \"" + CURRENT_DIRECTORY + filePath + "\"");
        } catch (Exception ex) {
            printWarning("Failed to save the value inside \"" +jsonPath+ "\" into the text file in the directory of \"" + CURRENT_DIRECTORY + filePath + "\"\n" + ex.getMessage());
        }
    }

    public void jsonPathValueContains(String jsonPath, String expectedResult) {
        Object responseString = Configuration.defaultConfiguration().jsonProvider().parse(getSavedValueForScenario("response"));
        if (responseString.toString().equals("")) {
            printInfo("No any JSON Paths found. Because the response is a no-content response for the given payload.");
        }
        if (responseString.toString().equals("[]")) {
            printInfo("No any JSON Paths found. Because the response is an empty array for the given payload.");
        }
        String jsonPathValue = String.valueOf(JsonPath.read(responseString, jsonPath));
        String nullableMessage = "JSON Path value for the \"" +jsonPath+ "\" is not contains the expected value.\nJSON Path value is: " + jsonPathValue +
                "\n"+ "Expected value to be contained is: " + expectedResult + "\n\n";
        Assert.assertTrue(jsonPathValue.contains(expectedResult), nullableMessage);
    }

    public void jsonPathValueNotContains(String jsonPath, String expectedResult) {
        Object responseString = Configuration.defaultConfiguration().jsonProvider().parse(getSavedValueForScenario("response"));
        if (responseString.toString().equals("")) {
            printInfo("No any JSON Paths found. Because the response is a no-content response for the given payload.");
        }
        if (responseString.toString().equals("[]")) {
            printInfo("No any JSON Paths found. Because the response is an empty array for the given payload.");
        }
        String jsonPathValue = String.valueOf(JsonPath.read(responseString, jsonPath));
        String nullableMessage = "JSON Path value for the \"" +jsonPath+ "\" is contains the expected value.\nJSON Path value is: " + jsonPathValue +
                "\n"+ "Expected value not to be contained is: " + expectedResult + "\n\n";
        Assert.assertFalse(jsonPathValue.contains(expectedResult), nullableMessage);
    }

    public void jsonPathAssertionEquals(String jsonPath, String expectedResult) {
        Object responseString = Configuration.defaultConfiguration().jsonProvider().parse(getSavedValueForScenario("response"));
        if (responseString.toString().equals("")) {
            printInfo("No any JSON Paths found. Because the response is a no-content response for the given payload.");
        }
        if (responseString.toString().equals("[]")) {
            printInfo("No any JSON Paths found. Because the response is an empty array for the given payload.");
        }
        String nullableMessage = "Expected value for the JSON Path of \"" +jsonPath+ "\" is not equal to the Actual value.\n";
        if (expectedResult.toLowerCase().equals("[]")) {
            String expectedResultForNull = "[]";
            Assert.assertEquals(JsonPath.read(responseString, jsonPath).toString(), expectedResultForNull, nullableMessage);
        }
        else if (expectedResult.toLowerCase().equals("null")) {
            String expectedResultForNull = null;
            Assert.assertEquals(JsonPath.read(responseString, jsonPath), expectedResultForNull, nullableMessage);
        }
        else if (expectedResult.toLowerCase().equals("true")) {
            Assert.assertEquals(JsonPath.read(responseString, jsonPath), Boolean.TRUE, nullableMessage);
        }
        else if (expectedResult.toLowerCase().equals("false")) {
            Assert.assertEquals(JsonPath.read(responseString, jsonPath), Boolean.FALSE, nullableMessage);
        }
        else if (expectedResult.trim().equals("")) {
            String expectedResultForEmpty = "";
            Assert.assertEquals(JsonPath.read(responseString, jsonPath), expectedResultForEmpty, nullableMessage);
        }
        else if (expectedResult.matches("\\d+")) {
            Assert.assertEquals(JsonPath.read(responseString, jsonPath).toString(), expectedResult, nullableMessage);
        }
        else if (expectedResult.matches("[-+]?\\d*\\.?\\d*")) {
            Assert.assertEquals(JsonPath.read(responseString, jsonPath).toString(), String.valueOf(expectedResult), nullableMessage);
        }
        else {
            Assert.assertEquals(String.valueOf(JsonPath.read(responseString, jsonPath)), expectedResult, nullableMessage);
        }
    }

    public void jsonPathAssertionNotEquals(String jsonPath, String expectedResult) {
        Object responseString = Configuration.defaultConfiguration().jsonProvider().parse(getSavedValueForScenario("response"));
        if (responseString.toString().equals("")) {
            printInfo("No any JSON Paths found. Because the response is a no-content response for the given payload.");
        }
        if (responseString.toString().equals("[]")) {
            printInfo("No any JSON Paths found. Because the response is an empty array for the given payload.");
        }
        String nullableMessage = "Expected value for the JSON Path of \"" +jsonPath+ "\" is equal to the Actual value.\n";
        if (expectedResult.toLowerCase().equals("[]")) {
            String expectedResultForNull = "[]";
            Assert.assertNotEquals(JsonPath.read(responseString, jsonPath).toString(), expectedResultForNull, nullableMessage);
        }
        else if (expectedResult.toLowerCase().equals("null")) {
            String expectedResultForNull = null;
            Assert.assertNotEquals(JsonPath.read(responseString, jsonPath), expectedResultForNull, nullableMessage);
        }
        else if (expectedResult.toLowerCase().equals("true")) {
            Assert.assertNotEquals(JsonPath.read(responseString, jsonPath), Boolean.TRUE, nullableMessage);
        }
        else if (expectedResult.toLowerCase().equals("false")) {
            Assert.assertNotEquals(JsonPath.read(responseString, jsonPath), Boolean.FALSE, nullableMessage);
        }
        else if (expectedResult.trim().equals("")) {
            String expectedResultForEmpty = "";
            Assert.assertNotEquals(JsonPath.read(responseString, jsonPath), expectedResultForEmpty, nullableMessage);
        }
        else if (expectedResult.matches("\\d+")) {
            Assert.assertNotEquals(JsonPath.read(responseString, jsonPath).toString(), expectedResult, nullableMessage);
        }
        else if (expectedResult.matches("[-+]?\\d*\\.?\\d*")) {
            Assert.assertNotEquals(JsonPath.read(responseString, jsonPath).toString(), String.valueOf(expectedResult), nullableMessage);
        }
        else {
            Assert.assertNotEquals(String.valueOf(JsonPath.read(responseString, jsonPath)), expectedResult, nullableMessage);
        }
    }

    public void isJsonPathExists(String jsonPath, Boolean isExists) {
        Object responseString = Configuration.defaultConfiguration().jsonProvider().parse(getSavedValueForScenario("response"));
        Boolean actualResult = Boolean.FALSE;
        try {
            JsonPath.read(responseString, jsonPath);
            actualResult = Boolean.TRUE;
        } catch (PathNotFoundException ex) {
            actualResult = Boolean.FALSE;
        }
        Assert.assertEquals(actualResult, isExists, "Expected and the Actual results are mismatched for the JSON Path \"" + jsonPath + "\"");
    }

    public void saveJsonArrayValuesToCsv(String jsonPath, String header1, String csvFilePath) throws ParseException, IOException {
        Object responseString = Configuration.defaultConfiguration().jsonProvider().parse(getSavedValueForScenario("response"));
        String JsonArrayResults = JsonPath.read(responseString, jsonPath).toString();
        JSONParser parser = new JSONParser();
        Object obj = parser.parse(JsonArrayResults);
        JSONArray array = (JSONArray)obj;
        File inputFile = new File(CURRENT_DIRECTORY + csvFilePath);
        inputFile.delete();
        inputFile.createNewFile();
        String[] header = {header1};
        CSVWriter writer = new CSVWriter(new FileWriter(inputFile), ',');
        writer.writeNext(header);
        for (int i=0; i<array.size(); i++){
            printInfo((String) array.get(i));
            writer.writeNext(new String[]{(String) array.get(i)});
        }

        writer.flush();
        writer.close();
    }

    public void dataStoreValueEquals(String dataStoreType, String dataStoreVariableName, String expectedValue){
        Assert.assertEquals(readFromDataStore(dataStoreType, dataStoreVariableName), expectedValue);
    }

    public void compareDataStoresEquals(String firstDataStoreType, String firstDataStoreVariableName, String secondDataStoreType, String secondDataStoreVariableName){
        Assert.assertEquals(readFromDataStore(firstDataStoreType, firstDataStoreVariableName), readFromDataStore(secondDataStoreType, secondDataStoreVariableName));
    }

    public void dataStoreValueNotEquals(String dataStoreType, String dataStoreVariableName, String expectedValue){
        Assert.assertNotEquals(readFromDataStore(dataStoreType, dataStoreVariableName), expectedValue,
                "Text inside " + dataStoreType + " Data Store [" + dataStoreVariableName + "] is equal to the expected value \"" + expectedValue + "\"\n");
    }

    public void compareDataStoresNotEquals(String firstDataStoreType, String firstDataStoreVariableName, String secondDataStoreType, String secondDataStoreVariableName){
        Assert.assertNotEquals(readFromDataStore(firstDataStoreType, firstDataStoreVariableName), readFromDataStore(secondDataStoreType, secondDataStoreVariableName),
                "Text inside " + firstDataStoreType + " Data Store [" + firstDataStoreVariableName + "] is equal to the text inside " +
                        secondDataStoreType + " Data Store [" + secondDataStoreVariableName + "]\n");
    }

    public void dataStoreValueContains(String dataStoreType, String dataStoreVariableName, String expectedValue){
        Assert.assertTrue(readFromDataStore(dataStoreType, dataStoreVariableName).contains(expectedValue),
                "Text inside " + dataStoreType + " Data Store [" + dataStoreVariableName + "] not contains the expected value \"" + expectedValue + "\"\n");
    }

    public void compareDataStoresContains(String firstDataStoreType, String firstDataStoreVariableName, String secondDataStoreType, String secondDataStoreVariableName){
        Assert.assertTrue(readFromDataStore(firstDataStoreType, firstDataStoreVariableName).contains(readFromDataStore(secondDataStoreType, secondDataStoreVariableName)),
                "Text inside " + firstDataStoreType + " Data Store [" + firstDataStoreVariableName + "] not contains the text inside " +
                        secondDataStoreType + " Data Store [" + secondDataStoreVariableName + "]\n");
    }

    public void dataStoreValueNotContains(String dataStoreType, String dataStoreVariableName, String expectedValue){
        Assert.assertFalse(readFromDataStore(dataStoreType, dataStoreVariableName).contains(expectedValue),
                "Text inside " + dataStoreType + " Data Store [" + dataStoreVariableName + "] contains the expected value \"" + expectedValue + "\"\n");
    }

    public void compareDataStoresNotContains(String firstDataStoreType, String firstDataStoreVariableName, String secondDataStoreType, String secondDataStoreVariableName){
        Assert.assertFalse(readFromDataStore(firstDataStoreType, firstDataStoreVariableName).contains(readFromDataStore(secondDataStoreType, secondDataStoreVariableName)),
                "Text inside " + firstDataStoreType + " Data Store [" + firstDataStoreVariableName + "] contains the text inside " +
                        secondDataStoreType + " Data Store [" + secondDataStoreVariableName + "]\n");
    }

    public void printResults(List<String> headersList, List<List<String>> rowsList, String additional) {
        Board board = new Board(75);
        String tableString = board.setInitialBlock(new StringTable(board, 75, headersList, rowsList).tableToBlocks()).build().getPreview();
        printInfo("\nResults " + additional + " from the database for the executed query: \n" + tableString);
    }

    public void savePropertyFileValuesToDataStore(String dataStoreType, String dataStoreVariableName, String propertyName){
        saveToDataStore(dataStoreType, dataStoreVariableName, System.getenv(propertyName));
    }

    public void saveCurrentEpochTime(String secondsOrMillis, String dataStoreType, String dataStoreVariableName){
        switch (secondsOrMillis.toLowerCase()){
            case "seconds":
                saveToDataStore(dataStoreType, dataStoreVariableName, String.valueOf(EpochTime.getCurrentEpochTimeInSeconds()));
                break;
            case "milliseconds":
                saveToDataStore(dataStoreType, dataStoreVariableName, String.valueOf(EpochTime.getCurrentEpochTimeInMilliSeconds()));
                break;
            default:
                Assert.fail("Invalid parameter for Seconds/Milliseconds. Please provide the string as Seconds or Milliseconds.");
        }
    }

    public void saveEpochTime(String timestampPattern, String timestamp, String secondsOrMillis, String dataStoreType, String dataStoreVariableName) throws java.text.ParseException {
        switch (secondsOrMillis.toLowerCase()){
            case "seconds":
                saveToDataStore(dataStoreType, dataStoreVariableName, String.valueOf(EpochTime.getEpochTimeInSeconds(timestampPattern, timestamp)));
                break;
            case "milliseconds":
                saveToDataStore(dataStoreType, dataStoreVariableName, String.valueOf(EpochTime.getEpochTimeInMilliSeconds(timestampPattern, timestamp)));
                break;
            default:
                Assert.fail("Invalid parameter for Seconds/Milliseconds. Please provide the string as Seconds or Milliseconds.");
        }
    }


}
