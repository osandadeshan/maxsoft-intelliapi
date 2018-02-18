package com.maxsoft.ata.request;

import com.maxsoft.ata.util.FileOperator;
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


public class CommonStepDefinitions extends BaseClass {
    public static final String FILE_SYNTAX = "<file:";
    public static final int FILE_SYNTAX_CHARACTER_COUNT = 6;

	// Use this method to print the testing environment name in the HTML report
	public void testEnvDetails(){
		testingEnvDetails();
	}

	// Use this method at the beginning of the scenario to identify which API is going to use in that scenario
	public void apiToBeInvoked(String apiEndpointName) throws IOException {
		super.apiToBeInvoked(apiEndpointName);
	}

	// Use this method to replace column values into timestamps by column name of a CSV file
	public void replaceCSVColumnValuesToTimestamps(String filePath, String columnName, String timestampPattern) throws IOException {
		replaceAllColumnValuesToTimestamps(CURRENT_DIRECTORY + filePath, columnName, timestampPattern);
	}

	// Use this method to set the header values for the JSON request template in the Excel file
	public void setRequestHeaders(Table table) throws IOException {
		List<TableRow> rows = table.getTableRows();
		List<String> columnNames = table.getColumnNames();
		Headers.clearHeaders();
		for (TableRow row : rows) {
            if (row.getCell(columnNames.get(1)).substring(0, Math.min(row.getCell(columnNames.get(1)).length(), FILE_SYNTAX_CHARACTER_COUNT)).toLowerCase().equals(FILE_SYNTAX)) {
                Headers.setRequestHeaders(row.getCell(columnNames.get(0)), FileOperator.readFromFile(CURRENT_DIRECTORY + row.getCell(columnNames.get(1)).substring(FILE_SYNTAX_CHARACTER_COUNT, row.getCell(columnNames.get(1)).length() - 1)));
            } else {
                Headers.setRequestHeaders(row.getCell(columnNames.get(0)), row.getCell(columnNames.get(1)));
            }
		}
		Headers.getFinalHeaders();
		Headers.printHeaders();
	}

	// Use this method to set the header values for the JSON request template in the Excel file using data store values
	public void setRequestHeadersFromDataStores(Table table) throws IOException {
		List<TableRow> rows = table.getTableRows();
		List<String> columnNames = table.getColumnNames();
		Headers.clearHeaders();
		for (TableRow row : rows) {
			String headerName = row.getCell(columnNames.get(0));
			String isRetrievedFromDataStore = row.getCell(columnNames.get(1));
			String dataStoreType = row.getCell(columnNames.get(2));
			String dataStoreVariableName = row.getCell(columnNames.get(3));
			String headerValue = row.getCell(columnNames.get(4));
			if (isRetrievedFromDataStore.toLowerCase().equals("true") || isRetrievedFromDataStore.toLowerCase().equals("yes") || isRetrievedFromDataStore.toLowerCase().equals("y")) {
				Headers.setRequestHeaders(headerName, readFromDataStore(dataStoreType, dataStoreVariableName));
			} else {
                if (headerValue.substring(0, Math.min(headerValue.length(), FILE_SYNTAX_CHARACTER_COUNT)).toLowerCase().equals(FILE_SYNTAX)) {
                    Headers.setRequestHeaders(headerName, FileOperator.readFromFile(CURRENT_DIRECTORY + headerValue.substring(FILE_SYNTAX_CHARACTER_COUNT, headerValue.length() - 1)));
                } else {
                    Headers.setRequestHeaders(headerName, headerValue);
                }
			}
		}
		Headers.getFinalHeaders();
		Headers.printHeaders();
	}

