package com.maxsoft.intelliapi.stepimpl.database;

import com.maxsoft.intelliapi.database.MySqlOperator;
import com.thoughtworks.gauge.Step;
import com.thoughtworks.gauge.Table;

import static com.maxsoft.intelliapi.util.LogUtil.printInfo;

/**
 * Project Name : MaxSoft-IntelliAPI
 * Developer    : Osanda Deshan
 * Version      : 1.0.0
 * Date         : 6/30/2018
 * Time         : 3:51 PM
 * Description  :
 **/

public class MySqlStepImpl {

    // Use this method to load the mysql driver
	@Step("Given a user successfully connected to the MySQL Driver")
    public void loadMySqlDriver() {
        MySqlOperator.loadDriver();
        printInfo("MySQL driver has been loaded successfully");
    }

    // Use this method to load the mysql database
	@Step("And the user need to connect to the <databaseName> MySQL database using username as <username> and password as <password>")
    public void loadMySqlDatabase(String databaseName, String username, String password) {
        MySqlOperator.initializeDbConnection(databaseName, username, password);
        printInfo("MySQL database has been connected successfully");
    }

    // Use this method to execute the mysql query
	@Step("When the user executes the MySQL query as <query>")
    public void executeGivenQuery(String query) {
        if (MySqlOperator.getResultsByExecutingQuery(query).toString().equals("")) {
            printInfo("No records found for the executed query");
        }
        if (MySqlOperator.getResultsByExecutingQuery(query) == null) {
			printInfo("The executed query is invalid");
        } else {
            MySqlOperator.getResultsByExecutingQuery(query);
            printInfo("Query has been successfully executed");
        }
    }

    // Use this method to validate all the data from the spec file with respect to the query results in row by row
	@Step("Then the results obtained from the MySQL database should contain the following <table>")
    public void verifyResults(Table table) {
        MySqlOperator.checkResultsAndReturnMismatches(table);
    }

    // Use this method to validate all the data from the spec file with respect to the query results at once, not row by row
	@Step("Then the results obtained from the MySQL database should equal to the following <table>")
    public void verifyAllResults(Table table) {
        MySqlOperator.checkAllResultsAtOnce(table);
    }

    // Use this method to close the mysql connection
	@Step("And the user close the MySQL database connection")
	public void closeDbConnection() {
        MySqlOperator.closeDbConnection();
	}
}
