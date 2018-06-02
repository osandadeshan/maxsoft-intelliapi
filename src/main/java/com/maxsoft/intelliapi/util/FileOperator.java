package com.maxsoft.intelliapi.util;

import com.thoughtworks.gauge.Gauge;

import java.io.*;
import java.util.Scanner;


/**
 * Created by Osanda on 7/31/2017.
 */


public abstract class FileOperator {

    public static void writeToFile(String text, String filePath){
        BufferedWriter writer = null;
            try
            {
                writer = new BufferedWriter( new FileWriter(filePath));
                writer.write(text);

            }
                catch ( IOException e)
                {
                }
                    finally
                    {
                        try
                        {
                            if ( writer != null)
                                writer.close( );
                        }
                        catch ( IOException e)
                        {
                        }
                    }
    }

    public static String readAccessTokenFromFile(String filePath){
        String content = null;
        try {
            content = String.valueOf(new Scanner(new File(filePath)).useDelimiter("\\Z").next());
            System.out.println("Successfully read the access token from the text file in the directory of \"" + filePath + "\"\n\n");
            Gauge.writeMessage("Successfully read the access token from the text file in the directory of \"" + filePath + "\"\n\n");
        } catch (FileNotFoundException e) {
            System.out.println("Reading the access token from the text file in the directory of \"" + filePath + "\" is failed\n\n");
            Gauge.writeMessage("Reading the access token from the text file in the directory of \"" + filePath + "\" is failed\n\n");
        }
        System.out.println(content);
        return content;
    }

    public static String readFromFile(String filePath){
        String content = null;
        try {
            content = String.valueOf(new Scanner(new File(filePath)).useDelimiter("\\Z").next());
        } catch (FileNotFoundException e) {
            System.out.println("Reading the text file in the directory of \"" + filePath + "\" is failed");
            Gauge.writeMessage("Reading the text file in the directory of \"" + filePath + "\" is failed");
        }
        System.out.println(content);
        return content;
    }


}