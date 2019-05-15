package com.maxsoft.intelliapi.api;

/**
 * Project Name : MaxSoft-IntelliAPI
 * Developer    : Osanda Deshan
 * Version      : 1.0.0
 * Date         : 6/30/2018
 * Time         : 3:51 PM
 * Description  :
 **/

import com.maxsoft.intelliapi.common.Base;
import com.maxsoft.intelliapi.util.reader.ApiDocument;
import com.thoughtworks.gauge.Gauge;
import io.restassured.http.Header;
import org.apache.log4j.Logger;
import java.io.IOException;
import java.util.LinkedList;
import java.util.List;


public class Headers extends Base {

    static String apiName = getSavedValueForScenario("apiName"); // Fetching Value from the Data Store
    static String request;
    static List<Header> headerList = new LinkedList<Header>();
    static {
        try {
            request = ApiDocument.getRequestPayloadTemplate(apiName);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private final static Logger logger = Logger.getLogger(Headers.class.getName());

    public static void printInfo(String text){
        logger.info(text);
        Gauge.writeMessage(text);
    }

    public Headers(List<Header> headerList) {
        super();
    }

    public static Headers setRequestHeaders(String headerName, String headerValue) {
        Header header = new Header(headerName, headerValue);
        headerList.add(header);
        return new Headers(headerList);
    }

    public static List<Header> getFinalHeaders(){
        return headerList;
    }

    public static void printHeaders() {
        printInfo("Header List: ");
        for(Header header : headerList) {
            printInfo(header.getName() + " = " + header.getValue());
        }
    }

    public static void clearHeaders() {
        headerList.clear();
    }


}
