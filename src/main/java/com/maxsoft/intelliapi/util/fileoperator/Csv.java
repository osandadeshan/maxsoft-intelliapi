package com.maxsoft.intelliapi.util.fileoperator;

/**
 * Project Name : MaxSoft-IntelliAPI
 * Developer    : Osanda Deshan
 * Version      : 1.0.0
 * Date         : 6/30/2018
 * Time         : 3:51 PM
 * Description  :
 **/

import com.opencsv.CSVReader;
import com.opencsv.CSVWriter;
import java.io.*;
import java.util.List;
import static com.maxsoft.intelliapi.common.Base.CURRENT_DIRECTORY;


public class Csv {

    public int getLinesCount(String filePath) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new FileReader(filePath));
        String input;
        int count = -1;
        while((input = bufferedReader.readLine()) != null)
        {
            count++;
        }
        return count;
    }

    public int getColumnIndexByColumnName(String filePath, String columnName) throws IOException {
        File inputFile = new File(filePath);
        // Read existing file
        CSVReader reader = new CSVReader(new FileReader(inputFile), ',');
        List<String[]> csvBody = reader.readAll();
        // Search the header name throughout the column names in row 0
        int i = 0;
        while (!csvBody.get(0)[i].equals(columnName)){
            i++;
        }
        reader.close();
        return i;
    }

    public void updateCSVByRowIndexAndColumnIndex(String filePath, String replacement, int row, int col) throws IOException {
        File inputFile = new File(filePath);
        // Read existing file
        CSVReader reader = new CSVReader(new FileReader(inputFile), ',');
        List<String[]> csvBody = reader.readAll();
        // get CSV row column  and replace with by using row and column
        csvBody.get(row)[col] = replacement;
        reader.close();
        // Write to CSV file which is open
        CSVWriter writer = new CSVWriter(new FileWriter(inputFile), ',');
        writer.writeAll(csvBody);
        writer.flush();
        writer.close();
    }

    public static void writeToCsv(String filePath, String header1, String data, int noOfIterations) throws IOException {
        File file = new File(CURRENT_DIRECTORY + filePath);
        file.delete();
        file.createNewFile();
        String[] header = {header1};
        CSVWriter writer = new CSVWriter(new FileWriter(file), ',');
        writer.writeNext(header);
        for (int i = 0; i < noOfIterations; i++) {
            writer.writeNext(new String[]{data});
        }
        writer.flush();
        writer.close();
    }


}
