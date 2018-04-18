package com.maxsoft.intelliapi.request;

import com.jayway.jsonpath.Configuration;
import com.jayway.jsonpath.JsonPath;
import com.jayway.jsonpath.PathNotFoundException;
import com.maxsoft.intelliapi.util.*;
import com.thoughtworks.gauge.Gauge;
import com.thoughtworks.gauge.datastore.DataStore;
import com.thoughtworks.gauge.datastore.DataStoreFactory;
import io.restassured.RestAssured;
import io.restassured.http.ContentType;
import io.restassured.http.Header;
import io.restassured.http.Headers;
import io.restassured.response.Response;
import io.restassured.specification.RequestSpecification;
import org.apache.commons.lang.StringUtils;
import org.json.JSONException;
import org.testng.Assert;
import java.io.File;
import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.List;
import java.util.concurrent.TimeUnit;
import static io.restassured.RestAssured.given;


/**
 * Created by Osanda on 7/12/2017.
 */


public class BaseClass {

    private static final String DEFAULT = "dev";
    private static final String DEV = "dev";
    private static final String QA = "qa";
    private static final String UAT = "uat";
    private static final String PROD = "prod";
    public String AUTHORIZATION_HEADER_NAME = System.getenv("header_name_for_authorization");
    public String AUTHENTICATION_FIRST_VALUE = System.getenv("authentication_first_value");
    public String CURRENT_DIRECTORY = System.getProperty("user.dir");
    public String ACCESS_TOKEN_FILE_PATH = CURRENT_DIRECTORY + File.separator + System.getenv("access_token_file_path");
    public String API_DOC_FILE_PATH = File.separator + System.getenv("api_document_path");
    public static String ENVIRONMENT = System.getenv("environment");
    public static String OS = System.getProperty("os.name");
    public String baseUrl = setUp();
    private Response response;
    private RequestSpecification request = getRequestSpecification();
    private static CsvOperator csvOperator = new CsvOperator();

    public void print(String text){
        System.out.println(text);
        Gauge.writeMessage(text);
    }

    public static void printRequest(String request) {
        System.out.println("Request is: " + "\n" + request);
        Gauge.writeMessage("Request is: " + "\n" + request);
    }

    public String getAPIDocumentFilePath() {
        return CURRENT_DIRECTORY + API_DOC_FILE_PATH;
    }

    public String getCurrentTimestamp(String timestampPattern){
        return new SimpleDateFormat(timestampPattern).format(new Date());
    }

    public void replaceAllColumnValuesToTimestamps(String filePath, String columnName, String timestampPattern) throws IOException {
        for(int i = 1; i<= csvOperator.getLinesCount(filePath); i++){
            csvOperator.updateCSVByRowIndexAndColumnIndex(filePath, getCurrentTimestamp(timestampPattern), i,
                    csvOperator.getColumnIndexByColumnName(filePath, columnName));
        }
    }

    public static String getSavedValueForScenario(String variableNameOfValueStoredInDataStore) {
        try {
            // Fetching Value from the Data Store
            DataStore scenarioStore = DataStoreFactory.getScenarioDataStore();
            String value = (String) scenarioStore.get(variableNameOfValueStoredInDataStore);
            return value;
        } catch (Exception ex) {
            System.out.println("Failed to read the text inside Scenario Data Store [" + variableNameOfValueStoredInDataStore + "]\n" + ex.getMessage());
            Gauge.writeMessage("Failed to read the text inside Scenario Data Store [" + variableNameOfValueStoredInDataStore + "]\n" + ex.getMessage());
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
            System.out.println("Failed to read the text inside Specification Data Store [" + variableNameOfValueStoredInDataStore + "]\n" + ex.getMessage());
            Gauge.writeMessage("Failed to read the text inside Specification Data Store [" + variableNameOfValueStoredInDataStore + "]\n" + ex.getMessage());
            return "";
        }
    }

