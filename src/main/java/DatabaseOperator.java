import com.thoughtworks.gauge.Gauge;
import com.thoughtworks.gauge.Step;
import com.thoughtworks.gauge.Table;
import java.sql.SQLException;


/**
 * Created by Osanda on 7/12/2017.
 */


public class DatabaseOperator extends ValidateDatabaseResults {
	
	static String MYSQL_DRIVER_LOADING_SUCCESS_MESSAGE = "MySQL driver has been loaded successfully";
	static String MYSQL_DATABASE_CONNECTION_SUCCESS_MESSAGE = "MySQL database has been connected successfully";
	static String QUERY_EXECUTION_SUCCESS_MESSAGE = "Query has been successfully executed";

	public void loadMySqlDriver() throws SQLException, ClassNotFoundException {
		MySqlConnector.loadDriver();
		System.out.println(MYSQL_DRIVER_LOADING_SUCCESS_MESSAGE);
		Gauge.writeMessage(MYSQL_DRIVER_LOADING_SUCCESS_MESSAGE);
	}

	public void loadMySqlDatabase (String databaseName, String username, String password) throws SQLException, ClassNotFoundException {
		MySqlConnector.connectDatabase(databaseName, username, password);
		System.out.println(MYSQL_DATABASE_CONNECTION_SUCCESS_MESSAGE);
        Gauge.writeMessage(MYSQL_DATABASE_CONNECTION_SUCCESS_MESSAGE);
	}

	public void executeGivenQuery(String query) {
		if (executeQuery(query).toString().equals("")){
			System.out.println("No records found for the executed query");
			Gauge.writeMessage("No records found for the executed query");
		}
		if (executeQuery(query) == null){
			System.out.println("The executed query is invalid");
			Gauge.writeMessage("The executed query is invalid");
		} else {
			executeQuery(query);
			System.out.println(QUERY_EXECUTION_SUCCESS_MESSAGE);
			Gauge.writeMessage(QUERY_EXECUTION_SUCCESS_MESSAGE);
		}
	}

	public void verifyResults( Table table) throws SQLException, ClassNotFoundException {
		verifyResultsAndReturnMismatches(table);
	}

	public void verifyAllResults( Table table) throws SQLException, ClassNotFoundException {
		verifyAllResultsAtOnce(table);
	}

	public void closeDbConnection() throws Exception {
		MySqlConnector.closeDbConnection();
	}
		
	
}
