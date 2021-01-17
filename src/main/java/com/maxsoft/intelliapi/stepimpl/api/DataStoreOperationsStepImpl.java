package com.maxsoft.intelliapi.stepimpl.api;

import com.maxsoft.intelliapi.util.DataStoreProcessor;
import com.maxsoft.intelliapi.util.reader.ApiDocumentReader;
import com.thoughtworks.gauge.Step;
import com.thoughtworks.gauge.Table;
import com.thoughtworks.gauge.TableRow;

import java.util.List;

import static com.maxsoft.intelliapi.util.FrameworkUtil.*;
import static com.maxsoft.intelliapi.util.DataStoreProcessor.readFromDataStore;
import static com.maxsoft.intelliapi.util.DataStoreProcessor.saveToDataStore;
import static com.maxsoft.intelliapi.util.LogUtil.printInfo;

/**
 * Project Name : MaxSoft-IntelliAPI
 * Developer    : Osanda Deshan
 * Version      : 1.0.0
 * Date         : 6/30/2018
 * Time         : 3:51 PM
 * Description  :
 **/

public class DataStoreOperationsStepImpl {

    // Use this method to save property file values into data stores
    @Step("And the user saves environment property file data into data stores <table>")
    public void savePropertyFileValuesToDataStore(Table table) {
        List<TableRow> rows = table.getTableRows();
        List<String> columnNames = table.getColumnNames();

        for (TableRow row : rows) {
            String dataStoreType = row.getCell(columnNames.get(0));
            String variableName = row.getCell(columnNames.get(1));
            String propertyName = row.getCell(columnNames.get(2));

            DataStoreProcessor.savePropertyFileValuesToDataStore(dataStoreType, variableName, propertyName);
        }
    }

    // Use this method to save data store values as a list in another data store
    @Step("And the user saves the values inside data stores as a <listDataType> data type list into <dataStoreType> type data store by referencing the variable name as <dataStoreVariableName> <table>")
    public void saveDataStoresAsList(String listDataType, String newDataStoreType, String newDataStoreVariableName,
                                     Table table) {
        List<TableRow> rows = table.getTableRows();
        List<String> columnNames = table.getColumnNames();
        String valueList = "";
        String concatString = "";

        if (listDataType.equalsIgnoreCase("string")) {
            concatString = "\"";
        }

        for (TableRow row : rows) {
            String dataStoreType = row.getCell(columnNames.get(0));
            String variableName = row.getCell(columnNames.get(1));

            valueList = valueList.concat(concatString)
                    .concat(readFromDataStore(dataStoreType, variableName).concat(concatString + ","));
        }
        valueList = valueList.replaceFirst(".$", "");
        saveToDataStore(newDataStoreType, newDataStoreVariableName, valueList);
        printInfo("Value List: " + valueList);
    }

    // Use this method to save strings in data store
    @Step("And the user saves the values inside data stores as follows <table>")
    public void saveValueToDataStore(Table table) {
        List<TableRow> rows = table.getTableRows();
        List<String> columnNames = table.getColumnNames();

        for (TableRow row : rows) {
            String dataStoreType = row.getCell(columnNames.get(0));
            String variableName = row.getCell(columnNames.get(1));
            String value = row.getCell(columnNames.get(2));

            saveToDataStore(dataStoreType, variableName, value);
        }
    }

    // Use this method to read strings from data store
    @Step("And the user read the values from data stores as follows <table>")
    public void readValueFromDataStores(Table table) {
        List<TableRow> rows = table.getTableRows();
        List<String> columnNames = table.getColumnNames();

        for (TableRow row : rows) {
            String dataStoreType = row.getCell(columnNames.get(0));
            String variableName = row.getCell(columnNames.get(1));

            readFromDataStore(dataStoreType, variableName);
        }
    }

    // Use this method to validate the content in data stores
    @Step("And the values inside the data stores equal to the following <table>")
    public void checkEqualityOfDataStoreValue(Table table) {
        List<TableRow> rows = table.getTableRows();
        List<String> columnNames = table.getColumnNames();

        for (TableRow row : rows) {
            String dataStoreType = row.getCell(columnNames.get(0));
            String variableName = row.getCell(columnNames.get(1));
            String expectedValue = row.getCell(columnNames.get(2));

            DataStoreProcessor.checkEqualityOfDataStoreValue(dataStoreType, variableName, expectedValue);
        }
    }

