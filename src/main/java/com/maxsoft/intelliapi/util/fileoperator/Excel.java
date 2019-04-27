package com.maxsoft.intelliapi.util.fileoperator;

/**
 * Project Name : MaxSoft-IntelliAPI
 * Developer    : Osanda Deshan
 * Version      : 1.0.0
 * Date         : 6/30/2018
 * Time         : 3:51 PM
 * Description  :
 **/

import com.maxsoft.intelliapi.api.Base;
import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.ss.usermodel.Sheet;
import org.apache.poi.ss.usermodel.Workbook;
import org.apache.poi.ss.util.CellAddress;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.util.Iterator;


public abstract class Excel {

	private static Base baseObj;

	static {
        baseObj = new Base();
    }

	private static int column;

	public static int findColumnNumber(String cellContent) throws IOException {
		FileInputStream inputStream = new FileInputStream(baseObj.getAPIDocumentFilePath());
		Workbook workbook = new XSSFWorkbook(inputStream);
		Sheet firstSheet = workbook.getSheetAt(0);
		Iterator<Row> iterator = firstSheet.iterator();
		CellAddress columnNumber = null;

		while(iterator.hasNext()){
			Row nextRow = iterator.next();
			Iterator<Cell> cellIterator = nextRow.cellIterator();
			while (cellIterator.hasNext()) {
				Cell cell = cellIterator.next();
				if(cell.getCellType()==Cell.CELL_TYPE_STRING){
					String text = cell.getStringCellValue();
					if (cellContent.equals(text)) {
						columnNumber=cell.getAddress();
						column = cell.getColumnIndex();
						break;
					}
				}
			}
		}
		workbook.close();
		return column;
	}

	public static int findRowNumber(String cellContent) throws IOException {
		FileInputStream excelFile = new FileInputStream(new File(baseObj.getAPIDocumentFilePath()));
		Workbook workbook = new XSSFWorkbook(excelFile);
		Sheet workSheet = workbook.getSheetAt(0);
		for (Row row : workSheet) {
			for (Cell cell : row) {
				if (cell.getCellType() == Cell.CELL_TYPE_STRING) {
					if (cell.getRichStringCellValue().getString().trim().equals(cellContent)) {
						return row.getRowNum();
					}
				}
			}
		}
		return 0;
	}

    public static int findRowNumber(String sheetName, String cellContent) throws IOException {
        FileInputStream excelFile = new FileInputStream(new File(baseObj.getAPIDocumentFilePath()));
        Workbook workbook = new XSSFWorkbook(excelFile);
        Sheet workSheet = workbook.getSheet(sheetName);
        for (Row row : workSheet) {
            for (Cell cell : row) {
                if (cell.getCellType() == Cell.CELL_TYPE_STRING) {
                    if (cell.getRichStringCellValue().getString().trim().equals(cellContent)) {
                        return row.getRowNum();
                    }
                }
            }
        }
        return 0;
    }


}
