package com.maxsoft.intelliapi.stepimpl.api;

import com.maxsoft.intelliapi.api.ApiInvoker;
import com.maxsoft.intelliapi.util.FrameworkUtil;
import com.thoughtworks.gauge.Step;
import io.restassured.http.Headers;

import static com.maxsoft.intelliapi.api.ApiRequestPayloadProcessor.getHeaders;
import static com.maxsoft.intelliapi.Constants.*;
import static com.maxsoft.intelliapi.util.DataStoreProcessor.getSavedValueForScenario;

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
