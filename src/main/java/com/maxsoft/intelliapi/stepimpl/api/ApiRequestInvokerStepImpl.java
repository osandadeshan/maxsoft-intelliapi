package com.maxsoft.intelliapi.stepimpl.api;

import com.maxsoft.intelliapi.api.ApiInvoker;
import com.thoughtworks.gauge.Step;
import io.restassured.http.Headers;

import static com.maxsoft.intelliapi.Constants.*;
import static com.maxsoft.intelliapi.api.ApiRequestPayloadProcessor.getHeaders;
import static com.maxsoft.intelliapi.api.JsonRequestProcessor.getApiWithAuthMultipleHeaders;
import static com.maxsoft.intelliapi.util.DataStoreProcessor.getSavedValueForScenario;
import static com.maxsoft.intelliapi.util.FrameworkUtil.isTrue;
import static com.maxsoft.intelliapi.util.FrameworkUtil.readAccessToken;
import static com.maxsoft.intelliapi.util.LogUtil.printInfo;

/**
 * Project Name    : MaxSoft-IntelliAPI
 * Developer       : Osanda Deshan
 * Version         : 1.0.0
 * Date            : 1/20/2021
 * Time            : 6:21 PM
 * Description     :
 **/

public class ApiRequestInvokerStepImpl {

/*  Use this method when you need to pass the JSON request in previous step and the access token from the text file
    into the GET/POST/PUT/DELETE API. The "saveRequestAuthConfigurations" must use before using this step   */
    @Step("When the user invokes the API")
    public void invokeApi() {
        String jsonRequest = String.valueOf(getSavedValueForScenario(VAR_API_JSON_REQUEST_BODY));
        String headerNamesList = getSavedValueForScenario(VAR_API_HEADER_NAMES_LIST);
        String headerValuesList = getSavedValueForScenario(VAR_API_HEADER_VALUES_LIST);

        if (headerNamesList == null || headerNamesList.equals("") ||
                headerValuesList == null || headerValuesList.equals("")) {
            ApiInvoker.invoke(jsonRequest, new Headers());
        } else {
            ApiInvoker.invoke(jsonRequest, new Headers(getHeaders(headerNamesList, headerValuesList)));
        }
    }

/*  Use this method to invoke a GET API from a request url in the response's JSON path.
    The "saveApiEndpointInResponseBody" must use before using this step   */
    @Step("When the user invokes the GET API")
    public void doGetRequestFromDataStore() {
        String invokingEndpoint = getSavedValueForScenario(VAR_API_ENDPOINT);
        String headerNamesList = getSavedValueForScenario(VAR_API_HEADER_NAMES_LIST);
        String headerValuesList = getSavedValueForScenario(VAR_API_HEADER_VALUES_LIST);

        String accessToken, isAuthenticationRequired, isAccessTokenRetrievedFromTextFile, accessTokenString;
        String accessTokenInFile = readAccessToken();

        try {
            isAuthenticationRequired = getSavedValueForScenario(IS_AUTHENTICATION_REQUIRED).toLowerCase();
            isAccessTokenRetrievedFromTextFile = getSavedValueForScenario(RETRIEVE_TOKEN_FROM_TEXT_FILE).toLowerCase();
            accessTokenString = getSavedValueForScenario(MANUAL_TOKEN);
        } catch (Exception ex) {
            isAuthenticationRequired = "";
            isAccessTokenRetrievedFromTextFile = "";
            accessTokenString = "";
        }

        if (isTrue(isAuthenticationRequired)) {
            if (isTrue(isAccessTokenRetrievedFromTextFile)) {
                accessToken = accessTokenInFile;
            } else {
                accessToken = accessTokenString;
            }
        } else {
            accessToken = "";
        }

        printInfo("", ApiRequestInvokerStepImpl.class);
        printInfo("", ApiRequestInvokerStepImpl.class);
        printInfo("Invoked API Endpoint:\n" + invokingEndpoint + "\n\n", ApiRequestInvokerStepImpl.class);
        printInfo("HTTP Method is: GET\n\n", ApiRequestInvokerStepImpl.class);

        if (headerNamesList == null || headerNamesList.equals("") ||
                headerValuesList == null || headerValuesList.equals("")) {
            getApiWithAuthMultipleHeaders(invokingEndpoint, accessToken, new Headers());
        } else {
            getApiWithAuthMultipleHeaders(invokingEndpoint, accessToken,
                    new Headers(getHeaders(headerNamesList, headerValuesList)));
        }
    }
}
