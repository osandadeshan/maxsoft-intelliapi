package com.maxsoft.intelliapi.database.mysql;

/**
 * Project Name : MaxSoft-IntelliAPI
 * Developer    : Osanda Deshan
 * Version      : 1.0.0
 * Date         : 6/30/2018
 * Time         : 3:51 PM
 * Description  :
 **/

import com.maxsoft.intelliapi.util.database.mysql.MySqlOperator;
import com.thoughtworks.gauge.Gauge;
import com.thoughtworks.gauge.Table;
import org.apache.log4j.Logger;
import java.io.IOException;
import java.sql.SQLException;


public class MySqlStepImpl extends MySqlOperator {

	private static final String MYSQL_DRIVER_LOADING_SUCCESS_MESSAGE = "MySQL driver has been loaded successfully";
	private static final String MYSQL_DATABASE_CONNECTION_SUCCESS_MESSAGE = "MySQL database has been connected successfully";
	private static final String QUERY_EXECUTION_SUCCESS_MESSAGE = "Query has been successfully executed";
	private static final String EMPTY_QUERY_MESSAGE = "No records found for the executed query";
	private static final String INVALID_QUERY_MESSAGE = "The executed query is invalid";

	private final static Logger logger = Logger.getLogger(MySqlStepImpl.class.getName());

	public static void printInfo(String text){
		logger.info(text);
		Gauge.writeMessage(text);
	}

	public MySqlStepImpl() throws IOException {
	}

	public void loadMySqlDriver() {
		MySqlOperator.loadDriver();
		printInfo(MYSQL_DRIVER_LOADING_SUCCESS_MESSAGE);
	}

	public void loadMySqlDatabase (String databaseName, String username, String password) throws SQLException {
		MySqlOperator.initializeDbConnection(databaseName, username, password);
		printInfo(MYSQL_DATABASE_CONNECTION_SUCCESS_MESSAGE);
	}

	public void executeGivenQuery(String query) {
		if (executeQuery(query).toString().equals("")){
			printInfo(EMPTY_QUERY_MESSAGE);
		}
		if (executeQuery(query) == null){
			printInfo(INVALID_QUERY_MESSAGE);
		} else {
			executeQuery(query);
			printInfo(QUERY_EXECUTION_SUCCESS_MESSAGE);
		}
	}

	public void verifyResults( Table table) throws SQLException {
		verifyResultsAndReturnMismatches(table);
	}

	public void verifyAllResults( Table table) throws SQLException {
		verifyAllResultsAtOnce(table);
	}

	public static void closeDbConnection() throws Exception {
		MySqlOperator.closeDbConnection();
	}


}
