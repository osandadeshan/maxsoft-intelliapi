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
    private DatabaseDataValidation databaseDataValidation= new DatabaseDataValidation();

	// Use this method to print the testing environment name in the HTML report
	@Step("Testing environment details")
	public void testEnvDetails(){
		commonStepDefinitions.testingEnvDetails();
	}
	
	// Use this method at the beginning of the scenario to identify which API is going to use in that scenario
	@Step("Given that a user needs to invoke <apiEndpointName>")
	public void apiToBeInvoked(String apiEndpointName) throws IOException {
		commonStepDefinitions.apiToBeInvoked(apiEndpointName);
	}
	
	// Use this method to set the attribute values for the JSON request template in the Excel file
	@Step("When the user set the request attributes as follows <table>")
	public void setRequestAttributes(Table table) throws IOException {
		commonStepDefinitions.setRequestAttributes(table);
	}

	@Step("When the user invokes the API using the valid access token <accessToken> and following path parameters <parameterTable>")
	public void invokeApiWithMultipleParameters(String accessToken, Table parameterTable) throws IOException {
		commonStepDefinitions.invokeApiWithMultipleParameters(accessToken, parameterTable);
	}

	@Step("When the user invokes the API using the following query parameters <parameterTable>")
	public void invokeApiWithQueryParameters(Table parameterTable) throws IOException {
		commonStepDefinitions.invokeApiWithQueryParameters(parameterTable);
	}
	
	/* Use this method when you need to pass the JSON request in previous step and the access token into the GET/POST API.
	   The "setRequestAttributes" must use before using this step */
	@Step("When the user invokes the API using the access token as <authorizationToken>")
	public void invokeApiInExcelWithToken(String authorizationToken) throws IOException {
		commonStepDefinitions.invokeApiInExcelWithToken(authorizationToken);
	}

	/* Use this method when you need to pass the JSON request in previous step and the access token from the text file into the GET/POST API.
	   The "setRequestAttributes" must use before using this step */
	@Step("When the user invokes the API using the valid access token")
	public void invokeApiInExcelWithToken() throws IOException {
		commonStepDefinitions.invokeApiInExcelWithToken();
	}
	
	// Use this method when you need to pass the JSON request and the access token into the GET/POST API
	@Step("When the user invokes the API using the following request <jsonRequest> and access token <authorizationToken>")
	public void invokeApiWithToken(String jsonRequest, String authorizationToken) throws IOException {
		commonStepDefinitions.invokeApiWithToken(jsonRequest, authorizationToken);
	}
	
	/* Use this method when you need to pass the JSON request into the GET/POST API. The access token will be taken automatically
	   from the response which you have invoked previously */
	@Step("When the user invokes the API using the following request <jsonRequest> and valid access token which saved in the data store named <accessToken>")
	public void invokeApiWithAccessToken(String jsonRequest, String accessToken) throws IOException {
		commonStepDefinitions.invokeApiWithAccessToken(jsonRequest, accessToken);
	}

	/* Use this method when you need to pass the JSON request into the GET/POST API. The access token will be taken automatically
	   from the text file which is saved for the login request you have invoked previously */
	@Step("When the user invokes the API using the following request <jsonRequest> and valid access token")
	public void invokeApiWithAccessToken(String jsonRequest) throws IOException {
		commonStepDefinitions.invokeApiWithAccessToken(jsonRequest);
	}
	
	// Use this method when you need to pass the JSON request into the GET/POST/PUT API which has no authentication
	@Step("When the user invokes the API using the following request <jsonRequest>")
	public void invokeApiWithNoAuth(String jsonRequest) throws IOException {
		commonStepDefinitions.invokeApiWithNoAuth(jsonRequest);
	}

	// Use this method when you need to invoke GET/POST/PUT API with previously set JSON payload which has no authentication
	@Step("When the user invokes the API using the above request payload")
	public void invokeApiWithNoAuth() throws IOException {
		commonStepDefinitions.invokeApiWithNoAuth();
	}
	
	// Use this method when you need to invoke the GET/POST API which has authentication and has no JSON request body
	@Step("When the user invokes the API using access token <authorizationToken>")
	public void invokeApiWithNoJsonRequest(String authorizationToken) throws IOException {
		commonStepDefinitions.invokeApiWithNoJsonRequest(authorizationToken);
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
	
	// Use this method to catch and save an attribute value of the response
	@Step("And get the attribute value for the attribute of <attributeName> in the response and save it in the data store named <variableNameOfValueToBeStoredInDataStore>")
	public void retrieveAttributeValue(String attributeName, String variableNameOfValueToBeStoredInDataStore) throws JSONException {
		commonStepDefinitions.retrieveAttributeValue(attributeName, variableNameOfValueToBeStoredInDataStore);
	}

	// Use this method to catch and save the access token of the login response
	@Step("And save the access token which is the attribute value of <attributeName> in the response")
	public void retrieveAccessToken(String attributeName) throws JSONException {
		commonStepDefinitions.retrieveAccessToken(attributeName);
	}

    @Step("Given a user successfully loaded the MySQL Driver")
    public void loadMySqlDriver() throws SQLException, ClassNotFoundException {
        databaseDataValidation.loadMySqlDriver();
    }

    @Step("When the user connects to the database of <databaseName> using username as <username> and password as <password>")
    public void loadMySqlDatabase (String databaseName, String username, String password) throws SQLException, ClassNotFoundException {
        databaseDataValidation.loadMySqlDatabase(databaseName, username, password);
    }

    @Step("Then the user executes query of <query>")
    public void executeGivenQuery(String query) {
        databaseDataValidation.executeGivenQuery(query);
    }

    @Step("And the results obtained from the database should contain the following <table>")
    public void verifyResults( Table table) throws SQLException, ClassNotFoundException {
        databaseDataValidation.verifyResults(table);
    }

    @Step("And the results obtained from the database should equal to the following <table>")
    public void verifyAllResults( Table table) throws SQLException, ClassNotFoundException {
        databaseDataValidation.verifyAllResults(table);
    }

    @Step("Close the database connection")
    public void closeDbConnection() throws Exception {
        databaseDataValidation.closeDbConnection();
    }
	
}
