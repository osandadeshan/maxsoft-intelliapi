package com.maxsoft.intelliapi.stepdefinition;

/**
 * Project Name : MaxSoft-IntelliAPI
 * Developer    : Osanda Deshan
 * Version      : 1.0.0
 * Date         : 6/30/2018
 * Time         : 3:51 PM
 * Description  :
 **/

import com.maxsoft.intelliapi.database.mongo.MongoStepImpl;
import com.maxsoft.intelliapi.database.mysql.MySqlStepImpl;
import com.maxsoft.intelliapi.api.ApiStepImpl;
import com.thoughtworks.gauge.Step;
import com.thoughtworks.gauge.Table;
import org.json.JSONException;
import org.json.simple.parser.ParseException;
import java.io.IOException;
import java.sql.SQLException;


public class AllStepsDefinitions{

    private ApiStepImpl apiStepImpl = new ApiStepImpl();
    private MongoStepImpl mongoStepImpl = new MongoStepImpl();
    private MySqlStepImpl mySQLStepImpl = new MySqlStepImpl();

    public AllStepsDefinitions() throws IOException {
    }

    // Use this method to print the testing environment name in the HTML report
    @Step("Configurations of the testing environment")
    public void testEnvDetails(){
        apiStepImpl.testingEnvDetails();
    }

    // Use this method at the beginning of the scenario to identify which API is going to use in that scenario
    @Step("Given that a user needs to invoke <apiEndpointName>")
    public void apiToBeInvoked(String apiEndpointName) throws IOException {
        apiStepImpl.apiToBeInvoked(apiEndpointName);
    }

    // Use this method to save property file values into data stores
    @Step("And the user saves environment property file data into data stores <table>")
    public void savePropertyFileValuesToDataStore(Table table) {
        apiStepImpl.savePropertyFileValuesToDataStore(table);
    }

    // Use this method to replace the placeholders inside the API Endpoint in Excel
    @Step("And the user set values to the API endpoint placeholders as follows <table>")
    public void setApiEndpointReplacements(Table table) throws IOException {
        apiStepImpl.setApiEndpointReplacements(table);
    }

    // Use this method to replace the placeholders inside the API Endpoint in Excel using data store values
    @Step("And the user set values to the API endpoint placeholders using data stores as follows <table>")
    public void setApiEndpointReplacementsFromDataStores(Table table) throws IOException {
        apiStepImpl.setApiEndpointReplacementsFromDataStores(table);
    }

    @Step("And replace the row values in <columnName> column of the CSV <filePath> into the <timestampPattern> timestamp pattern")
    public void replaceCSVColumn(String columnName, String filePath, String timestampPattern) throws IOException {
        apiStepImpl.replaceCSVColumnValuesToTimestamps(filePath, columnName, timestampPattern);
    }

    // Use this method to set the headers values for the JSON request
    @Step("And the user set the request headers as follows <table>")
    public void setRequestHeaders(Table table) throws IOException {
        apiStepImpl.setRequestHeaders(table);
    }

    // Use this method to set the headers values for the JSON request using data store values
    @Step("And the user set the request headers using data stores as follows <table>")
    public void setRequestHeadersFromDataStores(Table table) throws IOException {
        apiStepImpl.setRequestHeadersFromDataStores(table);
    }

    // Use this method to set the attribute values for the JSON request template in the Excel file
    @Step("And the user set the request attributes as follows <table>")
    public void setRequestPayloadJsonAttributes(Table table) throws IOException {
        apiStepImpl.setRequestAttributes(table);
    }

    // Use this method to set the attribute values for the JSON request template in the Excel file using data store values
    @Step("And the user set the request attributes using data stores as follows <table>")
    public void setPayloadJsonAttributesFromDataStores(Table table) throws IOException {
        apiStepImpl.setPayloadJsonAttributesFromDataStores(table);
    }

    // Use this method to set a custom request payload
    @Step("And the user set the request payload as follows <payload>")
    public void setRequestPayload(String payload) throws IOException {
        apiStepImpl.setRequestPayload(payload);
    }