    public static void saveValueForScenario(String variableNameOfValueToBeStoredInDataStore, String valueToBeStoredInDataStore) {
        try {
            // Adding value to the Data Store
            DataStore scenarioStore = DataStoreFactory.getScenarioDataStore();
            scenarioStore.put(variableNameOfValueToBeStoredInDataStore, valueToBeStoredInDataStore);
        } catch (Exception ex) {
            System.out.println("\"" + valueToBeStoredInDataStore + "\" is failed to save as a text in Scenario Data Store [" + variableNameOfValueToBeStoredInDataStore + "]\n" + ex.getMessage());
            Gauge.writeMessage("\"" + valueToBeStoredInDataStore + "\" is failed to save as a text in Scenario Data Store [" + variableNameOfValueToBeStoredInDataStore + "]\n" + ex.getMessage());
        }
    }

    public static void saveValueForSpecification(String variableNameOfValueToBeStoredInDataStore, String valueToBeStoredInDataStore) {
        try {
            // Adding value to the Data Store
            DataStore specDataStore = DataStoreFactory.getSpecDataStore();
            specDataStore.put(variableNameOfValueToBeStoredInDataStore, valueToBeStoredInDataStore);
        } catch (Exception ex) {
            System.out.println("\"" + valueToBeStoredInDataStore + "\" is failed to save as a text in Specification Data Store [" + variableNameOfValueToBeStoredInDataStore + "]\n" + ex.getMessage());
            Gauge.writeMessage("\"" + valueToBeStoredInDataStore + "\" is failed to save as a text in Specification Data Store [" + variableNameOfValueToBeStoredInDataStore + "]\n" + ex.getMessage());
        }
    }

    public static String getScenarioDataStoreValue(String variableNameOfValueStoredInDataStore) {
        try {
            // Fetching Value from the Data Store
            DataStore scenarioStore = DataStoreFactory.getScenarioDataStore();
            String value = (String) scenarioStore.get(variableNameOfValueStoredInDataStore);
            System.out.println("Text inside Scenario Data Store [" + variableNameOfValueStoredInDataStore + "] is: \"" + value + "\"");
            Gauge.writeMessage("Text inside Scenario Data Store [" + variableNameOfValueStoredInDataStore + "] is: \"" + value + "\"");
            return value;
        } catch (Exception ex) {
            System.out.println("Failed to read the text inside Scenario Data Store [" + variableNameOfValueStoredInDataStore + "]");
            Gauge.writeMessage("Failed to read the text inside Scenario Data Store [" + variableNameOfValueStoredInDataStore + "]");
            return "";
        }
    }

    public static String getSpecificationDataStoreValue(String variableNameOfValueStoredInDataStore) {
        try {
            // Fetching Value from the Data Store
            DataStore specDataStore = DataStoreFactory.getSpecDataStore();
            String value = (String) specDataStore.get(variableNameOfValueStoredInDataStore);
            System.out.println("Text inside Specification Data Store [" + variableNameOfValueStoredInDataStore + "] is: \"" + value + "\"");
            Gauge.writeMessage("Text inside Specification Data Store [" + variableNameOfValueStoredInDataStore + "] is: \"" + value + "\"");
            return value;
        } catch (Exception ex) {
            System.out.println("Failed to read the text inside Specification Data Store [" + variableNameOfValueStoredInDataStore + "]");
            Gauge.writeMessage("Failed to read the text inside Specification Data Store [" + variableNameOfValueStoredInDataStore + "]");
            return "";
        }
    }

