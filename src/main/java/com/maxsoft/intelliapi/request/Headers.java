package com.maxsoft.intelliapi.request;

import com.maxsoft.intelliapi.util.ApiDocumentReader;
import com.thoughtworks.gauge.Gauge;
import io.restassured.http.Header;
import java.io.IOException;
import java.util.LinkedList;
import java.util.List;


/**
 * Created by Osanda on 11/3/2017.
 */


public class Headers extends BaseClass {

    static String apiName = getSavedValueForScenario("apiName"); // Fetching Value from the Data Store
    static String request;
    static List<Header> headerList = new LinkedList<Header>();
    static {
        try {
            request = ApiDocumentReader.getRequestPayloadTemplate(apiName);
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
