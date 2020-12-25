package com.maxsoft.intelliapi.common;

import com.github.javafaker.Faker;
import com.maxsoft.intelliapi.util.fileoperator.CsvFile;
import com.maxsoft.intelliapi.util.fileoperator.TextFile;
import com.maxsoft.intelliapi.util.reader.EnvironmentPropertyReader;

import java.text.SimpleDateFormat;
import java.time.Instant;
import java.util.Date;
import java.util.Random;

import static com.maxsoft.intelliapi.common.Constants.*;
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

public class Base {

    public static void waitBySeconds(int seconds){
        Instant waitEndTime = Instant.now().plus(seconds, SECONDS);
        while (Instant.now().isBefore(waitEndTime)) {
            Instant tenSecondsAfterNowTime = Instant.now().plus(10, SECONDS);
            while (Instant.now().isBefore(tenSecondsAfterNowTime)) {}
            printInfo("Waited 10 seconds till timeout expires........");
        }
    }

    private static String getCurrentTimestamp(String timestampPattern){
        return new SimpleDateFormat(timestampPattern).format(new Date());
    }

    public static void replaceAllColumnValuesToCurrentTimestamp(String filePath, String columnName, String timestampPattern) {
        CsvFile csvFile = new CsvFile();
        for(int i = 1; i<= csvFile.getLinesCount(filePath); i++){
            csvFile.updateCSVByRowIndexAndColumnIndex(filePath, getCurrentTimestamp(timestampPattern), i,
                    csvFile.getColumnIndexByColumnName(filePath, columnName));
        }
    }

    public static void printTestingEnvDetails() {
        printInfo("Configurations of Test Execution Environment\n\n");
        printInfo("Operating System: " + OS);
        printInfo("Environment: " + ENVIRONMENT.toUpperCase());
        printInfo("Base URL: " + EnvironmentPropertyReader.getBaseUrl());
    }

    public static String readAccessToken() {
        String accessToken = "";
        try {
            accessToken = TextFile.readAccessToken(ACCESS_TOKEN_FILE_PATH);
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
        Faker faker = new Faker();
        return faker.name().firstName().concat(".").concat(faker.name().lastName()).concat("@").concat(domainName);
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
