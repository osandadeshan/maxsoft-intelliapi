package com.maxsoft.intelliapi.stepdefinition;

/**
 * Project Name : MaxSoft-IntelliAPI
 * Developer    : Osanda Deshan
 * Version      : 1.0.0
 * Date         : 6/30/2018
 * Time         : 3:51 PM
 * Description  :
 **/

import com.maxsoft.intelliapi.database.mysql.MySqlOperator;
import com.maxsoft.intelliapi.request.CommonStepImpl;
import com.thoughtworks.gauge.Step;
import com.thoughtworks.gauge.Table;
import org.json.JSONException;
import org.json.simple.parser.ParseException;
import java.io.IOException;
import java.sql.SQLException;


public class AllStepsDefinitions{

    private CommonStepImpl commonStepImpl = new CommonStepImpl();
    private MySqlOperator mySQLOperator = new MySqlOperator();

    // Use this method to print the testing environment name in the HTML report
    @Step("Configurations of the testing environment")
    public void testEnvDetails(){
        commonStepImpl.testingEnvDetails();
    }

    // Use this method at the beginning of the scenario to identify which API is going to use in that scenario
    @Step("Given that a user needs to invoke <apiEndpointName>")
    public void apiToBeInvoked(String apiEndpointName) throws IOException {
        commonStepImpl.apiToBeInvoked(apiEndpointName);
    }

    // Use this method to replace the placeholders inside the API Endpoint in Excel
    @Step("And the user set values to the API endpoint placeholders as follows <table>")
    public void setApiEndpointReplacements(Table table) throws IOException {
        commonStepImpl.setApiEndpointReplacements(table);
    }

    // Use this method to replace the placeholders inside the API Endpoint in Excel using data store values
    @Step("And the user set values to the API endpoint placeholders using data stores as follows <table>")
    public void setApiEndpointReplacementsFromDataStores(Table table) throws IOException {
        commonStepImpl.setApiEndpointReplacementsFromDataStores(table);
    }

    @Step("And replace the row values in <columnName> column of the CSV <filePath> into the <timestampPattern> timestamp pattern")
    public void replaceCSVColumn(String columnName, String filePath, String timestampPattern) throws IOException {
        commonStepImpl.replaceCSVColumnValuesToTimestamps(filePath, columnName, timestampPattern);
    }

    // Use this method to set the headers values for the JSON request
    @Step("And the user set the request headers as follows <table>")
    public void setRequestHeaders(Table table) throws IOException {
        commonStepImpl.setRequestHeaders(table);
    }

    // Use this method to set the headers values for the JSON request using data store values
    @Step("And the user set the request headers using data stores as follows <table>")
    public void setRequestHeadersFromDataStores(Table table) throws IOException {
        commonStepImpl.setRequestHeadersFromDataStores(table);
    }

    // Use this method to set the attribute values for the JSON request template in the Excel file
    @Step("And the user set the request attributes as follows <table>")
    public void setRequestPayloadJsonAttributes(Table table) throws IOException {
        commonStepImpl.setRequestAttributes(table);
    }

    // Use this method to set the attribute values for the JSON request template in the Excel file using data store values
    @Step("And the user set the request attributes using data stores as follows <table>")
    public void setPayloadJsonAttributesFromDataStores(Table table) throws IOException {
        commonStepImpl.setPayloadJsonAttributesFromDataStores(table);
    }

    // Use this method to set a custom request payload
    @Step("And the user set the request payload as follows <payload>")
    public void setRequestPayload(String payload) throws IOException {
        commonStepImpl.setRequestPayload(payload);
    }

    // Use this method to set the form-data key values for the request template in the Excel file
    @Step("And the user set the form-data key value pairs as follows <table>")
    public void setFormData(Table table) throws IOException {
        commonStepImpl.setFormData(table);
    }

    // Use this method to set the form-data key values for the request template in the Excel file using data store values
    @Step("And the user set the form-data key value pairs using data stores as follows <table>")
    public void setFormDataFromDataStores(Table table) throws IOException {
        commonStepImpl.setFormDataFromDataStores(table);
    }

    // Use this method to set the multipart file key value pairs for the request template in the Excel file
    @Step("And the user set the multipart file key value pairs as follows <table>")
    public void setMultipartFileData(Table table) throws IOException {
        commonStepImpl.setMultipartFileData(table);
    }

    // Use this method to set the query parameters
    @Step("And the user set the query parameters as follows <table>")
    public void setQueryParams(Table table) throws IOException {
        commonStepImpl.setQueryParams(table);
    }

    // Use this method to set the query parameters using data store values
    @Step("And the user set the query parameters using data stores as follows <table>")
    public void setQueryParamsFromDataStores(Table table) throws IOException {
        commonStepImpl.setQueryParamsFromDataStores(table);
    }

    // Use this method to set the path parameters
    @Step("And the user set the path parameters as follows <table>")
    public void setPathParams(Table table) throws IOException {
        commonStepImpl.setPathParams(table);
    }

    // Use this method to set the path parameters using data store values
    @Step("And the user set the path parameters using data stores as follows <table>")
    public void setPathParamsFromDataStores(Table table) throws IOException {
        commonStepImpl.setPathParamsFromDataStores(table);
    }

    // Use this method to set the attribute values for the JSON request template in the Excel file
    @Step("And the user set the request authentication configurations as follows <table>")
    public void saveRequestAuthConfigurations(Table table) throws IOException {
        commonStepImpl.saveRequestAuthConfigurations(table);
    }

    // Use this method to save strings in data store
    @Step("And the user save the values inside data stores as follows <table>")
    public void saveValueToDataStore(Table table){
        commonStepImpl.saveValueToDataStore(table);
    }

