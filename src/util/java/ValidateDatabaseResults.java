import com.thoughtworks.gauge.Gauge;
import com.thoughtworks.gauge.Table;
import com.thoughtworks.gauge.TableRow;
import org.testng.Assert;
import java.sql.ResultSet;
import java.sql.ResultSetMetaData;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;


/**
 * Created by Osanda on 7/31/2017.
 */


public class ValidateDatabaseResults extends BaseClass{

    ArrayList<Record> recordListForValuesInDatabase = new ArrayList<Record>();
    ArrayList<Record> recordListForValuesInSpecFile = new ArrayList<Record>();

    public Statement connectDb() throws SQLException, ClassNotFoundException {
        // Fetching username and password from the Data Store
        String username = getSavedValueForScenario("username");
        String password = getSavedValueForScenario("password");
        String databaseName = getSavedValueForScenario("databaseName");
        Statement statement = MySqlConnector.connectDatabase(databaseName, username, password);
        return statement;
    }

    public ResultSet executeQuery(String query) {
        ResultSet resultSet = null;
        try {
            resultSet = connectDb().executeQuery(query);
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
        Assert.assertTrue(recordListForValuesInSpecFile.equals(recordListForValuesInDatabase), "Results obtained from the database for the executed query and the expected results are different.\n");
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
        Compare.compareRecords(recordListForValuesInSpecFile, recordListForValuesInDatabase);
        if (!(recordListForValuesInSpecFile.equals(recordListForValuesInDatabase))) {
            printResults(headersList1, rowsList1, "obtained");
        }
        Assert.assertTrue(recordListForValuesInSpecFile.equals(recordListForValuesInDatabase), "Results obtained from the database for the executed query and the expected results are different.\n");
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


}
