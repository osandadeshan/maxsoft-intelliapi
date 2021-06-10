package com.maxsoft.intelliapi.api;

import com.jayway.jsonpath.Configuration;
import com.jayway.jsonpath.JsonPath;
import com.jayway.jsonpath.PathNotFoundException;
import com.maxsoft.intelliapi.util.fileoperator.TextFileOperator;
import com.opencsv.CSVWriter;
import io.restassured.response.Response;
import org.json.simple.JSONArray;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;
import org.testng.Assert;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.concurrent.TimeUnit;

import static com.maxsoft.intelliapi.Constants.*;
import static com.maxsoft.intelliapi.util.DataStoreProcessor.*;
import static com.maxsoft.intelliapi.util.LogUtil.printError;
import static com.maxsoft.intelliapi.util.LogUtil.printInfo;
import static io.restassured.module.jsv.JsonSchemaValidator.matchesJsonSchemaInClasspath;
import static org.hamcrest.MatcherAssert.assertThat;

/**
 * Project Name    : MaxSoft-IntelliAPI
 * Developer       : Osanda Deshan
 * Version         : 1.0.0
 * Date            : 12/12/2020
 * Time            : 9:56 AM
 * Description     :
 **/

public class ApiResponseProcessor {

    public static void saveStatusCode(Response response) {
        saveValueForScenario(VAR_API_RESPONSE_STATUS_CODE, String.valueOf(response.statusCode()));
    }

    public static void saveApiResponseBody(Response response) {
        saveValueForScenario(VAR_API_RESPONSE_BODY, response.prettyPrint());
    }

    public static void printResponseTime(Response response) {
        printInfo("Response Time is: " + response.getTimeIn(TimeUnit.MILLISECONDS) + "ms" + "\n\n");
    }

    public static void printResponse() {
        String response = getSavedValueForScenario(VAR_API_RESPONSE_BODY);
        if (response.equals("")) {
            printInfo("Response is Empty" + "\n\n");
        } else {
            printInfo("Response is: " + "\n" + response + "\n\n");
        }
    }

    public static void printResponseHeaders(Response response) {
        printInfo("Response Headers are: \n" + response.getHeaders().toString());
    }

    public static void clearInvokedApiEndpointArtifacts() {
        setScenarioDataStoreEmpty(VAR_API_NAME);
        setScenarioDataStoreEmpty(VAR_API_ENDPOINT);
        setScenarioDataStoreEmpty(VAR_API_PATH_PARAMS);
        setScenarioDataStoreEmpty(VAR_API_QUERY_PARAMS);
        setScenarioDataStoreEmpty(VAR_API_HEADER_NAMES_LIST);
        setScenarioDataStoreEmpty(VAR_API_HEADER_VALUES_LIST);
        setScenarioDataStoreEmpty(VAR_API_FORM_DATA_KEYS_LIST);
        setScenarioDataStoreEmpty(VAR_API_FORM_DATA_VALUES_LIST);

        for (int i = 1; i <= 5; i++) {
            setScenarioDataStoreEmpty(VAR_API_FORM_DATA_MULTIPART_FILE_KEY + i);
            setScenarioDataStoreEmpty(VAR_API_FORM_DATA_MULTIPART_FILE_PATH + i);
            setScenarioDataStoreEmpty(VAR_API_FORM_DATA_MULTIPART_MIME_TYPE + i);
        }

        setScenarioDataStoreEmpty(VAR_API_FORM_DATA_MULTIPART_FILES_COUNT);
    }

    public static void checkJsonPathValueContainsText(String jsonPath, String expectedJsonPathValue) {
        Object responseString = Configuration.defaultConfiguration().jsonProvider()
                .parse(getSavedValueForScenario(VAR_API_RESPONSE_BODY));

        if (responseString.toString().equals("")) {
            printInfo("No any JSON Paths found. Because the response is a no-content response for the given payload.");
        }

        if (responseString.toString().equals("[]")) {
            printInfo("No any JSON Paths found. Because the response is an empty array for the given payload.");
        }

        String actualJsonPathValue = JsonPath.read(responseString, jsonPath).toString();
        Assert.assertTrue(actualJsonPathValue.contains(expectedJsonPathValue),
                "JSON Path value for the \"" + jsonPath + "\" is contains the expected value.\nJSON Path value is: "
                        + actualJsonPathValue + "\n" + "Expected value not to be contained is: "
                        + expectedJsonPathValue + "\n\n");
    }

