package com.maxsoft.intelliapi.database;

import com.maxsoft.intelliapi.util.comparison.RecordsChecker;
import com.maxsoft.intelliapi.util.comparison.Record;
import com.maxsoft.intelliapi.util.table.Board;
import com.maxsoft.intelliapi.util.table.StringTable;
import com.thoughtworks.gauge.Table;
import com.thoughtworks.gauge.TableRow;
import org.testng.Assert;

import java.sql.*;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

import static com.maxsoft.intelliapi.Constants.*;
import static com.maxsoft.intelliapi.util.DataStoreProcessor.getSavedValueForScenario;
import static com.maxsoft.intelliapi.util.DataStoreProcessor.saveValueForScenario;
import static com.maxsoft.intelliapi.util.LogUtil.printError;
import static com.maxsoft.intelliapi.util.LogUtil.printInfo;

/**
 * Project Name : MaxSoft-IntelliAPI
 * Developer    : Osanda Deshan
 * Version      : 1.0.0
 * Date         : 6/30/2018
 * Time         : 3:51 PM
 * Description  :
 **/

public class MySqlOperator {

    static Connection dbConnection;
    static final ArrayList<Record> recordListForValuesInDatabase = new ArrayList<>();
    static final ArrayList<Record> recordListForValuesInSpecFile = new ArrayList<>();

