package com.maxsoft.intelliapi.util;

import com.thoughtworks.gauge.Gauge;
import org.apache.log4j.Logger;

/**
 * Project Name    : MaxSoft-IntelliAPI
 * Developer       : Osanda Deshan
 * Version         : 1.0.0
 * Date            : 12/5/2020
 * Time            : 9:06 PM
 * Description     :
 **/

public class LogUtil {

    private final static Logger logger = Logger.getLogger(LogUtil.class.getName());

    public static void printInfo(String text){
        logger.info(text);
        Gauge.writeMessage(text);
    }

    public static void printError(String text){
        logger.error(text);
        Gauge.writeMessage(text);
    }
}
