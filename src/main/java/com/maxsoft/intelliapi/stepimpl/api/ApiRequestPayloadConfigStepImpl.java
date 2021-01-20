package com.maxsoft.intelliapi.stepimpl.api;

import com.maxsoft.intelliapi.util.fileoperator.TextFile;
import com.maxsoft.intelliapi.util.reader.EnvironmentPropertyReader;
import com.thoughtworks.gauge.Step;
import com.thoughtworks.gauge.Table;
import com.thoughtworks.gauge.TableRow;

import java.util.List;

import static com.maxsoft.intelliapi.Constants.*;
import static com.maxsoft.intelliapi.api.ApiRequestPayloadProcessor.*;
import static com.maxsoft.intelliapi.api.ApiResponseProcessor.saveResponseJsonPathValue;
import static com.maxsoft.intelliapi.util.DataStoreProcessor.*;
import static com.maxsoft.intelliapi.util.FrameworkUtil.*;
import static com.maxsoft.intelliapi.util.LogUtil.printInfo;

/**
 * Project Name    : MaxSoft-IntelliAPI
 * Developer       : Osanda Deshan
 * Version         : 1.0.0
 * Date            : 12/19/2020
 * Time            : 10:28 AM
 * Description     :
 **/

public class ApiRequestPayloadConfigStepImpl {

    // Use this method at the beginning of the scenario to identify which API is going to use in that scenario
    @Step("Given that a user needs to invoke <apiEndpointName>")
    public void apiToBeInvoked(String apiEndpointName) {
        initializeApiToBeInvoked(apiEndpointName);
    }

    // Use this method before invoking a GET API from a request url in the response's JSON path
    @Step("Given that a user needs to invoke a GET API from the JSON Path value <jsonPath>")
    public void saveApiEndpointInResponseBody(String jsonPath) {
        saveResponseJsonPathValue(SCENARIO, VAR_API_ENDPOINT, jsonPath);
    }

    // Use this method to replace the placeholders inside the API Endpoint in Excel
    @Step("And the user set values to the API endpoint placeholders as follows <table>")
    public void setApiEndpointReplacements(Table table) {
        List<TableRow> rows = table.getTableRows();
        List<String> columnNames = table.getColumnNames();
        String invokingEndpoint = EnvironmentPropertyReader.getBaseUrl()
                .concat(getSavedValueForScenario(VAR_API_ENDPOINT));

        for (TableRow row : rows) {
            String placeholder = row.getCell(columnNames.get(0));
            String replacementText = row.getCell(columnNames.get(1));

            if (hasContainedFileSyntax(replacementText)) {
                invokingEndpoint = invokingEndpoint.replaceAll(placeholder,
                        TextFile.read(getFilePathFromFileSyntax(replacementText)));
            } else {
                invokingEndpoint = invokingEndpoint.replaceAll(placeholder, replacementText);
            }
        }
        saveValueForScenario(VAR_API_ENDPOINT, invokingEndpoint);
        printInfo("The final API Endpoint is:\n" + invokingEndpoint);
    }

    // Use this method to replace the placeholders inside the API Endpoint in Excel using data store values
    @Step("And the user set values to the API endpoint placeholders using data stores as follows <table>")
    public void setApiEndpointReplacementsFromDataStores(Table table) {
        List<TableRow> rows = table.getTableRows();
        List<String> columnNames = table.getColumnNames();
        String invokingEndpoint = EnvironmentPropertyReader.getBaseUrl()
                .concat(getSavedValueForScenario(VAR_API_ENDPOINT));

        for (TableRow row : rows) {
            String placeholder = row.getCell(columnNames.get(0));
            String isRetrievedFromDataStore = row.getCell(columnNames.get(1));
            String dataStoreType = row.getCell(columnNames.get(2));
            String dataStoreVariableName = row.getCell(columnNames.get(3));
            String replacementText = row.getCell(columnNames.get(4));

            if (isTrue(isRetrievedFromDataStore)) {
                invokingEndpoint = invokingEndpoint.replaceAll(placeholder,
                        readFromDataStore(dataStoreType, dataStoreVariableName));
            } else {
                if (hasContainedFileSyntax(replacementText)) {
                    invokingEndpoint = invokingEndpoint.replaceAll(placeholder,
                            TextFile.read(getFilePathFromFileSyntax(replacementText)));
                } else {
                    invokingEndpoint = invokingEndpoint.replaceAll(placeholder, replacementText);
                }
            }
        }
        saveValueForScenario(VAR_API_ENDPOINT, invokingEndpoint);
        printInfo("The final API Endpoint is:\n" + invokingEndpoint);
    }

