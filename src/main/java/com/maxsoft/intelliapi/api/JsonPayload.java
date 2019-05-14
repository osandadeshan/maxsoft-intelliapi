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
import org.apache.log4j.Logger;
import java.io.IOException;


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

	private final static Logger logger = Logger.getLogger(JsonPayload.class.getName());

	public static void printInfo(String text){
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
