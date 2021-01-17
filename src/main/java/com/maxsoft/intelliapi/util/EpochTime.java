package com.maxsoft.intelliapi.util;

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

    public static long getCurrentEpochTimeInSeconds() {
        return TimeUnit.MILLISECONDS.toSeconds(System.currentTimeMillis());
    }

    public static long getCurrentEpochTimeInMilliSeconds() {
        return System.currentTimeMillis();
    }

    public static long getEpochTimeInSeconds(String timestampPattern, String timestamp) {
        SimpleDateFormat sdf = new SimpleDateFormat(timestampPattern);
        long epochTime = 0;
        try {
            Date dt = sdf.parse(timestamp);
            long epoch = dt.getTime();
            epochTime = (int) (epoch / 1000);
        } catch (ParseException e) {
            e.printStackTrace();
        }
        return epochTime;
    }

    public static long getEpochTimeInMilliSeconds(String timestampPattern, String timestamp) {
        SimpleDateFormat sdf = new SimpleDateFormat(timestampPattern);
        long epochTime = 0;
        try {
            Date dt = sdf.parse(timestamp);
            epochTime = dt.getTime();
        } catch (ParseException e) {
            e.printStackTrace();
        }
        return epochTime;
    }
}
