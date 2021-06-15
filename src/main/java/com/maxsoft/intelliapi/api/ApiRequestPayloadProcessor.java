package com.maxsoft.intelliapi.api;

import com.maxsoft.intelliapi.util.reader.EnvironmentPropertyReader;
import io.restassured.http.Header;
import io.restassured.http.Headers;

import java.util.*;

import static com.maxsoft.intelliapi.Constants.*;
import static com.maxsoft.intelliapi.util.LogUtil.printInfo;
import static com.maxsoft.intelliapi.util.DataStoreProcessor.getSavedValueForScenario;
import static com.maxsoft.intelliapi.util.reader.ApiDocumentReader.*;

/**
 * Project Name    : MaxSoft-IntelliAPI
 * Developer       : Osanda Deshan
 * Version         : 1.0.0
 * Date            : 12/12/2020
 * Time            : 10:01 AM
 * Description     :
 **/

public class ApiRequestPayloadProcessor {

    public static void initializeApiToBeInvoked(String apiEndpointName) {
        setApiEndpoint(apiEndpointName);
        setHttpMethod(apiEndpointName);
        setBodyType(apiEndpointName);
        setRequestPayloadTemplate(apiEndpointName);

        printInfo("API Endpoint is: " + "\n" + getSavedValueForScenario(VAR_API_ENDPOINT) + "\n\n",
                ApiRequestPayloadProcessor.class);
        printInfo("HTTP Method is: " + getSavedValueForScenario(VAR_API_HTTP_METHOD) + "\n\n",
                ApiRequestPayloadProcessor.class);
    }

    public static String getApiEndpointToBeInvoked() {
        String invokingEndpoint = getSavedValueForScenario(VAR_API_ENDPOINT);
        invokingEndpoint = EnvironmentPropertyReader.getBaseUrl()
                .concat(invokingEndpoint).concat(getPathParams()).concat(getQueryParams());
        printInfo("Invoked API Endpoint: \n" + invokingEndpoint + "\n\n", ApiRequestPayloadProcessor.class);
        printInfo("HTTP Method is: " + getSavedValueForScenario(VAR_API_HTTP_METHOD) + "\n\n",
                ApiRequestPayloadProcessor.class);
        return invokingEndpoint;
    }

    public static String getQueryParams() {
        String queryParams = String.valueOf(getSavedValueForScenario(VAR_API_QUERY_PARAMS));

        if (queryParams.equals("") || queryParams.equals("null")) {
            queryParams = "";
        }
        return queryParams;
    }

    public static String getPathParams() {
        String pathParams = String.valueOf(getSavedValueForScenario(VAR_API_PATH_PARAMS));

        if (pathParams.equals("") || pathParams.equals("null")) {
            pathParams = "";
        }
        return pathParams;
    }

    public static List<Header> getHeaders(String headerNameList, String headerValueList) {
        if (headerNameList == null || headerNameList.equals("") || headerValueList == null
                || headerValueList.equals("")) {
            return null;
        } else {
            String[] stringHeaderNames = headerNameList.split(",");
            List<String> headerNames = Arrays.asList(stringHeaderNames);

            String[] stringHeaderValues = headerValueList.split(",");
            List<String> headerValues = Arrays.asList(stringHeaderValues);

            List<Header> headerList = new LinkedList<>();

            for (int i = 0; i < headerNames.size(); i++) {
                Header header = new Header(headerNames.get(i), headerValues.get(i));
                headerList.add(header);
            }
            return headerList;
        }
    }

    public static void printHeaders(String headerNameList, String headerValueList) {
        printInfo("Header List:", ApiRequestPayloadProcessor.class);

        for (Header header : new Headers(getHeaders(headerNameList, headerValueList))) {
            printInfo(header.getName() + " = " + header.getValue(), ApiRequestPayloadProcessor.class);
        }
    }

    public static Map<String, String> getFormData(String keysList, String valuesList) {
        if (keysList.equals("") || valuesList == null || valuesList.equals("")) {
            return null;
        } else {
            String[] stringKeys = keysList.split(",");
            List<String> keys = Arrays.asList(stringKeys);

            String[] stringValues = valuesList.split(",");
            List<String> values = Arrays.asList(stringValues);

            Map<String, String> formDataMap = new HashMap<>();

            for (int i = 0; i < keys.size(); i++) {
                formDataMap.put(keys.get(i), values.get(i));
            }
            return formDataMap;
        }
    }

    public static void printFormData(String headerNameList, String headerValueList) {
        printInfo("Form Params Map:", ApiRequestPayloadProcessor.class);

        for (Header header : new Headers(getHeaders(headerNameList, headerValueList))) {
            printInfo(header.getName() + " = " + header.getValue(), ApiRequestPayloadProcessor.class);
        }
    }
}