    public static void saveToScenarioDataStore(String variableNameOfValueToBeStoredInDataStore, String valueToBeStoredInDataStore) {
        try {
            // Adding value to the Data Store
            DataStore scenarioStore = DataStoreFactory.getScenarioDataStore();
            scenarioStore.put(variableNameOfValueToBeStoredInDataStore, valueToBeStoredInDataStore);
            System.out.println("\"" + valueToBeStoredInDataStore + "\" is successfully saved as a text in Scenario Data Store [" + variableNameOfValueToBeStoredInDataStore + "]");
            Gauge.writeMessage("\"" + valueToBeStoredInDataStore + "\" is successfully saved as a text in Scenario Data Store [" + variableNameOfValueToBeStoredInDataStore + "]");
        } catch (Exception ex) {
            System.out.println("\"" + valueToBeStoredInDataStore + "\" is failed to save as a text in Scenario Data Store [" + variableNameOfValueToBeStoredInDataStore + "]");
            Gauge.writeMessage("\"" + valueToBeStoredInDataStore + "\" is failed to save as a text in Scenario Data Store [" + variableNameOfValueToBeStoredInDataStore + "]");
        }
    }

    public static void saveToSpecificationDataStore(String variableNameOfValueToBeStoredInDataStore, String valueToBeStoredInDataStore) {
        try {
            // Adding value to the Data Store
            DataStore specDataStore = DataStoreFactory.getSpecDataStore();
            specDataStore.put(variableNameOfValueToBeStoredInDataStore, valueToBeStoredInDataStore);
            System.out.println("\"" + valueToBeStoredInDataStore + "\" is successfully saved as a text in Specification Data Store [" + variableNameOfValueToBeStoredInDataStore + "]");
            Gauge.writeMessage("\"" + valueToBeStoredInDataStore + "\" is successfully saved as a text in Specification Data Store [" + variableNameOfValueToBeStoredInDataStore + "]");
        } catch (Exception ex) {
            System.out.println("\"" + valueToBeStoredInDataStore + "\" is failed to save as a text in Specification Data Store [" + variableNameOfValueToBeStoredInDataStore + "]");
            Gauge.writeMessage("\"" + valueToBeStoredInDataStore + "\" is failed to save as a text in Specification Data Store [" + variableNameOfValueToBeStoredInDataStore + "]");
        }
    }

    public void saveToDataStore(String dataStoreType, String variableName, String valueToBeStored){
        if (dataStoreType.toLowerCase().equals("spec") || dataStoreType.toLowerCase().equals("specification")){
            saveToSpecificationDataStore(variableName, valueToBeStored);
        } else {
            saveToScenarioDataStore(variableName, valueToBeStored);
        }
    }

    public String readFromDataStore(String dataStoreType, String variableName){
        if (dataStoreType.toLowerCase().equals("spec") || dataStoreType.toLowerCase().equals("specification")){
            return getSpecificationDataStoreValue(variableName);
        } else {
            return getScenarioDataStoreValue(variableName);
        }
    }

    public String setUp() {
        String baseUrl = "";
        if (ENVIRONMENT == null) {
            ENVIRONMENT = DEFAULT;
        }
        if (ENVIRONMENT.toLowerCase().equals(DEV)) {
            baseUrl = System.getenv("dev_environment_base_url");
        }
        if (ENVIRONMENT.toLowerCase().equals(QA)) {
            baseUrl = System.getenv("qa_environment_base_url");
        }
        if (ENVIRONMENT.toLowerCase().equals(UAT)) {
            baseUrl = System.getenv("uat_environment_base_url");
        }
        if (ENVIRONMENT.toLowerCase().equals(PROD)) {
            baseUrl = System.getenv("prod_environment_base_url");
        }
        if (baseUrl == null) {
            baseUrl = "";
        }
        return baseUrl;
    }

    public RequestSpecification getRequestSpecification() {
        return RestAssured.given().contentType(ContentType.JSON);
    }

    public void printTestingEnvironmentName() {
        print("Environment: " + ENVIRONMENT.toUpperCase());
    }

    public void printTestingEnvironmentURL() {
        print("Base URL: " + baseUrl);
    }

    public void printTestingEnvironmentOS() {
        print("Operating System: " + OS);
    }

