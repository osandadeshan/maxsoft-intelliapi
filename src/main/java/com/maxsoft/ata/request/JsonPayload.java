package com.maxsoft.ata.request;

import com.maxsoft.ata.util.ApiDocumentReader;
import com.thoughtworks.gauge.Gauge;
import java.io.IOException;


/**
 * Created by Osanda on 8/5/2017.
 */


public abstract class JsonPayload extends BaseClass {
	
	static String apiName = getSavedValueForScenario("API_NAME"); // Fetching Value from the Data Store
	static String request;
	static {
		try {
			request = ApiDocumentReader.getRequestPayloadTemplate(apiName);
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	
	protected JsonPayload() throws IOException {
	}
	
	public static String setJsonAttributeValueAs(String attributeValueInJSONTemplate, String attributeValueToBeSet) throws IOException {
		String replaceWithAttributeValue = request.replace(attributeValueInJSONTemplate, attributeValueToBeSet);
		request = replaceWithAttributeValue;
		return request;
	}
	
	public static void saveFinalJsonRequestBody(){
		saveValueForScenario("finalJsonRequestBody", request);
		System.out.println("The JSON request body that you are going to use for the API is:\n" + request);
		Gauge.writeMessage("The JSON request body that you are going to use for the API is:\n" + request);
	}

	public static void saveFinalJsonRequestBody(String payload){
		saveValueForScenario("finalJsonRequestBody", payload);
		System.out.println("The JSON request body that you are going to use for the API is:\n" + payload);
		Gauge.writeMessage("The JSON request body that you are going to use for the API is:\n" + payload);
	}
	
	public static void setRequestToDefault() throws IOException {
		request = ApiDocumentReader.getRequestPayloadTemplate(getSavedValueForScenario("API_NAME"));
	}
	
	
}