    // Use this method to set the headers values for the JSON request
    @Step("And the user set the request headers as follows <table>")
    public void setRequestHeaders(Table table) {
        List<TableRow> rows = table.getTableRows();
        List<String> columnNames = table.getColumnNames();
        String headerNames = "", headerValues = "";

        for (TableRow row : rows) {
            String headerName = row.getCell(columnNames.get(0));
            String headerValue = row.getCell(columnNames.get(1));

            if (hasContainedFileSyntax(headerValue)) {
                headerNames = headerNames.concat(headerName).concat(",");
                headerValues = headerValues.concat(TextFile.read(getFilePathFromFileSyntax(headerValue))).concat(",");
            } else {
                headerNames = headerNames.concat(headerName).concat(",");
                headerValues = headerValues.concat(headerValue).concat(",");
            }
        }
        headerNames = headerNames.replaceFirst(".$","");
        headerValues = headerValues.replaceFirst(".$","");
        saveValueForScenario(VAR_API_HEADER_NAMES_LIST, headerNames);
        saveValueForScenario(VAR_API_HEADER_VALUES_LIST, headerValues);
        printHeaders(headerNames, headerValues);
    }

    // Use this method to set the headers values for the JSON request using data store values
    @Step("And the user set the request headers using data stores as follows <table>")
    public void setRequestHeadersFromDataStores(Table table) {
        List<TableRow> rows = table.getTableRows();
        List<String> columnNames = table.getColumnNames();
        String headerNames = "", headerValues = "";

        for (TableRow row : rows) {
            String headerName = row.getCell(columnNames.get(0));
            String isRetrievedFromDataStore = row.getCell(columnNames.get(1));
            String dataStoreType = row.getCell(columnNames.get(2));
            String dataStoreVariableName = row.getCell(columnNames.get(3));
            String headerValue = row.getCell(columnNames.get(4));

            if (isTrue(isRetrievedFromDataStore)) {
                headerNames = headerNames.concat(headerName).concat(",");
                headerValues = headerValues.concat(readFromDataStore(dataStoreType, dataStoreVariableName)).concat(",");
            } else {
                if (hasContainedFileSyntax(headerValue)) {
                    headerNames = headerNames.concat(headerName).concat(",");
                    headerValues = headerValues.concat(TextFile.read(getFilePathFromFileSyntax(headerValue))).concat(",");
                } else {
                    headerNames = headerNames.concat(headerName).concat(",");
                    headerValues = headerValues.concat(headerValue).concat(",");
                }
            }
        }
        headerNames = headerNames.replaceFirst(".$","");
        headerValues = headerValues.replaceFirst(".$","");
        saveValueForScenario(VAR_API_HEADER_NAMES_LIST, headerNames);
        saveValueForScenario(VAR_API_HEADER_VALUES_LIST, headerValues);
        printHeaders(headerNames, headerValues);
    }

    // Use this method to set the attribute values for the JSON request template in the Excel file
    @Step("And the user set the request attributes as follows <table>")
    public void setRequestPayloadJsonAttributes(Table table) {
        List<TableRow> rows = table.getTableRows();
        List<String> columnNames = table.getColumnNames();
        String jsonRequestBody = getSavedValueForScenario(VAR_API_JSON_REQUEST_BODY);

        for (TableRow row : rows) {
            String placeholder = row.getCell(columnNames.get(0));
            String replacementText = row.getCell(columnNames.get(1));

            if (replacementText.equalsIgnoreCase("\"null\"")){
                jsonRequestBody = jsonRequestBody.replaceAll("\"" + placeholder + "\"", "null");
            }
            else if (replacementText.equalsIgnoreCase("null")){
                jsonRequestBody = jsonRequestBody.replaceAll(placeholder, "null");
            }
            else if (hasContainedFileSyntax(replacementText)) {
                jsonRequestBody = jsonRequestBody.replaceAll(placeholder,
                        TextFile.read(getFilePathFromFileSyntax(replacementText)));
            }
            else {
                jsonRequestBody = jsonRequestBody.replaceAll(placeholder, replacementText);
            }
        }
        saveValueForScenario(VAR_API_JSON_REQUEST_BODY, jsonRequestBody);
        printInfo("The JSON request body that you are going to use for the API is:\n" + jsonRequestBody);
    }

