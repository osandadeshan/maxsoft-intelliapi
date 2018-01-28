package com.maxsoft.ata.request;

import com.maxsoft.ata.util.ApiDocumentReader;
import io.restassured.http.Header;
import java.io.IOException;
import java.util.LinkedList;
import java.util.List;


/**
 * Created by Osanda on 11/3/2017.
 */


public class Headers extends BaseClass {

    static String apiName = getSavedValueForScenario("API_NAME"); // Fetching Value from the Data Store
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

    public static void clearHeaders() throws IOException {
        headerList.clear();
    }


}
