package com.maxsoft.intelliapi.util.reader;

import com.maxsoft.intelliapi.util.fileoperator.ExcelFileOperator;
import org.apache.poi.ss.usermodel.Sheet;
import org.apache.poi.ss.usermodel.Workbook;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;

import java.io.FileInputStream;
import java.io.IOException;
import java.security.InvalidParameterException;

import static com.maxsoft.intelliapi.Constants.*;
import static com.maxsoft.intelliapi.util.DataStoreProcessor.saveValueForScenario;

/**
 * Project Name : MaxSoft-IntelliAPI
 * Developer    : Osanda Deshan
 * Version      : 1.0.0
 * Date         : 6/30/2018
 * Time         : 3:51 PM
 * Description  :
 **/

public abstract class ApiDocumentReader {

    private static final String apiDocFilePath = EnvironmentPropertyReader.getApiDocumentFilePath();
    private static String value = "";
    private static String error = "";

    public static void setApiEndpoint(String apiEndpointName) {
        int row, column;
        row = ExcelFileOperator.findRowNumber(apiEndpointName);
        column = ExcelFileOperator.findColumnNumber(apiEndpointName) + 1;
        error = "\"" + apiEndpointName + "\" API Endpoint Name is not exist in the API Document Excel file located in \""
                + apiDocFilePath + "\"";
        if (row == 0 && column == 1) {
            throw new InvalidParameterException(error);
        } else {
            saveValueForScenario(VAR_API_ENDPOINT, getDataFromExcel(row, column));
        }
    }

    public static void setHttpMethod(String apiEndpointName) {
        int row, column;
        row = ExcelFileOperator.findRowNumber(apiEndpointName);
        column = ExcelFileOperator.findColumnNumber(apiEndpointName) + 2;
        error = "\"" + apiEndpointName + "\" API Endpoint Name is not exist in the API Document Excel file located in \""
                + apiDocFilePath + "\"";
        if (row == 0 && column == 2) {
            throw new InvalidParameterException(error);
        } else {
            saveValueForScenario(VAR_API_HTTP_METHOD, getDataFromExcel(row, column));
        }
    }

    public static void setBodyType(String apiEndpointName) {
        int row, column;
        row = ExcelFileOperator.findRowNumber(apiEndpointName);
        column = ExcelFileOperator.findColumnNumber(apiEndpointName) + 3;
        error = "\"" + apiEndpointName + "\" API Endpoint Name is not exist in the API Document Excel file located in \""
                + apiDocFilePath + "\"";
        if (row == 0 && column == 2) {
            throw new InvalidParameterException(error);
        } else {
            saveValueForScenario(VAR_API_REQUEST_BODY_TYPE, getDataFromExcel(row, column));
        }
    }

    public static void setRequestPayloadTemplate(String apiEndpointName) {
        int row, column;
        row = ExcelFileOperator.findRowNumber(apiEndpointName);
        column = ExcelFileOperator.findColumnNumber(apiEndpointName) + 4;
        error = "\"" + apiEndpointName + "\" API Endpoint Name is not exist in the API Document Excel file located in \""
                + apiDocFilePath + "\"";
        if (row == 0 && column == 2) {
            throw new InvalidParameterException(error);
        } else {
            saveValueForScenario(VAR_API_JSON_REQUEST_BODY, getDataFromExcel(row, column));
        }
    }

    public static String getDataFromExcel(String sheetName, String cellContent) {
        String cellValue = "";
        int colNum = 1;
        try {
            FileInputStream excelFile = new FileInputStream(apiDocFilePath);
            Workbook workbook = new XSSFWorkbook(excelFile);
            Sheet workSheet = workbook.getSheet(sheetName);
            cellValue = workSheet.getRow(ExcelFileOperator.findRowNumber(sheetName, cellContent))
                    .getCell(colNum).getStringCellValue();
            return cellValue;
        } catch (IOException e) {
            e.printStackTrace();
        } catch (NullPointerException e) {
            throw new InvalidParameterException("Key \"" + cellContent + "\" is not found in \"" + sheetName + "\" sheet");
        }
        return cellValue;
    }

    private static String getDataFromExcel(int row, int column) {
        try {
            FileInputStream excelFile = new FileInputStream(apiDocFilePath);
            Workbook workbook = new XSSFWorkbook(excelFile);
            Sheet workSheet = workbook.getSheetAt(0);
            value = workSheet.getRow(row).getCell(column).getStringCellValue();
        } catch (IOException e) {
            e.printStackTrace();
        }
        return value;
    }
}
