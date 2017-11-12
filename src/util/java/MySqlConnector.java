import com.mysql.jdbc.CommunicationsException;
import com.thoughtworks.gauge.Gauge;
import org.junit.Assert;

import java.sql.*;


/**
 * Created by Osanda on 7/18/2017.
 */


public class MySqlConnector extends BaseClass{
    
    static String MYSQL_DRIVER_CLASS = "com.mysql.jdbc.Driver";
    static String DATABASE_SERVER_URL = System.getenv("database_url");
    static String MYSQL_DATABASE_CONNECTION_CLOSE_MESSAGE = "Database connection successfully closed";
    static Connection dbConnection;
    
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
    
    public static Statement connectDatabase(String databaseName, String username, String password) throws ClassNotFoundException, SQLException {
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

    public static void closeDbConnection() throws Exception {
        // Close DB connection
        if (dbConnection != null) {
            dbConnection.close();
            System.out.println(MYSQL_DATABASE_CONNECTION_CLOSE_MESSAGE);
            Gauge.writeMessage(MYSQL_DATABASE_CONNECTION_CLOSE_MESSAGE);
        }
    }
	
    
}