    public static void checkJsonPathValueNotContainsText(String jsonPath, String expectedJsonPathValue) {
        Object responseString = Configuration.defaultConfiguration().jsonProvider()
                .parse(getSavedValueForScenario(VAR_API_RESPONSE_BODY));

        if (responseString.toString().equals("")) {
            printInfo("No any JSON Paths found. Because the response is a no-content response for the given payload.");
        }

        if (responseString.toString().equals("[]")) {
            printInfo("No any JSON Paths found. Because the response is an empty array for the given payload.");
        }

        String actualJsonPathValue = JsonPath.read(responseString, jsonPath).toString();
        Assert.assertFalse(actualJsonPathValue.contains(expectedJsonPathValue), "JSON Path value for the \""
                + jsonPath + "\" is contains the expected value.\nJSON Path value is: " + actualJsonPathValue +
                "\n" + "Expected value not to be contained is: " + expectedJsonPathValue + "\n\n");
    }

    public static void checkJsonPathAssertionEqualsText(String jsonPath, String expectedJsonPathValue) {
        Object responseString = Configuration.defaultConfiguration().jsonProvider()
                .parse(getSavedValueForScenario(VAR_API_RESPONSE_BODY));

        if (responseString.toString().equals("")) {
            printInfo("No any JSON Paths found. Because the response is a no-content response for the given payload.");
        }

        if (responseString.toString().equals("[]")) {
            printInfo("No any JSON Paths found. Because the response is an empty array for the given payload.");
        }

        String nullableMessage = "Expected value for the JSON Path of \"" + jsonPath + "\" is not equal to the Actual value.\n";

        if (expectedJsonPathValue.equals("[]")) {
            Assert.assertEquals(JsonPath.read(responseString, jsonPath).toString(), "[]", nullableMessage);
        } else if (expectedJsonPathValue.equalsIgnoreCase("null")) {
            Assert.assertEquals(JsonPath.read(responseString, jsonPath), (String) null, nullableMessage);
        } else if (expectedJsonPathValue.equalsIgnoreCase("true")) {
            Assert.assertEquals(JsonPath.read(responseString, jsonPath), Boolean.TRUE, nullableMessage);
        } else if (expectedJsonPathValue.equalsIgnoreCase("false")) {
            Assert.assertEquals(JsonPath.read(responseString, jsonPath), Boolean.FALSE, nullableMessage);
        } else if (expectedJsonPathValue.trim().equals("")) {
            Assert.assertEquals(JsonPath.read(responseString, jsonPath), "", nullableMessage);
        } else if (expectedJsonPathValue.matches("\\d+")) {
            Assert.assertEquals(JsonPath.read(responseString, jsonPath).toString(), expectedJsonPathValue, nullableMessage);
        } else if (expectedJsonPathValue.matches("[-+]?\\d*\\.?\\d*")) {
            Assert.assertEquals(JsonPath.read(responseString, jsonPath).toString(), expectedJsonPathValue, nullableMessage);
        } else {
            Assert.assertEquals(JsonPath.read(responseString, jsonPath).toString(), expectedJsonPathValue, nullableMessage);
        }
    }

    public static void checkJsonPathAssertionNotEqualsText(String jsonPath, String expectedJsonPathValue) {
        Object responseString = Configuration.defaultConfiguration().jsonProvider()
                .parse(getSavedValueForScenario(VAR_API_RESPONSE_BODY));

        if (responseString.toString().equals("")) {
            printInfo("No any JSON Paths found. Because the response is a no-content response for the given payload.");
        }

        if (responseString.toString().equals("[]")) {
            printInfo("No any JSON Paths found. Because the response is an empty array for the given payload.");
        }

        String nullableMessage = "Expected value for the JSON Path of \"" + jsonPath + "\" is equal to the Actual value.\n";

        if (expectedJsonPathValue.equals("[]")) {
            Assert.assertNotEquals(JsonPath.read(responseString, jsonPath).toString(), "[]", nullableMessage);
        } else if (expectedJsonPathValue.equalsIgnoreCase("null")) {
            Assert.assertNotEquals(JsonPath.read(responseString, jsonPath), null, nullableMessage);
        } else if (expectedJsonPathValue.equalsIgnoreCase("true")) {
            Assert.assertNotEquals(JsonPath.read(responseString, jsonPath), Boolean.TRUE, nullableMessage);
        } else if (expectedJsonPathValue.equalsIgnoreCase("false")) {
            Assert.assertNotEquals(JsonPath.read(responseString, jsonPath), Boolean.FALSE, nullableMessage);
        } else if (expectedJsonPathValue.trim().equals("")) {
            Assert.assertNotEquals(JsonPath.read(responseString, jsonPath), "", nullableMessage);
        } else if (expectedJsonPathValue.matches("\\d+")) {
            Assert.assertNotEquals(JsonPath.read(responseString, jsonPath).toString(), expectedJsonPathValue, nullableMessage);
        } else if (expectedJsonPathValue.matches("[-+]?\\d*\\.?\\d*")) {
            Assert.assertNotEquals(JsonPath.read(responseString, jsonPath).toString(), expectedJsonPathValue, nullableMessage);
        } else {
            Assert.assertNotEquals(JsonPath.read(responseString, jsonPath), expectedJsonPathValue, nullableMessage);
        }
    }