	// Use this method to set the attribute values for the JSON request template in the Excel file
	public void setRequestAttributes(Table table) throws IOException {
		List<TableRow> rows = table.getTableRows();
		List<String> columnNames = table.getColumnNames();
		JsonPayload.setRequestToDefault();
		for (TableRow row : rows) {
			if (row.getCell(columnNames.get(1)).equalsIgnoreCase("\"null\"")){
				JsonPayload.setJsonAttributeValueAs("\""+row.getCell(columnNames.get(0))+"\"", "null");
			}
			else if (row.getCell(columnNames.get(1)).equalsIgnoreCase("null")){
				JsonPayload.setJsonAttributeValueAs(row.getCell(columnNames.get(0)), "null");
			}
			else if (row.getCell(columnNames.get(1)).substring(0, Math.min(row.getCell(columnNames.get(1)).length(), FILE_SYNTAX_CHARACTER_COUNT)).toLowerCase().equals(FILE_SYNTAX)) {
			  JsonPayload.setJsonAttributeValueAs(row.getCell(columnNames.get(0)), FileOperator.readFromFile(CURRENT_DIRECTORY + row.getCell(columnNames.get(1)).substring(FILE_SYNTAX_CHARACTER_COUNT, row.getCell(columnNames.get(1)).length()-1)));
            }
			else {
				JsonPayload.setJsonAttributeValueAs(row.getCell(columnNames.get(0)), row.getCell(columnNames.get(1)));
			}
		}
		JsonPayload.saveFinalJsonRequestBody();
	}

	// Use this method to set the attribute values for the JSON request template in the Excel file using data store values
	public void setPayloadJsonAttributesFromDataStores(Table table) throws IOException {
		List<TableRow> rows = table.getTableRows();
		List<String> columnNames = table.getColumnNames();
		JsonPayload.setRequestToDefault();
		for (TableRow row : rows) {
		    String valueToBeReplaced = row.getCell(columnNames.get(0));
		    String isRetrievedFromDataStore = row.getCell(columnNames.get(1));
		    String dataStoreType = row.getCell(columnNames.get(2));
		    String dataStoreVariableName = row.getCell(columnNames.get(3));
		    String replacementValue = row.getCell(columnNames.get(4));

			if (isRetrievedFromDataStore.toLowerCase().equals("true") || isRetrievedFromDataStore.toLowerCase().equals("yes") || isRetrievedFromDataStore.toLowerCase().equals("y")){
                JsonPayload.setJsonAttributeValueAs(valueToBeReplaced, readFromDataStore(dataStoreType, dataStoreVariableName));
            } else {
                if (replacementValue.equalsIgnoreCase("\"null\"")){
                    JsonPayload.setJsonAttributeValueAs("\""+valueToBeReplaced+"\"", "null");
                }
                else if (replacementValue.equalsIgnoreCase("null")){
                    JsonPayload.setJsonAttributeValueAs(valueToBeReplaced, "null");
                }
                else if (replacementValue.substring(0, Math.min(replacementValue.length(), FILE_SYNTAX_CHARACTER_COUNT)).toLowerCase().equals(FILE_SYNTAX)) {
                    JsonPayload.setJsonAttributeValueAs(valueToBeReplaced, FileOperator.readFromFile(CURRENT_DIRECTORY + replacementValue.substring(FILE_SYNTAX_CHARACTER_COUNT, replacementValue.length() - 1)));
                } else {
                    JsonPayload.setJsonAttributeValueAs(valueToBeReplaced, replacementValue);
                }
            }
		}
		JsonPayload.saveFinalJsonRequestBody();
	}