    // Use this method to set the attribute values for the JSON request template in the Excel file using data store values
    @Step("And the user set the request attributes using data stores as follows <table>")
    public void setPayloadJsonAttributesFromDataStores(Table table) {
        List<TableRow> rows = table.getTableRows();
        List<String> columnNames = table.getColumnNames();
        String jsonRequestBody = getSavedValueForScenario(VAR_API_JSON_REQUEST_BODY);

        for (TableRow row : rows) {
            String placeholder = row.getCell(columnNames.get(0));
            String isRetrievedFromDataStore = row.getCell(columnNames.get(1));
            String dataStoreType = row.getCell(columnNames.get(2));
            String dataStoreVariableName = row.getCell(columnNames.get(3));
            String replacementText = row.getCell(columnNames.get(4));

            if (isTrue(isRetrievedFromDataStore)){
                jsonRequestBody = jsonRequestBody.replaceAll(placeholder, readFromDataStore(dataStoreType, dataStoreVariableName));
            } else {
                if (replacementText.equalsIgnoreCase("\"null\"")){
                    jsonRequestBody = jsonRequestBody.replaceAll("\"" + placeholder + "\"", "null");
                }
                else if (replacementText.equalsIgnoreCase("null")){
                    jsonRequestBody = jsonRequestBody.replaceAll(placeholder, "null");
                }
                else if (hasContainedFileSyntax(replacementText)) {
                    jsonRequestBody = jsonRequestBody.replaceAll(placeholder,
                            TextFile.read(getFilePathFromFileSyntax(replacementText)));
                } else {
                    jsonRequestBody = jsonRequestBody.replaceAll(placeholder, replacementText);
                }
            }
        }
        saveValueForScenario(VAR_API_JSON_REQUEST_BODY, jsonRequestBody);
        printInfo("The JSON request body that you are going to use for the API is:\n" + jsonRequestBody);
    }

    // Use this method to set a custom request payload
    @Step("And the user set the request payload as follows <payload>")
    public void setRequestPayload(String payload) {
        saveValueForScenario(VAR_API_JSON_REQUEST_BODY, payload);
        printInfo("The JSON request body that you are going to use for the API is:\n" + payload);
    }

    // Use this method to replace the values of the request payload
    @Step("And the user set values to the request payload placeholders as follows <table>")
    public void replaceAttributesInRequestPayload(Table table) {
        String payloadWithPlaceholders = getSavedValueForScenario(VAR_API_JSON_REQUEST_BODY);
        String finalPayload;
        List<TableRow> rows = table.getTableRows();
        List<String> columnNames = table.getColumnNames();

        for (TableRow row : rows) {
            String placeholder = row.getCell(columnNames.get(0));
            String replacementText = row.getCell(columnNames.get(1));

            if (hasContainedFileSyntax(replacementText)) {
                payloadWithPlaceholders = payloadWithPlaceholders.replaceAll(placeholder,
                        TextFile.read(getFilePathFromFileSyntax(replacementText)));
            } else {
                payloadWithPlaceholders = payloadWithPlaceholders.replaceAll(placeholder, replacementText);
            }
        }
        finalPayload = payloadWithPlaceholders;
        saveValueForScenario(VAR_API_JSON_REQUEST_BODY, finalPayload);
        printInfo("The final JSON request body that you are going to use for the API is:\n" + finalPayload);
    }

    // Use this method to replace the values of the request payload using data stores
    @Step("And the user set values to the request payload placeholders using data stores as follows <table>")
    public void replaceAttributesInRequestPayloadFromDataStores(Table table) {
        String payloadWithPlaceholders = getSavedValueForScenario(VAR_API_JSON_REQUEST_BODY);
        String finalPayload;
        List<TableRow> rows = table.getTableRows();
        List<String> columnNames = table.getColumnNames();

        for (TableRow row : rows) {
            String placeholder = row.getCell(columnNames.get(0));
            String isRetrievedFromDataStore = row.getCell(columnNames.get(1));
            String dataStoreType = row.getCell(columnNames.get(2));
            String dataStoreVariableName = row.getCell(columnNames.get(3));
            String replacementText = row.getCell(columnNames.get(4));

            if (isTrue(isRetrievedFromDataStore)) {
                payloadWithPlaceholders = payloadWithPlaceholders.replaceAll(placeholder,
                        readFromDataStore(dataStoreType, dataStoreVariableName));
            } else {
                if (hasContainedFileSyntax(replacementText)) {
                    payloadWithPlaceholders = payloadWithPlaceholders.replaceAll(placeholder,
                            TextFile.read(getFilePathFromFileSyntax(replacementText)));
                } else {
                    payloadWithPlaceholders = payloadWithPlaceholders.replaceAll(placeholder, replacementText);
                }
            }
        }
        finalPayload = payloadWithPlaceholders;
        saveValueForScenario(VAR_API_JSON_REQUEST_BODY, finalPayload);
        printInfo("The final JSON request body that you are going to use for the API is:\n" + finalPayload);
    }

