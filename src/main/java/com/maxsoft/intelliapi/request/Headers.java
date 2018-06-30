package com.maxsoft.intelliapi.request;

/**
 * Project Name : MaxSoft-IntelliAPI
 * Developer    : Osanda Deshan
 * Version      : 1.0.0
 * Date         : 6/30/2018
 * Time         : 3:51 PM
 * Description  :
 **/

import com.maxsoft.intelliapi.util.reader.ApiDocument;
import com.thoughtworks.gauge.Gauge;
import io.restassured.http.Header;
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

    public Headers(List<Header> headerList) {
        super();
    }

    public static Headers setRequestHeaders(String headerName, String headerValue) throws IOException {
        Header header = new Header(headerName, headerValue);
        headerList.add(header);
        return new Headers(headerList);
    }

    public static List<Header> getFinalHeaders(){
        return headerList;
    }

    public static void printHeaders() {
        System.out.println("Header List: ");
        Gauge.writeMessage("Header List: ");
        for(Header header : headerList) {
            System.out.println(header.getName() + " = " + header.getValue());
            Gauge.writeMessage(header.getName() + " = " + header.getValue());
        }
    }

    public static void clearHeaders() throws IOException {
        headerList.clear();
    }


}
