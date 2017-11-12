import com.thoughtworks.gauge.Gauge;
import com.thoughtworks.gauge.Table;
import com.thoughtworks.gauge.TableRow;
import io.restassured.http.Header;
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

	// Use this method to set the header values for the JSON request template in the Excel file
	public void setRequestHeaders(Table table) throws IOException {
		List<TableRow> rows = table.getTableRows();
		List<String> columnNames = table.getColumnNames();
		Headers.clearHeaders();
		for (TableRow row : rows) {
			Headers.setRequestHeaders(row.getCell(columnNames.get(0)), row.getCell(columnNames.get(1)));
		}
		Headers.getFinalHeaders();
	}

	// Use this method to set the attribute values for the JSON request template in the Excel file
	public void setRequestAttributes(Table table) throws IOException {
		List<TableRow> rows = table.getTableRows();
		List<String> columnNames = table.getColumnNames();
		JsonPayload.setRequestToDefault();
		for (TableRow row : rows) {
			if (row.getCell(columnNames.get(1)).equalsIgnoreCase("null")){
				JsonPayload.setJsonAttributeValueAs("\""+row.getCell(columnNames.get(0))+"\"", "null");
			} else {
				JsonPayload.setJsonAttributeValueAs(row.getCell(columnNames.get(0)), row.getCell(columnNames.get(1)));
			}
		}
		JsonPayload.saveFinalJsonRequestBody();
	}

	public void invokeApiWithMultiplePathParameters(Table parameterTable) throws IOException {
        List<Header> headerList = Headers.getFinalHeaders();
        invokeApiWithMultiplePathParameters(parameterTable, headerList);
	}

    public void invokeApiWithQueryParameters(Table parameterTable) throws IOException {
        List<Header> headerList = Headers.getFinalHeaders();
        invokeApiWithQueryParameters(parameterTable, headerList);
    }

	public void invokeApiWithQueryParametersNoAuth(Table parameterTable) throws IOException {
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

	public void saveRequestConfigurations(Table configTable) {
		List<TableRow> rows = configTable.getTableRows();
		List<String> columnNames = configTable.getColumnNames();
		for (TableRow row : rows) {
			saveValueForScenario(row.getCell(columnNames.get(0)), row.getCell(columnNames.get(1)));
		}
	}

    public void setQueryParams(Table parameterTable){
        List<TableRow> rows = parameterTable.getTableRows();
        List<String> columnNames = parameterTable.getColumnNames();
        String queryParams = "";
        for (TableRow row : rows) {
            queryParams = queryParams + row.getCell(columnNames.get(0)) + "=" + row.getCell(columnNames.get(1)) + "&";
        }
        queryParams = queryParams.replaceAll(".$", "");
        System.out.println("Query parameters which will append to the request URL: " + queryParams);
        Gauge.writeMessage("Query parameters which will append to the request URL: " + queryParams);
        saveValueForScenario("queryParams", queryParams);
    }

    public void setPathParams(Table parameterTable){
        List<TableRow> rows = parameterTable.getTableRows();
        List<String> columnNames = parameterTable.getColumnNames();
        String pathParams = "";
        for (TableRow row : rows) {
            pathParams = pathParams + row.getCell(columnNames.get(1));
            pathParams = pathParams.concat("/");
        }
        System.out.println("Path parameters which will append to the request URL:");
        System.out.println(pathParams);
        Gauge.writeMessage("Path parameters which will append to the request URL:");
        Gauge.writeMessage(pathParams);
        saveValueForScenario("pathParams", pathParams);
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
		List<Header> headerList = Headers.getFinalHeaders();
		super.invokeApiWithTokenInTextFile(jsonRequest, headerList);
	}

	/* Use this method when you need to pass the JSON request in previous step and the access token from the text file into the GET/POST API.
	   The "saveRequestConfigurations" and "setRequestAttributes" must use before using this step */
	public void invokeConfiguredApi() throws IOException {
		String jsonRequest = String.valueOf(getSavedValueForScenario("finalJsonRequestBody"));
		if (jsonRequest.equals("") || jsonRequest.equals("null")){
		    jsonRequest = "";
        }
		List<Header> headerList = Headers.getFinalHeaders();
		if (headerList.isEmpty() || headerList.equals(null)){
		    headerList.clear();
        }
		super.invokeConfiguredApi(jsonRequest, headerList);
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
		List<Header> headerList = Headers.getFinalHeaders();
		super.invokeApiWithTokenInTextFile(jsonRequest, headerList);
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
		saveResponseAttributeValue(attributeName, variableNameOfValueToBeStoredInDataStore);
		Gauge.writeMessage("Attribute value: " + getSavedValueForSpecification(variableNameOfValueToBeStoredInDataStore));
	}

	// Use this method to catch and save the access token of the login response
	public void retrieveAccessToken(String attributeName) throws JSONException {
		saveAccessToken(attributeName);
	}
	
	
}