    // Use this method to set the form-data key values for the request template in the Excel file
    @Step("And the user set the form-data key value pairs as follows <table>")
    public void setFormData(Table table) {
        List<TableRow> rows = table.getTableRows();
        List<String> columnNames = table.getColumnNames();
        String keys = "", values = "";

        for (TableRow row : rows) {
            String key = row.getCell(columnNames.get(0));
            String value = row.getCell(columnNames.get(1));

            if (hasContainedFileSyntax(value)) {
                keys = keys.concat(key).concat(",");
                values = values.concat(TextFile.read(getFilePathFromFileSyntax(value))).concat(",");
            } else {
                keys = keys.concat(key).concat(",");
                values = values.concat(value).concat(",");
            }
        }
        keys = keys.replaceFirst(".$","");
        values = values.replaceFirst(".$","");
        saveValueForScenario(VAR_API_FORM_DATA_KEYS_LIST, keys);
        saveValueForScenario(VAR_API_FORM_DATA_VALUES_LIST, values);
        printFormData(keys, values);
    }

    // Use this method to set the form-data key values for the request template in the Excel file using data store values
    @Step("And the user set the form-data key value pairs using data stores as follows <table>")
    public void setFormDataFromDataStores(Table table) {
        List<TableRow> rows = table.getTableRows();
        List<String> columnNames = table.getColumnNames();
        String keys = "", values = "";

        for (TableRow row : rows) {
            String key = row.getCell(columnNames.get(0));
            String isRetrievedFromDataStore = row.getCell(columnNames.get(1));
            String dataStoreType = row.getCell(columnNames.get(2));
            String dataStoreVariableName = row.getCell(columnNames.get(3));
            String value = row.getCell(columnNames.get(4));

            if (isTrue(isRetrievedFromDataStore)) {
                keys = keys.concat(key).concat(",");
                values = values.concat(readFromDataStore(dataStoreType, dataStoreVariableName)).concat(",");
            } else {
                if (hasContainedFileSyntax(value)) {
                    keys = keys.concat(key).concat(",");
                    values = values.concat(TextFile.read(getFilePathFromFileSyntax(value))).concat(",");
                } else {
                    keys = keys.concat(key).concat(",");
                    values = values.concat(value).concat(",");
                }
            }
        }
        keys = keys.replaceFirst(".$","");
        values = values.replaceFirst(".$","");
        saveValueForScenario(VAR_API_FORM_DATA_KEYS_LIST, keys);
        saveValueForScenario(VAR_API_FORM_DATA_VALUES_LIST, values);
        printFormData(keys, values);
    }

    // Use this method to set the multipart file key value pairs for the request template in the Excel file
    @Step("And the user set the multipart file key value pairs as follows <table>")
    public void setMultipartFileData(Table table) {
        int noOfRows = 0;
        List<TableRow> rows = table.getTableRows();
        List<String> columnNames = table.getColumnNames();

        for (TableRow row : rows) {
            noOfRows++;
            String fileKey = row.getCell(columnNames.get(0));
            String filePath = row.getCell(columnNames.get(1));
            String mimeType = row.getCell(columnNames.get(2));

            saveValueForScenario(VAR_API_FORM_DATA_MULTIPART_FILE_KEY + noOfRows, fileKey);
            saveValueForScenario(VAR_API_FORM_DATA_MULTIPART_FILE_PATH + noOfRows, filePath);
            saveValueForScenario(VAR_API_FORM_DATA_MULTIPART_MIME_TYPE + noOfRows, mimeType);
        }
        saveValueForScenario(VAR_API_FORM_DATA_MULTIPART_FILES_COUNT, String.valueOf(noOfRows));
    }

    // Use this method to set the query parameters
    @Step("And the user set the query parameters as follows <table>")
    public void setQueryParams(Table table) {
        List<TableRow> rows = table.getTableRows();
        List<String> columnNames = table.getColumnNames();
        String queryParams = "?";

        for (TableRow row : rows) {
            String queryName = row.getCell(columnNames.get(0));
            String queryValue = row.getCell(columnNames.get(1));

            if (hasContainedFileSyntax(queryValue)) {
                queryParams = queryParams.concat(queryName + "=" +
                        TextFile.read(getFilePathFromFileSyntax(queryValue)) + "&");
            } else {
                queryParams = queryParams.concat(queryName + "=" + queryValue + "&");
            }
        }
        queryParams = queryParams.replaceAll(".$", "");
        printInfo("Query parameters which will append to the request URL: " + queryParams + "\n\n");
        saveValueForScenario(VAR_API_QUERY_PARAMS, queryParams);
    }

