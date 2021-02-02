package com.maxsoft.intelliapi.stepimpl.api;

import com.maxsoft.intelliapi.api.ApiResponseProcessor;
import com.maxsoft.intelliapi.util.fileoperator.TextFile;
import com.thoughtworks.gauge.Step;
import com.thoughtworks.gauge.Table;
import com.thoughtworks.gauge.TableRow;
import org.testng.Assert;

import java.util.List;

import static com.maxsoft.intelliapi.util.FrameworkUtil.*;
import static com.maxsoft.intelliapi.Constants.VAR_API_RESPONSE_STATUS_CODE;
import static com.maxsoft.intelliapi.util.DataStoreProcessor.getSavedValueForScenario;
import static com.maxsoft.intelliapi.util.DataStoreProcessor.readFromDataStore;

/**
 * Project Name    : MaxSoft-IntelliAPI
 * Developer       : Osanda Deshan
 * Version         : 1.0.0
 * Date            : 12/21/2020
 * Time            : 7:11 PM
 * Description     :
 **/

public class ApiResponseValidatorStepImpl {

    // Use this method to validate the status code of the response
    @Step("Then the status code for the request is <statusCode>")
    public void checkResponseStatusCode(String statusCode){
        Assert.assertEquals(getSavedValueForScenario(VAR_API_RESPONSE_STATUS_CODE), statusCode,
                "The expected status code for the request is not equal to the actual status code\n");
    }

    // Use this method to validate the content of the response using JSON Path Assertions
    @Step("And the JSON Path values of the response should contains the following <table>")
    public void checkJsonPathValueContainsText(Table table){
        List<TableRow> rows = table.getTableRows();
        List<String> columnNames = table.getColumnNames();

        for (TableRow row : rows) {
            String jsonPath = row.getCell(columnNames.get(0));
            String jsonPathValue = row.getCell(columnNames.get(1));

            if (hasContainedFileSyntax(jsonPathValue)) {
                ApiResponseProcessor.checkJsonPathValueContainsText(jsonPath,
                        TextFile.read(getFilePathFromFileSyntax(jsonPathValue)));
            } else {
                ApiResponseProcessor.checkJsonPathValueContainsText(jsonPath, jsonPathValue);
            }
        }
    }

    // Use this method to validate the content of the response using JSON Path Assertions with data stores
    @Step("And the JSON Path values of the response should contains the values inside the data stores <table>")
    public void checkJsonPathValueFromDataStoreContainsText(Table table){
        List<TableRow> rows = table.getTableRows();
        List<String> columnNames = table.getColumnNames();

        for (TableRow row : rows) {
            String jsonPath = row.getCell(columnNames.get(0));
            String isRetrievedFromDataStore = row.getCell(columnNames.get(1));
            String dataStoreType = row.getCell(columnNames.get(2));
            String dataStoreVariableName = row.getCell(columnNames.get(3));
            String jsonPathValue = row.getCell(columnNames.get(4));

            if(isTrue(isRetrievedFromDataStore)) {
                ApiResponseProcessor.checkJsonPathValueContainsText(jsonPath,
                        readFromDataStore(dataStoreType, dataStoreVariableName));
            } else {
                if (hasContainedFileSyntax(jsonPathValue)) {
                    ApiResponseProcessor.checkJsonPathValueContainsText(jsonPath,
                            TextFile.read(getFilePathFromFileSyntax(jsonPathValue)));
                } else {
                    ApiResponseProcessor.checkJsonPathValueContainsText(jsonPath, jsonPathValue);
                }
            }
        }
    }

    // Use this method to validate the content of the response using JSON Path Assertions
    @Step("And the JSON Path values of the response should not contains the following <table>")
    public void checkJsonPathValueNotContainsText(Table table){
        List<TableRow> rows = table.getTableRows();
        List<String> columnNames = table.getColumnNames();

        for (TableRow row : rows) {
            String jsonPath = row.getCell(columnNames.get(0));
            String jsonPathValue = row.getCell(columnNames.get(1));

            if (hasContainedFileSyntax(jsonPathValue)) {
                ApiResponseProcessor.checkJsonPathValueNotContainsText(jsonPath,
                        TextFile.read(getFilePathFromFileSyntax(jsonPathValue)));
            } else {
                ApiResponseProcessor.checkJsonPathValueNotContainsText(jsonPath, jsonPathValue);
            }
        }
    }

    // Use this method to validate the content of the response using JSON Path Assertions with data stores
    @Step("And the JSON Path values of the response should not contains the values inside the data stores <table>")
    public void checkJsonPathValueFromDataStoreNotContainsText(Table table){
        List<TableRow> rows = table.getTableRows();
        List<String> columnNames = table.getColumnNames();

        for (TableRow row : rows) {
            String jsonPath = row.getCell(columnNames.get(0));
            String isRetrievedFromDataStore = row.getCell(columnNames.get(1));
            String dataStoreType = row.getCell(columnNames.get(2));
            String dataStoreVariableName = row.getCell(columnNames.get(3));
            String jsonPathValue = row.getCell(columnNames.get(4));

            if(isTrue(isRetrievedFromDataStore)) {
                ApiResponseProcessor.checkJsonPathValueNotContainsText(jsonPath,
                        readFromDataStore(dataStoreType, dataStoreVariableName));
            } else {
                if (hasContainedFileSyntax(jsonPathValue)) {
                    ApiResponseProcessor.checkJsonPathValueNotContainsText(jsonPath,
                            TextFile.read(getFilePathFromFileSyntax(jsonPathValue)));
                } else {
                    ApiResponseProcessor.checkJsonPathValueNotContainsText(jsonPath, jsonPathValue);
                }
            }
        }
    }

