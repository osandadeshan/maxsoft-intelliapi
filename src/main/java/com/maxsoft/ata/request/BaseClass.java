package com.maxsoft.ata.request;

import com.jayway.jsonpath.Configuration;
import com.jayway.jsonpath.JsonPath;
import com.jayway.jsonpath.PathNotFoundException;
import com.maxsoft.ata.util.ApiDocumentReader;
import com.maxsoft.ata.util.Board;
import com.maxsoft.ata.util.FileOperator;
import com.maxsoft.ata.util.StringTable;
import com.thoughtworks.gauge.Gauge;
import com.thoughtworks.gauge.Table;
import com.thoughtworks.gauge.TableRow;
import com.thoughtworks.gauge.datastore.DataStore;
import com.thoughtworks.gauge.datastore.DataStoreFactory;
import io.restassured.RestAssured;
import io.restassured.http.ContentType;
import io.restassured.http.Header;
import io.restassured.http.Headers;
import io.restassured.response.Response;
import io.restassured.response.ValidatableResponse;
import io.restassured.specification.RequestSpecification;
import org.apache.commons.lang.StringUtils;
import org.hamcrest.CoreMatchers;
import org.json.JSONException;
import org.testng.Assert;

import java.io.File;
import java.io.IOException;
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
    private static final String GET = "get";
    private static final String POST = "post";
    private static final String PUT = "put";
    private static final String DELETE = "delete";
    public String AUTHORIZATION_HEADER_NAME = System.getenv("header_name_for_authorization");
    public String AUTHENTICATION_FIRST_VALUE = System.getenv("authentication_first_value");
    public String CURRENT_DIRECTORY = System.getProperty("user.dir");
    public String ACCESS_TOKEN_FILE_PATH = CURRENT_DIRECTORY + File.separator + System.getenv("access_token_file_path");
    public String API_DOC_FILE_PATH = File.separator + System.getenv("api_document_path");
    String ENVIRONMENT = System.getenv("environment");
    public String SERVER_HOST = setUp();
    private Response response;
    private ValidatableResponse json;
    private RequestSpecification request = getRequestSpecification();

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
        String HOST = "";
        if (ENVIRONMENT == null) {
            ENVIRONMENT = DEFAULT;
        }
        if (ENVIRONMENT.toLowerCase().equals(DEV)) {
            HOST = System.getenv("dev_server_host");
        }
        if (ENVIRONMENT.toLowerCase().equals(QA)) {
            HOST = System.getenv("qa_server_host");
        }
        if (ENVIRONMENT.toLowerCase().equals(UAT)) {
            HOST = System.getenv("uat_server_host");
        }
        if (ENVIRONMENT.toLowerCase().equals(PROD)) {
            HOST = System.getenv("prod_server_host");
        }
        if (HOST == null) {
            HOST = "";
        }
        return HOST;
    }

    public RequestSpecification getRequestSpecification() {
        return RestAssured.given().contentType(ContentType.JSON);
    }

    public void printTestingEnvironmentName() {
        System.out.println("Testing environment name: " + ENVIRONMENT.toUpperCase());
        Gauge.writeMessage("Testing environment name: " + ENVIRONMENT.toUpperCase());
    }

    public void printTestingEnvironmentURL() {
        System.out.println("Testing environment URL: " + SERVER_HOST);
        Gauge.writeMessage("Testing environment URL: " + SERVER_HOST);
    }

    public void testingEnvDetails() {
        printTestingEnvironmentName();
        printTestingEnvironmentURL();
    }

    public void printApiEndpoint(String apiEndpoint) {
        System.out.println("API Endpoint is: " + "\n" + apiEndpoint);
        Gauge.writeMessage("API Endpoint is: " + "\n" + apiEndpoint);
    }

    public void printResponse() {
        String response = getSavedValueForScenario("response");
        if (response.equals("")) {
            System.out.println("Response is empty for the given payload");
            Gauge.writeMessage("Response is empty for the given payload");
        } else if (response.equals("[]")) {
            System.out.println("Response is null for the given payload");
            Gauge.writeMessage("Response is null for the given payload");
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
        saveValueForScenario("API_NAME", apiEndpointName);
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

    public void postAPI(String jsonPayload) throws IOException {
        String apiName = getSavedValueForScenario("API_NAME"); // Fetching Value from the Data Store
        // Executing API and getting the response
        response = given()
                .contentType("application/json")
                .body(jsonPayload)
                .when()
                .post(SERVER_HOST.concat(ApiEndpoints.getApiEndpointByName(apiName)));
        getStatusCode();
        getResponse();
        printResponse();
    }

    public void postAPI(String apiEndpoint, String jsonPayload) {
        response = given()
                .contentType("application/json")
                .body(jsonPayload)
                .when()
                .post(SERVER_HOST.concat(apiEndpoint));
        getStatusCode();
        getResponse();
        printResponse();
    }

    public void postAPIWithAuth(String jsonPayload, String headerValue) throws IOException {
        String apiName = getSavedValueForScenario("API_NAME"); // Fetching Value from the Data Store
        String invokingEndpoint = SERVER_HOST.concat(ApiEndpoints.getApiEndpointByName(apiName)).concat(getPathParams().concat(getQueryParams()));
        System.out.println("Invoked API Endpoint: \n" + invokingEndpoint);
        Gauge.writeMessage("Invoked API Endpoint: \n" + invokingEndpoint);
        // Executing API and getting the response
        if (headerValue == null) {
            response = given()
                    .contentType("application/json")
                    .body(jsonPayload)
                    .when()
                    .post(invokingEndpoint);
        } else {
            response = given()
                    .contentType("application/json")
                    .header(AUTHORIZATION_HEADER_NAME, headerValue) //Some API contains access token to run with the API
                    .body(jsonPayload)
                    .when()
                    .post(SERVER_HOST.concat(ApiEndpoints.getApiEndpointByName(apiName)));
        }
        getStatusCode();
        getResponse();
        printResponse();
    }

    public void postAPIWithAuthMultipleHeaders(String jsonPayload, String accessToken, List<Header> headerList) throws IOException {
        String apiName = getSavedValueForScenario("API_NAME"); // Fetching Value from the Data Store
        String invokingEndpoint = SERVER_HOST.concat(ApiEndpoints.getApiEndpointByName(apiName)).concat(getPathParams().concat(getQueryParams()));
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

    public void postAPIWithAuth(String headerValue) throws IOException {
        String apiName = getSavedValueForScenario("API_NAME"); // Fetching Value from the Data Store
        // Executing API and getting the response
        response = given()
                .contentType("application/json")
                .header(AUTHORIZATION_HEADER_NAME, headerValue) //Some API contains headers to run with the API
                .when()
                .post(SERVER_HOST.concat(ApiEndpoints.getApiEndpointByName(apiName)));
        getStatusCode();
        getResponse();
        printResponse();
    }

    public void postAPIWithAuth(String apiEndpoint, String jsonPayload, String headerName, String headerValue) throws IOException {
        response = given()
                .contentType("application/json")
                .header(headerName, headerValue) //Some API contains headers to run with the API
                .body(jsonPayload)
                .when()
                .post(ApiEndpoints.getApiEndpointByName(apiEndpoint));
        getStatusCode();
        getResponse();
        printResponse();
    }

    public void getAPI() throws IOException {
        String apiName = getSavedValueForScenario("API_NAME"); // Fetching Value from the Data Store
        response = request
                .given()
                .when()
                .get(SERVER_HOST.concat(ApiEndpoints.getApiEndpointByName(apiName)));
        getStatusCode();
        getResponse();
        printResponse();
    }

    public void getAPIByAppendingParam(String parameter, String headerValue) throws IOException {
        String apiName = getSavedValueForScenario("API_NAME"); // Fetching Value from the Data Store
        System.out.println(SERVER_HOST.concat(ApiEndpoints.getApiEndpointByName(apiName) + "/" + parameter));
        response = request
                .given()
                .header(AUTHORIZATION_HEADER_NAME, headerValue) //Some API contains headers to run with the API
                .when()
                .get(SERVER_HOST.concat(ApiEndpoints.getApiEndpointByName(apiName) + "/" + parameter));
        printResponse();
        getResponse();
        getStatusCode();
    }

    public void getAPIByAppendingPathParamsAndMultipleHeaders(String parameter, String headerValue, List<Header> headerList) throws IOException {
        String apiName = getSavedValueForScenario("API_NAME"); // Fetching Value from the Data Store
        Headers headers = new Headers(headerList);
        System.out.println(SERVER_HOST.concat(ApiEndpoints.getApiEndpointByName(apiName) + "/" + parameter));
        response = request
                .given()
                .header(AUTHORIZATION_HEADER_NAME, headerValue) //Some API contains access token to run with the API
                .headers(headers) //Some API contains headers to run with the API
                .when()
                .get(SERVER_HOST.concat(ApiEndpoints.getApiEndpointByName(apiName) + "/" + parameter));
        printResponse();
        getResponse();
        getStatusCode();
    }

    public void invokeApiWithMultiplePathParameters(Table parameterTable, List<Header> headerList) throws IOException {
        String apiName = getSavedValueForScenario("API_NAME"); // Fetching Value from the Data Store
        Boolean isAccessTokenIncluded = Boolean.valueOf(getSavedValueForScenario("isAccessTokenIncluded"));
        Boolean isAccessTokenRetrievedFromTextFile = Boolean.valueOf(getSavedValueForScenario("isAccessTokenRetrievedFromTextFile"));
        Boolean isHeadersInclueded = Boolean.valueOf(getSavedValueForScenario("isHeadersInclueded"));
        String accessTokenString = String.valueOf(getSavedValueForScenario("accessTokenString"));
        String accessTokenInFile = readAccessToken(); // Fetching token from the text file
        String accessToken = "";

        if (isAccessTokenIncluded.equals(Boolean.TRUE)) {
            if (isAccessTokenRetrievedFromTextFile.equals(Boolean.TRUE)) {
                accessToken = accessTokenInFile;
            } else {
                accessToken = accessTokenString;
            }
        } else {
            accessToken = "";
        }
        List<TableRow> rows = parameterTable.getTableRows();
        List<String> columnNames = parameterTable.getColumnNames();
        String param = "";
        for (TableRow row : rows) {
            param = param + row.getCell(columnNames.get(1));
            param = param.concat("/");
        }
        System.out.println(param);
        if (isHeadersInclueded.equals(Boolean.TRUE)) {
            if (ApiDocumentReader.getHttpMethod(apiName).equals("GET")) {
                getAPIByAppendingPathParamsAndMultipleHeaders(param, accessToken, headerList);
                printApiEndpoint(ApiEndpoints.getApiEndpointByName(getSavedValueForScenario("API_NAME")).concat("/" + param));
            }
        } else {
            if (ApiDocumentReader.getHttpMethod(apiName).equals("GET")) {
                getAPIByAppendingParam(param, accessToken);
                printApiEndpoint(ApiEndpoints.getApiEndpointByName(getSavedValueForScenario("API_NAME")).concat("/" + param));
            }
        }
    }

    public void getAPIByAppendingParamWithNoAuth(String parameter) throws IOException {
        String apiName = getSavedValueForScenario("API_NAME"); // Fetching Value from the Data Store
        response = request
                .given()
                .when()
                .get(SERVER_HOST.concat(ApiEndpoints.getApiEndpointByName(apiName) + "/" + parameter));
        printResponse();
        getResponse();
        getStatusCode();
    }

    public void getAPI(String apiEndpoint, String queryParameters, String queryValues) throws IOException {
        response = request
                .given()
                .queryParam("q", queryParameters + queryValues)
                .when()
                .get(SERVER_HOST.concat(apiEndpoint));
        getStatusCode();
        getResponse();
        printResponse();
    }

    public void getAPI(String query) throws IOException {
        String headerValue = "";
        String apiName = getSavedValueForScenario("API_NAME"); // Fetching Value from the Data Store
        String requestEndPoint = "";
        String printText = "";
        if (query.equals("")) {
            requestEndPoint = SERVER_HOST.concat(ApiEndpoints.getApiEndpointByName(apiName));
            printText = "API Endpoint doesn't have any query parameters and query values. \n";
        } else {
            requestEndPoint = SERVER_HOST.concat(ApiEndpoints.getApiEndpointByName(apiName)) + "?" + query;
            printText = "API Endpoint with query parameters and query values: \n" + ApiEndpoints.getApiEndpointByName(apiName) + "?" + query;
        }
        response = request
                .given()
                // .header(AUTHORIZATION_HEADER_NAME, headerValue) //Some API contains headers to run with the API
                .when()
                .get(requestEndPoint);
        System.out.println(printText);
        Gauge.writeMessage(printText);
        getStatusCode();
        getResponse();
        printResponse();
    }

    public void getAPIWithAuthAndQueryParams(String accessToken, String query) throws IOException {
        String apiName = getSavedValueForScenario("API_NAME"); // Fetching Value from the Data Store
        String requestEndPoint = "";
        String printText = "";
        if (query.equals("")) {
            requestEndPoint = SERVER_HOST.concat(ApiEndpoints.getApiEndpointByName(apiName));
            printText = "API Endpoint doesn't have any query parameters and query values. \n";
        } else {
            requestEndPoint = SERVER_HOST.concat(ApiEndpoints.getApiEndpointByName(apiName)) + "?" + query;
            printText = "API Endpoint with query parameters and query values: \n" + ApiEndpoints.getApiEndpointByName(apiName) + "?" + query;
        }
        response = request
                .given()
                .header(AUTHORIZATION_HEADER_NAME, accessToken) //Some API contains headers to run with the API
                .when()
                .get(requestEndPoint);
        System.out.println(printText);
        Gauge.writeMessage(printText);
        getStatusCode();
        getResponse();
        printResponse();
    }

    public void getAPIWithMultipleHeadersAndAuthAndQueryParams(String accessToken, String query, List<Header> headerList) throws IOException {
        String apiName = getSavedValueForScenario("API_NAME"); // Fetching Value from the Data Store
        Headers headers = new Headers(headerList);
        String requestEndPoint = "";
        String printText = "";
        if (query.equals("")) {
            requestEndPoint = SERVER_HOST.concat(ApiEndpoints.getApiEndpointByName(apiName));
            printText = "API Endpoint doesn't have any query parameters and query values. \n";
        } else {
            requestEndPoint = SERVER_HOST.concat(ApiEndpoints.getApiEndpointByName(apiName)) + "?" + query;
            printText = "API Endpoint with query parameters and query values: \n" + ApiEndpoints.getApiEndpointByName(apiName) + "?" + query;
        }
        response = request
                .given()
                .header(AUTHORIZATION_HEADER_NAME, accessToken) //Some API contains access token to run with the API
                .headers(headers) //Some API contains headers to run with the API
                .when()
                .get(requestEndPoint);
        System.out.println(printText);
        Gauge.writeMessage(printText);
        getStatusCode();
        getResponse();
        printResponse();
    }

    public void invokeApiWithQueryParameters(Table parameterTable, List<Header> headerList) throws IOException {
        String apiName = getSavedValueForScenario("API_NAME"); // Fetching Value from the Data Store
        Boolean isAccessTokenIncluded = Boolean.valueOf(getSavedValueForScenario("isAccessTokenIncluded"));
        Boolean isAccessTokenRetrievedFromTextFile = Boolean.valueOf(getSavedValueForScenario("isAccessTokenRetrievedFromTextFile"));
        Boolean isHeadersInclueded = Boolean.valueOf(getSavedValueForScenario("isHeadersInclueded"));
        String accessTokenString = String.valueOf(getSavedValueForScenario("accessTokenString"));
        String accessTokenInFile = readAccessToken(); // Fetching token from the text file
        String accessToken = "";

        if (isAccessTokenIncluded.equals(Boolean.TRUE)) {
            if (isAccessTokenRetrievedFromTextFile.equals(Boolean.TRUE)) {
                accessToken = accessTokenInFile;
            } else {
                accessToken = accessTokenString;
            }
        } else {
            accessToken = "";
        }

        List<TableRow> rows = parameterTable.getTableRows();
        List<String> columnNames = parameterTable.getColumnNames();
        String query = "";
        for (TableRow row : rows) {
            query = query + row.getCell(columnNames.get(0)) + "=" + row.getCell(columnNames.get(1)) + "&";
        }
        query = query.replaceAll(".$", "");
        if (isHeadersInclueded.equals(Boolean.TRUE)) {
            if (ApiDocumentReader.getHttpMethod(apiName).equals("GET")) {
                if (query.equals("=")) {
                    getAPIWithMultipleHeadersAndAuthAndQueryParams(accessToken, "", headerList);
                } else {
                    getAPIWithMultipleHeadersAndAuthAndQueryParams(accessToken, query, headerList);
                }
            }
        } else {
            if (ApiDocumentReader.getHttpMethod(apiName).equals("GET")) {
                if (query.equals("=")) {
                    getAPIWithAuthAndQueryParams(accessToken, "");
                } else {
                    getAPIWithAuthAndQueryParams(accessToken, query);
                }
            }
        }
    }

    public void getAPIWithAuth(String apiEndpoint, String headerValue, String queryParameters, String queryValues) {
        response = request
                .given()
                .header(AUTHORIZATION_HEADER_NAME, headerValue) //Some API contains headers to run with the API
                .queryParam("q", queryParameters + queryValues)
                .when()
                .get(SERVER_HOST.concat(apiEndpoint));
        getStatusCode();
        getResponse();
        printResponse();
    }

    public void getAPIWithAuth(String accessToken) throws IOException {
        String apiName = getSavedValueForScenario("API_NAME"); // Fetching Value from the Data Store
        String invokingEndpoint = SERVER_HOST.concat(ApiEndpoints.getApiEndpointByName(apiName)).concat(getPathParams().concat(getQueryParams()));
        System.out.println("Invoked API Endpoint: \n" + invokingEndpoint);
        Gauge.writeMessage("Invoked API Endpoint: \n" + invokingEndpoint);
        response = request
                .given()
                .header(AUTHORIZATION_HEADER_NAME, accessToken) //Some API contains access token to run with the API
                .when()
                .get(invokingEndpoint);
        getStatusCode();
        getResponse();
        printResponse();
    }

    public void getAPIWithAuthMultipleHeaders(String accessToken, List<Header> headerList) throws IOException {
        String apiName = getSavedValueForScenario("API_NAME"); // Fetching Value from the Data Store
        String invokingEndpoint = SERVER_HOST.concat(ApiEndpoints.getApiEndpointByName(apiName)).concat(getPathParams().concat(getQueryParams()));
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

    public void invokeApiWithToken(String jsonPayload, String headerValue) throws IOException {
        String apiName = getSavedValueForScenario("API_NAME"); // Fetching Value from the Data Store
        System.out.println("You have invoked a " + ApiDocumentReader.getHttpMethod(apiName));
        if (ApiDocumentReader.getHttpMethod(apiName).equals("POST")) {
            // Executing API and getting the response
            postAPIWithAuth(jsonPayload, headerValue);
        } else if (ApiDocumentReader.getHttpMethod(apiName).equals("PUT")) {
            // Executing API and getting the response
            putAPIWithAuth(jsonPayload, headerValue);
        } else if (ApiDocumentReader.getHttpMethod(apiName).equals("GET")) {
            // Executing API and getting the response
            getAPIWithAuth(headerValue);
        } else {
            System.out.println("HTTP Method type is not implemented");
            Gauge.writeMessage("HTTP Method type is not implemented");
        }
    }

    public void invokeApiWithTokenInDataStore(String jsonPayload, String accessToken) throws IOException {
        String apiName = getSavedValueForScenario("API_NAME"); // Fetching Value from the Data Store
        System.out.println("You are going to invoked a " + ApiDocumentReader.getHttpMethod(apiName));
        String headerValue = AUTHENTICATION_FIRST_VALUE + getSavedValueForSpecification(accessToken); // Fetching Value from the Data Store
        if (ApiDocumentReader.getHttpMethod(apiName).equals("POST")) {
            // Executing API and getting the response
            postAPIWithAuth(jsonPayload, headerValue);
        } else if (ApiDocumentReader.getHttpMethod(apiName).equals("PUT")) {
            // Executing API and getting the response
            putAPIWithAuth(jsonPayload, headerValue);
        } else if (ApiDocumentReader.getHttpMethod(apiName).equals("GET")) {
            // Executing API and getting the response
            getAPIWithAuth(headerValue);
        } else {
            System.out.println("HTTP Method type is not implemented");
            Gauge.writeMessage("HTTP Method type is not implemented");
        }
    }

    public void invokeApiWithTokenInTextFile(String jsonPayload, List<Header> headerList) throws IOException {
        String apiName = getSavedValueForScenario("API_NAME"); // Fetching Value from the Data Store
        System.out.println("You are going to invoked a " + ApiDocumentReader.getHttpMethod(apiName));
        String accessToken = readAccessToken(); // Fetching token from the text file
        if (ApiDocumentReader.getHttpMethod(apiName).equals("POST")) {
            // Executing API and getting the response
            postAPIWithAuthMultipleHeaders(jsonPayload, accessToken, headerList);
        } else if (ApiDocumentReader.getHttpMethod(apiName).equals("PUT")) {
            // Executing API and getting the response
            putAPIWithAuth(jsonPayload, accessToken);
        } else if (ApiDocumentReader.getHttpMethod(apiName).equals("GET")) {
            // Executing API and getting the response
            getAPIWithAuthMultipleHeaders(accessToken, headerList);
        } else {
            System.out.println("HTTP Method type is not implemented");
            Gauge.writeMessage("HTTP Method type is not implemented");
        }
    }

    public enum HttpMethod {
        GET, POST, PUT, DELETE
    }

    public void invokeConfiguredApi(String jsonPayload, List<Header> headerList) throws IOException {
        String apiName = getSavedValueForScenario("API_NAME"); // Fetching Value from the Data Store
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

    public void invokeApiWithoutRequestWithToken() throws IOException {
        String apiName = getSavedValueForScenario("API_NAME"); // Fetching Value from the Data Store
        System.out.println("You are going to invoked a " + ApiDocumentReader.getHttpMethod(apiName));
        String headerValue = AUTHENTICATION_FIRST_VALUE + getSavedValueForSpecification("accessToken"); // Fetching Value from the Data Store
        if (ApiDocumentReader.getHttpMethod(apiName).equals("POST")) {
            // Executing API and getting the response
            postAPIWithAuth(headerValue);
        } else if (ApiDocumentReader.getHttpMethod(apiName).equals("PUT")) {
            // Executing API and getting the response
            putAPIWithAuth("", headerValue);
        } else if (ApiDocumentReader.getHttpMethod(apiName).equals("GET")) {
            // Executing API and getting the response
            getAPIWithAuth(headerValue);
        } else {
            System.out.println("HTTP Method type is not implemented");
            Gauge.writeMessage("HTTP Method type is not implemented");
        }
    }

    public void invokeApiWithoutRequestWithToken(String headerValue) throws IOException {
        String apiName = getSavedValueForScenario("API_NAME"); // Fetching Value from the Data Store
        System.out.println("You are going to invoked a " + ApiDocumentReader.getHttpMethod(apiName));
        if (ApiDocumentReader.getHttpMethod(apiName).equals("POST")) {
            // Executing API and getting the response
            postAPIWithAuth(headerValue);
        } else if (ApiDocumentReader.getHttpMethod(apiName).equals("PUT")) {
            // Executing API and getting the response
            putAPIWithAuth("", headerValue);
        } else if (ApiDocumentReader.getHttpMethod(apiName).equals("GET")) {
            // Executing API and getting the response
            getAPIWithAuth(headerValue);
        } else {
            System.out.println("HTTP Method type is not implemented");
            Gauge.writeMessage("HTTP Method type is not implemented");
        }
    }

    public void invokeApiWithNoAuth(String jsonPayload) throws IOException {
        String apiName = getSavedValueForScenario("API_NAME"); // Fetching Value from the Data Store
        System.out.println("You are going to invoked a " + ApiDocumentReader.getHttpMethod(apiName));
        if (ApiDocumentReader.getHttpMethod(apiName).equals("POST")) {
            // Executing API and getting the response
            postAPI(jsonPayload);
        } else if (ApiDocumentReader.getHttpMethod(apiName).equals("PUT")) {
            // Executing API and getting the response
            putAPIWithAuth(jsonPayload, "");
        } else if (ApiDocumentReader.getHttpMethod(apiName).equals("GET")) {
            // Executing API and getting the response
            getAPI();
        } else {
            System.out.println("HTTP Method type is not implemented");
            Gauge.writeMessage("HTTP Method type is not implemented");
        }
    }

    public void putAPIWithAuth(String jsonPayload, String headerValue) throws IOException {
        String apiName = getSavedValueForScenario("API_NAME"); // Fetching Value from the Data Store
        String invokingEndpoint = SERVER_HOST.concat(ApiEndpoints.getApiEndpointByName(apiName)).concat(getPathParams().concat(getQueryParams()));
        System.out.println("Invoked API Endpoint: \n" + invokingEndpoint);
        Gauge.writeMessage("Invoked API Endpoint: \n" + invokingEndpoint);
        // Executing API and getting the response
        if (headerValue == null) {
            response = given()
                    .contentType("application/json")
                    .body(jsonPayload)
                    .when()
                    .put(invokingEndpoint);
        } else {
            response = given()
                    .contentType("application/json")
                    .header(AUTHORIZATION_HEADER_NAME, headerValue) //Some API contains headers to run with the API
                    .body(jsonPayload)
                    .when()
                    .put(invokingEndpoint);
        }
        getStatusCode();
        getResponse();
        printResponse();
    }

    public void putAPIWithAuthMultipleHeaders(String jsonPayload, String accessToken, List<Header> headerList) throws IOException {
        String apiName = getSavedValueForScenario("API_NAME"); // Fetching Value from the Data Store
        String invokingEndpoint = SERVER_HOST.concat(ApiEndpoints.getApiEndpointByName(apiName)).concat(getPathParams().concat(getQueryParams()));
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
        String apiName = getSavedValueForScenario("API_NAME"); // Fetching Value from the Data Store
        String invokingEndpoint = SERVER_HOST.concat(ApiEndpoints.getApiEndpointByName(apiName)).concat(getPathParams().concat(getQueryParams()));
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

    public ValidatableResponse verifyStatusCode(int statusCode) {
        json = response.then().statusCode(statusCode);
        return json;
    }

    public void verifyResponseStatusCode(String statusCode) {
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

    // Asserts on JSON fields with single values
    public void responseEquals(Table responseFields) {
        for (TableRow row : responseFields.getTableRows()) {
            Gauge.writeMessage(row.getCell("Key" + " | " + row.getCell("Value")));
            if (StringUtils.isNumeric(row.getCell("Value"))) {
                json.body(row.getCell("Key"), CoreMatchers.equalTo(Integer.parseInt(row.getCell("Value"))));
            } else if (StringUtils.isAlphanumeric(row.getCell("Value"))) {
                json.body(row.getCell("Key"), CoreMatchers.equalTo(row.getCell("Value")));
            } else {
                if (row.getCell("Value") == null) {
                    json.body(row.getCell("Key"), CoreMatchers.equalTo(null));
                }
            }
        }
    }

    public void jsonPathValueContains(String jsonPath, String expectedResult) {
        Object responseString = Configuration.defaultConfiguration().jsonProvider().parse(getSavedValueForScenario("response"));
        if (responseString.toString().equals("")) {
            System.out.println("No any JSON Paths found. Because the response is empty for the given payload");
            Gauge.writeMessage("No any JSON Paths found. Because the response is empty for the given payload");
        }
            if (responseString.toString().equals("[]")) {
                System.out.println("No any JSON Paths found. Because the response is null for the given payload");
                Gauge.writeMessage("No any JSON Paths found. Because the response is null for the given payload");
            }
        String jsonPathValue = JsonPath.read(responseString, jsonPath).toString();
        String nullableMessage = "JSON Path value for the \"" +jsonPath+ "\" is not contains the expected value.\nJSON Path value is: " + jsonPathValue +
                "\n"+ "Expected value to be contained is: " + expectedResult + "\n\n";
        Assert.assertTrue(jsonPathValue.contains(expectedResult), nullableMessage);
    }

    public void jsonPathValueNotContains(String jsonPath, String expectedResult) {
        Object responseString = Configuration.defaultConfiguration().jsonProvider().parse(getSavedValueForScenario("response"));
        if (responseString.toString().equals("")) {
            System.out.println("No any JSON Paths found. Because the response is empty for the given payload");
            Gauge.writeMessage("No any JSON Paths found. Because the response is empty for the given payload");
        }
            if (responseString.toString().equals("[]")) {
                System.out.println("No any JSON Paths found. Because the response is null for the given payload");
                Gauge.writeMessage("No any JSON Paths found. Because the response is null for the given payload");
            }
        String jsonPathValue = JsonPath.read(responseString, jsonPath).toString();
        String nullableMessage = "JSON Path value for the \"" +jsonPath+ "\" is contains the expected value.\nJSON Path value is: " + jsonPathValue +
                "\n"+ "Expected value not to be contained is: " + expectedResult + "\n\n";
        Assert.assertFalse(jsonPathValue.contains(expectedResult), nullableMessage);
    }

    public void jsonPathAssertionEquals(String jsonPath, String expectedResult) {
        Object responseString = Configuration.defaultConfiguration().jsonProvider().parse(getSavedValueForScenario("response"));
        if (responseString.toString().equals("")) {
            System.out.println("No any JSON Paths found. Because the response is empty for the given payload");
            Gauge.writeMessage("No any JSON Paths found. Because the response is empty for the given payload");
        }
            if (responseString.toString().equals("[]")) {
                System.out.println("No any JSON Paths found. Because the response is null for the given payload");
                Gauge.writeMessage("No any JSON Paths found. Because the response is null for the given payload");
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
            System.out.println("No any JSON Paths found. Because the response is empty for the given payload");
            Gauge.writeMessage("No any JSON Paths found. Because the response is empty for the given payload");
        }
            if (responseString.toString().equals("[]")) {
                System.out.println("No any JSON Paths found. Because the response is null for the given payload");
                Gauge.writeMessage("No any JSON Paths found. Because the response is null for the given payload");
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