    // Use this method to compare the content in two data stores
    @Step("And the values inside two data stores should be equal <table>")
    public void checkEqualityOfTwoDataStoreValues(Table table) {
        List<TableRow> rows = table.getTableRows();
        List<String> columnNames = table.getColumnNames();

        for (TableRow row : rows) {
            String firstDataStoreType = row.getCell(columnNames.get(0));
            String firstDataStoreVariableName = row.getCell(columnNames.get(1));
            String secondDataStoreType = row.getCell(columnNames.get(2));
            String secondDataStoreVariableName = row.getCell(columnNames.get(3));

            DataStoreProcessor.checkEqualityOfTwoDataStoreValues(firstDataStoreType, firstDataStoreVariableName,
                    secondDataStoreType, secondDataStoreVariableName);
        }
    }

    // Use this method to validate the content in data stores
    @Step("And the values inside the data stores not equal to the following <table>")
    public void checkInequalityOfDataStoreValue(Table table) {
        List<TableRow> rows = table.getTableRows();
        List<String> columnNames = table.getColumnNames();

        for (TableRow row : rows) {
            String dataStoreType = row.getCell(columnNames.get(0));
            String variableName = row.getCell(columnNames.get(1));
            String expectedValue = row.getCell(columnNames.get(2));

            DataStoreProcessor.checkInequalityOfDataStoreValue(dataStoreType, variableName, expectedValue);
        }
    }

    // Use this method to compare the content in two data stores
    @Step("And the values inside two data stores should not be equal <table>")
    public void checkInequalityOfTwoDataStoreValues(Table table) {
        List<TableRow> rows = table.getTableRows();
        List<String> columnNames = table.getColumnNames();

        for (TableRow row : rows) {
            String firstDataStoreType = row.getCell(columnNames.get(0));
            String firstDataStoreVariableName = row.getCell(columnNames.get(1));
            String secondDataStoreType = row.getCell(columnNames.get(2));
            String secondDataStoreVariableName = row.getCell(columnNames.get(3));

            DataStoreProcessor.checkInequalityOfTwoDataStoreValues(firstDataStoreType, firstDataStoreVariableName,
                    secondDataStoreType, secondDataStoreVariableName);
        }
    }

    // Use this method to validate the content in data stores
    @Step("And the values inside the data stores contain the following <table>")
    public void checkDataStoreValueContainsText(Table table) {
        List<TableRow> rows = table.getTableRows();
        List<String> columnNames = table.getColumnNames();

        for (TableRow row : rows) {
            String dataStoreType = row.getCell(columnNames.get(0));
            String variableName = row.getCell(columnNames.get(1));
            String expectedValue = row.getCell(columnNames.get(2));

            DataStoreProcessor.checkDataStoreValueContainsText(dataStoreType, variableName, expectedValue);
        }
    }

    // Use this method to compare the content in two data stores
    @Step("And the value inside a data store should contain the value of the other data store <table>")
    public void checkOneDataStoreValueContainsInAnotherDataStore(Table table) {
        List<TableRow> rows = table.getTableRows();
        List<String> columnNames = table.getColumnNames();

        for (TableRow row : rows) {
            String firstDataStoreType = row.getCell(columnNames.get(0));
            String firstDataStoreVariableName = row.getCell(columnNames.get(1));
            String secondDataStoreType = row.getCell(columnNames.get(2));
            String secondDataStoreVariableName = row.getCell(columnNames.get(3));

            DataStoreProcessor.checkOneDataStoreValueContainsInAnotherDataStore(firstDataStoreType,
                    firstDataStoreVariableName, secondDataStoreType, secondDataStoreVariableName);
        }
    }

    // Use this method to validate the content in data stores
    @Step("And the values inside the data stores not contain the following <table>")
    public void checkDataStoreValueNotContainsText(Table table) {
        List<TableRow> rows = table.getTableRows();
        List<String> columnNames = table.getColumnNames();

        for (TableRow row : rows) {
            String dataStoreType = row.getCell(columnNames.get(0));
            String variableName = row.getCell(columnNames.get(1));
            String expectedValue = row.getCell(columnNames.get(2));

            DataStoreProcessor.checkDataStoreValueNotContainsText(dataStoreType, variableName, expectedValue);
        }
    }

    // Use this method to compare the content in two data stores
    @Step("And the value inside a data store should not contain the value of the other data store <table>")
    public void checkOneDataStoreValueNotContainsInAnotherDataStore(Table table) {
        List<TableRow> rows = table.getTableRows();
        List<String> columnNames = table.getColumnNames();

        for (TableRow row : rows) {
            String firstDataStoreType = row.getCell(columnNames.get(0));
            String firstDataStoreVariableName = row.getCell(columnNames.get(1));
            String secondDataStoreType = row.getCell(columnNames.get(2));
            String secondDataStoreVariableName = row.getCell(columnNames.get(3));

            DataStoreProcessor.checkOneDataStoreValueNotContainsInAnotherDataStore(firstDataStoreType,
                    firstDataStoreVariableName, secondDataStoreType, secondDataStoreVariableName);
        }
    }

