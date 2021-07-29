package com.maxsoft.intelliapi.util.fileoperator;

import com.maxsoft.intelliapi.util.reader.EnvironmentPropertyReader;
import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.ss.usermodel.Sheet;
import org.apache.poi.ss.usermodel.Workbook;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;

import java.io.FileInputStream;
import java.io.IOException;
import java.util.Iterator;
import java.util.Objects;

/**
 * Project Name : MaxSoft-IntelliAPI
 * Developer    : Osanda Deshan
 * Version      : 1.0.0
 * Date         : 6/30/2018
 * Time         : 3:51 PM
 * Description  :
 **/

public abstract class ExcelFileOperator {

    public static int findColumnNumber(String cellContent) {
        String columnNumber = null;

        try {
            FileInputStream inputStream = new FileInputStream(EnvironmentPropertyReader.getApiDocumentFilePath());
            Workbook workbook = new XSSFWorkbook(inputStream);
            Sheet firstSheet = workbook.getSheetAt(0);

            for (Row nextRow : firstSheet) {
                Iterator<Cell> cellIterator = nextRow.cellIterator();
                while (cellIterator.hasNext()) {
                    Cell cell = cellIterator.next();
                    if (cell.getCellType() == Cell.CELL_TYPE_STRING) {
                        String text = cell.getStringCellValue();
                        if (cellContent.equals(text)) {
                            columnNumber = String.valueOf(cell.getColumnIndex());
                            break;
                        }
                    }
                }
            }
            workbook.close();
        } catch (IOException e) {
            e.printStackTrace();
        }

        return Integer.parseInt(Objects.requireNonNull(columnNumber));
    }

    public static int findRowNumber(String cellContent) {
        String rowNumber = null;

        try {
            FileInputStream excelFile = new FileInputStream(EnvironmentPropertyReader.getApiDocumentFilePath());
            Workbook workbook = new XSSFWorkbook(excelFile);
            Sheet workSheet = workbook.getSheetAt(0);
            for (Row row : workSheet) {
                for (Cell cell : row) {
                    if (cell.getCellType() == Cell.CELL_TYPE_STRING) {
                        if (cell.getRichStringCellValue().getString().trim().equals(cellContent)) {
                            rowNumber = String.valueOf(row.getRowNum());
                            break;
                        }
                    }
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        return Integer.parseInt(Objects.requireNonNull(rowNumber));
    }

    public static int findRowNumber(String sheetName, String cellContent) {
        String rowNumber = null;

        try {
            FileInputStream excelFile = new FileInputStream(EnvironmentPropertyReader.getApiDocumentFilePath());
            Workbook workbook = new XSSFWorkbook(excelFile);
            Sheet workSheet = workbook.getSheet(sheetName);
            for (Row row : workSheet) {
                for (Cell cell : row) {
                    if (cell.getCellType() == Cell.CELL_TYPE_STRING) {
                        if (cell.getRichStringCellValue().getString().trim().equals(cellContent)) {
                            rowNumber = String.valueOf(row.getRowNum());
                            break;
                        }
                    }
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        return Integer.parseInt(Objects.requireNonNull(rowNumber));
    }
}