    // Use this method to set the query parameters using data store values
    @Step("And the user set the query parameters using data stores as follows <table>")
    public void setQueryParamsFromDataStores(Table table) {
        List<TableRow> rows = table.getTableRows();
        List<String> columnNames = table.getColumnNames();
        String queryParams = "?";

        for (TableRow row : rows) {
            String queryName = row.getCell(columnNames.get(0));
            String isRetrievedFromDataStore = row.getCell(columnNames.get(1));
            String dataStoreType = row.getCell(columnNames.get(2));
            String dataStoreVariableName = row.getCell(columnNames.get(3));
            String queryValue = row.getCell(columnNames.get(4));

            if (isTrue(isRetrievedFromDataStore)) {
                queryParams = queryParams.concat(queryName + "=" +
                        readFromDataStore(dataStoreType, dataStoreVariableName) + "&");
            } else {
                if (hasContainedFileSyntax(queryValue)) {
                    queryParams = queryParams.concat(queryName + "=" +
                            TextFile.read(getFilePathFromFileSyntax(queryValue)) + "&");
                } else {
                    queryParams = queryParams.concat(queryName + "=" + queryValue + "&");
                }
            }
        }
        queryParams = queryParams.replaceAll(".$", "");
        printInfo("Query parameters which will append to the request URL: " + queryParams + "\n\n");
        saveValueForScenario(VAR_API_QUERY_PARAMS, queryParams);
    }

    // Use this method to set the path parameters
    @Step("And the user set the path parameters as follows <table>")
    public void setPathParams(Table table) {
        List<TableRow> rows = table.getTableRows();
        List<String> columnNames = table.getColumnNames();
        String pathParams = "/";

        for (TableRow row : rows) {
            String pathName = row.getCell(columnNames.get(0));
            String pathValue = row.getCell(columnNames.get(1));

            if (hasContainedFileSyntax(pathValue)) {
                pathParams = pathParams.concat(TextFile.read(getFilePathFromFileSyntax(pathValue)));
            } else {
                pathParams = pathParams.concat(pathValue);
            }
            pathParams = pathParams.concat("/");
        }
        pathParams = pathParams.replaceAll(".$", "");
        printInfo("Path parameters which will append to the request URL:" + pathParams + "\n\n");
        saveValueForScenario(VAR_API_PATH_PARAMS, pathParams);
    }

    // Use this method to set the path parameters using data store values
    @Step("And the user set the path parameters using data stores as follows <table>")
    public void setPathParamsFromDataStores(Table table) {
        List<TableRow> rows = table.getTableRows();
        List<String> columnNames = table.getColumnNames();
        String pathParams = "/";

        for (TableRow row : rows) {
            String isRetrievedFromDataStore = row.getCell(columnNames.get(1));
            String dataStoreType = row.getCell(columnNames.get(2));
            String dataStoreVariableName = row.getCell(columnNames.get(3));
            String pathValue = row.getCell(columnNames.get(4));

            if(isTrue(isRetrievedFromDataStore)) {
                pathParams = pathParams.concat(readFromDataStore(dataStoreType, dataStoreVariableName));
            } else {
                if (hasContainedFileSyntax(pathValue)) {
                    pathParams = pathParams.concat(TextFile.read(getFilePathFromFileSyntax(pathValue)));
                } else {
                    pathParams = pathParams.concat(pathValue);
                }
            }
            pathParams = pathParams.concat("/");
        }
        pathParams = pathParams.replaceAll(".$", "");
        printInfo("Path parameters which will append to the request URL:" + pathParams + "\n\n");
        saveValueForScenario(VAR_API_PATH_PARAMS, pathParams);
    }

    // Use this method to set the request authentication
    @Step("And the user set the request authentication configurations as follows <table>")
    public void saveRequestAuthConfigurations(Table table) {
        List<TableRow> rows = table.getTableRows();
        List<String> columnNames = table.getColumnNames();

        for (TableRow row : rows) {
            String authConfig = row.getCell(columnNames.get(0));
            String value = row.getCell(columnNames.get(1));

            if (hasContainedFileSyntax(value)) {
                saveValueForScenario(authConfig, TextFile.read(getFilePathFromFileSyntax(value)));
            } else {
                saveValueForScenario(authConfig, value);
            }
        }
    }
}
