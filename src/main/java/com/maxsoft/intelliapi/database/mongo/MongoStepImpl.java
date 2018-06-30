package com.maxsoft.intelliapi.database.mongo;

/**
 * Project Name : MaxSoft-IntelliAPI
 * Developer    : Osanda Deshan
 * Version      : 1.0.0
 * Date         : 6/30/2018
 * Time         : 7:46 PM
 * Description  :
 **/

import com.maxsoft.intelliapi.api.Base;
import com.maxsoft.intelliapi.util.database.mongo.MongoOperator;
import com.maxsoft.intelliapi.util.fileoperator.TextFile;
import com.thoughtworks.gauge.Table;
import com.thoughtworks.gauge.TableRow;
import org.json.JSONException;
import java.util.List;


public class MongoStepImpl extends Base {

    public static final String FILE_SYNTAX = "<file:";
    public static final int FILE_SYNTAX_CHARACTER_COUNT = FILE_SYNTAX.length();

    // Use this method to set the database authentication
    public void saveDatabaseAuthConfigurations(Table configTable) {
        List<TableRow> rows = configTable.getTableRows();
        List<String> columnNames = configTable.getColumnNames();
        for (TableRow row : rows) {
            if (row.getCell(columnNames.get(1)).substring(0, Math.min(row.getCell(columnNames.get(1)).length(), FILE_SYNTAX_CHARACTER_COUNT)).toLowerCase().equals(FILE_SYNTAX)) {
                saveValueForScenario(row.getCell(columnNames.get(0)), TextFile.read(CURRENT_DIRECTORY + row.getCell(columnNames.get(1)).substring(FILE_SYNTAX_CHARACTER_COUNT, row.getCell(columnNames.get(1)).length() - 1)));
            } else {
                saveValueForScenario(row.getCell(columnNames.get(0)), row.getCell(columnNames.get(1)));
            }
        }
    }

    // Use this method to set the database and collection
    public void saveDatabaseNameCollectionName(String databaseName, String collectionName) {
        saveValueForScenario("databaseName", databaseName);
        saveValueForScenario("collectionName", collectionName);
    }

    // Execute database query
    public void executeMongoDbQuery(String key, String value) throws JSONException {

        String isAuthenticationRequired = "";
        String userName = "";
        String source = "";
        String password = "";
        String databaseName = "";
        String collectionName = "";
        boolean isAuthenticationProvided = Boolean.FALSE;

        try {
            isAuthenticationRequired = String.valueOf(getSavedValueForScenario(
                    "Is authentication credentials required?").toLowerCase());
            userName = String.valueOf(getSavedValueForScenario(
                    "Username").toLowerCase());
            source = String.valueOf(getSavedValueForScenario(
                    "Source"));
            password = String.valueOf(getSavedValueForScenario(
                    "Password"));
            databaseName = String.valueOf(getSavedValueForScenario(
                    "databaseName"));
            collectionName = String.valueOf(getSavedValueForScenario(
                    "collectionName"));
        } catch (Exception ex){
            isAuthenticationRequired = "";
            userName = "";
            password = "";
            source = "";
            databaseName = "";
            collectionName = "";
        }

        if (Boolean.valueOf(isAuthenticationRequired).equals(Boolean.TRUE) || isAuthenticationRequired.equals("yes") || isAuthenticationRequired.equals("y")) {
            isAuthenticationProvided = Boolean.TRUE;
        } else {
            isAuthenticationProvided = Boolean.FALSE;
        }

        MongoOperator.executeQuery(isAuthenticationProvided, userName, source, password, databaseName, collectionName, key, value);
    }


}
