package com.maxsoft.intelliapi.stepimpl.api;

import com.maxsoft.intelliapi.api.ApiInvoker;
import com.maxsoft.intelliapi.util.FrameworkUtil;
import com.thoughtworks.gauge.Step;
import io.restassured.http.Headers;

import static com.maxsoft.intelliapi.api.ApiRequestPayloadProcessor.getHeaders;
import static com.maxsoft.intelliapi.Constants.*;
import static com.maxsoft.intelliapi.api.ApiResponseProcessor.saveResponseJsonPathValue;
import static com.maxsoft.intelliapi.api.JsonRequestProcessor.getApiWithAuthMultipleHeaders;
import static com.maxsoft.intelliapi.util.DataStoreProcessor.getSavedValueForScenario;
import static com.maxsoft.intelliapi.util.FrameworkUtil.isTrue;
import static com.maxsoft.intelliapi.util.FrameworkUtil.readAccessToken;
import static com.maxsoft.intelliapi.util.LogUtil.printInfo;

/**
 * Project Name    : MaxSoft-IntelliAPI
 * Developer       : Osanda Deshan
 * Version         : 1.0.0
 * Date            : 12/24/2020
 * Time            : 12:10 AM
 * Description     :
 **/

public class OtherStepImpl {

    // Use this method to print the testing environment name in the HTML report
    @Step("Print configuration details of the testing environment")
    public void printTestingEnvDetails() {
        FrameworkUtil.printTestingEnvDetails();
    }

    /* Use this method when you need to pass the JSON request in previous step and the access token from the text file into the GET/POST/PUT/DELETE API.
       The "saveRequestAuthConfigurations" must use before using this step */
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

    @Step("And the user saves an API request url in the JSON Path <jsonPath> to a data store")
    public void saveApiEndpointInResponseBody(String jsonPath) {
        saveResponseJsonPathValue(SCENARIO, VAR_API_ENDPOINT, jsonPath);
    }

    @Step("And invoke a GET request from the API request url saved in the data store")
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

        printInfo("");
        printInfo("");
        printInfo("Invoked API Endpoint:\n" + invokingEndpoint + "\n\n");
        printInfo("HTTP Method is: GET\n\n");

        if (headerNamesList == null || headerNamesList.equals("") ||
                headerValuesList == null || headerValuesList.equals("")) {
            getApiWithAuthMultipleHeaders(invokingEndpoint, accessToken, new Headers());
        } else {
            getApiWithAuthMultipleHeaders(invokingEndpoint, accessToken,
                    new Headers(getHeaders(headerNamesList, headerValuesList)));
        }
    }

    // Use this method to replace the rows of a column in a given CSV with the timestamp
    @Step("And replace the row values in <columnName> column of the CSV <filePath> into the <timestampPattern> timestamp pattern")
    public void replaceAllColumnValuesToCurrentTimestamp(String columnName, String filePath, String timestampPattern) {
        FrameworkUtil.replaceAllColumnValuesToCurrentTimestamp(CURRENT_DIRECTORY + filePath, columnName, timestampPattern);
    }

    // Use this method to wait for a given time period
    @Step("And the user waits <seconds> seconds")
    public void waitBySeconds(String seconds) {
        FrameworkUtil.waitBySeconds(Integer.parseInt(seconds));
    }
}