    public void testingEnvDetails() {
        print("————————————————————————————————————————————————");
        print("Configurations of Test Execution Environment");
        print("————————————————————————————————————————————————\n");
        printTestingEnvironmentOS();
        printTestingEnvironmentName();
        printTestingEnvironmentURL();
        print("————————————————————————————————————————————————");
    }

    public void printApiEndpoint(String apiEndpoint) {
        System.out.println("API Endpoint is: " + "\n" + apiEndpoint);
        Gauge.writeMessage("API Endpoint is: " + "\n" + apiEndpoint);
    }

    public void printResponse() {
        String response = getSavedValueForScenario("response");
        if (response.equals("")) {
            System.out.println("No Content Response");
            Gauge.writeMessage("No Content Response");
        } else {
            System.out.println("Response is: " + "\n" + response);
            Gauge.writeMessage("Response is: " + "\n" + response);
        }
    }

    public void printResponseTime(){
        print("Response Time is: " + response.getTimeIn(TimeUnit.MILLISECONDS) + "ms");
    }

    public void printResponseHeaders() {
        print("Response Headers are: \n" + response.getHeaders().toString());
    }

    public void apiToBeInvoked(String apiEndpointName) throws IOException {
        saveValueForScenario("apiName", apiEndpointName);
        // Print API Endpoint
        printApiEndpoint(ApiEndpoints.getApiEndpointByName(apiEndpointName));
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

    public void postAPIWithAuthMultipleHeaders(String jsonPayload, String accessToken, List<Header> headerList) throws IOException {
        String apiName = getSavedValueForScenario("apiName"); // Fetching Value from the Data Store
        String invokingEndpoint = baseUrl.concat(ApiEndpoints.getApiEndpointByName(apiName)).concat(getPathParams().concat(getQueryParams()));
        System.out.println("Invoked API Endpoint: \n" + invokingEndpoint);
        Gauge.writeMessage("Invoked API Endpoint: \n" + invokingEndpoint);
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
    }

    public void getAPIWithAuthMultipleHeaders(String accessToken, List<Header> headerList) throws IOException {
        String apiName = getSavedValueForScenario("apiName"); // Fetching Value from the Data Store
        String invokingEndpoint = baseUrl.concat(ApiEndpoints.getApiEndpointByName(apiName)).concat(getPathParams().concat(getQueryParams()));
        System.out.println("Invoked API Endpoint: \n" + invokingEndpoint);
        Gauge.writeMessage("Invoked API Endpoint: \n" + invokingEndpoint);
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
            getStatusCode();
            getResponse();
            printResponseTime();
            printResponse();
            printResponseHeaders();
        }
    }

    public void putAPIWithAuthMultipleHeaders(String jsonPayload, String accessToken, List<Header> headerList) throws IOException {
        String apiName = getSavedValueForScenario("apiName"); // Fetching Value from the Data Store
        String invokingEndpoint = baseUrl.concat(ApiEndpoints.getApiEndpointByName(apiName)).concat(getPathParams().concat(getQueryParams()));
        System.out.println("Invoked API Endpoint: \n" + invokingEndpoint);
        Gauge.writeMessage("Invoked API Endpoint: \n" + invokingEndpoint);
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
    }

    public void deleteAPIWithAuthMultipleHeaders(String jsonPayload, String accessToken, List<Header> headerList) throws IOException {
        String apiName = getSavedValueForScenario("apiName"); // Fetching Value from the Data Store
        String invokingEndpoint = baseUrl.concat(ApiEndpoints.getApiEndpointByName(apiName)).concat(getPathParams().concat(getQueryParams()));
        System.out.println("Invoked API Endpoint: \n" + invokingEndpoint);
        Gauge.writeMessage("Invoked API Endpoint: \n" + invokingEndpoint);
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
    }

    public enum HttpMethod {
        GET, POST, PUT, DELETE
    }