    // Use this method to validate the content of the response using JSON Path Assertions
    @Step("And the JSON Path Assertions for the response should be equal to the following <table>")
    public void checkJsonPathAssertionEqualsText(Table table){
        List<TableRow> rows = table.getTableRows();
        List<String> columnNames = table.getColumnNames();

        for (TableRow row : rows) {
            String jsonPath = row.getCell(columnNames.get(0));
            String jsonPathValue = row.getCell(columnNames.get(1));

            if (hasContainedFileSyntax(jsonPathValue)) {
                ApiResponseProcessor.checkJsonPathAssertionEqualsText(jsonPath,
                        TextFile.read(getFilePathFromFileSyntax(jsonPathValue)));
            } else {
                ApiResponseProcessor.checkJsonPathAssertionEqualsText(jsonPath, jsonPathValue);
            }
        }
    }

    // Use this method to validate the content of the response using JSON Path Assertions with data stores
    @Step("And the JSON Path Assertions for the response should be equal to the values inside the data stores <table>")
    public void checkJsonPathAssertionFromDataStoreEqualsText(Table table){
        List<TableRow> rows = table.getTableRows();
        List<String> columnNames = table.getColumnNames();

        for (TableRow row : rows) {
            String jsonPath = row.getCell(columnNames.get(0));
            String isRetrievedFromDataStore = row.getCell(columnNames.get(1));
            String dataStoreType = row.getCell(columnNames.get(2));
            String dataStoreVariableName = row.getCell(columnNames.get(3));
            String jsonPathValue = row.getCell(columnNames.get(4));

            if(isTrue(isRetrievedFromDataStore)) {
                ApiResponseProcessor.checkJsonPathAssertionEqualsText(jsonPath,
                        readFromDataStore(dataStoreType, dataStoreVariableName));
            } else {
                if (hasContainedFileSyntax(jsonPathValue)) {
                    ApiResponseProcessor.checkJsonPathAssertionEqualsText(jsonPath,
                            TextFile.read(getFilePathFromFileSyntax(jsonPathValue)));
                } else {
                    ApiResponseProcessor.checkJsonPathAssertionEqualsText(jsonPath, jsonPathValue);
                }
            }
        }
    }

    // Use this method to validate the content of the response using JSON Path Assertions
    @Step("And the JSON Path Assertions for the response should not be equal to the following <table>")
    public void checkJsonPathAssertionNotEqualsText(Table table){
        List<TableRow> rows = table.getTableRows();
        List<String> columnNames = table.getColumnNames();

        for (TableRow row : rows) {
            String jsonPath = row.getCell(columnNames.get(0));
            String jsonPathValue = row.getCell(columnNames.get(1));

            if (hasContainedFileSyntax(jsonPathValue)) {
                ApiResponseProcessor.checkJsonPathAssertionNotEqualsText(jsonPath,
                        TextFile.read(getFilePathFromFileSyntax(jsonPathValue)));
            } else {
                ApiResponseProcessor.checkJsonPathAssertionNotEqualsText(jsonPath, jsonPathValue);
            }
        }
    }

    // Use this method to validate the content of the response using JSON Path Assertions with data stores
    @Step("And the JSON Path Assertions for the response should not be equal to the values inside the data stores <responseFields>")
    public void checkJsonPathAssertionFromDataStoreNotEqualsText(Table table){
        List<TableRow> rows = table.getTableRows();
        List<String> columnNames = table.getColumnNames();

        for (TableRow row : rows) {
            String jsonPath = row.getCell(columnNames.get(0));
            String isRetrievedFromDataStore = row.getCell(columnNames.get(1));
            String dataStoreType = row.getCell(columnNames.get(2));
            String dataStoreVariableName = row.getCell(columnNames.get(3));
            String jsonPathValue = row.getCell(columnNames.get(4));

            if(isTrue(isRetrievedFromDataStore)) {
                ApiResponseProcessor.checkJsonPathAssertionNotEqualsText(jsonPath,
                        readFromDataStore(dataStoreType, dataStoreVariableName));
            } else {
                if (hasContainedFileSyntax(jsonPathValue)) {
                    ApiResponseProcessor.checkJsonPathAssertionNotEqualsText(jsonPath,
                            TextFile.read(getFilePathFromFileSyntax(jsonPathValue)));
                } else {
                    ApiResponseProcessor.checkJsonPathAssertionNotEqualsText(jsonPath, jsonPathValue);
                }
            }
        }
    }

    // Use this method to validate the node of the JSON Path is exists
    @Step("And the JSON Path Existence in the response should be equal to the following <jsonPaths>")
    public void checkJsonPathExistence(Table table){
        List<TableRow> rows = table.getTableRows();
        List<String> columnNames = table.getColumnNames();

        for (TableRow row : rows) {
            String jsonPath = row.getCell(columnNames.get(0));
            String jsonPathValue = row.getCell(columnNames.get(1));

            if (hasContainedFileSyntax(jsonPathValue)) {
                ApiResponseProcessor.checkJsonPathExistence(jsonPath,
                        Boolean.valueOf(TextFile.read(getFilePathFromFileSyntax(jsonPathValue))));
            } else {
                ApiResponseProcessor.checkJsonPathExistence(jsonPath, Boolean.valueOf(jsonPathValue));
            }
        }
    }

    // Use this method to validate the JSON Schema
    @Step("And validate the response against the JSON Schema saved in <jsonSchemaFileName>")
    public void validateJsonSchema(String jsonSchemaFileName) {
        ApiResponseProcessor.validateJsonSchema(jsonSchemaFileName);
    }
}
