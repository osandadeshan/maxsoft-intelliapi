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

    private static final String CURRENT_DIRECTORY = System.getProperty("user.dir");
    private static final Properties propertyFile = new Properties();
    private static final DecimalFormat df = new DecimalFormat(".##");
    static String fileSeparator = File.separator;
    private static final String propertyFilePath = CURRENT_DIRECTORY + fileSeparator + "env" + fileSeparator + "default"
            + fileSeparator + "default.properties";
    private static InputStream input = null;

    private static String readFile(String path, Charset encoding) throws IOException {
        byte[] encoded = Files.readAllBytes(Paths.get(path));
        return new String(encoded, encoding);
    }

    private static String milliSecondsToTime(int milliseconds) {
        int milli = milliseconds % 1000;
        int sec = milliseconds / 1000;
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

    public static String getExecutionStatusColor() {
        switch (getExecutionStatus().toLowerCase()) {
            case "passed":
                return "style=\"color:green;\"";
            case "failed":
                return "style=\"color:red;\"";
            case "skipped":
                return "style=\"color:gray;\"";
            default:
                return "";
        }
    }

    public static String getExecutionStatus() {
        try {
            input = new FileInputStream(propertyFilePath);
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
        String executionStatus = null;
        try {
            String jsonFilePath = CURRENT_DIRECTORY + fileSeparator + propertyFile.getProperty("gauge_reports_dir") + fileSeparator +
                    "json-report" + fileSeparator + "result.json";

            Object responseString = Configuration.defaultConfiguration().jsonProvider().parse(readFile(jsonFilePath, Charset.defaultCharset()));

            executionStatus = JsonPath.read(responseString, "$.executionStatus").toString();
            executionStatus = executionStatus.substring(0, 1).toUpperCase() + executionStatus.substring(1);
        } catch (IOException e) {
            e.printStackTrace();
        }
        return executionStatus;
    }

    public static String getPassedScenarioCount() {
        try {
            input = new FileInputStream(propertyFilePath);
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
        String passedScenarioCount = null;
        try {
            String jsonFilePath = CURRENT_DIRECTORY + fileSeparator + propertyFile.getProperty("gauge_reports_dir") + fileSeparator +
                    "json-report" + fileSeparator + "result.json";

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
        String failedScenariosCount = null;
        try {
            String jsonFilePath = CURRENT_DIRECTORY + fileSeparator + propertyFile.getProperty("gauge_reports_dir") + fileSeparator +
                    "json-report" + fileSeparator + "result.json";

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
        String skippedScenariosCount = null;
        try {
            String jsonFilePath = CURRENT_DIRECTORY + fileSeparator + propertyFile.getProperty("gauge_reports_dir") + fileSeparator +
                    "json-report" + fileSeparator + "result.json";

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

        String jsonFilePath = CURRENT_DIRECTORY + fileSeparator + propertyFile.getProperty("gauge_reports_dir")
                + fileSeparator + "json-report" + fileSeparator + "result.json";

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

        String jsonFilePath = CURRENT_DIRECTORY + fileSeparator + propertyFile.getProperty("gauge_reports_dir")
                + fileSeparator + "json-report" + fileSeparator + "result.json";

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

    public static List<String> getPassedScenarioPercentageList() throws IOException, ParseException {
        try {
            input = new FileInputStream(propertyFilePath);
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

        String jsonFilePath = CURRENT_DIRECTORY + fileSeparator + propertyFile.getProperty("gauge_reports_dir")
                + fileSeparator + "json-report" + fileSeparator + "result.json";

        JSONParser parser = new JSONParser();

        Object obj = parser.parse(new FileReader(jsonFilePath));
        JSONObject jsonObject = (JSONObject) obj;
        String JsonArrayResults = JsonPath.read(jsonObject, "$.specResults").toString();
        JSONArray jsonArray = (JSONArray) parser.parse(JsonArrayResults);

        List<String> passedScenariosPercentageList = new ArrayList<>();

        for (Object object : jsonArray) {
            JSONObject jsonObject1 = (JSONObject) object;
            int passedScenarioCount = Integer.parseInt(jsonObject1.get("passedScenarioCount").toString());
            int failedScenarioCount = Integer.parseInt(jsonObject1.get("failedScenarioCount").toString());
            int skippedScenarioCount = Integer.parseInt(jsonObject1.get("skippedScenarioCount").toString());
            int totalScenarioCount = passedScenarioCount + failedScenarioCount + skippedScenarioCount;
            double passedScenariosPercentage = 0;
            if (totalScenarioCount != 0) {
                passedScenariosPercentage = Double.parseDouble(df.format((double) (passedScenarioCount * 100) / (double) totalScenarioCount));
            }
            passedScenariosPercentageList.add(passedScenariosPercentage + "%");
        }
        return passedScenariosPercentageList;
    }

    public static List<String> getFailedScenarioCountList() throws IOException, ParseException {
        try {
            input = new FileInputStream(propertyFilePath);
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

        String jsonFilePath = CURRENT_DIRECTORY + fileSeparator + propertyFile.getProperty("gauge_reports_dir")
                + fileSeparator + "json-report" + fileSeparator + "result.json";

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

    public static List<String> getFailedScenarioPercentageList() throws IOException, ParseException {
        try {
            input = new FileInputStream(propertyFilePath);
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

        String jsonFilePath = CURRENT_DIRECTORY + fileSeparator + propertyFile.getProperty("gauge_reports_dir")
                + fileSeparator + "json-report" + fileSeparator + "result.json";

        JSONParser parser = new JSONParser();

        Object obj = parser.parse(new FileReader(jsonFilePath));
        JSONObject jsonObject = (JSONObject) obj;
        String JsonArrayResults = JsonPath.read(jsonObject, "$.specResults").toString();
        JSONArray jsonArray = (JSONArray) parser.parse(JsonArrayResults);

        List<String> failedScenariosPercentageList = new ArrayList<>();

        for (Object object : jsonArray) {
            JSONObject jsonObject1 = (JSONObject) object;
            int passedScenarioCount = Integer.parseInt(jsonObject1.get("passedScenarioCount").toString());
            int failedScenarioCount = Integer.parseInt(jsonObject1.get("failedScenarioCount").toString());
            int skippedScenarioCount = Integer.parseInt(jsonObject1.get("skippedScenarioCount").toString());
            int totalScenarioCount = passedScenarioCount + failedScenarioCount + skippedScenarioCount;
            double failedScenariosPercentage = 0;
            if (totalScenarioCount != 0) {
                failedScenariosPercentage = Double.parseDouble(df.format((double) (failedScenarioCount * 100)
                        / (double) totalScenarioCount));
            }
            failedScenariosPercentageList.add(failedScenariosPercentage + "%");
        }
        return failedScenariosPercentageList;
    }

    public static List<String> getSkippedScenarioCountList() throws IOException, ParseException {
        try {
            input = new FileInputStream(propertyFilePath);
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

        String jsonFilePath = CURRENT_DIRECTORY + fileSeparator + propertyFile.getProperty("gauge_reports_dir")
                + fileSeparator + "json-report" + fileSeparator + "result.json";

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

    public static List<String> getSkippedScenarioPercentageList() throws IOException, ParseException {
        try {
            input = new FileInputStream(propertyFilePath);
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

        String jsonFilePath = CURRENT_DIRECTORY + fileSeparator + propertyFile.getProperty("gauge_reports_dir")
                + fileSeparator + "json-report" + fileSeparator + "result.json";

        JSONParser parser = new JSONParser();

        Object obj = parser.parse(new FileReader(jsonFilePath));
        JSONObject jsonObject = (JSONObject) obj;
        String JsonArrayResults = JsonPath.read(jsonObject, "$.specResults").toString();
        JSONArray jsonArray = (JSONArray) parser.parse(JsonArrayResults);

        List<String> skippedScenariosPercentageList = new ArrayList<>();

        for (Object object : jsonArray) {
            JSONObject jsonObject1 = (JSONObject) object;
            int passedScenarioCount = Integer.parseInt(jsonObject1.get("passedScenarioCount").toString());
            int failedScenarioCount = Integer.parseInt(jsonObject1.get("failedScenarioCount").toString());
            int skippedScenarioCount = Integer.parseInt(jsonObject1.get("skippedScenarioCount").toString());
            int totalScenarioCount = passedScenarioCount + failedScenarioCount + skippedScenarioCount;
            double skippedScenariosPercentage = 0;
            if (totalScenarioCount != 0) {
                skippedScenariosPercentage = Double.parseDouble(df.format((double) (skippedScenarioCount * 100)
                        / (double) totalScenarioCount));
            }
            skippedScenariosPercentageList.add(skippedScenariosPercentage + "%");
        }
        return skippedScenariosPercentageList;
    }

    public static String getExecutionResults() {
        try {
            input = new FileInputStream(propertyFilePath);
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

        try {
            String jsonFilePath = CURRENT_DIRECTORY + fileSeparator + propertyFile.getProperty("gauge_reports_dir")
                    + fileSeparator + "json-report" + fileSeparator + "result.json";

            Object responseString = Configuration.defaultConfiguration().jsonProvider().parse(readFile(jsonFilePath,
                    Charset.defaultCharset()));

            String projectName = JsonPath.read(responseString, "$.projectName").toString();
            String timestamp = JsonPath.read(responseString, "$.timestamp").toString();
            String environment = JsonPath.read(responseString, "$.environment").toString();
            String executionTime = JsonPath.read(responseString, "$.executionTime").toString();
            String executionStatus = JsonPath.read(responseString, "$.executionStatus").toString();

            int passedScenariosCount = Integer.parseInt(JsonPath.read(responseString,
                    "$.passedScenariosCount").toString());
            int failedScenariosCount = Integer.parseInt(JsonPath.read(responseString,
                    "$.failedScenariosCount").toString());
            int skippedScenariosCount = Integer.parseInt(JsonPath.read(responseString,
                    "$.skippedScenariosCount").toString());
            int totalScenariosCount = passedScenariosCount + failedScenariosCount + skippedScenariosCount;
            double passedScenariosPercentage = Double.parseDouble
                    (df.format((double) (passedScenariosCount * 100) / (double) totalScenariosCount));
            double failedScenariosPercentage = Double.parseDouble
                    (df.format((double) (failedScenariosCount * 100) / (double) totalScenariosCount));
            double skippedScenariosPercentage = Double.parseDouble
                    (df.format((double) (skippedScenariosCount * 100) / (double) totalScenariosCount));

            int passedSpecsCount = Integer.parseInt(JsonPath.read(responseString,
                    "$.passedSpecsCount").toString());
            int failedSpecsCount = Integer.parseInt(JsonPath.read(responseString,
                    "$.failedSpecsCount").toString());
            int skippedSpecsCount = Integer.parseInt(JsonPath.read(responseString,
                    "$.skippedSpecsCount").toString());
            int totalSpecsCount = passedSpecsCount + failedSpecsCount + skippedSpecsCount;
            double passedSpecsPercentage = Double.parseDouble
                    (df.format((double) (passedSpecsCount * 100) / (double) totalSpecsCount));
            double failedSpecsPercentage = Double.parseDouble
                    (df.format((double) (failedSpecsCount * 100) / (double) totalSpecsCount));
            double skippedSpecsPercentage = Double.parseDouble
                    (df.format((double) (skippedSpecsCount * 100) / (double) totalSpecsCount));

            Double successRate = Double.valueOf(df.format((double) passedScenariosCount * 100 / totalScenariosCount));
            Double failRate = Double.valueOf(df.format((double) failedScenariosCount * 100 / totalScenariosCount));

            return EmailTemplate.get()
                    .replaceAll("#projectName", projectName)
                    .replaceAll("#timestamp", timestamp)
                    .replaceAll("#environment",
                            environment.substring(0, 1).toUpperCase() + environment.substring(1))
                    .replaceAll("#executionTime", milliSecondsToTime(Integer.parseInt(executionTime)))
                    .replaceAll("#executionStatus",
                            executionStatus.substring(0, 1).toUpperCase() + executionStatus.substring(1))
                    .replaceAll("#successRate", successRate + "%")
                    .replaceAll("#failRate", failRate + "%")

                    .replaceAll("#totalScenariosCount", String.valueOf(totalScenariosCount))
                    .replaceAll("#passedScenariosCount", String.valueOf(passedScenariosCount))
                    .replaceAll("#passedScenarioPercentage", passedScenariosPercentage + "%")
                    .replaceAll("#failedScenariosCount", String.valueOf(failedScenariosCount))
                    .replaceAll("#failedScenarioPercentage", failedScenariosPercentage + "%")
                    .replaceAll("#skippedScenariosCount", String.valueOf(skippedScenariosCount))
                    .replaceAll("#skippedScenarioPercentage", skippedScenariosPercentage + "%")

                    .replaceAll("#totalSpecsCount", String.valueOf(totalSpecsCount))
                    .replaceAll("#passedSpecsCount", String.valueOf(passedSpecsCount))
                    .replaceAll("#passedSpecsPercentage", passedSpecsPercentage + "%")
                    .replaceAll("#failedSpecsCount", String.valueOf(failedSpecsCount))
                    .replaceAll("#failedSpecsPercentage", failedSpecsPercentage + "%")
                    .replaceAll("#skippedSpecsCount", String.valueOf(skippedSpecsCount))
                    .replaceAll("#skippedSpecsPercentage", skippedSpecsPercentage + "%");
        } catch (Exception ex) {
            ex.getStackTrace();
        }
        return "An error occurred while fetching the execution results from json-report";
    }
}

