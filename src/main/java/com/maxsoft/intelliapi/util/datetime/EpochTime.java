package com.maxsoft.intelliapi.util.datetime;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.concurrent.TimeUnit;

/**
 * Project Name : MaxSoft-IntelliAPI
 * Developer    : Osanda Deshan
 * Version      : 1.0.0
 * Date         : 9/25/2018
 * Time         : 11:37 AM
 * Description  :
 **/


public class EpochTime {

    public static long getCurrentEpochTimeInSeconds(){
        return TimeUnit.MILLISECONDS.toSeconds(System.currentTimeMillis());
    }

    public static long getCurrentEpochTimeInMilliSeconds(){
        return System.currentTimeMillis();
    }

    public static long getEpochTimeInSeconds(String timestampPattern, String timestamp) throws ParseException {
        SimpleDateFormat sdf = new SimpleDateFormat(timestampPattern);
        Date dt = sdf.parse(timestamp);
        long epoch = dt.getTime();
        return (int)(epoch/1000);
    }

    public static long getEpochTimeInMilliSeconds(String timestampPattern, String timestamp) throws ParseException {
        SimpleDateFormat sdf = new SimpleDateFormat(timestampPattern);
        Date dt = sdf.parse(timestamp);
        long epoch = dt.getTime();
        return epoch;
    }


}
