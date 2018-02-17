package com.maxsoft.ata.util;

import com.opencsv.CSVReader;
import com.opencsv.CSVWriter;
import java.io.*;
import java.util.List;


public class CSV {

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

//replacement.concat(String.valueOf(i))
}
