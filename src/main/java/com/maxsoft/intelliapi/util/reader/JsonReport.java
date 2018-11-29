package com.maxsoft.intelliapi.util.reader;

/**
 * Project Name : MaxSoft-IntelliAPI
 * Developer    : Osanda Deshan
 * Version      : 1.0.0
 * Date         : 6/30/2018
 * Time         : 3:51 PM
 * Description  :
 **/

import com.jayway.jsonpath.Configuration;
import com.jayway.jsonpath.JsonPath;
import com.maxsoft.intelliapi.util.email.EmailTemplate;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;
import java.io.*;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.text.DecimalFormat;
import java.util.ArrayList;
import java.util.List;
import java.util.Properties;


public class JsonReport {

    public static final String CURRENT_DIRECTORY = System.getProperty("user.dir");
    static Properties propertyFile = new Properties();
    static InputStream input = null;
    public static String propertyFilePath = CURRENT_DIRECTORY + File.separator + "env" + File.separator + "default"
            + File.separator + "default.properties";

    public static String readFile(String path, Charset encoding) throws IOException {
        byte[] encoded = Files.readAllBytes(Paths.get(path));
        return new String(encoded, encoding);
    }

    public static String milliSecondsToTime(int millisec) {
        int milli = millisec % 1000;
        int sec = millisec / 1000;
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

    public static List<String> getSpecHeadingList() throws IOException, ParseException {
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

        String jsonFilePath = CURRENT_DIRECTORY + File.separator + propertyFile.getProperty("gauge_reports_dir") + File.separator +
                "json-report" + File.separator + "result.json";

        JSONParser parser = new JSONParser();

        Object obj = parser.parse(new FileReader(jsonFilePath));
        JSONObject jsonObject = (JSONObject) obj;
        String JsonArrayResults = JsonPath.read(jsonObject, "$.specResults").toString();
        JSONArray jsonArray = (JSONArray) parser.parse(JsonArrayResults);

        List<String> specHeadingList = new ArrayList<>();

        for (Object object : jsonArray) {
            JSONObject jsonObject1 = (JSONObject) object;
            String specHeading = jsonObject1.get("specHeading").toString();
            specHeadingList.add(specHeading);
        }
        return specHeadingList;
    }

    public static List<String> getPassedScenarioCountList() throws IOException, ParseException {
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

        String jsonFilePath = CURRENT_DIRECTORY + File.separator + propertyFile.getProperty("gauge_reports_dir") + File.separator +
                "json-report" + File.separator + "result.json";

        JSONParser parser = new JSONParser();

        Object obj = parser.parse(new FileReader(jsonFilePath));
        JSONObject jsonObject = (JSONObject) obj;
        String JsonArrayResults = JsonPath.read(jsonObject, "$.specResults").toString();
        JSONArray jsonArray = (JSONArray) parser.parse(JsonArrayResults);

        List<String> passedScenarioCountList = new ArrayList<>();

        for (Object object : jsonArray) {
            JSONObject jsonObject1 = (JSONObject) object;
            String passedScenarioCount = jsonObject1.get("passedScenarioCount").toString();
            passedScenarioCountList.add(passedScenarioCount);
        }
        return passedScenarioCountList;
    }

    public static List<String> getFailedScenarioCountList() throws IOException, ParseException {
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

        String jsonFilePath = CURRENT_DIRECTORY + File.separator + propertyFile.getProperty("gauge_reports_dir") + File.separator +
                "json-report" + File.separator + "result.json";

        JSONParser parser = new JSONParser();

        Object obj = parser.parse(new FileReader(jsonFilePath));
        JSONObject jsonObject = (JSONObject) obj;
        String JsonArrayResults = JsonPath.read(jsonObject, "$.specResults").toString();
        JSONArray jsonArray = (JSONArray) parser.parse(JsonArrayResults);

        List<String> failedScenarioCountList = new ArrayList<>();

        for (Object object : jsonArray) {
            JSONObject jsonObject1 = (JSONObject) object;
            String failedScenarioCount = jsonObject1.get("failedScenarioCount").toString();
            failedScenarioCountList.add(failedScenarioCount);
        }
        return failedScenarioCountList;
    }

    public static List<String> getSkippedScenarioCountList() throws IOException, ParseException {
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

        String jsonFilePath = CURRENT_DIRECTORY + File.separator + propertyFile.getProperty("gauge_reports_dir") + File.separator +
                "json-report" + File.separator + "result.json";

        JSONParser parser = new JSONParser();

        Object obj = parser.parse(new FileReader(jsonFilePath));
        JSONObject jsonObject = (JSONObject) obj;
        String JsonArrayResults = JsonPath.read(jsonObject, "$.specResults").toString();
        JSONArray jsonArray = (JSONArray) parser.parse(JsonArrayResults);

        List<String> skippedScenarioCountList = new ArrayList<>();

        for (Object object : jsonArray) {
            JSONObject jsonObject1 = (JSONObject) object;
            String skippedScenarioCount = jsonObject1.get("skippedScenarioCount").toString();
            skippedScenarioCountList.add(skippedScenarioCount);
        }
        return skippedScenarioCountList;
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
            Double successRate = Double.valueOf(df.format((double) passedScenariosCount * 100/ totalScenariosCount));
            Double failRate = Double.valueOf(df.format((double) failedScenariosCount * 100/ totalScenariosCount));

            String executionResults = EmailTemplate.get()
                    .replaceAll("#projectName", projectName)
                    .replaceAll("#timestamp", timestamp)
                    .replaceAll("#environment", environment.substring(0, 1).toUpperCase() + environment.substring(1))
                    .replaceAll("#executionTime", milliSecondsToTime(Integer.valueOf(executionTime)))
                    .replaceAll("#executionStatus", executionStatus.substring(0, 1).toUpperCase() + executionStatus.substring(1))
                    .replaceAll("#successRate", successRate.toString() + "%")
                    .replaceAll("#failRate", failRate.toString() + "%")

                    .replaceAll("#totalScenariosCount", String.valueOf(totalScenariosCount))
                    .replaceAll("#passedScenariosCount", String.valueOf(passedScenariosCount))
                    .replaceAll("#failedScenariosCount", String.valueOf(failedScenariosCount))
                    .replaceAll("#skippedScenariosCount", String.valueOf(skippedScenariosCount))

                    .replaceAll("#totalSpecsCount", String.valueOf(totalSpecsCount))
                    .replaceAll("#passedSpecsCount", String.valueOf(passedSpecsCount))
                    .replaceAll("#failedSpecsCount", String.valueOf(failedSpecsCount))
                    .replaceAll("#skippedSpecsCount", String.valueOf(skippedSpecsCount));

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


}