    // Use this method to replace the values of the request payload
    @Step("And the user set values to the request payload placeholders as follows <table>")
    public void replaceAttributesInRequestPayload(Table table) throws IOException {
        apiStepImpl.replaceAttributesInRequestPayload(table);
    }

    // Use this method to replace the values of the request payload using data stores
    @Step("And the user set values to the request payload placeholders using data stores as follows <table>")
    public void replaceAttributesInRequestPayloadFromDataStores(Table table) throws IOException {
        apiStepImpl.replaceAttributesInRequestPayloadFromDataStores(table);
    }

    // Use this method to set the form-data key values for the request template in the Excel file
    @Step("And the user set the form-data key value pairs as follows <table>")
    public void setFormData(Table table) throws IOException {
        apiStepImpl.setFormData(table);
    }

    // Use this method to set the form-data key values for the request template in the Excel file using data store values
    @Step("And the user set the form-data key value pairs using data stores as follows <table>")
    public void setFormDataFromDataStores(Table table) throws IOException {
        apiStepImpl.setFormDataFromDataStores(table);
    }

    // Use this method to set the multipart file key value pairs for the request template in the Excel file
    @Step("And the user set the multipart file key value pairs as follows <table>")
    public void setMultipartFileData(Table table) throws IOException {
        apiStepImpl.setMultipartFileData(table);
    }

    // Use this method to set the query parameters
    @Step("And the user set the query parameters as follows <table>")
    public void setQueryParams(Table table) throws IOException {
        apiStepImpl.setQueryParams(table);
    }

    // Use this method to set the query parameters using data store values
    @Step("And the user set the query parameters using data stores as follows <table>")
    public void setQueryParamsFromDataStores(Table table) throws IOException {
        apiStepImpl.setQueryParamsFromDataStores(table);
    }

    // Use this method to set the path parameters
    @Step("And the user set the path parameters as follows <table>")
    public void setPathParams(Table table) throws IOException {
        apiStepImpl.setPathParams(table);
    }

    // Use this method to set the path parameters using data store values
    @Step("And the user set the path parameters using data stores as follows <table>")
    public void setPathParamsFromDataStores(Table table) throws IOException {
        apiStepImpl.setPathParamsFromDataStores(table);
    }

    // Use this method to set the request authentication
    @Step("And the user set the request authentication configurations as follows <table>")
    public void saveRequestAuthConfigurations(Table table) throws IOException {
        apiStepImpl.saveRequestAuthConfigurations(table);
    }

    // Use this method to save data store values as a list in another data store
    @Step("And the user saves the values inside data stores as a <listType> data type list into <dataStoreType> type data store by referencing the variable name as <dataStoreVariableName> <table>")
    public void saveDataStoresAsList(String listType, String dataStoreType, String dataStoreVariableName, Table table){
        apiStepImpl.saveDataStoresAsList(listType, dataStoreType, dataStoreVariableName, table);
    }

    // Use this method to save strings in data store
    @Step("And the user saves the values inside data stores as follows <table>")
    public void saveValueToDataStore(Table table){
        apiStepImpl.saveValueToDataStore(table);
    }

    // Use this method to read strings from data store
    @Step("And the user read the values from data stores as follows <table>")
    public void readValueFromDataStore(Table table){
        apiStepImpl.readValueFromDataStore(table);
    }

    /* Use this method when you need to pass the JSON request in previous step and the access token from the text file into the GET/POST/PUT/DELETE API.
       The "saveRequestAuthConfigurations" must use before using this step */
    @Step("When the user invokes the API")
    public void invokeApi() throws IOException {
        apiStepImpl.invokeApi();
    }

    // Use this method to validate the status code of the response
    @Step("Then the status code for the request is <statusCode>")
    public void verifyResponseStatusCode(String statusCode){
        apiStepImpl.isResponseStatusCodeEqualTo(statusCode);
    }

