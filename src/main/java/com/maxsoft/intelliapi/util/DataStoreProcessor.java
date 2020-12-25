package com.maxsoft.intelliapi.util;

import com.thoughtworks.gauge.datastore.DataStore;
import com.thoughtworks.gauge.datastore.DataStoreFactory;
import org.testng.Assert;

import java.security.InvalidParameterException;

import static com.maxsoft.intelliapi.common.Constants.*;
import static com.maxsoft.intelliapi.util.LogUtil.printError;
import static com.maxsoft.intelliapi.util.LogUtil.printInfo;

/**
 * Project Name    : MaxSoft-IntelliAPI
 * Developer       : Osanda Deshan
 * Version         : 1.0.0
 * Date            : 12/5/2020
 * Time            : 9:04 PM
 * Description     :
 **/

public class DataStoreProcessor {

    public static String getSavedValueForScenario(String variableName) {
        try {
            DataStore scenarioStore = DataStoreFactory.getScenarioDataStore();
            return (String) scenarioStore.get(variableName);
        } catch (Exception ex) {
            printError("Failed to read the text inside Scenario Data Store ["
                    + variableName + "]\n" + ex.getMessage());
            return "";
        }
    }

    public static void saveValueForScenario(String variableName, String textToBeStored) {
        try {
            DataStore scenarioStore = DataStoreFactory.getScenarioDataStore();
            scenarioStore.put(variableName, textToBeStored);
        } catch (Exception ex) {
            printError("\"" + textToBeStored + "\" is failed to save as a text in Scenario Data Store ["
                    + variableName + "]\n" + ex.getMessage());
        }
    }

    public static void saveToDataStore(String dataStoreType, String variableName, String textToBeStored) {
        switch (dataStoreType.toLowerCase()) {
            case SPEC:
            case SPECIFICATION:
                saveToSpecificationDataStore(variableName, textToBeStored);
                break;
            case SCENARIO:
                saveToScenarioDataStore(variableName, textToBeStored);
                break;
            case SUITE:
                saveToSuiteDataStore(variableName, textToBeStored);
                break;
            default:
                Assert.fail("Please provide a valid data store type");
        }
    }

    public static String readFromDataStore(String dataStoreType, String variableName) {
        String value = "";
        switch (dataStoreType.toLowerCase()) {
            case SPEC:
            case SPECIFICATION:
                value = getSpecificationDataStoreValue(variableName);
                break;
            case SCENARIO:
                value = getScenarioDataStoreValue(variableName);
                break;
            case SUITE:
                value = getSuiteDataStoreValue(variableName);
                break;
            default:
                Assert.fail("Please provide a valid data store type");
        }
        return value;
    }

    public static void setScenarioDataStoreEmpty(String dataStoreName) {
        saveValueForScenario(dataStoreName, "");
    }

    public static void checkEqualityOfDataStoreValue(String dataStoreType, String variableName, String expectedValue) {
        Assert.assertEquals(readFromDataStore(dataStoreType, variableName), expectedValue);
    }

    public static void checkEqualityOfTwoDataStoreValues(String firstDataStoreType, String variableName,
                                                         String secondDataStoreType, String secondDataStoreVariableName) {
        Assert.assertEquals(readFromDataStore(firstDataStoreType, variableName),
                readFromDataStore(secondDataStoreType, secondDataStoreVariableName));
    }

    public static void checkInequalityOfDataStoreValue(String dataStoreType, String variableName, String expectedValue) {
        Assert.assertNotEquals(readFromDataStore(dataStoreType, variableName), expectedValue,
                "Text inside " + dataStoreType + " Data Store [" + variableName
                        + "] is equal to the expected value \"" + expectedValue + "\"\n");
    }

    public static void checkInequalityOfTwoDataStoreValues(String firstDataStoreType, String variableName,
                                                           String secondDataStoreType, String secondDataStoreVariableName) {
        Assert.assertNotEquals(readFromDataStore(firstDataStoreType, variableName),
                readFromDataStore(secondDataStoreType, secondDataStoreVariableName),
                "Text inside " + firstDataStoreType + " Data Store [" + variableName
                        + "] is equal to the text inside " + secondDataStoreType + " Data Store ["
                        + secondDataStoreVariableName + "]\n");
    }

    public static void checkDataStoreValueContainsText(String dataStoreType, String variableName, String expectedValue) {
        Assert.assertTrue(readFromDataStore(dataStoreType, variableName).contains(expectedValue),
                "Text inside " + dataStoreType + " Data Store [" + variableName
                        + "] not contains the expected value \"" + expectedValue + "\"\n");
    }

    public static void checkOneDataStoreValueContainsInAnotherDataStore(String firstDataStoreType,
                                                                        String firstDataStoreVariableName,
                                                                        String secondDataStoreType,
                                                                        String secondDataStoreVariableName) {
        Assert.assertTrue(readFromDataStore(firstDataStoreType, firstDataStoreVariableName)
                        .contains(readFromDataStore(secondDataStoreType, secondDataStoreVariableName)),
                "Text inside " + firstDataStoreType + " Data Store [" + firstDataStoreVariableName
                        + "] not contains the text inside " + secondDataStoreType + " Data Store ["
                        + secondDataStoreVariableName + "]\n");
    }

    public static void checkDataStoreValueNotContainsText(String dataStoreType, String variableName, String expectedValue) {
        Assert.assertFalse(readFromDataStore(dataStoreType, variableName).contains(expectedValue),
                "Text inside " + dataStoreType + " Data Store [" + variableName
                        + "] contains the expected value \"" + expectedValue + "\"\n");
    }

