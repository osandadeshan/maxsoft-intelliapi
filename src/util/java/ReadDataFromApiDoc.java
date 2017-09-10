import org.apache.poi.ss.usermodel.*;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;


/**
 * Created by Osanda on 7/14/2017.
 */


public abstract class ReadDataFromApiDoc {
	
	private static final String FILE_PATH = System.getProperty("user.dir") + "\\" + System.getenv("api_document_path");
	private static String value = "";
	
	public static String getDataFromExcel(int row, int column) {
		try {
			FileInputStream excelFile = new FileInputStream(new File(FILE_PATH));
			System.out.println(FILE_PATH);
			Workbook workbook = new XSSFWorkbook(excelFile);
			Sheet workSheet = workbook.getSheetAt(0);
			value = workSheet.getRow(row).getCell(column).getStringCellValue();
			System.out.println(value);
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
		return value;
	}
	
	public static String getAPIEndpoint(String apiEndpointName) throws IOException {
		int row, column;
		row = GetCellAddressInExcel.findRowNumber(apiEndpointName);
		column = GetCellAddressInExcel.findColumnNumber(apiEndpointName) + 1;
		return getDataFromExcel(row, column);
	}
	
	public static String getHttpMethod(String apiEndpointName) throws IOException {
		int row, column;
		row = GetCellAddressInExcel.findRowNumber(apiEndpointName);
		column = GetCellAddressInExcel.findColumnNumber(apiEndpointName) + 2;
		return getDataFromExcel(row, column);
	}
	
	public static String getRequestTemplate(String apiEndpointName) throws IOException {
		int row, column;
		row = GetCellAddressInExcel.findRowNumber(apiEndpointName);
		column = GetCellAddressInExcel.findColumnNumber(apiEndpointName) + 3;
		return getDataFromExcel(row, column);
	}
	
	
}