    // Use this method to add integer values in data stores and save to a new data store
    @Step("And add the integer values in data stores and save it in a <newDataStoreType> type data store named <newDataStoreVariableName> <table>")
    public void addIntegerValuesInDataStoresAndSaveToNewDataStore(String newDataStoreType,
                                                                  String newDataStoreVariableName, Table table) {
        List<TableRow> rows = table.getTableRows();
        List<String> columnNames = table.getColumnNames();
        int finalVal = 0;

        for (TableRow row : rows) {
            String dataStoreType = row.getCell(columnNames.get(0));
            String variableName = row.getCell(columnNames.get(1));

            finalVal = finalVal + Integer.parseInt(readFromDataStore(dataStoreType, variableName));
        }
        saveToDataStore(newDataStoreType, newDataStoreVariableName, String.valueOf(finalVal));
    }

    // Use this method to subtract integer values in data stores and save to a new data store
    @Step("And subtract the integer values in data stores and save it in a new data store <table>")
    public void subtractIntegerValuesInDataStoresAndSaveToNewDataStore(Table table) {
        List<TableRow> rows = table.getTableRows();
        List<String> columnNames = table.getColumnNames();
        int finalVal;

        for (TableRow row : rows) {
            String firstDataStoreType = row.getCell(columnNames.get(0));
            String firstDataStoreVariableName = row.getCell(columnNames.get(1));
            String secondDataStoreType = row.getCell(columnNames.get(2));
            String secondDataStoreVariableName = row.getCell(columnNames.get(3));
            String newDataStoreType = row.getCell(columnNames.get(4));
            String newDataStoreVariableName = row.getCell(columnNames.get(5));

            finalVal = Integer.parseInt(readFromDataStore(firstDataStoreType, firstDataStoreVariableName)) -
                    Integer.parseInt(readFromDataStore(secondDataStoreType, secondDataStoreVariableName));

            saveToDataStore(newDataStoreType, newDataStoreVariableName, String.valueOf(finalVal));
        }
    }

    // Use this method to divide integer values in data stores and save to a new data store
    @Step("And divide the integer values in data stores and save it in a new data store <table>")
    public void divideIntegerValuesInDataStoresAndSaveToNewDataStore(Table table) {
        List<TableRow> rows = table.getTableRows();
        List<String> columnNames = table.getColumnNames();
        Float finalVal;

        for (TableRow row : rows) {
            String firstDataStoreType = row.getCell(columnNames.get(0));
            String firstDataStoreVariableName = row.getCell(columnNames.get(1));
            String secondDataStoreType = row.getCell(columnNames.get(2));
            String secondDataStoreVariableName = row.getCell(columnNames.get(3));
            String newDataStoreType = row.getCell(columnNames.get(4));
            String newDataStoreVariableName = row.getCell(columnNames.get(5));

            finalVal = (float) Integer.parseInt(readFromDataStore(firstDataStoreType, firstDataStoreVariableName)) /
                    (float) Integer.parseInt((readFromDataStore(secondDataStoreType, secondDataStoreVariableName)));

            saveToDataStore(newDataStoreType, newDataStoreVariableName, String.valueOf(finalVal));
        }
    }

    // Use this method to multiply integer values in data stores and save to a new data store
    @Step("And multiply the integer values in data stores and save it in a <newDataStoreType> type data store named <newDataStoreVariableName> <table>")
    public void multiplyIntegerValuesInDataStoresAndSaveToNewDataStore(String newDataStoreType,
                                                                       String newDataStoreVariableName, Table table) {
        List<TableRow> rows = table.getTableRows();
        List<String> columnNames = table.getColumnNames();
        int finalVal = 1;

        for (TableRow row : rows) {
            String dataStoreType = row.getCell(columnNames.get(0));
            String variableName = row.getCell(columnNames.get(1));

            finalVal = finalVal * Integer.parseInt(readFromDataStore(dataStoreType, variableName));
        }
        saveToDataStore(newDataStoreType, newDataStoreVariableName, String.valueOf(finalVal));
    }

