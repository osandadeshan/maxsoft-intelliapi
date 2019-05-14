package com.maxsoft.intelliapi.util.fileoperator;

/**
 * Project Name : MaxSoft-IntelliAPI
 * Developer    : Osanda Deshan
 * Version      : 1.0.0
 * Date         : 6/30/2018
 * Time         : 3:51 PM
 * Description  :
 **/

import com.thoughtworks.gauge.Gauge;
import org.apache.log4j.Logger;
import java.io.*;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Scanner;
import static com.maxsoft.intelliapi.common.Base.getSavedValueForScenario;


public abstract class TextFile {

    private final static Logger logger = Logger.getLogger(TextFile.class.getName());

    public static void printInfo(String text){
        logger.info(text +"\n");
        Gauge.writeMessage(text);
    }

    public static void printError(String text){
        logger.error(text +"\n");
        Gauge.writeMessage(text);
    }

    public static void write(String text, String filePath){
        BufferedWriter writer = null;
        try
        {
            Path pathToFile = Paths.get(filePath);
            Files.createDirectories(pathToFile.getParent());
            File file = new File(filePath);
            file.delete();
            file.createNewFile();
            writer = new BufferedWriter(new FileWriter(filePath));
            writer.write(text);
        }
        catch (IOException e)
        {
        }
        finally
        {
            try
            {
                if (writer != null)
                    writer.close();
            }
            catch (IOException e)
            {
            }
        }
    }

    public static String readAccessToken(String filePath){
        String content = null;
        String isAuthenticationRequired = getSavedValueForScenario("Is authentication required?").toLowerCase();
        String isAccessTokenRetrievedFromTextFile = getSavedValueForScenario("Do you need to retrieve the access token from the text file?").toLowerCase();
        String accessTokenString = getSavedValueForScenario("Provide the access token if you need to authorize the API manually").toLowerCase();
        try {
            content = String.valueOf(new Scanner(new File(filePath)).useDelimiter("\\Z").next());
            if ((Boolean.valueOf(isAuthenticationRequired).equals(Boolean.TRUE) || isAuthenticationRequired.equals("yes") ||
                    isAuthenticationRequired.equals("y")) && (Boolean.valueOf(isAccessTokenRetrievedFromTextFile).equals(Boolean.TRUE) ||
                    isAccessTokenRetrievedFromTextFile.equals("yes") || isAccessTokenRetrievedFromTextFile.equals("y"))) {
                printInfo("Successfully read the access token from the text file in the directory of \"" + filePath + "\"\n\n");
            }
        } catch (FileNotFoundException e) {
            if ((Boolean.valueOf(isAuthenticationRequired).equals(Boolean.TRUE) || isAuthenticationRequired.equals("yes") ||
                    isAuthenticationRequired.equals("y")) && (Boolean.valueOf(isAccessTokenRetrievedFromTextFile).equals(Boolean.TRUE) ||
                    isAccessTokenRetrievedFromTextFile.equals("yes") || isAccessTokenRetrievedFromTextFile.equals("y"))) {
                printError("Reading the access token from the text file in the directory of \"" + filePath + "\" is failed\n\n");
            }
        }
        logger.info(content);
        return content;
    }

    public static String read(String filePath){
        String content = null;
        try {
            content = String.valueOf(new Scanner(new File(filePath)).useDelimiter("\\Z").next());
        } catch (FileNotFoundException e) {
            printError("Reading the text file in the directory of \"" + filePath + "\" is failed");
        }
        logger.info(content);
        return content;
    }


}