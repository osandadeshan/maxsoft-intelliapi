package com.maxsoft.intelliapi.util.fileoperator;

import java.io.*;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Scanner;

import static com.maxsoft.intelliapi.util.FrameworkUtil.isTrue;
import static com.maxsoft.intelliapi.Constants.IS_AUTHENTICATION_REQUIRED;
import static com.maxsoft.intelliapi.Constants.RETRIEVE_TOKEN_FROM_TEXT_FILE;
import static com.maxsoft.intelliapi.util.DataStoreProcessor.getSavedValueForScenario;
import static com.maxsoft.intelliapi.util.LogUtil.printError;
import static com.maxsoft.intelliapi.util.LogUtil.printInfo;

/**
 * Project Name : MaxSoft-IntelliAPI
 * Developer    : Osanda Deshan
 * Version      : 1.0.0
 * Date         : 6/30/2018
 * Time         : 3:51 PM
 * Description  :
 **/

public abstract class TextFileOperator {

    public static void write(String text, String filePath) {
        BufferedWriter writer = null;

        try {
            Path pathToFile = Paths.get(filePath);
            Files.createDirectories(pathToFile.getParent());
            File file = new File(filePath);
            file.delete();
            file.createNewFile();
            writer = new BufferedWriter(new FileWriter(filePath));
            writer.write(text);
        } catch (IOException ignored) {
        } finally {
            try {
                if (writer != null)
                    writer.close();
            } catch (IOException ignored) {
            }
        }
    }

    public static String read(String filePath) {
        String content = null;

        try {
            content = String.valueOf(new Scanner(new File(filePath)).useDelimiter("\\Z").next());
        } catch (FileNotFoundException e) {
            printError("Reading the text file in the directory of \"" + filePath + "\" is failed due to "
                    + e.getMessage(), TextFileOperator.class);
        }
        printInfo(content, TextFileOperator.class);
        return content;
    }

    public static String readAccessToken(String filePath) {
        String content = null;
        String isAuthenticationRequired = getSavedValueForScenario(IS_AUTHENTICATION_REQUIRED).toLowerCase();
        String isAccessTokenRetrievedFromTextFile = getSavedValueForScenario(RETRIEVE_TOKEN_FROM_TEXT_FILE).toLowerCase();

        try {
            content = String.valueOf(new Scanner(new File(filePath)).useDelimiter("\\Z").next());
            if (isTrue(isAuthenticationRequired) && isTrue(isAccessTokenRetrievedFromTextFile)) {
                printInfo("Successfully read the access token from the text file in the directory of \""
                        + filePath + "\"\n\n", TextFileOperator.class);
            }
        } catch (FileNotFoundException e) {
            printError("Reading the access token from the text file in the directory of \""
                    + filePath + "\" is failed due to " + e.getMessage() + "\n\n", TextFileOperator.class);
        }
        printInfo(content, TextFileOperator.class);
        return content;
    }
}