    // Use this method to validate the content of the response using JSON Path Assertions
    @Step("And the JSON Path values of the response should contains the following <responseFields>")
    public void jsonPathValueContains(Table table){
        apiStepImpl.jsonPathValueContains(table);
    }

    // Use this method to validate the content of the response using JSON Path Assertions with data stores
    @Step("And the JSON Path values of the response should contains the values inside the data stores <responseFields>")
    public void jsonPathValueFromDataStoreContains(Table table){
        apiStepImpl.jsonPathValueFromDataStoreContains(table);
    }

    // Use this method to validate the content of the response using JSON Path Assertions
    @Step("And the JSON Path values of the response should not contains the following <responseFields>")
    public void jsonPathValueNotContains(Table table){
        apiStepImpl.jsonPathValueNotContains(table);
    }

    // Use this method to validate the content of the response using JSON Path Assertions with data stores
    @Step("And the JSON Path values of the response should not contains the values inside the data stores <responseFields>")
    public void jsonPathValueFromDataStoreNotContains(Table table){
        apiStepImpl.jsonPathValueFromDataStoreNotContains(table);
    }

    // Use this method to validate the content of the response using JSON Path Assertions
    @Step("And the JSON Path Assertions for the response should be equal to the following <responseFields>")
    public void jsonPathAssertionEquals(Table table){
        apiStepImpl.jsonPathAssertionEquals(table);
    }

    // Use this method to validate the content of the response using JSON Path Assertions with data stores
    @Step("And the JSON Path Assertions for the response should be equal to the values inside the data stores <responseFields>")
    public void jsonPathAssertionFromDataStoreEquals(Table table){
        apiStepImpl.jsonPathAssertionFromDataStoreEquals(table);
    }

    // Use this method to validate the content of the response using JSON Path Assertions
    @Step("And the JSON Path Assertions for the response should not be equal to the following <responseFields>")
    public void jsonPathAssertionNotEquals(Table table){
        apiStepImpl.jsonPathAssertionNotEquals(table);
    }

    // Use this method to validate the content of the response using JSON Path Assertions with data stores
    @Step("And the JSON Path Assertions for the response should not be equal to the values inside the data stores <responseFields>")
    public void jsonPathAssertionFromDataStoreNotEquals(Table table){
        apiStepImpl.jsonPathAssertionFromDataStoreNotEquals(table);
    }

    // Use this method to validate the node of the JSON Path is exists
    @Step("And the JSON Path Existence in the response should be equal to the following <jsonPaths>")
    public void jsonPathExistence(Table table){
        apiStepImpl.isJsonPathExists(table);
    }

    // Use this method to retrieve and save the values of JSON Paths in the response
    @Step("And save the JSON Path values in the response inside the data stores <table>")
    public void saveJsonPathValue(Table table) throws JSONException {
        apiStepImpl.saveJsonPathValues(table);
    }

    // Use this method to retrieve and save the access token of the login response
    @Step("And save the access token in the response which is located inside the JSON Path of <attributeName>")
    public void saveAccessToken(String jsonPath) throws JSONException {
        apiStepImpl.saveAccessToken(jsonPath);
    }

    // Use this method to retrieve and save the attribute values of the response into text files
    @Step("And save the JSON Path values of the response into text files <table>")
    public void saveResponseData(Table table) throws JSONException {
        apiStepImpl.saveResponseData(table);
    }

    // Use this method to retrieve and save the response JSON array values in a CSV file
    @Step("And save the JSON Array values of the response into CSV files <table>")
    public void saveJsonArrayValuesToCsv(Table table) throws ParseException, IOException {
        apiStepImpl.saveJsonArrayValuesToCsv(table);
    }

    // Use this method to validate the content in data stores
    @Step("And the values inside the data stores equal to the following <table>")
    public void dataStoreValueEquals(Table table) {
        apiStepImpl.dataStoreValueEquals(table);
    }

