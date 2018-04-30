package com.maxsoft.intelliapi.util;

import java.io.File;
import java.io.IOException;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;


/**
 * Created by Osanda on 3/30/2018.
 */


public class ExecutionResults {

    public static final String CURRENT_DIRECTORY = System.getProperty("user.dir");
    public static final String FILE_PATH = CURRENT_DIRECTORY + File.separator + "logs" + File.separator + "gauge.log";
    public static final String UPDATES_AVAILABLE_MESSAGE = "Updates are available";

    public static String readFromGaugeLog(String filePath, int lines) {
        File file = new File(filePath);
        java.io.RandomAccessFile fileHandler = null;
        try {
            fileHandler =
                    new java.io.RandomAccessFile( file, "r" );
            long fileLength = fileHandler.length() - 1;
            StringBuilder sb = new StringBuilder();
            int line = 0;

            for(long filePointer = fileLength; filePointer != -1; filePointer--){
                fileHandler.seek( filePointer );
                int readByte = fileHandler.readByte();

                if( readByte == 0xA ) {
                    if (filePointer < fileLength) {
                        line = line + 1;
                    }
                } else if( readByte == 0xD ) {
                    if (filePointer < fileLength-1) {
                        line = line + 1;
                    }
                }
                if (line >= lines) {
                    break;
                }
                sb.append( ( char ) readByte );
            }

            String lastLine = sb.reverse().toString();
            return lastLine;
        } catch( java.io.FileNotFoundException e ) {
            e.printStackTrace();
            return null;
        } catch( java.io.IOException e ) {
            e.printStackTrace();
            return null;
        }
        finally {
            if (fileHandler != null )
                try {
                    fileHandler.close();
                } catch (IOException e) {
                }
        }
    }

    public static String getTestResultsAsString() {
        String result = ("-------------------------------------------------------------------------------------------------------------\n" +
                         "Test Execution Results: \n" +
                         "-------------------------------------------------------------------------------------------------------------\n"
                         + readFromGaugeLog(FILE_PATH, getLineCountToPrint()) +
                         "\n-------------------------------------------------------------------------------------------------------------");
        System.out.println(result);
        return result;
    }

    public static String getExecutedTime() throws ParseException {
        int i = 4;
        if (getLineCountToPrint() == 5){
            i = 4;
        } else {
            i = 5;
        }
        String time = getTestResultsAsString().split("\r\n|\n|\r")[i];
        SimpleDateFormat sdf1 = new SimpleDateFormat("HH:mm:ss");
        SimpleDateFormat sdf2 = new SimpleDateFormat("hh:mm:ss aa");
        Date date = sdf1.parse(time);
        return (sdf2.format(date));
    }

    public static void deleteLogFile(){
        try{
            File file = new File(FILE_PATH);
            if(file.delete()){
                System.out.println(file.getName() + " is deleted!");
            }else{
                System.out.println("Delete operation is failed.");
            }
        }catch(Exception e){
            e.printStackTrace();
        }
    }

    public static int getLineCountToPrint(){
        int lineCount = 4;
            if(readFromGaugeLog(FILE_PATH, 1).contains(UPDATES_AVAILABLE_MESSAGE)){
                lineCount = 5;
                return lineCount;
            } else {
                return lineCount;
            }
    }


}
