import com.thoughtworks.gauge.Gauge;
import com.thoughtworks.gauge.Table;
import com.thoughtworks.gauge.TableRow;
import org.json.JSONException;
import java.io.IOException;
import java.util.List;


/**
 * Created by Osanda on 7/18/2017.
 */


public class CommonStepDefinitions extends BaseClass{

	// Use this method to print the testing environment name in the HTML report
	public void testEnvDetails(){
		testingEnvDetails();
	}
	
	// Use this method at the beginning of the scenario to identify which API is going to use in that scenario
	public void apiToBeInvoked(String apiEndpointName) throws IOException {
		super.apiToBeInvoked(apiEndpointName);
	}
	
	// Use this method to set the attribute values for the JSON request template in the Excel file
	public void setRequestAttributes(Table table) throws IOException {
		List<TableRow> rows = table.getTableRows();
		List<String> columnNames = table.getColumnNames();
		RequestCreator.setRequestToDefault();
		for (TableRow row : rows) {
			if (row.getCell(columnNames.get(1)).equalsIgnoreCase("null")){
				RequestCreator.setRequestAttributeValueAs("\""+row.getCell(columnNames.get(0))+"\"", "null");
			} else {
				RequestCreator.setRequestAttributeValueAs(row.getCell(columnNames.get(0)), row.getCell(columnNames.get(1)));
			}
		}
		RequestCreator.getFinalJsonRequestBody();
	}

	public void invokeApiWithMultipleParameters(String accessToken, Table parameterTable) throws IOException {
		List<TableRow> rows = parameterTable.getTableRows();
		List<String> columnNames = parameterTable.getColumnNames();
		String param = "";
		for (TableRow row : rows) {
			param = param + row.getCell(columnNames.get(1));
			param = param.concat("/");
		}
		System.out.println(param);
		super.getAPIByAppendingParam(param, accessToken);
		printApiEndpoint(ApiEndpoints.getApiEndpointByName(getSavedValueForScenario("API_NAME")).concat("/" + param));
	}

	public void invokeApiWithQueryParameters(Table parameterTable) throws IOException {
		List<TableRow> rows = parameterTable.getTableRows();
		List<String> columnNames = parameterTable.getColumnNames();
		String query = "";
		for (TableRow row : rows) {
			query = query + row.getCell(columnNames.get(0)) + "=" + row.getCell(columnNames.get(1)) + "&";
		}
		query = query.replaceAll(".$", "");
		if (query.equals("=")){
			super.getAPI("");
		} else {
			super.getAPI(query);
		}
	}
	
	/* Use this method when you need to pass the JSON request in previous step and the access token into the GET/POST API.
	   The "setRequestAttributes" must use before using this step */
	public void invokeApiInExcelWithToken(String authorizationToken) throws IOException {
		String jsonRequest = getSavedValueForScenario("finalJsonRequestBody");
		super.invokeApiWithToken(jsonRequest, authorizationToken);
	}

	/* Use this method when you need to pass the JSON request in previous step and the access token from the text file into the GET/POST API.
	   The "setRequestAttributes" must use before using this step */
	public void invokeApiInExcelWithToken() throws IOException {
		String jsonRequest = getSavedValueForScenario("finalJsonRequestBody");
		super.invokeApiWithTokenInTextFile(jsonRequest);
	}
	
	// Use this method when you need to pass the JSON request and the access token into the GET/POST API
	public void invokeApiWithToken(String jsonRequest, String authorizationToken) throws IOException {
		super.invokeApiWithToken(jsonRequest, authorizationToken);
	}
	
	/* Use this method when you need to pass the JSON request into the GET/POST API. The access token will be taken automatically
	   from the response which you have invoked previously */
	public void invokeApiWithAccessToken(String jsonRequest, String accessToken) throws IOException {
		super.invokeApiWithTokenInDataStore(jsonRequest, accessToken);
	}

	/* Use this method when you need to pass the JSON request into the GET/POST API. The access token will be taken automatically
	   from the text file which is saved for the login request you have invoked previously */
	public void invokeApiWithAccessToken(String jsonRequest) throws IOException {
		super.invokeApiWithTokenInTextFile(jsonRequest);
	}
	
	// Use this method when you need to pass the JSON request into the GET/POST/PUT API which has no authentication
	public void invokeApiWithNoAuth(String jsonRequest) throws IOException {
		super.invokeApiWithNoAuth(jsonRequest);
	}

	// Use this method when you need to invoke GET/POST/PUT API with previously set JSON payload which has no authentication
	public void invokeApiWithNoAuth() throws IOException {
		String jsonRequest = getSavedValueForScenario("finalJsonRequestBody");
		super.invokeApiWithNoAuth(jsonRequest);
	}
	
	// Use this method when you need to invoke the GET/POST API which has authentication and has no JSON request body
	public void invokeApiWithNoJsonRequest(String authorizationToken) throws IOException {
		super.invokeApiWithoutRequestWithToken(authorizationToken);
	}
	
	// Use this method to validate the status code of the response
	public void verifyResponseStatusCode(String statusCode){
		super.verifyResponseStatusCode(statusCode);
	}
	
	// Use this method to validate the content of the response using JSON Path Assertions
	public void jsonPathAssertions(Table table){
		List<TableRow> rows = table.getTableRows();
		List<String> columnNames = table.getColumnNames();
		for (TableRow row : rows) {
			jsonPathAssertion(row.getCell(columnNames.get(0)),row.getCell(columnNames.get(1)));
		}
	}
	
	// Use this method to catch and save an attribute value of the response
	public void retrieveAttributeValue(String attributeName, String variableNameOfValueToBeStoredInDataStore) throws JSONException {
		getResponseAttributeValue(attributeName, variableNameOfValueToBeStoredInDataStore);
		Gauge.writeMessage("Attribute value: " + getSavedValueForSpecification(variableNameOfValueToBeStoredInDataStore));
	}

	// Use this method to catch and save the access token of the login response
	public void retrieveAccessToken(String attributeName) throws JSONException {
		saveAccessToken(attributeName);
	}
	
	
}
