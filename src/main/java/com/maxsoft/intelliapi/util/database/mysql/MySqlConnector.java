package com.maxsoft.intelliapi.util.database.mysql;

/**
 * Project Name : MaxSoft-IntelliAPI
 * Developer    : Osanda Deshan
 * Version      : 1.0.0
 * Date         : 6/30/2018
 * Time         : 3:51 PM
 * Description  :
 **/

import com.maxsoft.intelliapi.request.Base;
import com.maxsoft.intelliapi.util.comparison.Comparison;
import com.maxsoft.intelliapi.util.comparison.Record;
import com.mysql.jdbc.CommunicationsException;
import com.thoughtworks.gauge.Gauge;
import com.thoughtworks.gauge.Table;
import com.thoughtworks.gauge.TableRow;
import org.junit.Assert;
import java.sql.*;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;


public class MySqlConnector extends Base {

    static String MYSQL_DRIVER_CLASS = "com.mysql.jdbc.Driver";
    static String DATABASE_SERVER_URL = System.getenv("database_url");
    static String MYSQL_DATABASE_CONNECTION_CLOSE_MESSAGE = "Database connection successfully closed";
    static Connection dbConnection;
    ArrayList<Record> recordListForValuesInDatabase = new ArrayList<Record>();
    ArrayList<Record> recordListForValuesInSpecFile = new ArrayList<Record>();

    public static void loadDriver() throws CommunicationsException{
        try {
            try {
                Class.forName(MYSQL_DRIVER_CLASS);
            } catch (ClassNotFoundException e) {
                Assert.fail("JDBC driver was not successfully loaded due to ClassNotFoundException for the given driver \"" + e.getMessage() + "\"");
            }
        } catch (Exception e) {
            Assert.fail("JDBC driver was not successfully loaded due to ClassNotFoundException for the given driver \"" + e.getMessage() + "\"");
        }
    }

    public static Statement initializeDbConnection(String databaseName, String username, String password) throws ClassNotFoundException, SQLException {
        String databaseUrl = DATABASE_SERVER_URL + databaseName;
        try {
            dbConnection = DriverManager.getConnection(databaseUrl, username, password);
        } catch (CommunicationsException e) {
            Assert.fail("MySQL database was not successfully connected due to " + e.getMessage());
        } catch (Exception e) {
            Assert.fail("MySQL database was not successfully connected due to " + e.getMessage());
        }
        // Adding username to the Data Store
        saveValueForScenario("username", username);
        // Adding password to the Data Store
        saveValueForScenario("password", password);
        // Adding database name to the Data Store
        saveValueForScenario("databaseName", databaseName);
        Statement statement = dbConnection.createStatement();
        return statement;
    }

    public Statement connectDatabase() throws SQLException, ClassNotFoundException {
        // Fetching username and password from the Data Store
        String username = getSavedValueForScenario("username");
        String password = getSavedValueForScenario("password");
        String databaseName = getSavedValueForScenario("databaseName");
        Statement statement = MySqlConnector.initializeDbConnection(databaseName, username, password);
        return statement;
    }

    public ResultSet executeQuery(String query) {
        ResultSet resultSet = null;
        try {
            resultSet = connectDatabase().executeQuery(query);
        } catch (SQLException e) {
            System.out.println("The executed query is invalid");
            Gauge.writeMessage("The executed query is invalid");
            e.printStackTrace();
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        }
        // Adding query to the Data Store
        saveValueForScenario("query", query);
        return resultSet;
    }