    // Use this method to compare the content in two data stores
    @Step("And the values inside two data stores should be equal <table>")
    public void compareDataStoresEquals(Table table) {
        apiStepImpl.compareDataStoresEquals(table);
    }

    // Use this method to validate the content in data stores
    @Step("And the values inside the data stores not equal to the following <table>")
    public void dataStoreValueNotEquals(Table table) {
        apiStepImpl.dataStoreValueNotEquals(table);
    }

    // Use this method to compare the content in two data stores
    @Step("And the values inside two data stores should not be equal <table>")
    public void compareDataStoresNotEquals(Table table) {
        apiStepImpl.compareDataStoresNotEquals(table);
    }

    // Use this method to validate the content in data stores
    @Step("And the values inside the data stores contain the following <table>")
    public void dataStoreValueContains(Table table) {
        apiStepImpl.dataStoreValueContains(table);
    }

    // Use this method to compare the content in two data stores
    @Step("And the value inside a data store should contain the value of the other data store <table>")
    public void compareDataStoresContains(Table table) {
        apiStepImpl.compareDataStoresContains(table);
    }

    // Use this method to validate the content in data stores
    @Step("And the values inside the data stores not contain the following <table>")
    public void dataStoreValueNotContains(Table table) {
        apiStepImpl.dataStoreValueNotContains(table);
    }

    // Use this method to compare the content in two data stores
    @Step("And the value inside a data store should not contain the value of the other data store <table>")
    public void compareDataStoresNotContains(Table table) {
        apiStepImpl.compareDataStoresNotContains(table);
    }

    // Use this method to add integer values in data stores and save to a new data store
    @Step("Add the integer values in data stores and save it in a <dataStoreType> type data store named <dataStoreVariableName> <table>")
    public void addIntegerValuesInDataStore(String dataStoreType, String dataStoreVariableName, Table table) {
        apiStepImpl.addIntegerValuesInDataStore(dataStoreType, dataStoreVariableName, table);
    }

    // Use this method to subtract integer values in data stores and save to a new data store
    @Step("Subtract the integer values in data stores and save it in a <dataStoreType> type data store named <dataStoreVariableName> <table>")
    public void subtractIntegerValuesInDataStore(String dataStoreType, String dataStoreVariableName, Table table) {
        apiStepImpl.subtractIntegerValuesInDataStore(dataStoreType, dataStoreVariableName, table);
    }

    // Use this method to divide integer values in data stores and save to a new data store
    @Step("Divide the integer values in data stores and save it in a <dataStoreType> type data store named <dataStoreVariableName> <table>")
    public void divideIntegerValuesInDataStore(String dataStoreType, String dataStoreVariableName, Table table) {
        apiStepImpl.divideIntegerValuesInDataStore(dataStoreType, dataStoreVariableName, table);
    }

    // Use this method to multiply integer values in data stores and save to a new data store
    @Step("Multiply the integer values in data stores and save it in a <dataStoreType> type data store named <dataStoreVariableName> <table>")
    public void multiplyIntegerValuesInDataStore(String dataStoreType, String dataStoreVariableName, Table table) {
        apiStepImpl.multiplyIntegerValuesInDataStore(dataStoreType, dataStoreVariableName, table);
    }

    // Use this method to add decimal values in data stores and save to a new data store
    @Step("Add the decimal values in data stores and save it in a <dataStoreType> type data store named <dataStoreVariableName> <table>")
    public void addDecimalValuesInDataStore(String dataStoreType, String dataStoreVariableName, Table table) {
        apiStepImpl.addDecimalValuesInDataStore(dataStoreType, dataStoreVariableName, table);
    }

    // Use this method to subtract decimal values in data stores and save to a new data store
    @Step("Subtract the decimal values in data stores and save it in a <dataStoreType> type data store named <dataStoreVariableName> <table>")
    public void subtractDecimalValuesInDataStore(String dataStoreType, String dataStoreVariableName, Table table) {
        apiStepImpl.subtractDecimalValuesInDataStore(dataStoreType, dataStoreVariableName, table);
    }

