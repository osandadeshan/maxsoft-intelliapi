package com.maxsoft.intelliapi.util.fileoperator;

import com.opencsv.CSVReader;
import com.opencsv.CSVWriter;

import java.io.*;
import java.util.List;

import static com.maxsoft.intelliapi.Constants.CURRENT_DIRECTORY;

/**
 * Project Name : MaxSoft-IntelliAPI
 * Developer    : Osanda Deshan
 * Version      : 1.0.0
 * Date         : 6/30/2018
 * Time         : 3:51 PM
 * Description  :
 **/

public class CsvFileOperator {

    public static void writeToCsv(String filePath, String header1, String data, int noOfIterations) {
        try {
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
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public int getLinesCount(String filePath) {
        int count = -1;

        try {
            BufferedReader bufferedReader = new BufferedReader(new FileReader(filePath));

            while (bufferedReader.readLine() != null) {
                count++;
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        return count;
    }

    public int getColumnIndexByColumnName(String filePath, String columnName) {
        int i = 0;

        try {
            File inputFile = new File(filePath);
            CSVReader reader = new CSVReader(new FileReader(inputFile), ',');
            List<String[]> csvBody = reader.readAll();

            while (!csvBody.get(0)[i].equals(columnName)) {
                i++;
            }
            reader.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
        return i;
    }

    public void updateCSVByRowIndexAndColumnIndex(String filePath, String replacement, int row, int col) {
        try {
            File inputFile = new File(filePath);
            CSVReader reader = new CSVReader(new FileReader(inputFile), ',');
            List<String[]> csvBody = reader.readAll();
            csvBody.get(row)[col] = replacement;
            reader.close();
            CSVWriter writer = new CSVWriter(new FileWriter(inputFile), ',');
            writer.writeAll(csvBody);
            writer.flush();
            writer.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
