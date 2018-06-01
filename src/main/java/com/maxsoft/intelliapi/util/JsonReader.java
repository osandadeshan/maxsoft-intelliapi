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
import java.text.DecimalFormat;
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

            int passedScenariosCount = Integer.valueOf(JsonPath.read(responseString, "$.passedScenariosCount").toString());
            int failedScenariosCount = Integer.valueOf(JsonPath.read(responseString, "$.failedScenariosCount").toString());
            int skippedScenariosCount = Integer.valueOf(JsonPath.read(responseString, "$.skippedScenariosCount").toString());
            int totalScenariosCount = passedScenariosCount + failedScenariosCount + skippedScenariosCount;

            int passedSpecsCount = Integer.valueOf(JsonPath.read(responseString, "$.passedSpecsCount").toString());
            int failedSpecsCount = Integer.valueOf(JsonPath.read(responseString, "$.failedSpecsCount").toString());
            int skippedSpecsCount = Integer.valueOf(JsonPath.read(responseString, "$.skippedSpecsCount").toString());
            int totalSpecsCount = passedSpecsCount + failedSpecsCount + skippedSpecsCount;

            DecimalFormat df = new DecimalFormat(".##");
            String successRate = df.format((double) passedScenariosCount * 100/ totalScenariosCount) + "%";
            String failRate = df.format((double) failedScenariosCount * 100/ totalScenariosCount) + "%";

            String executionResults = "<img src=\"cid:image\" alt=\"Pie Chart For Test Execution Results\" align=\"left\"> <br /><br /><br />" +
                    "<table style=\"width:68%; text-align:left\" border=\"0\">" +
                    "<tr align=\"left\"><td><b>" + "Project Name </td>" + "<td>" + projectName + "<td></tr>" +
                    "<tr><td><b>" + "Timestamp </td>" + "<td>" + timestamp + "<td></tr>" +
                    "<tr><td><b>" + "Environment </td>" + "<td>" + environment.substring(0, 1).toUpperCase() + environment.substring(1) + "<td></tr>" +
                    "<tr><td><b>" + "Execution Time </td>" + "<td>" + milliSecondsToTime(Integer.valueOf(executionTime)) + "<td></tr>" +
                    "<tr><td><b>" + "Execution Status </td>" + "<td>" + executionStatus.substring(0, 1).toUpperCase() + executionStatus.substring(1) + "<td></tr>" +
                    "<tr><td><b>" + "Success Rate </td>" + "<td>" + successRate + "<td></tr>" +
                    "<tr><td><b>" + "Fail Rate </td>" + "<td>" + failRate + "<td></tr><br />" +
                    "<tr><td><b><u>" + "Scenario Information </td></tr>" +
                    "<tr><td><b>" + "Total Scenarios Count </td>" + "<td>" + totalScenariosCount + "<td></tr>" +
                    "<tr><td><b>" + "Passed Scenarios Count </td>" + "<td>" + passedScenariosCount + "<td></tr>" +
                    "<tr><td><b>" + "Failed Scenarios Count </td>" + "<td>" + failedScenariosCount + "<td></tr>" +
                    "<tr><td><b>" + "Skipped Scenarios Count </td>" + "<td>" + skippedScenariosCount + "<td></tr><br />" +
                    "<tr><td><b><u>" + "Specification Information </td></tr>" +
                    "<tr><td><b>" + "Total Specs Count </td>" + "<td>" + totalSpecsCount + "<td></tr>" +
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