    // Use this method to divide decimal values in data stores and save to a new data store
    @Step("Divide the decimal values in data stores and save it in a <dataStoreType> type data store named <dataStoreVariableName> <table>")
    public void divideDecimalValuesInDataStore(String dataStoreType, String dataStoreVariableName, Table table) {
        apiStepImpl.divideDecimalValuesInDataStore(dataStoreType, dataStoreVariableName, table);
    }

    // Use this method to multiply decimal values in data stores and save to a new data store
    @Step("Multiply the decimal values in data stores and save it in a <dataStoreType> type data store named <dataStoreVariableName> <table>")
    public void multiplyDecimalValuesInDataStore(String dataStoreType, String dataStoreVariableName, Table table) {
        apiStepImpl.multiplyDecimalValuesInDataStore(dataStoreType, dataStoreVariableName, table);
    }

    // Use this method to save current epochTime into data stores
    @Step("And the user saves the current epoch time in <secondsOrMillis> inside data stores <table>")
    public void saveCurrentEpochTime(String secondsOrMillis, Table table) {
        apiStepImpl.saveCurrentEpochTime(secondsOrMillis, table);
    }

    // Use this method to convert a given format timestamp into epochTime and save it into data stores
    @Step("And the user converts the <timestampPattern> formatted <timestamp> timestamp into epoch time in <secondsOrMillis> and saves inside data stores <table>")
    public void saveEpochTime(String timestampPattern, String timestamp, String secondsOrMillis, Table table) throws java.text.ParseException {
        apiStepImpl.saveEpochTime(timestampPattern, timestamp, secondsOrMillis, table);
    }

    // Use this method to save api document test data into data stores
    @Step("And the user saves test data inside excel file into data stores <table>")
    public void saveExcelDataToDataStore(Table table){
        apiStepImpl.saveExcelDataToDataStore(table);
    }

    @Step("Given a user successfully connected to the MySQL Driver")
    public void loadMySqlDriver() {
        mySQLStepImpl.loadMySqlDriver();
    }

    @Step("And the user need to connect to the <databaseName> MySQL database using username as <username> and password as <password>")
    public void loadMySqlDatabase (String databaseName, String username, String password) throws SQLException {
        mySQLStepImpl.loadMySqlDatabase(databaseName, username, password);
    }

    @Step("When the user executes the MySQL query as <query>")
    public void executeMySqlQuery(String query) {
        mySQLStepImpl.executeGivenQuery(query);
    }

    @Step("Then the results obtained from the MySQL database should contain the following <table>")
    public void verifyResults( Table table) throws SQLException {
        mySQLStepImpl.verifyResults(table);
    }

    @Step("Then the results obtained from the MySQL database should equal to the following <table>")
    public void verifyAllResults( Table table) throws SQLException {
        mySQLStepImpl.verifyAllResults(table);
    }

    @Step("And the user close the MySQL database connection")
    public void closeMySqlConnection() throws Exception {
        mySQLStepImpl.closeDbConnection();
    }

    @Step("Given a user need to connect to the <databaseName> Mongo database and <collectionName> collection")
    public void setMongoDatabaseCollection(String databaseName, String collectionName){
        mongoStepImpl.saveDatabaseNameCollectionName(databaseName, collectionName);
    }

    @Step("And the user set the MongoDB authentication as follows <configTable>")
    public void setDatabaseAuthConfigurations(Table configTable){
        mongoStepImpl.saveDatabaseAuthConfigurations(configTable);
    }

    @Step("When the user executes the Mongo query using key as <key> and value as <value>")
    public void executeMongoQuery(String key, String value) throws JSONException {
        mongoStepImpl.executeMongoDbQuery(key, value);
    }

    @Step("When the user executes the Mongo query using data stores as follows <table>")
    public void readDataStoreAndExecuteMongoDbQuery(Table table) throws JSONException {
        mongoStepImpl.readDataStoreAndExecuteMongoDbQuery(table);
    }


}
