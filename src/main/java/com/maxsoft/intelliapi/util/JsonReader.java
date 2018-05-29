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

    public static String getPassedScenarioCount() {
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
        String passedScenarioCount = "";
        try {
            String jsonFilePath = CURRENT_DIRECTORY + File.separator + propertyFile.getProperty("gauge_reports_dir") + File.separator +
                    "json-report" + File.separator + "result.json";

            Object responseString = Configuration.defaultConfiguration().jsonProvider().parse(readFile(jsonFilePath, Charset.defaultCharset()));

            passedScenarioCount = JsonPath.read(responseString, "$.passedScenariosCount").toString();
        } catch (IOException e) {
            e.printStackTrace();
        }
        return passedScenarioCount;
    }

    public static String getFailedScenarioCount() {
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
        String failedScenariosCount = "";
        try {
            String jsonFilePath = CURRENT_DIRECTORY + File.separator + propertyFile.getProperty("gauge_reports_dir") + File.separator +
                    "json-report" + File.separator + "result.json";

            Object responseString = Configuration.defaultConfiguration().jsonProvider().parse(readFile(jsonFilePath, Charset.defaultCharset()));

            failedScenariosCount = JsonPath.read(responseString, "$.failedScenariosCount").toString();
        } catch (IOException e) {
            e.printStackTrace();
        }
        return failedScenariosCount;
    }

    public static String getSkippedScenarioCount() {
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
        String skippedScenariosCount = "";
        try {
            String jsonFilePath = CURRENT_DIRECTORY + File.separator + propertyFile.getProperty("gauge_reports_dir") + File.separator +
                    "json-report" + File.separator + "result.json";

            Object responseString = Configuration.defaultConfiguration().jsonProvider().parse(readFile(jsonFilePath, Charset.defaultCharset()));

            skippedScenariosCount = JsonPath.read(responseString, "$.skippedScenariosCount").toString();
        } catch (IOException e) {
            e.printStackTrace();
        }
        return skippedScenariosCount;
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
            String executionStatus = JsonPath.read(responseString, "$.executionStatus").toString();
            String passedScenarioCount = JsonPath.read(responseString, "$.passedScenariosCount").toString();
            String failedScenarioCount = JsonPath.read(responseString, "$.failedScenariosCount").toString();
            String skippedScenarioCount = JsonPath.read(responseString, "$.skippedScenariosCount").toString();
            String passedSpecsCount = JsonPath.read(responseString, "$.passedSpecsCount").toString();
            String failedSpecsCount = JsonPath.read(responseString, "$.failedSpecsCount").toString();
            String skippedSpecsCount = JsonPath.read(responseString, "$.skippedSpecsCount").toString();
            String successRate = String.valueOf(Integer.valueOf(passedScenarioCount) * 100 /
                    (Integer.valueOf(passedScenarioCount) + Integer.valueOf(failedScenarioCount) + Integer.valueOf(skippedScenarioCount)))
                    + "%";
            String failRate = String.valueOf(Integer.valueOf(failedScenarioCount) * 100 /
                    (Integer.valueOf(passedScenarioCount) + Integer.valueOf(failedScenarioCount) + Integer.valueOf(skippedScenarioCount)))
                    + "%";

            String executionResults = "<img src=\"cid:image\"> <br /><br />" +
                    "<table style=\"width:100%; text-align:left\" border=\"0\">" +
                    "<tr><td><b>" + "Project Name </td>" + "<td>" + projectName + "<td></tr>" +
                    "<tr><td><b>" + "Timestamp </td>" + "<td>" + timestamp + "<td></tr>" +
                    "<tr><td><b>" + "Environment </td>" + "<td>" + environment.substring(0, 1).toUpperCase() + environment.substring(1) + "<td></tr>" +
                    "<tr><td><b>" + "Execution Time </td>" + "<td>" + milliSecondsToTime(Integer.valueOf(executionTime)) + "<td></tr>" +
                    "<tr><td><b>" + "Execution Status </td>" + "<td>" + executionStatus.substring(0, 1).toUpperCase() + executionStatus.substring(1) + "<td></tr>" +
                    "<tr><td><b>" + "Success Rate </td>" + "<td>" + successRate + "<td></tr>" +
                    "<tr><td><b>" + "Fail Rate </td>" + "<td>" + failRate + "<td></tr>" +
                    "<tr><td><b>" + "Passed Scenario Count </td>" + "<td>" + passedScenarioCount + "<td></tr>" +
                    "<tr><td><b>" + "Failed Scenario Count </td>" + "<td>" + failedScenarioCount + "<td></tr>" +
                    "<tr><td><b>" + "Skipped Scenario Count </td>" + "<td>" + skippedScenarioCount + "<td></tr>" +
                    "<tr><td><b>" + "Passed Specs Count </td>" + "<td>" + passedSpecsCount + "<td></tr>" +
                    "<tr><td><b>" + "Failed Specs Count </td>" + "<td>" + failedSpecsCount + "<td></tr>" +
                    "<tr><td><b>" + "Skipped Specs Count </td>" + "<td>" + skippedSpecsCount + "<td></tr>" ;

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