    // Use this method to add decimal values in data stores and save to a new data store
    @Step("And add the decimal values in data stores and save it in a <newDataStoreType> type data store named <newDataStoreVariableName> <table>")
    public void addDecimalValuesInDataStoresAndSaveToNewDataStore(String newDataStoreType,
                                                                  String newDataStoreVariableName, Table table) {
        List<TableRow> rows = table.getTableRows();
        List<String> columnNames = table.getColumnNames();
        float finalVal = 0;

        for (TableRow row : rows) {
            String dataStoreType = row.getCell(columnNames.get(0));
            String variableName = row.getCell(columnNames.get(1));

            finalVal = finalVal + Float.parseFloat(readFromDataStore(dataStoreType, variableName));
        }
        saveToDataStore(newDataStoreType, newDataStoreVariableName, String.valueOf(finalVal));
    }

    // Use this method to subtract decimal values in data stores and save to a new data store
    @Step("And subtract the decimal values in data stores and save it in a new data store <table>")
    public void subtractDecimalValuesInDataStoresAndSaveToNewDataStore(Table table) {
        List<TableRow> rows = table.getTableRows();
        List<String> columnNames = table.getColumnNames();
        float finalVal;

        for (TableRow row : rows) {
            String firstDataStoreType = row.getCell(columnNames.get(0));
            String firstDataStoreVariableName = row.getCell(columnNames.get(1));
            String secondDataStoreType = row.getCell(columnNames.get(2));
            String secondDataStoreVariableName = row.getCell(columnNames.get(3));
            String newDataStoreType = row.getCell(columnNames.get(4));
            String newDataStoreVariableName = row.getCell(columnNames.get(5));

            finalVal = Float.parseFloat(readFromDataStore(firstDataStoreType, firstDataStoreVariableName)) -
                    Float.parseFloat(readFromDataStore(secondDataStoreType, secondDataStoreVariableName));

            saveToDataStore(newDataStoreType, newDataStoreVariableName, String.valueOf(finalVal));
        }
    }

    // Use this method to divide decimal values in data stores and save to a new data store
    @Step("And divide the decimal values in data stores and save it in a new data store <table>")
    public void divideDecimalValuesInDataStoresAndSaveToNewDataStore(Table table) {
        List<TableRow> rows = table.getTableRows();
        List<String> columnNames = table.getColumnNames();
        Float finalVal;

        for (TableRow row : rows) {
            String firstDataStoreType = row.getCell(columnNames.get(0));
            String firstDataStoreVariableName = row.getCell(columnNames.get(1));
            String secondDataStoreType = row.getCell(columnNames.get(2));
            String secondDataStoreVariableName = row.getCell(columnNames.get(3));
            String newDataStoreType = row.getCell(columnNames.get(4));
            String newDataStoreVariableName = row.getCell(columnNames.get(5));

            finalVal = Float.parseFloat(readFromDataStore(firstDataStoreType, firstDataStoreVariableName)) /
                    Float.parseFloat(readFromDataStore(secondDataStoreType, secondDataStoreVariableName));

            saveToDataStore(newDataStoreType, newDataStoreVariableName, String.valueOf(finalVal));
        }
    }

    // Use this method to multiply decimal values in data stores and save to a new data store
    @Step("And multiply the decimal values in data stores and save it in a <newDataStoreType> type data store named <newDataStoreVariableName> <table>")
    public void multiplyDecimalValuesInDataStoresAndSaveToNewDataStore(String newDataStoreType,
                                                                       String newDataStoreVariableName, Table table) {
        List<TableRow> rows = table.getTableRows();
        List<String> columnNames = table.getColumnNames();
        float finalVal = Float.parseFloat("1");

        for (TableRow row : rows) {
            String dataStoreType = row.getCell(columnNames.get(0));
            String variableName = row.getCell(columnNames.get(1));

            finalVal = finalVal * Float.parseFloat(readFromDataStore(dataStoreType, variableName));
        }
        saveToDataStore(newDataStoreType, newDataStoreVariableName, String.valueOf(finalVal));
    }

    // Use this method to concat values in data stores and save to a new data store
    @Step("And concat values in data stores and save it in a <dataStoreType> type data store named <dataStoreVariableName> <table>")
    public void concatDataStoreValues(String newDataStoreType, String newDataStoreVariableName, Table table) {
        List<TableRow> rows = table.getTableRows();
        List<String> columnNames = table.getColumnNames();
        String finalString = "";

        for (TableRow row : rows) {
            String dataStoreType = row.getCell(columnNames.get(0));
            String variableName = row.getCell(columnNames.get(1));

            if (variableName.equalsIgnoreCase("${space}")) {
                finalString = finalString.concat(" ");
            } else {
                finalString = finalString.concat(readFromDataStore(dataStoreType, variableName));
            }
        }
        saveToDataStore(newDataStoreType, newDataStoreVariableName, finalString);
    }

