package com.maxsoft.intelliapi.api;

/**
 * Project Name : MaxSoft-IntelliAPI
 * Developer    : Osanda Deshan
 * Version      : 1.0.0
 * Date         : 6/30/2018
 * Time         : 3:51 PM
 * Description  :
 **/

import com.maxsoft.intelliapi.common.Base;
import com.maxsoft.intelliapi.util.reader.ApiDocument;
import com.thoughtworks.gauge.Gauge;
import java.io.IOException;
import java.util.logging.FileHandler;
import java.util.logging.Logger;
import java.util.logging.SimpleFormatter;


public abstract class JsonPayload extends Base {

	static String apiName = getSavedValueForScenario("apiName"); // Fetching Value from the Data Store
	static String request;
	static {
		try {
			request = ApiDocument.getRequestPayloadTemplate(apiName);
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	private static Logger logger = Logger.getLogger(JsonPayload.class.getName());
	private static FileHandler fileHandler;
	private static SimpleFormatter formatter = new SimpleFormatter();

	static {
		try {
			fileHandler = new FileHandler(INTELLIAPI_LOGS_FILE_PATH, true);
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	public static void printInfo(String text){
		logger.addHandler(fileHandler);
		fileHandler.setFormatter(formatter);
		logger.info(text +"\n");
		Gauge.writeMessage(text);
	}

	public static String setJsonAttributeValueAs(String attributeValueInJSONTemplate, String attributeValueToBeSet) throws IOException {
		String replaceWithAttributeValue = request.replace(attributeValueInJSONTemplate, attributeValueToBeSet);
		request = replaceWithAttributeValue;
		return request;
	}

	public static void saveFinalJsonRequestBody(){
		saveValueForScenario("finalJsonRequestBody", request);
		printInfo("The JSON request body that you are going to use for the API is:\n" + request);
	}

	public static void saveFinalJsonRequestBody(String payload){
		saveValueForScenario("finalJsonRequestBody", payload);
		printInfo("The JSON request body that you are going to use for the API is:\n" + payload);
	}

	public static void setRequestToDefault() throws IOException {
		request = ApiDocument.getRequestPayloadTemplate(getSavedValueForScenario("apiName"));
	}


}