	// Use this method to set a custom request payload
	public void setRequestPayload(String payload) throws IOException {
		JsonPayload.saveFinalJsonRequestBody(payload);
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

	public void saveRequestAuthConfigurations(Table configTable) {
		List<TableRow> rows = configTable.getTableRows();
		List<String> columnNames = configTable.getColumnNames();
		for (TableRow row : rows) {
			saveValueForScenario(row.getCell(columnNames.get(0)), row.getCell(columnNames.get(1)));
		}
	}

    public void setQueryParams(Table parameterTable){
        List<TableRow> rows = parameterTable.getTableRows();
        List<String> columnNames = parameterTable.getColumnNames();
        String queryParams = "?";
        for (TableRow row : rows) {
            if (row.getCell(columnNames.get(1)).substring(0, Math.min(row.getCell(columnNames.get(1)).length(), FILE_SYNTAX_CHARACTER_COUNT)).toLowerCase().equals(FILE_SYNTAX)) {
                queryParams = queryParams.concat(row.getCell(columnNames.get(0)) + "=" + FileOperator.readFromFile(CURRENT_DIRECTORY + row.getCell(columnNames.get(1)).substring(FILE_SYNTAX_CHARACTER_COUNT, row.getCell(columnNames.get(1)).length() - 1)) + "&");
            } else {
                queryParams = queryParams.concat(row.getCell(columnNames.get(0)) + "=" + row.getCell(columnNames.get(1)) + "&");
            }
        }
        queryParams = queryParams.replaceAll(".$", "");
        System.out.println("Query parameters which will append to the request URL: " + queryParams);
        Gauge.writeMessage("Query parameters which will append to the request URL: " + queryParams);
        saveValueForScenario("queryParams", queryParams);
    }

    public void setQueryParamsFromDataStores(Table parameterTable){
        List<TableRow> rows = parameterTable.getTableRows();
        List<String> columnNames = parameterTable.getColumnNames();
        String queryParams = "?";
        for (TableRow row : rows) {
            String queryName = row.getCell(columnNames.get(0));
            String isRetrievedFromDataStore = row.getCell(columnNames.get(1));
            String dataStoreType = row.getCell(columnNames.get(2));
            String dataStoreVariableName = row.getCell(columnNames.get(3));
            String queryValue = row.getCell(columnNames.get(4));
            if (isRetrievedFromDataStore.toLowerCase().equals("true") || isRetrievedFromDataStore.toLowerCase().equals("yes") || isRetrievedFromDataStore.toLowerCase().equals("y")) {
                queryParams = queryParams.concat(queryName + "=" + readFromDataStore(dataStoreType, dataStoreVariableName) + "&");
            } else {
                if (queryValue.substring(0, Math.min(queryValue.length(), FILE_SYNTAX_CHARACTER_COUNT)).toLowerCase().equals(FILE_SYNTAX)) {
                    queryParams = queryParams.concat(queryName + "=" + FileOperator.readFromFile(CURRENT_DIRECTORY + queryValue.substring(FILE_SYNTAX_CHARACTER_COUNT, queryValue.length() - 1)) + "&");
                } else {
                    queryParams = queryParams.concat(queryName + "=" + queryValue + "&");
                }
            }
        }
        queryParams = queryParams.replaceAll(".$", "");
        System.out.println("Query parameters which will append to the request URL: " + queryParams);
        Gauge.writeMessage("Query parameters which will append to the request URL: " + queryParams);
        saveValueForScenario("queryParams", queryParams);
    }

    public void setPathParams(Table parameterTable){
        List<TableRow> rows = parameterTable.getTableRows();
        List<String> columnNames = parameterTable.getColumnNames();
        String pathParams = "/";
        for (TableRow row : rows) {
            if (row.getCell(columnNames.get(1)).substring(0, Math.min(row.getCell(columnNames.get(1)).length(), FILE_SYNTAX_CHARACTER_COUNT)).toLowerCase().equals(FILE_SYNTAX)) {
                pathParams = pathParams.concat(FileOperator.readFromFile(CURRENT_DIRECTORY + row.getCell(columnNames.get(1)).substring(FILE_SYNTAX_CHARACTER_COUNT, row.getCell(columnNames.get(1)).length() - 1)));
            } else {
                pathParams = pathParams.concat(row.getCell(columnNames.get(1)));
            }
            pathParams = pathParams.concat("/");
        }
        pathParams = pathParams.substring(0, pathParams.length() - 1);
        System.out.println("Path parameters which will append to the request URL:" + pathParams);
        Gauge.writeMessage("Path parameters which will append to the request URL:" + pathParams);
        saveValueForScenario("pathParams", pathParams);
    }

    public void setPathParamsFromDataStores(Table parameterTable){
        List<TableRow> rows = parameterTable.getTableRows();
        List<String> columnNames = parameterTable.getColumnNames();
        String pathParams = "/";
        for (TableRow row : rows) {
            String isRetrievedFromDataStore = row.getCell(columnNames.get(1));
            String dataStoreType = row.getCell(columnNames.get(2));
            String dataStoreVariableName = row.getCell(columnNames.get(3));
            String pathValue = row.getCell(columnNames.get(4));
                if(isRetrievedFromDataStore.toLowerCase().equals("true") || isRetrievedFromDataStore.toLowerCase().equals("yes") || isRetrievedFromDataStore.toLowerCase().equals("y")) {
                    pathParams = pathParams.concat(readFromDataStore(dataStoreType, dataStoreVariableName));
                } else {
                    if (pathValue.substring(0, Math.min(pathValue.length(), FILE_SYNTAX_CHARACTER_COUNT)).toLowerCase().equals(FILE_SYNTAX)) {
                        pathParams = pathParams.concat(FileOperator.readFromFile(CURRENT_DIRECTORY + pathValue.substring(FILE_SYNTAX_CHARACTER_COUNT, pathValue.length() - 1)));
                    } else {
                        pathParams = pathParams.concat(pathValue);
                    }
                }
            pathParams = pathParams.concat("/");
        }
        pathParams = pathParams.substring(0, pathParams.length() - 1);
        System.out.println("Path parameters which will append to the request URL:" + pathParams);
        Gauge.writeMessage("Path parameters which will append to the request URL:" + pathParams);
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
	   The "saveRequestAuthConfigurations" and "setRequestAttributes" must use before using this step */
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
	
	// Use this method to validate the content of the response
	public void jsonPathValueContains(Table table){
		List<TableRow> rows = table.getTableRows();
		List<String> columnNames = table.getColumnNames();
		for (TableRow row : rows) {
            if (row.getCell(columnNames.get(1)).substring(0, Math.min(row.getCell(columnNames.get(1)).length(), FILE_SYNTAX_CHARACTER_COUNT)).toLowerCase().equals(FILE_SYNTAX)) {
                jsonPathValueContains(row.getCell(columnNames.get(0)), FileOperator.readFromFile(CURRENT_DIRECTORY + row.getCell(columnNames.get(1)).substring(FILE_SYNTAX_CHARACTER_COUNT, row.getCell(columnNames.get(1)).length() - 1)));
            } else {
                jsonPathValueContains(row.getCell(columnNames.get(0)), row.getCell(columnNames.get(1)));
            }
		}
	}

	// Use this method to validate the content of the response with data stores
	public void jsonPathValueFromDataStoreContains(Table table){
		List<TableRow> rows = table.getTableRows();
		List<String> columnNames = table.getColumnNames();
		for (TableRow row : rows) {
            String jsonPath = row.getCell(columnNames.get(0));
            String isRetrievedFromDataStore = row.getCell(columnNames.get(1));
            String dataStoreType = row.getCell(columnNames.get(2));
            String dataStoreVariableName = row.getCell(columnNames.get(3));
            String expectedValue = row.getCell(columnNames.get(4));
            if(isRetrievedFromDataStore.toLowerCase().equals("true") || isRetrievedFromDataStore.toLowerCase().equals("yes") || isRetrievedFromDataStore.toLowerCase().equals("y")) {
                jsonPathValueContains(jsonPath, readFromDataStore(dataStoreType, dataStoreVariableName));
            } else {
                if (expectedValue.substring(0, Math.min(expectedValue.length(), FILE_SYNTAX_CHARACTER_COUNT)).toLowerCase().equals(FILE_SYNTAX)) {
                    jsonPathValueContains(jsonPath, FileOperator.readFromFile(CURRENT_DIRECTORY + expectedValue.substring(FILE_SYNTAX_CHARACTER_COUNT, expectedValue.length() - 1)));
                } else {
                    jsonPathValueContains(jsonPath, expectedValue);
                }
            }
		}
	}

	// Use this method to validate the content of the response
	public void jsonPathValueNotContains(Table table){
		List<TableRow> rows = table.getTableRows();
		List<String> columnNames = table.getColumnNames();
		for (TableRow row : rows) {
            if (row.getCell(columnNames.get(1)).substring(0, Math.min(row.getCell(columnNames.get(1)).length(), FILE_SYNTAX_CHARACTER_COUNT)).toLowerCase().equals(FILE_SYNTAX)) {
                jsonPathValueNotContains(row.getCell(columnNames.get(0)), FileOperator.readFromFile(CURRENT_DIRECTORY + row.getCell(columnNames.get(1)).substring(FILE_SYNTAX_CHARACTER_COUNT, row.getCell(columnNames.get(1)).length() - 1)));
            } else {
                jsonPathValueNotContains(row.getCell(columnNames.get(0)), row.getCell(columnNames.get(1)));
            }
		}
	}

    // Use this method to validate the content of the response with data stores
    public void jsonPathValueFromDataStoreNotContains(Table table){
        List<TableRow> rows = table.getTableRows();
        List<String> columnNames = table.getColumnNames();
        for (TableRow row : rows) {
            String jsonPath = row.getCell(columnNames.get(0));
            String isRetrievedFromDataStore = row.getCell(columnNames.get(1));
            String dataStoreType = row.getCell(columnNames.get(2));
            String dataStoreVariableName = row.getCell(columnNames.get(3));
            String expectedValue = row.getCell(columnNames.get(4));
            if(isRetrievedFromDataStore.toLowerCase().equals("true") || isRetrievedFromDataStore.toLowerCase().equals("yes") || isRetrievedFromDataStore.toLowerCase().equals("y")) {
                jsonPathValueNotContains(jsonPath, readFromDataStore(dataStoreType, dataStoreVariableName));
            } else {
                if (expectedValue.substring(0, Math.min(expectedValue.length(), FILE_SYNTAX_CHARACTER_COUNT)).toLowerCase().equals(FILE_SYNTAX)) {
                    jsonPathValueNotContains(jsonPath, FileOperator.readFromFile(CURRENT_DIRECTORY + expectedValue.substring(FILE_SYNTAX_CHARACTER_COUNT, expectedValue.length() - 1)));
                } else {
                    jsonPathValueNotContains(jsonPath, expectedValue);
                }
            }
        }
    }

	// Use this method to validate the content of the response using JSON Path Assertions
	public void jsonPathAssertionEquals(Table table){
		List<TableRow> rows = table.getTableRows();
		List<String> columnNames = table.getColumnNames();
		for (TableRow row : rows) {
			if (row.getCell(columnNames.get(1)).substring(0, Math.min(row.getCell(columnNames.get(1)).length(), FILE_SYNTAX_CHARACTER_COUNT)).toLowerCase().equals(FILE_SYNTAX)) {
                jsonPathAssertionEquals(row.getCell(columnNames.get(0)), FileOperator.readFromFile(CURRENT_DIRECTORY + row.getCell(columnNames.get(1)).substring(FILE_SYNTAX_CHARACTER_COUNT, row.getCell(columnNames.get(1)).length()-1)));
            } else {
                jsonPathAssertionEquals(row.getCell(columnNames.get(0)), row.getCell(columnNames.get(1)));
            }
		}
	}

    // Use this method to validate the content of the response using JSON Path Assertions with data stores
    public void jsonPathAssertionFromDataStoreEquals(Table table){
        List<TableRow> rows = table.getTableRows();
        List<String> columnNames = table.getColumnNames();
        for (TableRow row : rows) {
            String jsonPath = row.getCell(columnNames.get(0));
            String isRetrievedFromDataStore = row.getCell(columnNames.get(1));
            String dataStoreType = row.getCell(columnNames.get(2));
            String dataStoreVariableName = row.getCell(columnNames.get(3));
            String expectedValue = row.getCell(columnNames.get(4));
            if(isRetrievedFromDataStore.toLowerCase().equals("true") || isRetrievedFromDataStore.toLowerCase().equals("yes") || isRetrievedFromDataStore.toLowerCase().equals("y")) {
                jsonPathAssertionEquals(jsonPath, readFromDataStore(dataStoreType, dataStoreVariableName));
            } else {
                if (expectedValue.substring(0, Math.min(expectedValue.length(), FILE_SYNTAX_CHARACTER_COUNT)).toLowerCase().equals(FILE_SYNTAX)) {
                    jsonPathAssertionEquals(jsonPath, FileOperator.readFromFile(CURRENT_DIRECTORY + expectedValue.substring(FILE_SYNTAX_CHARACTER_COUNT, expectedValue.length()-1)));
                } else {
                    jsonPathAssertionEquals(jsonPath, expectedValue);
                }
            }
        }
    }

	// Use this method to validate the content of the response using JSON Path Assertions
	public void jsonPathAssertionNotEquals(Table table){
		List<TableRow> rows = table.getTableRows();
		List<String> columnNames = table.getColumnNames();
		for (TableRow row : rows) {
            if (row.getCell(columnNames.get(1)).substring(0, Math.min(row.getCell(columnNames.get(1)).length(), FILE_SYNTAX_CHARACTER_COUNT)).toLowerCase().equals(FILE_SYNTAX)) {
                jsonPathAssertionNotEquals(row.getCell(columnNames.get(0)), FileOperator.readFromFile(CURRENT_DIRECTORY + row.getCell(columnNames.get(1)).substring(FILE_SYNTAX_CHARACTER_COUNT, row.getCell(columnNames.get(1)).length() - 1)));
            } else {
                jsonPathAssertionNotEquals(row.getCell(columnNames.get(0)), row.getCell(columnNames.get(1)));
            }
		}
	}

	// Use this method to validate the content of the response using JSON Path Assertions with data stores
	public void jsonPathAssertionFromDataStoreNotEquals(Table table){
		List<TableRow> rows = table.getTableRows();
		List<String> columnNames = table.getColumnNames();
		for (TableRow row : rows) {
			String jsonPath = row.getCell(columnNames.get(0));
			String isRetrievedFromDataStore = row.getCell(columnNames.get(1));
			String dataStoreType = row.getCell(columnNames.get(2));
			String dataStoreVariableName = row.getCell(columnNames.get(3));
			String expectedValue = row.getCell(columnNames.get(4));
			if(isRetrievedFromDataStore.toLowerCase().equals("true") || isRetrievedFromDataStore.toLowerCase().equals("yes") || isRetrievedFromDataStore.toLowerCase().equals("y")) {
                jsonPathAssertionNotEquals(jsonPath, readFromDataStore(dataStoreType, dataStoreVariableName));
            } else {
                if (expectedValue.substring(0, Math.min(expectedValue.length(), FILE_SYNTAX_CHARACTER_COUNT)).toLowerCase().equals(FILE_SYNTAX)) {
                    jsonPathAssertionNotEquals(jsonPath, FileOperator.readFromFile(CURRENT_DIRECTORY + expectedValue.substring(FILE_SYNTAX_CHARACTER_COUNT, expectedValue.length() - 1)));
                } else {
                    jsonPathAssertionNotEquals(jsonPath, expectedValue);
                }
            }
		}
	}

	// Use this method to validate the JSON Path Existence in the response
	public void isJsonPathExists(Table table){
		List<TableRow> rows = table.getTableRows();
		List<String> columnNames = table.getColumnNames();
		for (TableRow row : rows) {
			isJsonPathExists(row.getCell(columnNames.get(0)), Boolean.valueOf(row.getCell(columnNames.get(1))));
		}
	}

	// Use this method to catch and save a jsonPath value of the response
	public void saveJsonPathValues(Table table) throws JSONException {
        List<TableRow> rows = table.getTableRows();
        List<String> columnNames = table.getColumnNames();
        for (TableRow row : rows) {
            saveResponseJsonPathValue(row.getCell(columnNames.get(0)), row.getCell(columnNames.get(1)), row.getCell(columnNames.get(2)));
        }
	}

	// Use this method to catch and save the access token of the login response
	public void saveAccessToken(String jsonPath) throws JSONException {
		super.saveAccessToken(jsonPath);
	}

	// Use this method to save strings in data store
	public void saveValueToDataStore(Table table){
		List<TableRow> rows = table.getTableRows();
		List<String> columnNames = table.getColumnNames();
		for (TableRow row : rows) {
			saveToDataStore(row.getCell(columnNames.get(0)),row.getCell(columnNames.get(1)), row.getCell(columnNames.get(2)));
		}
	}

	// Use this method to read strings from data store
	public void readValueFromDataStore(Table table){
		List<TableRow> rows = table.getTableRows();
		List<String> columnNames = table.getColumnNames();
		for (TableRow row : rows) {
			readFromDataStore(row.getCell(columnNames.get(0)),row.getCell(columnNames.get(1)));
		}
	}


}
