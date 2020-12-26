package com.maxsoft.intelliapi.stepimpl.database;

import com.maxsoft.intelliapi.database.MongoOperator;
import com.maxsoft.intelliapi.util.fileoperator.TextFile;
import com.thoughtworks.gauge.Step;
import com.thoughtworks.gauge.Table;
import com.thoughtworks.gauge.TableRow;

import java.util.List;

import static com.maxsoft.intelliapi.util.FrameworkUtil.*;
import static com.maxsoft.intelliapi.common.Constants.*;
import static com.maxsoft.intelliapi.util.DataStoreProcessor.*;

/**
 * Project Name : MaxSoft-IntelliAPI
 * Developer    : Osanda Deshan
 * Version      : 1.0.0
 * Date         : 6/30/2018
 * Time         : 7:46 PM
 * Description  :
 **/

public class MongoStepImpl {

    // Use this method to set the mongo database and collection
    @Step("Given a user need to connect to the <databaseName> Mongo database and <collectionName> collection")
    public void saveDatabaseNameCollectionName(String databaseName, String collectionName) {
        saveValueForScenario(MONGO_DATABASE_NAME, databaseName);
        saveValueForScenario(MONGO_COLLECTION_NAME, collectionName);
    }

    // Use this method to set the mongo database authentication
    @Step("And the user set the MongoDB authentication as follows <configTable>")
    public void saveDatabaseAuthConfigurations(Table configTable) {
        List<TableRow> rows = configTable.getTableRows();
        List<String> columnNames = configTable.getColumnNames();

        for (TableRow row : rows) {
            String config = row.getCell(columnNames.get(0));
            String value = row.getCell(columnNames.get(1));

            if (hasContainedFileSyntax(value)) {
                saveValueForScenario(config, TextFile.read(getFilePathFromFileSyntax(value)));
            } else {
                saveValueForScenario(config, value);
            }
        }
    }

    // Use this method to execute the mongo database query
    @Step("When the user executes the Mongo query using key as <key> and value as <value>")
    public void executeMongoDbQuery(String key, String value) {
        String isAuthenticationRequired, userName, source, password, databaseName, collectionName;
        boolean isAuthenticationProvided;

        try {
            isAuthenticationRequired = getSavedValueForScenario(IS_MONGO_NEED_AUTHENTICATION).toLowerCase();
            userName = getSavedValueForScenario(MONGO_USERNAME).toLowerCase();
            source = String.valueOf(getSavedValueForScenario(MONGO_SOURCE));
            password = String.valueOf(getSavedValueForScenario(MONGO_PASSWORD));
            databaseName = String.valueOf(getSavedValueForScenario(MONGO_DATABASE_NAME));
            collectionName = String.valueOf(getSavedValueForScenario(MONGO_COLLECTION_NAME));
        } catch (Exception ex) {
            isAuthenticationRequired = "";
            userName = "";
            password = "";
            source = "";
            databaseName = "";
            collectionName = "";
        }

        if (isTrue(isAuthenticationRequired)) {
            isAuthenticationProvided = Boolean.TRUE;
        } else {
            isAuthenticationProvided = Boolean.FALSE;
        }

        MongoOperator.executeQuery(isAuthenticationProvided, userName, source, password, databaseName, collectionName,
                key, value);
    }

    // Use this method to execute the mongo database query from data store values
    @Step("When the user executes the Mongo query using data stores as follows <table>")
    public void readDataStoreAndExecuteMongoDbQuery(Table table) {
        String isAuthenticationRequired, userName, source, password, databaseName, collectionName;
        boolean isAuthenticationProvided;

        try {
            isAuthenticationRequired = getSavedValueForScenario(IS_MONGO_NEED_AUTHENTICATION).toLowerCase();
            userName = getSavedValueForScenario(MONGO_USERNAME).toLowerCase();
            source = String.valueOf(getSavedValueForScenario(MONGO_SOURCE));
            password = String.valueOf(getSavedValueForScenario(MONGO_PASSWORD));
            databaseName = String.valueOf(getSavedValueForScenario(MONGO_DATABASE_NAME));
            collectionName = String.valueOf(getSavedValueForScenario(MONGO_COLLECTION_NAME));
        } catch (Exception ex) {
            isAuthenticationRequired = "";
            userName = "";
            password = "";
            source = "";
            databaseName = "";
            collectionName = "";
        }

        if (isTrue(isAuthenticationRequired)) {
            isAuthenticationProvided = Boolean.TRUE;
        } else {
            isAuthenticationProvided = Boolean.FALSE;
        }

        List<TableRow> rows = table.getTableRows();
        List<String> columnNames = table.getColumnNames();

        for (TableRow row : rows) {
            String key = row.getCell(columnNames.get(0));
            String isRetrievedFromDataStore = row.getCell(columnNames.get(1));
            String dataStoreType = row.getCell(columnNames.get(2));
            String dataStoreVariableName = row.getCell(columnNames.get(3));
            String value = row.getCell(columnNames.get(4));

            if (isTrue(isRetrievedFromDataStore)) {
                MongoOperator.executeQuery(isAuthenticationProvided, userName, source, password, databaseName,
                        collectionName, key, readFromDataStore(dataStoreType, dataStoreVariableName));
            } else {
                if (hasContainedFileSyntax(value)) {
                    MongoOperator.executeQuery(isAuthenticationProvided, userName, source, password, databaseName,
                            collectionName, key, TextFile.read(getFilePathFromFileSyntax(value)));
                } else {
                    MongoOperator.executeQuery(isAuthenticationProvided, userName, source, password, databaseName,
                            collectionName, key, value);
                }
            }
        }
    }
}
