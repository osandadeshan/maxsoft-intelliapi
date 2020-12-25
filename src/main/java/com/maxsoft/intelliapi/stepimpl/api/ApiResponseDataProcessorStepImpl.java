package com.maxsoft.intelliapi.stepimpl.api;

import com.thoughtworks.gauge.Step;
import com.thoughtworks.gauge.Table;
import com.thoughtworks.gauge.TableRow;

import java.util.List;

import static com.maxsoft.intelliapi.api.ApiResponse.*;

/**
 * Project Name    : MaxSoft-IntelliAPI
 * Developer       : Osanda Deshan
 * Version         : 1.0.0
 * Date            : 12/21/2020
 * Time            : 7:29 PM
 * Description     :
 **/

public class ApiResponseDataProcessorStepImpl {

    // Use this method to retrieve and save the values of JSON Paths in the response
    @Step("And save the JSON Path values in the response inside the data stores <table>")
    public void saveJsonPathValue(Table table) {
        List<TableRow> rows = table.getTableRows();
        List<String> columnNames = table.getColumnNames();

        for (TableRow row : rows) {
            String dataStoreType = row.getCell(columnNames.get(0));
            String variableName = row.getCell(columnNames.get(1));
            String jsonPath = row.getCell(columnNames.get(2));

            saveResponseJsonPathValue(dataStoreType, variableName, jsonPath);
        }
    }

    // Use this method to retrieve and save the access token of the login response
    @Step("And save the access token in the response which is located inside the JSON Path of <jsonPath>")
    public void saveAccessToken(String jsonPath) {
        saveAccessTokenToTextFile(jsonPath);
    }

    // Use this method to retrieve and save the attribute values of the response into text files
    @Step("And save the JSON Path values of the response into text files <table>")
    public void saveResponseData(Table table) {
        List<TableRow> rows = table.getTableRows();
        List<String> columnNames = table.getColumnNames();

        for (TableRow row : rows) {
            String jsonPath = row.getCell(columnNames.get(0));
            String filePath = row.getCell(columnNames.get(1));

            saveResponseDataToTextFile(jsonPath, filePath);
        }
    }

    // Use this method to retrieve and save the response JSON array values in a CSV file
    @Step("And save the JSON Array values of the response into CSV files <table>")
    public void saveJsonArrayValuesToCsvFile(Table table) {
        List<TableRow> rows = table.getTableRows();
        List<String> columnNames = table.getColumnNames();

        for (TableRow row : rows) {
            String jsonPath = row.getCell(columnNames.get(0));
            String headerName = row.getCell(columnNames.get(1));
            String csvFilePath = row.getCell(columnNames.get(2));

            saveJsonArrayValuesToCsv(jsonPath, headerName, csvFilePath);
        }
    }
}