    public static void loadDriver() {
        try {
            try {
                Class.forName(MYSQL_DRIVER);
            } catch (ClassNotFoundException e) {
                throw new ClassNotFoundException("JDBC driver was not successfully loaded due to ClassNotFoundException "
                        + "for the given driver \"" + e.getMessage() + "\"");
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public static Statement initializeDbConnection(String databaseName, String username, String password) {
        Statement statement = null;
        try {
            dbConnection = DriverManager.getConnection(MYSQL_DATABASE_URL + "/" + databaseName, username, password);
            saveValueForScenario(MYSQL_USERNAME, username);
            saveValueForScenario(MYSQL_PASSWORD, password);
            saveValueForScenario(MYSQL_DATABASE_NAME, databaseName);
            statement = dbConnection.createStatement();
        } catch (Exception e) {
            Assert.fail("MySQL database was not successfully connected due to " + e.getMessage());
        }
        return statement;
    }

    public static ResultSet getResultsByExecutingQuery(String query) {
        ResultSet resultSet = null;

        try {
            resultSet = connectDatabase().executeQuery(query);
        } catch (SQLException e) {
            printError("The executed query is invalid", MySqlOperator.class);
            e.printStackTrace();
        }
        saveValueForScenario(MYSQL_QUERY, query);
        return resultSet;
    }

    // This method is used to validate all the data from the spec file with respect to the query results at once, not row by row
    public static void checkAllResultsAtOnce(Table tableForExpectedResults) {
        try {
            String query = getSavedValueForScenario(MYSQL_QUERY);
            ResultSet resultSet = getResultsByExecutingQuery(query);
            getColumnNames(resultSet);

            List<String> headersList1 = new ArrayList<>();

            for (int i = 1; i <= resultSet.getMetaData().getColumnCount(); i++) {
                headersList1.add(resultSet.getMetaData().getColumnName(i));
            }

            List<List<String>> rowsList1 = new ArrayList<>();

            while (resultSet.next()) {
                ArrayList<String> data = new ArrayList<>();

                for (int i = 1; i <= resultSet.getMetaData().getColumnCount(); i++) {
                    data.add(resultSet.getString(i));
                }
                Record record = new Record(data);
                rowsList1.add(data);
                recordListForValuesInDatabase.add(record);
            }
            printResults(headersList1, rowsList1);

            List<List<String>> rowsList2 = new ArrayList<>();

            for (TableRow row : tableForExpectedResults.getTableRows()) {
                Record record = new Record(new ArrayList<>(row.getCellValues()));
                rowsList2.add(row.getCellValues());
                recordListForValuesInSpecFile.add(record);
            }

            Assert.assertEquals(recordListForValuesInDatabase, recordListForValuesInSpecFile,
                    "Results obtained from the database for the executed query and the expected results are different.\n");
        } catch (SQLException throwable) {
            throwable.printStackTrace();
        }
        recordListForValuesInDatabase.clear();
        recordListForValuesInSpecFile.clear();
    }

    // This method is used to validate all the data from the spec file with respect to the query results in row by row
    public static void checkResultsAndReturnMismatches(Table table) {
        try {
            String query = getSavedValueForScenario(MYSQL_QUERY);
            ResultSet resultSet = getResultsByExecutingQuery(query);
            getColumnNames(resultSet);

            List<String> headersList1 = new ArrayList<>();

            for (int i = 1; i <= resultSet.getMetaData().getColumnCount(); i++) {
                headersList1.add(resultSet.getMetaData().getColumnName(i));
            }
            List<List<String>> rowsList1 = new ArrayList<>();

            while (resultSet.next()) {
                ArrayList<String> data = new ArrayList<>();

                for (int i = 1; i <= resultSet.getMetaData().getColumnCount(); i++) {
                    data.add(resultSet.getString(i));
                }
                Record record = new Record(data);
                rowsList1.add(data);
                recordListForValuesInDatabase.add(record);
            }

            List<List<String>> rowsList2 = new ArrayList<>();

            for (TableRow row : table.getTableRows()) {
                Record record = new Record(new ArrayList<>(row.getCellValues()));
                rowsList2.add(row.getCellValues());
                recordListForValuesInSpecFile.add(record);
            }

            Collections.sort(recordListForValuesInSpecFile);
            Collections.sort(recordListForValuesInDatabase);
            RecordsChecker.compare(recordListForValuesInSpecFile, recordListForValuesInDatabase);

            if (!(recordListForValuesInSpecFile.equals(recordListForValuesInDatabase))) {
                printResults(headersList1, rowsList1);
            }

            Assert.assertTrue(recordListForValuesInDatabase.containsAll(recordListForValuesInSpecFile),
                    "Results obtained from the database for the executed query and the expected results are different.\n");
        } catch (SQLException throwable) {
            throwable.printStackTrace();
        }
        recordListForValuesInDatabase.clear();
        recordListForValuesInSpecFile.clear();
    }

    public static void closeDbConnection() {
        if (dbConnection != null) {
            try {
                dbConnection.close();
            } catch (SQLException throwable) {
                throwable.printStackTrace();
            }
            printInfo("Database connection successfully closed", MySqlOperator.class);
        }
    }

    private static Statement connectDatabase() {
        return MySqlOperator.initializeDbConnection(getSavedValueForScenario(MYSQL_DATABASE_NAME),
                getSavedValueForScenario(MYSQL_USERNAME), getSavedValueForScenario(MYSQL_PASSWORD));
    }

    private static void getRecordsInRows(ResultSet resultSet) {
        printInfo("Records in the rows: ", MySqlOperator.class);
        try {
            ResultSetMetaData metadata = resultSet.getMetaData();
            int columnCount = metadata.getColumnCount();
            while (resultSet.next()) {
                StringBuilder row = new StringBuilder();
                for (int i = 1; i <= columnCount; i++) {
                    row.append(resultSet.getString(i)).append(", ");
                }
                printInfo(row.toString(), MySqlOperator.class);
            }
        } catch (SQLException throwable) {
            throwable.printStackTrace();
        }
    }

    private static String getColumnNamesByIndex(ResultSet resultSet, int index) {
        String columnNames = null;
        try {
            ResultSetMetaData metadata = resultSet.getMetaData();
            columnNames = metadata.getColumnName(index);
        } catch (SQLException throwable) {
            throwable.printStackTrace();
        }
        return columnNames;
    }

    private static void getColumnNames(ResultSet resultSet) {
        try {
            ResultSetMetaData metadata = resultSet.getMetaData();
            int columnCount = metadata.getColumnCount();
            printInfo("Column Names: ", MySqlOperator.class);
            for (int i = 1; i <= columnCount; i++) {
                printInfo(metadata.getColumnName(i), MySqlOperator.class);
            }
            printInfo("\n", MySqlOperator.class);
            printInfo("Column count: " + columnCount + "\n", MySqlOperator.class);
        } catch (SQLException throwable) {
            throwable.printStackTrace();
        }
    }

    private static void printResults(List<String> headersList, List<List<String>> rowsList) {
        Board board = new Board(75);
        String tableString = board.setInitialBlock(new StringTable(board, 75, headersList, rowsList)
                .tableToBlocks()).build().getPreview();
        printInfo("\n", MySqlOperator.class);
        printInfo("Results obtained from the database for the executed query: \n" + tableString, MySqlOperator.class);
    }
}
