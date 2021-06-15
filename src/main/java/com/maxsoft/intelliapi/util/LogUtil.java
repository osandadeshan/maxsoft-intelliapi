package com.maxsoft.intelliapi.util;

import com.thoughtworks.gauge.Gauge;
import org.apache.logging.log4j.LogManager;

/**
 * Project Name    : MaxSoft-IntelliAPI
 * Developer       : Osanda Deshan
 * Version         : 1.0.0
 * Date            : 12/5/2020
 * Time            : 9:06 PM
 * Description     :
 **/

public class LogUtil {

    public static void printInfo(String text, final Class<?> clazz){
        LogManager.getLogger(clazz).info(text);
        Gauge.writeMessage(text);
    }

    public static void printError(String text, final Class<?> clazz){
        LogManager.getLogger(clazz).error(text);
        Gauge.writeMessage(text);
    }
}