    public static void checkOneDataStoreValueNotContainsInAnotherDataStore(String firstDataStoreType,
                                                                           String firstDataStoreVariableName,
                                                                           String secondDataStoreType,
                                                                           String secondDataStoreVariableName) {
        Assert.assertFalse(readFromDataStore(firstDataStoreType, firstDataStoreVariableName)
                        .contains(readFromDataStore(secondDataStoreType, secondDataStoreVariableName)),
                "Text inside " + firstDataStoreType + " Data Store [" + firstDataStoreVariableName
                        + "] contains the text inside " + secondDataStoreType + " Data Store ["
                        + secondDataStoreVariableName + "]\n");
    }

    public static void savePropertyFileValuesToDataStore(String dataStoreType, String variableName, String propertyName) {
        saveToDataStore(dataStoreType, variableName, System.getenv(propertyName));
    }

    public static void saveCurrentEpochTimeToDataStore(String secondsOrMillis,
                                                       String dataStoreType, String dataStoreVariableName) {
        switch (secondsOrMillis.toLowerCase()) {
            case "seconds":
                saveToDataStore(dataStoreType, dataStoreVariableName,
                        String.valueOf(EpochTime.getCurrentEpochTimeInSeconds()));
                break;
            case "milliseconds":
                saveToDataStore(dataStoreType, dataStoreVariableName,
                        String.valueOf(EpochTime.getCurrentEpochTimeInMilliSeconds()));
                break;
            default:
                throw new InvalidParameterException("Invalid parameter for Seconds/Milliseconds. " +
                        "Please provide the string as Seconds or Milliseconds.");
        }
    }

    public static void saveEpochTimeToDataStore(String timestampPattern, String timestamp, String secondsOrMillis,
                                                String dataStoreType, String dataStoreVariableName) {
        switch (secondsOrMillis.toLowerCase()) {
            case "seconds":
                saveToDataStore(dataStoreType, dataStoreVariableName,
                        String.valueOf(EpochTime.getEpochTimeInSeconds(timestampPattern, timestamp)));
                break;
            case "milliseconds":
                saveToDataStore(dataStoreType, dataStoreVariableName,
                        String.valueOf(EpochTime.getEpochTimeInMilliSeconds(timestampPattern, timestamp)));
                break;
            default:
                throw new InvalidParameterException("Invalid parameter for Seconds/Milliseconds. " +
                        "Please provide the string as Seconds or Milliseconds.");
        }
    }

    private static String getScenarioDataStoreValue(String variableName) {
        try {
            DataStore scenarioStore = DataStoreFactory.getScenarioDataStore();
            String value = (String) scenarioStore.get(variableName);
            printInfo("Text inside Scenario Data Store [" + variableName
                    + "] is: \"" + value + "\"" + "\n");
            return value;
        } catch (Exception ex) {
            printError("Failed to read the text inside Scenario Data Store ["
                    + variableName + "]" + "\n");
            return "";
        }
    }

    private static String getSpecificationDataStoreValue(String variableName) {
        try {
            DataStore specDataStore = DataStoreFactory.getSpecDataStore();
            String value = (String) specDataStore.get(variableName);
            printInfo("Text inside Specification Data Store [" + variableName
                    + "] is: \"" + value + "\"" + "\n");
            return value;
        } catch (Exception ex) {
            printError("Failed to read the text inside Specification Data Store ["
                    + variableName + "]" + "\n");
            return "";
        }
    }

    private static String getSuiteDataStoreValue(String variableName) {
        try {
            DataStore suiteStore = DataStoreFactory.getSuiteDataStore();
            String value = (String) suiteStore.get(variableName);
            printInfo("Text inside Suite Data Store [" + variableName + "] is: \""
                    + value + "\"" + "\n");
            return value;
        } catch (Exception ex) {
            printError("Failed to read the text inside Suite Data Store [" + variableName
                    + "]" + "\n");
            return "";
        }
    }

    private static void saveToScenarioDataStore(String variableName, String textToBeStored) {
        try {
            DataStore scenarioStore = DataStoreFactory.getScenarioDataStore();
            scenarioStore.put(variableName, textToBeStored);
            printInfo("\"" + textToBeStored + "\" is successfully saved as a text in Scenario Data Store ["
                    + variableName + "]");
        } catch (Exception ex) {
            printError("\"" + textToBeStored + "\" is failed to save as a text in Scenario Data Store ["
                    + variableName + "]");
        }
    }

    private static void saveToSpecificationDataStore(String variableName, String textToBeStored) {
        try {
            DataStore specDataStore = DataStoreFactory.getSpecDataStore();
            specDataStore.put(variableName, textToBeStored);
            printInfo("\"" + textToBeStored + "\" is successfully saved as a text in Specification Data Store ["
                    + variableName + "]");
        } catch (Exception ex) {
            printError("\"" + textToBeStored + "\" is failed to save as a text in Specification Data Store ["
                    + variableName + "]");
        }
    }

    private static void saveToSuiteDataStore(String variableName, String textToBeStored) {
        try {
            DataStore suiteStore = DataStoreFactory.getSuiteDataStore();
            suiteStore.put(variableName, textToBeStored);
            printInfo("\"" + textToBeStored + "\" is successfully saved as a text in Suite Data Store ["
                    + variableName + "]");
        } catch (Exception ex) {
            printError("\"" + textToBeStored + "\" is failed to save as a text in Suite Data Store ["
                    + variableName + "]");
        }
    }
}