    // This method is used to validate all the data from the spec file with respect to the query results at once, not row by row
    public void verifyAllResultsAtOnce(Table tableForExpectedResults) throws SQLException, ClassNotFoundException {
        // Fetching query from the Data Store
        String query = getSavedValueForScenario("query");
        ResultSet resultSet = executeQuery(query);
        getColumnNames(resultSet);

        List<String> headersList1 = new ArrayList<String>();
        for(int i=1; i<=resultSet.getMetaData().getColumnCount(); i++){
            headersList1.add(resultSet.getMetaData().getColumnName(i));
        }
        List<List<String>> rowsList1 = new ArrayList<List<String>>();
        while (resultSet.next()) {
            ArrayList<String> data = new ArrayList<String>();
            for(int i=1; i<=resultSet.getMetaData().getColumnCount(); i++){
                data.add(resultSet.getString(i));
            }
            Record record = new Record(data);
            rowsList1.add(data);
            recordListForValuesInDatabase.add(record);
        }
        printResults(headersList1, rowsList1, "obtained");

        List<String> headersList2 = tableForExpectedResults.getColumnNames();
        List<List<String>> rowsList2 = new ArrayList<List<String>>();
        for (TableRow row : tableForExpectedResults.getTableRows()) {
            Record record = new Record(new ArrayList<String>(row.getCellValues()));
            rowsList2.add(row.getCellValues());
            recordListForValuesInSpecFile.add(record);
        }
        //printResults(headersList2, rowsList2, "expected");
        org.testng.Assert.assertTrue(recordListForValuesInSpecFile.equals(recordListForValuesInDatabase), "Results obtained from the database for the executed query and the expected results are different.\n");
    }

    // This method is used to validate all the data from the spec file with respect to the query results in row by row
    public void verifyResultsAndReturnMismatches(Table tableForExpectedResults) throws SQLException, ClassNotFoundException {
        // Fetching query from the Data Store
        String query = getSavedValueForScenario("query");
        ResultSet resultSet = executeQuery(query);
        getColumnNames(resultSet);

        List<String> headersList1 = new ArrayList<String>();
        for(int i=1; i<=resultSet.getMetaData().getColumnCount(); i++){
            headersList1.add(resultSet.getMetaData().getColumnName(i));
        }
        List<List<String>> rowsList1 = new ArrayList<List<String>>();
        while (resultSet.next()) {
            ArrayList<String> data = new ArrayList<String>();
            for(int i=1; i<=resultSet.getMetaData().getColumnCount(); i++){
                data.add(resultSet.getString(i));
            }
            Record record = new Record(data);
            rowsList1.add(data);
            recordListForValuesInDatabase.add(record);
        }

        List<String> headersList2 = tableForExpectedResults.getColumnNames();
        List<List<String>> rowsList2 = new ArrayList<List<String>>();
        for (TableRow row : tableForExpectedResults.getTableRows()) {
            Record record = new Record(new ArrayList<String>(row.getCellValues()));
            rowsList2.add(row.getCellValues());
            recordListForValuesInSpecFile.add(record);
        }
        //printResults(headersList2, rowsList2, "expected");

        Collections.sort(recordListForValuesInSpecFile);
        Collections.sort(recordListForValuesInDatabase);
        Comparison.compareRecords(recordListForValuesInSpecFile, recordListForValuesInDatabase);
        if (!(recordListForValuesInSpecFile.equals(recordListForValuesInDatabase))) {
            printResults(headersList1, rowsList1, "obtained");
        }
        org.testng.Assert.assertTrue(recordListForValuesInSpecFile.equals(recordListForValuesInDatabase), "Results obtained from the database for the executed query and the expected results are different.\n");
    }

    public void getColumnNames(ResultSet resultSet) throws SQLException {
        ResultSetMetaData metadata = resultSet.getMetaData();
        int columnCount = metadata.getColumnCount();
        System.out.println("\nColumn Names: ");
        for (int i = 1; i <= columnCount; i++) {
            System.out.println(metadata.getColumnName(i));
        }
        System.out.println("Column count: "+columnCount);
        System.out.println();
    }

    public void getRecordsinRows(ResultSet resultSet) throws SQLException {
        System.out.println("Records in the rows: ");
        ResultSetMetaData metadata = resultSet.getMetaData();
        int columnCount = metadata.getColumnCount();
        while (resultSet.next()) {
            String row = "";
            for (int i = 1; i <= columnCount; i++) {
                row += resultSet.getString(i) + ", ";
            }
            System.out.println(row);
        }
    }

    public String getColumnNamesByIndex(ResultSet resultSet, int index) throws SQLException {
        ResultSetMetaData metadata = resultSet.getMetaData();
        return metadata.getColumnName(index);
    }

    public static void closeDbConnection() throws Exception {
        // Close DB connection
        if (dbConnection != null) {
            dbConnection.close();
            System.out.println(MYSQL_DATABASE_CONNECTION_CLOSE_MESSAGE);
            Gauge.writeMessage(MYSQL_DATABASE_CONNECTION_CLOSE_MESSAGE);
        }
    }


}