    // Use this method to read strings from data store
    @Step("And the user read the values from data stores as follows <table>")
    public void readValueFromDataStore(Table table){
        commonStepImpl.readValueFromDataStore(table);
    }

    /* Use this method when you need to pass the JSON request in previous step and the access token from the text file into the GET/POST/PUT/DELETE API.
       The "saveRequestAuthConfigurations" must use before using this step */
    @Step("When the user invokes the API")
    public void invokeApi() throws IOException {
        commonStepImpl.invokeApi();
    }

    // Use this method to validate the status code of the response
    @Step("Then the status code for the request is <statusCode>")
    public void verifyResponseStatusCode(String statusCode){
        commonStepImpl.isResponseStatusCodeEqualTo(statusCode);
    }

    // Use this method to validate the content of the response using JSON Path Assertions
    @Step("And the JSON Path values of the response should contains the following <responseFields>")
    public void jsonPathValueContains(Table table){
        commonStepImpl.jsonPathValueContains(table);
    }

    // Use this method to validate the content of the response using JSON Path Assertions with data stores
    @Step("And the JSON Path values of the response should contains the values inside the data stores <responseFields>")
    public void jsonPathValueFromDataStoreContains(Table table){
        commonStepImpl.jsonPathValueFromDataStoreContains(table);
    }

    // Use this method to validate the content of the response using JSON Path Assertions
    @Step("And the JSON Path values of the response should not contains the following <responseFields>")
    public void jsonPathValueNotContains(Table table){
        commonStepImpl.jsonPathValueNotContains(table);
    }

    // Use this method to validate the content of the response using JSON Path Assertions with data stores
    @Step("And the JSON Path values of the response should not contains the values inside the data stores <responseFields>")
    public void jsonPathValueFromDataStoreNotContains(Table table){
        commonStepImpl.jsonPathValueFromDataStoreNotContains(table);
    }

    // Use this method to validate the content of the response using JSON Path Assertions
    @Step("And the JSON Path Assertions for the response should be equal to the following <responseFields>")
    public void jsonPathAssertionEquals(Table table){
        commonStepImpl.jsonPathAssertionEquals(table);
    }

    // Use this method to validate the content of the response using JSON Path Assertions with data stores
    @Step("And the JSON Path Assertions for the response should be equal to the values inside the data stores <responseFields>")
    public void jsonPathAssertionFromDataStoreEquals(Table table){
        commonStepImpl.jsonPathAssertionFromDataStoreEquals(table);
    }

    // Use this method to validate the content of the response using JSON Path Assertions
    @Step("And the JSON Path Assertions for the response should not be equal to the following <responseFields>")
    public void jsonPathAssertionNotEquals(Table table){
        commonStepImpl.jsonPathAssertionNotEquals(table);
    }

    // Use this method to validate the content of the response using JSON Path Assertions with data stores
    @Step("And the JSON Path Assertions for the response should not be equal to the values inside the data stores <responseFields>")
    public void jsonPathAssertionFromDataStoreNotEquals(Table table){
        commonStepImpl.jsonPathAssertionFromDataStoreNotEquals(table);
    }

    // Use this method to validate the node of the JSON Path is exists
    @Step("And the JSON Path Existence in the response should be equal to the following <jsonPaths>")
    public void jsonPathExistence(Table table){
        commonStepImpl.isJsonPathExists(table);
    }

    // Use this method to retrieve and save the values of JSON Paths in the response
    @Step("And save the JSON Path values in the response inside the data stores <table>")
    public void saveJsonPathValue(Table table) throws JSONException {
        commonStepImpl.saveJsonPathValues(table);
    }

    // Use this method to retrieve and save the access token of the login response
    @Step("And save the access token in the response which is located inside the JSON Path of <attributeName>")
    public void saveAccessToken(String jsonPath) throws JSONException {
        commonStepImpl.saveAccessToken(jsonPath);
    }

    // Use this method to retrieve and save the attribute values of the response into text files
    @Step("And save the JSON Path values of the response into text files <table>")
    public void saveResponseData(Table table) throws JSONException {
        commonStepImpl.saveResponseData(table);
    }

    // Use this method to retrieve and save the response JSON array values in a CSV file
    @Step("And save the JSON Array values of the response into CSV files <table>")
    public void saveJsonArrayValuesToCsv(Table table) throws ParseException, IOException {
        commonStepImpl.saveJsonArrayValuesToCsv(table);
    }

    @Step("Given a user successfully connected to the MySQL Driver")
    public void loadMySqlDriver() throws SQLException, ClassNotFoundException {
        mySQLOperator.loadMySqlDriver();
    }

    @Step("When the user connects to the database of <databaseName> using username as <username> and password as <password>")
    public void loadMySqlDatabase (String databaseName, String username, String password) throws SQLException, ClassNotFoundException {
        mySQLOperator.loadMySqlDatabase(databaseName, username, password);
    }

    @Step("Then the user executes the query as <query>")
    public void executeGivenQuery(String query) {
        mySQLOperator.executeGivenQuery(query);
    }

    @Step("And the results obtained from the database should contain the following <table>")
    public void verifyResults( Table table) throws SQLException, ClassNotFoundException {
        mySQLOperator.verifyResults(table);
    }

    @Step("And the results obtained from the database should equal to the following <table>")
    public void verifyAllResults( Table table) throws SQLException, ClassNotFoundException {
        mySQLOperator.verifyAllResults(table);
    }

    @Step("And the user close the database connection")
    public void closeDbConnection() throws Exception {
        mySQLOperator.closeDbConnection();
    }


}
