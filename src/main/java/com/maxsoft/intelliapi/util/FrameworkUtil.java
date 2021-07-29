package com.maxsoft.intelliapi.util;

import com.github.javafaker.Faker;
import com.maxsoft.intelliapi.util.fileoperator.CsvFileOperator;
import com.maxsoft.intelliapi.util.fileoperator.TextFileOperator;
import com.maxsoft.intelliapi.util.reader.EnvironmentPropertyReader;

import java.security.InvalidParameterException;
import java.text.SimpleDateFormat;
import java.time.Instant;
import java.util.Date;
import java.util.Random;

import static com.maxsoft.intelliapi.Constants.*;
import static com.maxsoft.intelliapi.util.LogUtil.printInfo;
import static java.time.temporal.ChronoUnit.SECONDS;

/**
 * Project Name : MaxSoft-IntelliAPI
 * Developer    : Osanda Deshan
 * Version      : 1.0.0
 * Date         : 6/30/2018
 * Time         : 3:51 PM
 * Description  :
 **/

public class FrameworkUtil {

    private static final Faker faker = new Faker();

    public static void waitBySeconds(int seconds){
        Instant waitEndTime = Instant.now().plus(seconds, SECONDS);
        while (Instant.now().isBefore(waitEndTime)) {
            Instant tenSecondsAfterNowTime = Instant.now().plus(10, SECONDS);
            while (Instant.now().isBefore(tenSecondsAfterNowTime)) {}
            printInfo("Waited 10 seconds till timeout expires........", FrameworkUtil.class);
        }
    }

    private static String getCurrentTimestamp(String timestampPattern){
        return new SimpleDateFormat(timestampPattern).format(new Date());
    }

    public static void replaceAllColumnValuesToCurrentTimestamp(String filePath, String columnName, String timestampPattern) {
        CsvFileOperator csvFileOperator = new CsvFileOperator();
        for(int i = 1; i<= csvFileOperator.getLinesCount(filePath); i++){
            csvFileOperator.updateCSVByRowIndexAndColumnIndex(filePath, getCurrentTimestamp(timestampPattern), i,
                    csvFileOperator.getColumnIndexByColumnName(filePath, columnName));
        }
    }

    public static void printTestingEnvDetails() {
        printInfo("Configurations of test execution environment\n\n", FrameworkUtil.class);
        printInfo("Operating System: " + OS, FrameworkUtil.class);
        printInfo("Environment: " + ENVIRONMENT.toUpperCase(), FrameworkUtil.class);
        printInfo("Base URL: " + EnvironmentPropertyReader.getBaseUrl(), FrameworkUtil.class);
    }

    public static String readAccessToken() {
        String accessToken = "";
        try {
            accessToken = TextFileOperator.readAccessToken(ACCESS_TOKEN_FILE_PATH);
        } catch (Exception ignored) {
        }
        return accessToken;
    }

    public static String getRandomText() {
        String acceptedLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        StringBuilder salt = new StringBuilder();
        Random random = new Random();
        while (salt.length() < 18) { // length of the random string.
            int index = (int) (random.nextFloat() * acceptedLetters.length());
            salt.append(acceptedLetters.charAt(index));
        }
        return salt.toString();
    }

    public static String getRandomEmail(String domainName) {
        return faker.name().firstName().concat(".").concat(faker.name().lastName()).concat("@").concat(domainName);
    }

    public static String getRandomData(String expectedDataType) {
        String randomData;

        switch (expectedDataType.toLowerCase()) {
            case FIRST_NAME:
                randomData = faker.name().firstName();
                break;
            case LAST_NAME:
                randomData = faker.name().lastName();
                break;
            case FULL_NAME:
                randomData = faker.name().firstName() + " " + faker.name().lastName();
                break;
            case ADDRESS:
                randomData = faker.address().fullAddress();
                break;
            default:
                throw new InvalidParameterException("Invalid expected data type. Please provide one of these as the " +
                        "expected data type " + FIRST_NAME + " | " + LAST_NAME + " | " + FULL_NAME + " | " + ADDRESS);
        }

        return randomData;
    }

    public static boolean isTrue(String rowCell) {
        boolean flag;
        flag = rowCell.equalsIgnoreCase("true") || rowCell.equalsIgnoreCase("t") ||
                rowCell.equalsIgnoreCase("yes") || rowCell.equalsIgnoreCase("y");
        return flag;
    }

    public static boolean hasContainedFileSyntax(String text) {
        return text.substring(0, Math.min(text.length(), FILE_SYNTAX_CHARACTER_COUNT)).equalsIgnoreCase(FILE_SYNTAX_PREFIX);
    }

    public static String getFilePathFromFileSyntax(String rowCell) {
        return CURRENT_DIRECTORY + rowCell.substring(FILE_SYNTAX_CHARACTER_COUNT, rowCell.length() - 1);
    }
}