    // Use this method to concat a random text with data store values and save in a new/existing data store
    @Step("And concat random text and save it in a data store as follows <table>")
    public void concatRandomTextAndSaveToDataStore(Table table) {
        List<TableRow> rows = table.getTableRows();
        List<String> columnNames = table.getColumnNames();

        for (TableRow row : rows) {
            String isRetrievedFromDataStore = row.getCell(columnNames.get(0));
            String dataStoreType = row.getCell(columnNames.get(1));
            String variableName = row.getCell(columnNames.get(2));
            String expectedValue = row.getCell(columnNames.get(3));
            String needToSaveToNewDataStore = row.getCell(columnNames.get(4));
            String newDataStoreType = row.getCell(columnNames.get(5));
            String newDataStoreVariableName = row.getCell(columnNames.get(6));

            if (isTrue(isRetrievedFromDataStore)) {
                String newText = readFromDataStore(dataStoreType, variableName).concat(getRandomText());
                if (isTrue(needToSaveToNewDataStore)) {
                    saveToDataStore(newDataStoreType, newDataStoreVariableName, newText);
                } else {
                    saveToDataStore(dataStoreType, variableName, newText);
                }
            } else {
                saveToDataStore(newDataStoreType, newDataStoreVariableName, expectedValue.concat(getRandomText()));
            }
        }
    }

    // Use this method to generate random email and save in a new/existing data store
    @Step("And generate random email and save it in a data store as follows <table>")
    public void generateRandomEmailAndSaveToDataStore(Table table) {
        List<TableRow> rows = table.getTableRows();
        List<String> columnNames = table.getColumnNames();

        for (TableRow row : rows) {
            String dataStoreType = row.getCell(columnNames.get(0));
            String variableName = row.getCell(columnNames.get(1));
            String domainName = row.getCell(columnNames.get(2));

            saveToDataStore(dataStoreType, variableName, getRandomEmail(domainName));
        }
    }

    // Use this method to save current epochTime into data stores
    @Step("And the user saves the current epoch time in <secondsOrMillis> inside data stores <table>")
    public void saveCurrentEpochTimeToDataStore(String secondsOrMillis, Table table) {
        List<TableRow> rows = table.getTableRows();
        List<String> columnNames = table.getColumnNames();

        for (TableRow row : rows) {
            String dataStoreType = row.getCell(columnNames.get(0));
            String variableName = row.getCell(columnNames.get(1));

            DataStoreProcessor.saveCurrentEpochTimeToDataStore(secondsOrMillis, dataStoreType, variableName);
        }
    }

    // Use this method to convert a given format timestamp into epochTime and save it into data stores
    @Step("And the user converts a timestamp into epoch time and saves inside data stores <table>")
    public void saveEpochTimeToDataStore(Table table) {
        List<TableRow> rows = table.getTableRows();
        List<String> columnNames = table.getColumnNames();

        for (TableRow row : rows) {
            String timestampPattern = row.getCell(columnNames.get(0));
            String isRetrievedFromDataStore = row.getCell(columnNames.get(1));
            String dataStoreType = row.getCell(columnNames.get(2));
            String variableName = row.getCell(columnNames.get(3));
            String timestamp = row.getCell(columnNames.get(4));
            String secondsOrMillis = row.getCell(columnNames.get(5));
            String epochTimeDataStoreType = row.getCell(columnNames.get(6));
            String epochTimeDataStoreVariableName = row.getCell(columnNames.get(7));

            if (isTrue(isRetrievedFromDataStore)) {
                DataStoreProcessor.saveEpochTimeToDataStore(timestampPattern,
                        readFromDataStore(dataStoreType, variableName), secondsOrMillis,
                        epochTimeDataStoreType, epochTimeDataStoreVariableName);
            } else {
                DataStoreProcessor.saveEpochTimeToDataStore(timestampPattern, timestamp, secondsOrMillis,
                        epochTimeDataStoreType, epochTimeDataStoreVariableName);
            }
        }
    }

    // Use this method to save api document test data into data stores
    @Step("And the user saves test data inside excel file into data stores <table>")
    public void saveExcelDataToDataStore(Table table) {
        List<TableRow> rows = table.getTableRows();
        List<String> columnNames = table.getColumnNames();

        for (TableRow row : rows) {
            String dataStoreType = row.getCell(columnNames.get(0));
            String variableName = row.getCell(columnNames.get(1));
            String sheetName = row.getCell(columnNames.get(2));
            String key = row.getCell(columnNames.get(3));

            saveToDataStore(dataStoreType, variableName, ApiDocumentReader.getDataFromExcel(sheetName, key));
        }
    }
}
