package com.maxsoft.ata.step;

import com.maxsoft.ata.database.MySqlOperator;
import com.maxsoft.ata.request.CommonStepDefinitions;
import com.thoughtworks.gauge.Step;
import com.thoughtworks.gauge.Table;
import org.json.JSONException;
import java.io.IOException;
import java.sql.SQLException;


/**
 * Created by Osanda on 7/18/2017.
 */


public class AllStepsDefinitions{

	private CommonStepDefinitions commonStepDefinitions = new CommonStepDefinitions();
    private MySqlOperator mySQLOperator = new MySqlOperator();

	// Use this method to print the testing environment name in the HTML report
	@Step("Get the configuration details of the testing environment")
	public void testEnvDetails(){
		commonStepDefinitions.testingEnvDetails();
	}
	
	// Use this method at the beginning of the scenario to identify which API is going to use in that scenario
	@Step("Given that a user needs to invoke <apiEndpointName>")
	public void apiToBeInvoked(String apiEndpointName) throws IOException {
		commonStepDefinitions.apiToBeInvoked(apiEndpointName);
	}
	
	// Use this method to set the headers values for the JSON request
	@Step("And the user set the request headers as follows <table>")
	public void setRequestHeaders(Table table) throws IOException {
		commonStepDefinitions.setRequestHeaders(table);
	}

	// Use this method to set the attribute values for the JSON request template in the Excel file
	@Step("And the user set the request attributes as follows <table>")
	public void setRequestPayloadJsonAttributes(Table table) throws IOException {
		commonStepDefinitions.setRequestAttributes(table);
	}

	// Use this method to set the query parameters
	@Step("And the user set the query parameters as follows <table>")
	public void setQueryParams(Table table) throws IOException {
		commonStepDefinitions.setQueryParams(table);
	}

	// Use this method to set the path parameters
	@Step("And the user set the path parameters as follows <table>")
	public void setPathParams(Table table) throws IOException {
		commonStepDefinitions.setPathParams(table);
	}

	// Use this method to set the attribute values for the JSON request template in the Excel file
	@Step("And the user set the request authentication configurations as follows <table>")
	public void saveRequestAuthConfigurations(Table table) throws IOException {
		commonStepDefinitions.saveRequestConfigurations(table);
	}

	/* Use this method when you need to pass the JSON request in previous step and the access token from the text file into the GET/POST/PUT/DELETE API.
	   The "saveRequestAuthConfigurations" must use before using this step */
	@Step("When the user invokes the API")
	public void invokeApi() throws IOException {
		commonStepDefinitions.invokeConfiguredApi();
	}

	// Use this method to validate the status code of the response
	@Step("Then the status code for the request is <statusCode>")
	public void verifyResponseStatusCode(String statusCode){
		commonStepDefinitions.verifyResponseStatusCode(statusCode);
	}
	
	// Use this method to validate the content of the response using JSON Path Assertions
	@Step("And the JSON Path Assertions for the response should be equal to the following <responseFields>")
	public void jsonPathAssertions(Table table){
		commonStepDefinitions.jsonPathAssertions(table);
	}
	
	// Use this method to retrieve and save an attribute value of the response
	@Step("And get the attribute value for the attribute of <attributeName> in the response and save it in a data store named <variableNameOfValueToBeStoredInDataStore>")
	public void retrieveAttributeValue(String attributeName, String variableNameOfValueToBeStoredInDataStore) throws JSONException {
		commonStepDefinitions.retrieveAttributeValue(attributeName, variableNameOfValueToBeStoredInDataStore);
	}

	// Use this method to retrieve and save the access token of the login response
	@Step("And save the access token which is the attribute value of <attributeName> in the response")
	public void retrieveAccessToken(String attributeName) throws JSONException {
		commonStepDefinitions.retrieveAccessToken(attributeName);
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