    public void invokeApi(String jsonPayload, List<Header> headerList) throws IOException {
        String apiName = getSavedValueForScenario("apiName"); // Fetching Value from the Data Store
        System.out.println("You are going to invoked a " + ApiDocumentReader.getHttpMethod(apiName));
        String accessTokenInFile = readAccessToken(); // Fetching token from the text file
        String accessToken = "";
        String isAuthenticationRequired = "";
        String isAccessTokenRetrievedFromTextFile = "";
        String accessTokenString = "";

        try {
            isAuthenticationRequired = String.valueOf(getSavedValueForScenario("Is authentication required?").toLowerCase());
            isAccessTokenRetrievedFromTextFile = String.valueOf(getSavedValueForScenario("Do you need to retrieve the access token from the text file?").toLowerCase());
            accessTokenString = String.valueOf(getSavedValueForScenario("Provide the access token if you need to authorize the API manually").toLowerCase());
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

        HttpMethod httpMethod = HttpMethod.valueOf(ApiDocumentReader.getHttpMethod(apiName).toUpperCase());
        switch (httpMethod){
            case GET: getAPIWithAuthMultipleHeaders(accessToken, headerList); break;
            case POST: postAPIWithAuthMultipleHeaders(jsonPayload, accessToken, headerList); break;
            case PUT: putAPIWithAuthMultipleHeaders(jsonPayload, accessToken, headerList); break;
            case DELETE: deleteAPIWithAuthMultipleHeaders(jsonPayload, accessToken, headerList); break;
            default: print("HTTP Method is not implemented");
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
        System.out.println(jsonData);
        Object dataObject = JsonPath.parse(jsonData).read(jsonPath);
        String jsonPathValue = dataObject.toString();
        // Save the value of response into a Data Store
        saveToDataStore(dataStoreType, variableName, jsonPathValue);
    }

    public void saveAccessToken(String jsonPath) throws JSONException {
        String jsonData = getSavedValueForScenario("response");
        System.out.println(jsonData);
        Object dataObject = JsonPath.parse(jsonData).read(jsonPath);
        String jsonPathValue = dataObject.toString();
        if (AUTHENTICATION_FIRST_VALUE == null || AUTHENTICATION_FIRST_VALUE.equals(" ") || AUTHENTICATION_FIRST_VALUE.equals("")) {
            AUTHENTICATION_FIRST_VALUE = "";
        }
        System.out.println("Access token: " + AUTHENTICATION_FIRST_VALUE + jsonPathValue);
        // Save the token into a file
        try {
            FileOperator.writeToFile(AUTHENTICATION_FIRST_VALUE + jsonPathValue, ACCESS_TOKEN_FILE_PATH);
            System.out.println("Successfully saved the access token into the text file in the directory of \"" + ACCESS_TOKEN_FILE_PATH + "\"");
            Gauge.writeMessage("Successfully saved the access token into the text file in the directory of \"" + ACCESS_TOKEN_FILE_PATH + "\"");
        } catch (Exception ex) {
            System.out.println("Failed to save the access token into the text file in the directory of \"" + ACCESS_TOKEN_FILE_PATH + "\"\n" + ex.getMessage());
            Gauge.writeMessage("Failed to save the access token into the text file in the directory of \"" + ACCESS_TOKEN_FILE_PATH + "\"\n" + ex.getMessage());
        }
    }

    public String readAccessToken() {
        String accessToken = "";
        try {
            accessToken = FileOperator.readAccessTokenFromFile(ACCESS_TOKEN_FILE_PATH);
        } catch (Exception ex) {
        } finally {
            return accessToken;
        }
    }

    public void jsonPathValueContains(String jsonPath, String expectedResult) {
        Object responseString = Configuration.defaultConfiguration().jsonProvider().parse(getSavedValueForScenario("response"));
        if (responseString.toString().equals("")) {
            System.out.println("No any JSON Paths found. Because the response is a no-content response for the given payload.");
            Gauge.writeMessage("No any JSON Paths found. Because the response is a no-content response for the given payload.");
        }
            if (responseString.toString().equals("[]")) {
                System.out.println("No any JSON Paths found. Because the response is an empty array for the given payload.");
                Gauge.writeMessage("No any JSON Paths found. Because the response is an empty array for the given payload.");
            }
        String jsonPathValue = JsonPath.read(responseString, jsonPath).toString();
        String nullableMessage = "JSON Path value for the \"" +jsonPath+ "\" is not contains the expected value.\nJSON Path value is: " + jsonPathValue +
                "\n"+ "Expected value to be contained is: " + expectedResult + "\n\n";
        Assert.assertTrue(jsonPathValue.contains(expectedResult), nullableMessage);
    }

    public void jsonPathValueNotContains(String jsonPath, String expectedResult) {
        Object responseString = Configuration.defaultConfiguration().jsonProvider().parse(getSavedValueForScenario("response"));
        if (responseString.toString().equals("")) {
            System.out.println("No any JSON Paths found. Because the response is a no-content response for the given payload.");
            Gauge.writeMessage("No any JSON Paths found. Because the response is a no-content response for the given payload.");
        }
            if (responseString.toString().equals("[]")) {
                System.out.println("No any JSON Paths found. Because the response is an empty array for the given payload.");
                Gauge.writeMessage("No any JSON Paths found. Because the response is an empty array for the given payload.");
            }
        String jsonPathValue = JsonPath.read(responseString, jsonPath).toString();
        String nullableMessage = "JSON Path value for the \"" +jsonPath+ "\" is contains the expected value.\nJSON Path value is: " + jsonPathValue +
                "\n"+ "Expected value not to be contained is: " + expectedResult + "\n\n";
        Assert.assertFalse(jsonPathValue.contains(expectedResult), nullableMessage);
    }

    public void jsonPathAssertionEquals(String jsonPath, String expectedResult) {
        Object responseString = Configuration.defaultConfiguration().jsonProvider().parse(getSavedValueForScenario("response"));
        if (responseString.toString().equals("")) {
            System.out.println("No any JSON Paths found. Because the response is a no-content response for the given payload.");
            Gauge.writeMessage("No any JSON Paths found. Because the response is a no-content response for the given payload.");
        }
            if (responseString.toString().equals("[]")) {
                System.out.println("No any JSON Paths found. Because the response is an empty array for the given payload.");
                Gauge.writeMessage("No any JSON Paths found. Because the response is an empty array for the given payload.");
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
                    Assert.assertEquals(StringUtils.strip(String.valueOf(JsonPath.read(responseString, jsonPath)), "\"[]"), expectedResult, nullableMessage);
                }
    }

    public void jsonPathAssertionNotEquals(String jsonPath, String expectedResult) {
        Object responseString = Configuration.defaultConfiguration().jsonProvider().parse(getSavedValueForScenario("response"));
        if (responseString.toString().equals("")) {
            System.out.println("No any JSON Paths found. Because the response is a no-content response for the given payload.");
            Gauge.writeMessage("No any JSON Paths found. Because the response is a no-content response for the given payload.");
        }
            if (responseString.toString().equals("[]")) {
                System.out.println("No any JSON Paths found. Because the response is an empty array for the given payload.");
                Gauge.writeMessage("No any JSON Paths found. Because the response is an empty array for the given payload.");
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
                    Assert.assertNotEquals(StringUtils.strip(String.valueOf(JsonPath.read(responseString, jsonPath)), "\"[]"), expectedResult, nullableMessage);
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

    public void printResults(List<String> headersList, List<List<String>> rowsList, String additional) {
        Board board = new Board(75);
        String tableString = board.setInitialBlock(new StringTable(board, 75, headersList, rowsList).tableToBlocks()).build().getPreview();
        System.out.println("\nResults " + additional + " from the database for the executed query: \n" + tableString);
        Gauge.writeMessage("\nResults " + additional + " from the database for the executed query: \n" + tableString);
    }


}