    public static void checkJsonPathExistence(String jsonPath, Boolean isExists) {
        Object responseString = Configuration.defaultConfiguration().jsonProvider()
                .parse(getSavedValueForScenario(VAR_API_RESPONSE_BODY));
        Boolean actualResult;

        try {
            JsonPath.read(responseString, jsonPath);
            actualResult = Boolean.TRUE;
        } catch (PathNotFoundException ex) {
            actualResult = Boolean.FALSE;
        }
        Assert.assertEquals(actualResult, isExists,
                "Expected and the Actual results are mismatched for the JSON Path \"" + jsonPath + "\"");
    }

    public static void saveJsonArrayValuesToCsv(String jsonPath, String headerName, String csvFilePath) {
        Object responseString = Configuration.defaultConfiguration().jsonProvider()
                .parse(getSavedValueForScenario(VAR_API_RESPONSE_BODY));
        String JsonArrayResults = JsonPath.read(responseString, jsonPath).toString();

        try {
            Object obj = new JSONParser().parse(JsonArrayResults);
            JSONArray array = (JSONArray) obj;
            File inputFile = new File(CURRENT_DIRECTORY + csvFilePath);
            inputFile.delete();
            inputFile.createNewFile();
            String[] header = {headerName};
            CSVWriter writer = new CSVWriter(new FileWriter(inputFile), ',');
            writer.writeNext(header);
            for (Object object : array) {
                printInfo(object.toString());
                writer.writeNext(new String[]{object.toString()});
            }
            writer.flush();
            writer.close();
        } catch (IOException | ParseException ex) {
            ex.printStackTrace();
        }
    }

    public static void saveResponseJsonPathValue(String dataStoreType, String variableName, String jsonPath) {
        String jsonData = getSavedValueForScenario(VAR_API_RESPONSE_BODY);
        Object dataObject = JsonPath.parse(jsonData).read(jsonPath);
        String jsonPathValue = dataObject.toString();
        saveToDataStore(dataStoreType, variableName, jsonPathValue);
    }

    public static void saveAccessTokenToTextFile(String jsonPath) {
        String jsonData = getSavedValueForScenario(VAR_API_RESPONSE_BODY);
        Object dataObject = JsonPath.parse(jsonData).read(jsonPath);
        String jsonPathValue = dataObject.toString();

        if (AUTHENTICATION_FIRST_VALUE == null || AUTHENTICATION_FIRST_VALUE.equals(" ")
                || AUTHENTICATION_FIRST_VALUE.equals("")) {
            AUTHENTICATION_FIRST_VALUE = "";
        }

        try {
            TextFileOperator.write(AUTHENTICATION_FIRST_VALUE + jsonPathValue, ACCESS_TOKEN_FILE_PATH);
            printInfo("Successfully saved the access token into the text file in the directory of \""
                    + ACCESS_TOKEN_FILE_PATH + "\"");
        } catch (Exception ex) {
            printError("Failed to save the access token into the text file in the directory of \""
                    + ACCESS_TOKEN_FILE_PATH + "\"\n" + ex.getMessage());
        }
    }

    public static void saveResponseDataToTextFile(String jsonPath, String filePath) {
        String jsonData = getSavedValueForScenario(VAR_API_RESPONSE_BODY);
        Object dataObject = JsonPath.parse(jsonData).read(jsonPath);
        String jsonPathValue = dataObject.toString();

        try {
            File file = new File(CURRENT_DIRECTORY + filePath);
            if (!file.exists()) {
                file.createNewFile();
            }
            TextFileOperator.write(jsonPathValue, CURRENT_DIRECTORY + filePath);
            printInfo("Successfully saved the value inside \"" + jsonPath + "\" into the text file in the directory of \""
                    + CURRENT_DIRECTORY + filePath + "\"");
        } catch (Exception ex) {
            printError("Failed to save the value inside \"" + jsonPath + "\" into the text file in the directory of \""
                    + CURRENT_DIRECTORY + filePath + "\"\n" + ex.getMessage());
        }
    }

    public static void validateJsonSchema(String jsonSchemaFileName) {
        assertThat(getSavedValueForScenario(VAR_API_RESPONSE_BODY), matchesJsonSchemaInClasspath(jsonSchemaFileName));
    }
}
