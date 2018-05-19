/*
 Developer      : Osanda Deshan 
 Created Date   : 5/12/2018
 Project        : MaxSoft-IntelliAPI
 */

package com.maxsoft.intelliapi.util;

import com.jayway.jsonpath.Configuration;
import com.jayway.jsonpath.JsonPath;
import java.io.*;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Properties;


public class JsonReader {

	public static final String CURRENT_DIRECTORY = System.getProperty("user.dir");
	static Properties propertyFile = new Properties();
	static InputStream input = null;
	public static String propertyFilePath = CURRENT_DIRECTORY + File.separator + "env" + File.separator + "default"
			+ File.separator + "default.properties";

	public static String readFile(String path, Charset encoding) throws IOException {
		byte[] encoded = Files.readAllBytes(Paths.get(path));
		return new String(encoded, encoding);
	}

	public static String getExecutionResults() {
		try {
			input = new FileInputStream(propertyFilePath);
			// load a properties file
			propertyFile.load(input);
		} catch (IOException ex) {
			ex.printStackTrace();
		} finally {
			if (input != null) {
				try {
					input.close();
				} catch (IOException e) {
					e.printStackTrace();
				}
			}
		}

		try
		{
			String jsonFilePath = CURRENT_DIRECTORY + File.separator + propertyFile.getProperty("gauge_reports_dir") + File.separator +
					"json-report" + File.separator + "result.json";

			Object responseString = Configuration.defaultConfiguration().jsonProvider().parse(readFile(jsonFilePath, Charset.defaultCharset()));

			String projectName = JsonPath.read(responseString, "$.projectName").toString();
			String timestamp = JsonPath.read(responseString, "$.timestamp").toString();
			String environment = JsonPath.read(responseString, "$.environment").toString();
			String executionTime = JsonPath.read(responseString, "$.executionTime").toString();
			String executionStatus = JsonPath.read(responseString, "$.executionStatus").toString();;
			String successRate = JsonPath.read(responseString, "$.successRate").toString();
			String failRate = String.valueOf(100 - Integer.valueOf(successRate));
			String passedSpecsCount = JsonPath.read(responseString, "$.passedSpecsCount").toString();
			String failedSpecsCount = JsonPath.read(responseString, "$.failedSpecsCount").toString();
			String skippedSpecsCount = JsonPath.read(responseString, "$.skippedSpecsCount").toString();
			//		  String passedScenarioCount = JsonPath.read(responseString, "$.passedScenarioCount").toString();
			//		  String failedScenarioCount = JsonPath.read(responseString, "$.failedScenarioCount").toString();
			//		  String skippedScenarioCount = JsonPath.read(responseString, "$.skippedScenarioCount").toString();

			String executionResults = "-------------------------------------------------------------------------------------------------------------\n" +
					"-------------------------------------------------------------------------------------------------------------\n\n" +
					"Test Execution Results: \n\n" +
					"-------------------------------------------------------------------------------------------------------------\n" +
					"-------------------------------------------------------------------------------------------------------------\n\n\n" +
					                  "Project Name        : " + projectName + "\n\n" +
									  "Timestamp           : " + timestamp + "\n\n" +
									  "Environment         : " + environment.substring(0, 1).toUpperCase() + environment.substring(1) + "\n\n" +
									  "Execution Time      : " + milliSecondsToTime(Integer.valueOf(executionTime)) + "\n\n" +
									  "Execution Status    : " + executionStatus.substring(0, 1).toUpperCase() + executionStatus.substring(1) + "\n\n" +
									  "Success Rate        : " + successRate + "%\n\n" +
									  "Fail Rate           : " + failRate + "%\n\n" +
									  "Passed Specs Count  : " + passedSpecsCount + "\n\n" +
									  "Failed Specs Count  : " + failedSpecsCount + "\n\n" +
									  "Skipped Specs Count : " + skippedSpecsCount +
					"\n\n-------------------------------------------------------------------------------------------------------------";

			System.out.println(executionResults);
			return executionResults;
		}
		catch (FileNotFoundException ex){
			ex.getStackTrace();
		}
		catch (IOException ex){
			ex.getStackTrace();
		}
		catch (Exception ex){
			ex.getStackTrace();
		}
		return "An error occurred while fetching the execution results from json-report";
	}

	public static String milliSecondsToTime(int millisec) {
		int milli = millisec % 1000;
		int sec = millisec/1000;
		int second = sec % 60;
		int minute = sec / 60;
		if (minute >= 60) {
			int hour = minute / 60;
			minute %= 60;
			return hour + "h " + (minute < 10 ? "0" + minute : minute) + "m " + (second < 10 ? "0" + second : second) + "s " +
					milli + "ms";
		} else {
			return minute + "m " + (second < 10 ? "0" + second : second) + "s " + milli + "ms";
		}
	}


}
