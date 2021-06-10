package com.maxsoft.intelliapi.api;

import io.restassured.RestAssured;
import io.restassured.http.ContentType;
import io.restassured.http.Headers;
import io.restassured.response.Response;

import java.io.File;
import java.util.Collections;
import java.util.Map;

import static com.maxsoft.intelliapi.api.ApiRequestPayloadProcessor.getFormData;
import static com.maxsoft.intelliapi.api.ApiResponseProcessor.*;
import static com.maxsoft.intelliapi.Constants.*;
import static com.maxsoft.intelliapi.util.DataStoreProcessor.getSavedValueForScenario;
import static io.restassured.RestAssured.given;
import static io.restassured.config.EncoderConfig.encoderConfig;

/**
 * Project Name    : MaxSoft-IntelliAPI
 * Developer       : Osanda Deshan
 * Version         : 1.0.0
 * Date            : 12/12/2020
 * Time            : 10:34 AM
 * Description     :
 **/

public class FormDataRequestProcessor {

    public static void postFormDataApiWithAuthMultipleHeaders(String invokingEndpoint, String accessToken, Headers headers) {
        Response response;

        // File Keys
        String fileKey1 = getSavedValueForScenario(VAR_API_FORM_DATA_MULTIPART_FILE_KEY + "1");
        String fileKey2 = getSavedValueForScenario(VAR_API_FORM_DATA_MULTIPART_FILE_KEY + "2");
        String fileKey3 = getSavedValueForScenario(VAR_API_FORM_DATA_MULTIPART_FILE_KEY + "3");
        String fileKey4 = getSavedValueForScenario(VAR_API_FORM_DATA_MULTIPART_FILE_KEY + "4");
        String fileKey5 = getSavedValueForScenario(VAR_API_FORM_DATA_MULTIPART_FILE_KEY + "5");

        // File Paths
        String filePath1 = CURRENT_DIRECTORY + getSavedValueForScenario(VAR_API_FORM_DATA_MULTIPART_FILE_PATH + "1");
        String filePath2 = CURRENT_DIRECTORY + getSavedValueForScenario(VAR_API_FORM_DATA_MULTIPART_FILE_PATH + "2");
        String filePath3 = CURRENT_DIRECTORY + getSavedValueForScenario(VAR_API_FORM_DATA_MULTIPART_FILE_PATH + "3");
        String filePath4 = CURRENT_DIRECTORY + getSavedValueForScenario(VAR_API_FORM_DATA_MULTIPART_FILE_PATH + "4");
        String filePath5 = CURRENT_DIRECTORY + getSavedValueForScenario(VAR_API_FORM_DATA_MULTIPART_FILE_PATH + "5");

        // File Mime Types
        String mimeType1 = getSavedValueForScenario(VAR_API_FORM_DATA_MULTIPART_MIME_TYPE + "1");
        String mimeType2 = getSavedValueForScenario(VAR_API_FORM_DATA_MULTIPART_MIME_TYPE + "2");
        String mimeType3 = getSavedValueForScenario(VAR_API_FORM_DATA_MULTIPART_MIME_TYPE + "3");
        String mimeType4 = getSavedValueForScenario(VAR_API_FORM_DATA_MULTIPART_MIME_TYPE + "4");
        String mimeType5 = getSavedValueForScenario(VAR_API_FORM_DATA_MULTIPART_MIME_TYPE + "5");

        int noOfMultipartFiles = 0;

        try {
            noOfMultipartFiles = Integer.parseInt(getSavedValueForScenario(VAR_API_FORM_DATA_MULTIPART_FILES_COUNT));
        } catch (Exception ignored) {
        }

        Map<String, String> formParams;
        String keyList = getSavedValueForScenario(VAR_API_FORM_DATA_KEYS_LIST);
        String valueList = getSavedValueForScenario(VAR_API_FORM_DATA_VALUES_LIST);

        if (keyList == null || valueList == null) {
            formParams = Collections.emptyMap();
        } else {
            formParams = getFormData(keyList, valueList);
        }

        switch (noOfMultipartFiles) {

            case 1:
                if (accessToken == null || accessToken.equals("")) {
                    response = given()
                            .config(
                                    RestAssured.config()
                                            .encoderConfig(
                                                    encoderConfig()
                                                            .encodeContentTypeAs(VAR_API_MULTIPART_FORM_DATA, ContentType.TEXT)))
                            .formParams(formParams)
                            .multiPart(fileKey1, new File(filePath1), mimeType1)
                            .headers(headers)
                            .when()
                            .post(invokingEndpoint);
                } else {
                    response = given()
                            .config(
                                    RestAssured.config()
                                            .encoderConfig(
                                                    encoderConfig()
                                                            .encodeContentTypeAs(VAR_API_MULTIPART_FORM_DATA, ContentType.TEXT)))
                            .header(AUTHORIZATION_HEADER_NAME, accessToken)
                            .headers(headers)
                            .formParams(formParams)
                            .multiPart(fileKey1, new File(filePath1), mimeType1)
                            .when()
                            .post(invokingEndpoint);
                }
                break;

            case 2:
                if (accessToken == null || accessToken.equals("")) {
                    response = given()
                            .config(
                                    RestAssured.config()
                                            .encoderConfig(
                                                    encoderConfig()
                                                            .encodeContentTypeAs(VAR_API_MULTIPART_FORM_DATA, ContentType.TEXT)))
                            .formParams(formParams)
                            .multiPart(fileKey1, new File(filePath1), mimeType1)
                            .multiPart(fileKey2, new File(filePath2), mimeType2)
                            .headers(headers)
                            .when()
                            .post(invokingEndpoint);
                } else {
                    response = given()
                            .config(
                                    RestAssured.config()
                                            .encoderConfig(
                                                    encoderConfig()
                                                            .encodeContentTypeAs(VAR_API_MULTIPART_FORM_DATA, ContentType.TEXT)))
                            .header(AUTHORIZATION_HEADER_NAME, accessToken)
                            .headers(headers)
                            .formParams(formParams)
                            .multiPart(fileKey1, new File(filePath1), mimeType1)
                            .multiPart(fileKey2, new File(filePath2), mimeType2)
                            .when()
                            .post(invokingEndpoint);
                }
                break;

            case 3:
                if (accessToken == null || accessToken.equals("")) {
                    response = given()
                            .config(
                                    RestAssured.config()
                                            .encoderConfig(
                                                    encoderConfig()
                                                            .encodeContentTypeAs(VAR_API_MULTIPART_FORM_DATA, ContentType.TEXT)))
                            .formParams(formParams)
                            .multiPart(fileKey1, new File(filePath1), mimeType1)
                            .multiPart(fileKey2, new File(filePath2), mimeType2)
                            .multiPart(fileKey3, new File(filePath3), mimeType3)
                            .headers(headers)
                            .when()
                            .post(invokingEndpoint);
                } else {
                    response = given()
                            .config(
                                    RestAssured.config()
                                            .encoderConfig(
                                                    encoderConfig()
                                                            .encodeContentTypeAs(VAR_API_MULTIPART_FORM_DATA, ContentType.TEXT)))
                            .header(AUTHORIZATION_HEADER_NAME, accessToken)
                            .headers(headers)
                            .formParams(formParams)
                            .multiPart(fileKey1, new File(filePath1), mimeType1)
                            .multiPart(fileKey2, new File(filePath2), mimeType2)
                            .multiPart(fileKey3, new File(filePath3), mimeType3)
                            .when()
                            .post(invokingEndpoint);
                }
                break;

            case 4:
                if (accessToken == null || accessToken.equals("")) {
                    response = given()
                            .config(
                                    RestAssured.config()
                                            .encoderConfig(
                                                    encoderConfig()
                                                            .encodeContentTypeAs(VAR_API_MULTIPART_FORM_DATA, ContentType.TEXT)))
                            .formParams(formParams)
                            .multiPart(fileKey1, new File(filePath1), mimeType1)
                            .multiPart(fileKey2, new File(filePath2), mimeType2)
                            .multiPart(fileKey3, new File(filePath3), mimeType3)
                            .multiPart(fileKey4, new File(filePath4), mimeType4)
                            .headers(headers)
                            .when()
                            .post(invokingEndpoint);
                } else {
                    response = given()
                            .config(
                                    RestAssured.config()
                                            .encoderConfig(
                                                    encoderConfig()
                                                            .encodeContentTypeAs(VAR_API_MULTIPART_FORM_DATA, ContentType.TEXT)))
                            .header(AUTHORIZATION_HEADER_NAME, accessToken)
                            .headers(headers)
                            .formParams(formParams)
                            .multiPart(fileKey1, new File(filePath1), mimeType1)
                            .multiPart(fileKey2, new File(filePath2), mimeType2)
                            .multiPart(fileKey3, new File(filePath3), mimeType3)
                            .multiPart(fileKey4, new File(filePath4), mimeType4)
                            .when()
                            .post(invokingEndpoint);
                }
                break;

            case 5:
                if (accessToken == null || accessToken.equals("")) {
                    response = given()
                            .config(
                                    RestAssured.config()
                                            .encoderConfig(
                                                    encoderConfig()
                                                            .encodeContentTypeAs(VAR_API_MULTIPART_FORM_DATA, ContentType.TEXT)))
                            .formParams(formParams)
                            .multiPart(fileKey1, new File(filePath1), mimeType1)
                            .multiPart(fileKey2, new File(filePath2), mimeType2)
                            .multiPart(fileKey3, new File(filePath3), mimeType3)
                            .multiPart(fileKey4, new File(filePath4), mimeType4)
                            .multiPart(fileKey5, new File(filePath5), mimeType5)
                            .headers(headers)
                            .when()
                            .post(invokingEndpoint);
                } else {
                    response = given()
                            .config(
                                    RestAssured.config()
                                            .encoderConfig(
                                                    encoderConfig()
                                                            .encodeContentTypeAs(VAR_API_MULTIPART_FORM_DATA, ContentType.TEXT)))
                            .header(AUTHORIZATION_HEADER_NAME, accessToken)
                            .headers(headers)
                            .formParams(formParams)
                            .multiPart(fileKey1, new File(filePath1), mimeType1)
                            .multiPart(fileKey2, new File(filePath2), mimeType2)
                            .multiPart(fileKey3, new File(filePath3), mimeType3)
                            .multiPart(fileKey4, new File(filePath4), mimeType4)
                            .multiPart(fileKey5, new File(filePath5), mimeType5)
                            .when()
                            .post(invokingEndpoint);
                }
                break;

            default:
                if (accessToken == null || accessToken.equals("")) {
                    response = given()
                            .config(
                                    RestAssured.config()
                                            .encoderConfig(
                                                    encoderConfig()
                                                            .encodeContentTypeAs(VAR_API_MULTIPART_FORM_DATA, ContentType.TEXT)))
                            .formParams(formParams)
                            .headers(headers)
                            .when()
                            .post(invokingEndpoint);
                } else {
                    response = given()
                            .config(
                                    RestAssured.config()
                                            .encoderConfig(
                                                    encoderConfig()
                                                            .encodeContentTypeAs(VAR_API_MULTIPART_FORM_DATA, ContentType.TEXT)))
                            .formParams(formParams)
                            .header(AUTHORIZATION_HEADER_NAME, accessToken)
                            .headers(headers)
                            .when()
                            .post(invokingEndpoint);
                }
                break;
        }

        saveStatusCode(response);
        saveApiResponseBody(response);
        printResponseTime(response);
        printResponse();
        printResponseHeaders(response);
        clearInvokedApiEndpointArtifacts();
    }

    public static void putFormDataApiWithAuthMultipleHeaders(String invokingEndpoint, String accessToken, Headers headers) {
        Response response;

        // File Keys
        String fileKey1 = getSavedValueForScenario(VAR_API_FORM_DATA_MULTIPART_FILE_KEY + "1");
        String fileKey2 = getSavedValueForScenario(VAR_API_FORM_DATA_MULTIPART_FILE_KEY + "2");
        String fileKey3 = getSavedValueForScenario(VAR_API_FORM_DATA_MULTIPART_FILE_KEY + "3");
        String fileKey4 = getSavedValueForScenario(VAR_API_FORM_DATA_MULTIPART_FILE_KEY + "4");
        String fileKey5 = getSavedValueForScenario(VAR_API_FORM_DATA_MULTIPART_FILE_KEY + "5");

        // File Paths
        String filePath1 = CURRENT_DIRECTORY + getSavedValueForScenario(VAR_API_FORM_DATA_MULTIPART_FILE_PATH + "1");
        String filePath2 = CURRENT_DIRECTORY + getSavedValueForScenario(VAR_API_FORM_DATA_MULTIPART_FILE_PATH + "2");
        String filePath3 = CURRENT_DIRECTORY + getSavedValueForScenario(VAR_API_FORM_DATA_MULTIPART_FILE_PATH + "3");
        String filePath4 = CURRENT_DIRECTORY + getSavedValueForScenario(VAR_API_FORM_DATA_MULTIPART_FILE_PATH + "4");
        String filePath5 = CURRENT_DIRECTORY + getSavedValueForScenario(VAR_API_FORM_DATA_MULTIPART_FILE_PATH + "5");

        // File Mime Types
        String mimeType1 = getSavedValueForScenario(VAR_API_FORM_DATA_MULTIPART_MIME_TYPE + "1");
        String mimeType2 = getSavedValueForScenario(VAR_API_FORM_DATA_MULTIPART_MIME_TYPE + "2");
        String mimeType3 = getSavedValueForScenario(VAR_API_FORM_DATA_MULTIPART_MIME_TYPE + "3");
        String mimeType4 = getSavedValueForScenario(VAR_API_FORM_DATA_MULTIPART_MIME_TYPE + "4");
        String mimeType5 = getSavedValueForScenario(VAR_API_FORM_DATA_MULTIPART_MIME_TYPE + "5");

        int noOfMultipartFiles = 0;

        try {
            noOfMultipartFiles = Integer.parseInt(getSavedValueForScenario(VAR_API_FORM_DATA_MULTIPART_FILES_COUNT));
        } catch (Exception ignored) {
        }

        Map<String, String> formParams;
        String keyList = getSavedValueForScenario(VAR_API_FORM_DATA_KEYS_LIST);
        String valueList = getSavedValueForScenario(VAR_API_FORM_DATA_VALUES_LIST);

        if (keyList == null || valueList == null) {
            formParams = Collections.emptyMap();
        } else {
            formParams = getFormData(keyList, valueList);
        }

        switch (noOfMultipartFiles) {

            case 1:
                if (accessToken == null || accessToken.equals("")) {
                    response = given()
                            .config(
                                    RestAssured.config()
                                            .encoderConfig(
                                                    encoderConfig()
                                                            .encodeContentTypeAs(VAR_API_MULTIPART_FORM_DATA, ContentType.TEXT)))
                            .formParams(formParams)
                            .multiPart(fileKey1, new File(filePath1), mimeType1)
                            .headers(headers)
                            .when()
                            .put(invokingEndpoint);
                } else {
                    response = given()
                            .config(
                                    RestAssured.config()
                                            .encoderConfig(
                                                    encoderConfig()
                                                            .encodeContentTypeAs(VAR_API_MULTIPART_FORM_DATA, ContentType.TEXT)))
                            .header(AUTHORIZATION_HEADER_NAME, accessToken)
                            .headers(headers)
                            .formParams(formParams)
                            .multiPart(fileKey1, new File(filePath1), mimeType1)
                            .when()
                            .put(invokingEndpoint);
                }
                break;

            case 2:
                if (accessToken == null || accessToken.equals("")) {
                    response = given()
                            .config(
                                    RestAssured.config()
                                            .encoderConfig(
                                                    encoderConfig()
                                                            .encodeContentTypeAs(VAR_API_MULTIPART_FORM_DATA, ContentType.TEXT)))
                            .formParams(formParams)
                            .multiPart(fileKey1, new File(filePath1), mimeType1)
                            .multiPart(fileKey2, new File(filePath2), mimeType2)
                            .headers(headers)
                            .when()
                            .put(invokingEndpoint);
                } else {
                    response = given()
                            .config(
                                    RestAssured.config()
                                            .encoderConfig(
                                                    encoderConfig()
                                                            .encodeContentTypeAs(VAR_API_MULTIPART_FORM_DATA, ContentType.TEXT)))
                            .header(AUTHORIZATION_HEADER_NAME, accessToken)
                            .headers(headers)
                            .formParams(formParams)
                            .multiPart(fileKey1, new File(filePath1), mimeType1)
                            .multiPart(fileKey2, new File(filePath2), mimeType2)
                            .when()
                            .put(invokingEndpoint);
                }
                break;

            case 3:
                if (accessToken == null || accessToken.equals("")) {
                    response = given()
                            .config(
                                    RestAssured.config()
                                            .encoderConfig(
                                                    encoderConfig()
                                                            .encodeContentTypeAs(VAR_API_MULTIPART_FORM_DATA, ContentType.TEXT)))
                            .formParams(formParams)
                            .multiPart(fileKey1, new File(filePath1), mimeType1)
                            .multiPart(fileKey2, new File(filePath2), mimeType2)
                            .multiPart(fileKey3, new File(filePath3), mimeType3)
                            .headers(headers)
                            .when()
                            .put(invokingEndpoint);
                } else {
                    response = given()
                            .config(
                                    RestAssured.config()
                                            .encoderConfig(
                                                    encoderConfig()
                                                            .encodeContentTypeAs(VAR_API_MULTIPART_FORM_DATA, ContentType.TEXT)))
                            .header(AUTHORIZATION_HEADER_NAME, accessToken)
                            .headers(headers)
                            .formParams(formParams)
                            .multiPart(fileKey1, new File(filePath1), mimeType1)
                            .multiPart(fileKey2, new File(filePath2), mimeType2)
                            .multiPart(fileKey3, new File(filePath3), mimeType3)
                            .when()
                            .put(invokingEndpoint);
                }
                break;

            case 4:
                if (accessToken == null || accessToken.equals("")) {
                    response = given()
                            .config(
                                    RestAssured.config()
                                            .encoderConfig(
                                                    encoderConfig()
                                                            .encodeContentTypeAs(VAR_API_MULTIPART_FORM_DATA, ContentType.TEXT)))
                            .formParams(formParams)
                            .multiPart(fileKey1, new File(filePath1), mimeType1)
                            .multiPart(fileKey2, new File(filePath2), mimeType2)
                            .multiPart(fileKey3, new File(filePath3), mimeType3)
                            .multiPart(fileKey4, new File(filePath4), mimeType4)
                            .headers(headers)
                            .when()
                            .put(invokingEndpoint);
                } else {
                    response = given()
                            .config(
                                    RestAssured.config()
                                            .encoderConfig(
                                                    encoderConfig()
                                                            .encodeContentTypeAs(VAR_API_MULTIPART_FORM_DATA, ContentType.TEXT)))
                            .header(AUTHORIZATION_HEADER_NAME, accessToken)
                            .headers(headers)
                            .formParams(formParams)
                            .multiPart(fileKey1, new File(filePath1), mimeType1)
                            .multiPart(fileKey2, new File(filePath2), mimeType2)
                            .multiPart(fileKey3, new File(filePath3), mimeType3)
                            .multiPart(fileKey4, new File(filePath4), mimeType4)
                            .when()
                            .put(invokingEndpoint);
                }
                break;

            case 5:
                if (accessToken == null || accessToken.equals("")) {
                    response = given()
                            .config(
                                    RestAssured.config()
                                            .encoderConfig(
                                                    encoderConfig()
                                                            .encodeContentTypeAs(VAR_API_MULTIPART_FORM_DATA, ContentType.TEXT)))
                            .formParams(formParams)
                            .multiPart(fileKey1, new File(filePath1), mimeType1)
                            .multiPart(fileKey2, new File(filePath2), mimeType2)
                            .multiPart(fileKey3, new File(filePath3), mimeType3)
                            .multiPart(fileKey4, new File(filePath4), mimeType4)
                            .multiPart(fileKey5, new File(filePath5), mimeType5)
                            .headers(headers)
                            .when()
                            .put(invokingEndpoint);
                } else {
                    response = given()
                            .config(
                                    RestAssured.config()
                                            .encoderConfig(
                                                    encoderConfig()
                                                            .encodeContentTypeAs(VAR_API_MULTIPART_FORM_DATA, ContentType.TEXT)))
                            .header(AUTHORIZATION_HEADER_NAME, accessToken)
                            .headers(headers)
                            .formParams(formParams)
                            .multiPart(fileKey1, new File(filePath1), mimeType1)
                            .multiPart(fileKey2, new File(filePath2), mimeType2)
                            .multiPart(fileKey3, new File(filePath3), mimeType3)
                            .multiPart(fileKey4, new File(filePath4), mimeType4)
                            .multiPart(fileKey5, new File(filePath5), mimeType5)
                            .when()
                            .put(invokingEndpoint);
                }
                break;

            default:
                if (accessToken == null || accessToken.equals("")) {
                    response = given()
                            .config(
                                    RestAssured.config()
                                            .encoderConfig(
                                                    encoderConfig()
                                                            .encodeContentTypeAs(VAR_API_MULTIPART_FORM_DATA, ContentType.TEXT)))
                            .formParams(formParams)
                            .headers(headers)
                            .when()
                            .put(invokingEndpoint);
                } else {
                    response = given()
                            .config(
                                    RestAssured.config()
                                            .encoderConfig(
                                                    encoderConfig()
                                                            .encodeContentTypeAs(VAR_API_MULTIPART_FORM_DATA, ContentType.TEXT)))
                            .formParams(formParams)
                            .header(AUTHORIZATION_HEADER_NAME, accessToken)
                            .headers(headers)
                            .when()
                            .put(invokingEndpoint);
                }
                break;
        }

        saveStatusCode(response);
        saveApiResponseBody(response);
        printResponseTime(response);
        printResponse();
        printResponseHeaders(response);
        clearInvokedApiEndpointArtifacts();
    }

    public static void patchFormDataApiWithAuthMultipleHeaders(String invokingEndpoint, String accessToken, Headers headers) {
        Response response;

        // File Keys
        String fileKey1 = getSavedValueForScenario(VAR_API_FORM_DATA_MULTIPART_FILE_KEY + "1");
        String fileKey2 = getSavedValueForScenario(VAR_API_FORM_DATA_MULTIPART_FILE_KEY + "2");
        String fileKey3 = getSavedValueForScenario(VAR_API_FORM_DATA_MULTIPART_FILE_KEY + "3");
        String fileKey4 = getSavedValueForScenario(VAR_API_FORM_DATA_MULTIPART_FILE_KEY + "4");
        String fileKey5 = getSavedValueForScenario(VAR_API_FORM_DATA_MULTIPART_FILE_KEY + "5");

        // File Paths
        String filePath1 = CURRENT_DIRECTORY + getSavedValueForScenario(VAR_API_FORM_DATA_MULTIPART_FILE_PATH + "1");
        String filePath2 = CURRENT_DIRECTORY + getSavedValueForScenario(VAR_API_FORM_DATA_MULTIPART_FILE_PATH + "2");
        String filePath3 = CURRENT_DIRECTORY + getSavedValueForScenario(VAR_API_FORM_DATA_MULTIPART_FILE_PATH + "3");
        String filePath4 = CURRENT_DIRECTORY + getSavedValueForScenario(VAR_API_FORM_DATA_MULTIPART_FILE_PATH + "4");
        String filePath5 = CURRENT_DIRECTORY + getSavedValueForScenario(VAR_API_FORM_DATA_MULTIPART_FILE_PATH + "5");

        // File Mime Types
        String mimeType1 = getSavedValueForScenario(VAR_API_FORM_DATA_MULTIPART_MIME_TYPE + "1");
        String mimeType2 = getSavedValueForScenario(VAR_API_FORM_DATA_MULTIPART_MIME_TYPE + "2");
        String mimeType3 = getSavedValueForScenario(VAR_API_FORM_DATA_MULTIPART_MIME_TYPE + "3");
        String mimeType4 = getSavedValueForScenario(VAR_API_FORM_DATA_MULTIPART_MIME_TYPE + "4");
        String mimeType5 = getSavedValueForScenario(VAR_API_FORM_DATA_MULTIPART_MIME_TYPE + "5");

        int noOfMultipartFiles = 0;

        try {
            noOfMultipartFiles = Integer.parseInt(getSavedValueForScenario(VAR_API_FORM_DATA_MULTIPART_FILES_COUNT));
        } catch (Exception ignored) {
        }

        Map<String, String> formParams;
        String keyList = getSavedValueForScenario(VAR_API_FORM_DATA_KEYS_LIST);
        String valueList = getSavedValueForScenario(VAR_API_FORM_DATA_VALUES_LIST);

        if (keyList == null || valueList == null) {
            formParams = Collections.emptyMap();
        } else {
            formParams = getFormData(keyList, valueList);
        }

        switch (noOfMultipartFiles) {

            case 1:
                if (accessToken == null || accessToken.equals("")) {
                    response = given()
                            .config(
                                    RestAssured.config()
                                            .encoderConfig(
                                                    encoderConfig()
                                                            .encodeContentTypeAs(VAR_API_MULTIPART_FORM_DATA, ContentType.TEXT)))
                            .formParams(formParams)
                            .multiPart(fileKey1, new File(filePath1), mimeType1)
                            .headers(headers)
                            .when()
                            .patch(invokingEndpoint);
                } else {
                    response = given()
                            .config(
                                    RestAssured.config()
                                            .encoderConfig(
                                                    encoderConfig()
                                                            .encodeContentTypeAs(VAR_API_MULTIPART_FORM_DATA, ContentType.TEXT)))
                            .header(AUTHORIZATION_HEADER_NAME, accessToken)
                            .headers(headers)
                            .formParams(formParams)
                            .multiPart(fileKey1, new File(filePath1), mimeType1)
                            .when()
                            .patch(invokingEndpoint);
                }
                break;

            case 2:
                if (accessToken == null || accessToken.equals("")) {
                    response = given()
                            .config(
                                    RestAssured.config()
                                            .encoderConfig(
                                                    encoderConfig()
                                                            .encodeContentTypeAs(VAR_API_MULTIPART_FORM_DATA, ContentType.TEXT)))
                            .formParams(formParams)
                            .multiPart(fileKey1, new File(filePath1), mimeType1)
                            .multiPart(fileKey2, new File(filePath2), mimeType2)
                            .headers(headers)
                            .when()
                            .patch(invokingEndpoint);
                } else {
                    response = given()
                            .config(
                                    RestAssured.config()
                                            .encoderConfig(
                                                    encoderConfig()
                                                            .encodeContentTypeAs(VAR_API_MULTIPART_FORM_DATA, ContentType.TEXT)))
                            .header(AUTHORIZATION_HEADER_NAME, accessToken)
                            .headers(headers)
                            .formParams(formParams)
                            .multiPart(fileKey1, new File(filePath1), mimeType1)
                            .multiPart(fileKey2, new File(filePath2), mimeType2)
                            .when()
                            .patch(invokingEndpoint);
                }
                break;

            case 3:
                if (accessToken == null || accessToken.equals("")) {
                    response = given()
                            .config(
                                    RestAssured.config()
                                            .encoderConfig(
                                                    encoderConfig()
                                                            .encodeContentTypeAs(VAR_API_MULTIPART_FORM_DATA, ContentType.TEXT)))
                            .formParams(formParams)
                            .multiPart(fileKey1, new File(filePath1), mimeType1)
                            .multiPart(fileKey2, new File(filePath2), mimeType2)
                            .multiPart(fileKey3, new File(filePath3), mimeType3)
                            .headers(headers)
                            .when()
                            .patch(invokingEndpoint);
                } else {
                    response = given()
                            .config(
                                    RestAssured.config()
                                            .encoderConfig(
                                                    encoderConfig()
                                                            .encodeContentTypeAs(VAR_API_MULTIPART_FORM_DATA, ContentType.TEXT)))
                            .header(AUTHORIZATION_HEADER_NAME, accessToken)
                            .headers(headers)
                            .formParams(formParams)
                            .multiPart(fileKey1, new File(filePath1), mimeType1)
                            .multiPart(fileKey2, new File(filePath2), mimeType2)
                            .multiPart(fileKey3, new File(filePath3), mimeType3)
                            .when()
                            .patch(invokingEndpoint);
                }
                break;

            case 4:
                if (accessToken == null || accessToken.equals("")) {
                    response = given()
                            .config(
                                    RestAssured.config()
                                            .encoderConfig(
                                                    encoderConfig()
                                                            .encodeContentTypeAs(VAR_API_MULTIPART_FORM_DATA, ContentType.TEXT)))
                            .formParams(formParams)
                            .multiPart(fileKey1, new File(filePath1), mimeType1)
                            .multiPart(fileKey2, new File(filePath2), mimeType2)
                            .multiPart(fileKey3, new File(filePath3), mimeType3)
                            .multiPart(fileKey4, new File(filePath4), mimeType4)
                            .headers(headers)
                            .when()
                            .patch(invokingEndpoint);
                } else {
                    response = given()
                            .config(
                                    RestAssured.config()
                                            .encoderConfig(
                                                    encoderConfig()
                                                            .encodeContentTypeAs(VAR_API_MULTIPART_FORM_DATA, ContentType.TEXT)))
                            .header(AUTHORIZATION_HEADER_NAME, accessToken)
                            .headers(headers)
                            .formParams(formParams)
                            .multiPart(fileKey1, new File(filePath1), mimeType1)
                            .multiPart(fileKey2, new File(filePath2), mimeType2)
                            .multiPart(fileKey3, new File(filePath3), mimeType3)
                            .multiPart(fileKey4, new File(filePath4), mimeType4)
                            .when()
                            .patch(invokingEndpoint);
                }
                break;

            case 5:
                if (accessToken == null || accessToken.equals("")) {
                    response = given()
                            .config(
                                    RestAssured.config()
                                            .encoderConfig(
                                                    encoderConfig()
                                                            .encodeContentTypeAs(VAR_API_MULTIPART_FORM_DATA, ContentType.TEXT)))
                            .formParams(formParams)
                            .multiPart(fileKey1, new File(filePath1), mimeType1)
                            .multiPart(fileKey2, new File(filePath2), mimeType2)
                            .multiPart(fileKey3, new File(filePath3), mimeType3)
                            .multiPart(fileKey4, new File(filePath4), mimeType4)
                            .multiPart(fileKey5, new File(filePath5), mimeType5)
                            .headers(headers)
                            .when()
                            .patch(invokingEndpoint);
                } else {
                    response = given()
                            .config(
                                    RestAssured.config()
                                            .encoderConfig(
                                                    encoderConfig()
                                                            .encodeContentTypeAs(VAR_API_MULTIPART_FORM_DATA, ContentType.TEXT)))
                            .header(AUTHORIZATION_HEADER_NAME, accessToken)
                            .headers(headers)
                            .formParams(formParams)
                            .multiPart(fileKey1, new File(filePath1), mimeType1)
                            .multiPart(fileKey2, new File(filePath2), mimeType2)
                            .multiPart(fileKey3, new File(filePath3), mimeType3)
                            .multiPart(fileKey4, new File(filePath4), mimeType4)
                            .multiPart(fileKey5, new File(filePath5), mimeType5)
                            .when()
                            .patch(invokingEndpoint);
                }
                break;

            default:
                if (accessToken == null || accessToken.equals("")) {
                    response = given()
                            .config(
                                    RestAssured.config()
                                            .encoderConfig(
                                                    encoderConfig()
                                                            .encodeContentTypeAs(VAR_API_MULTIPART_FORM_DATA, ContentType.TEXT)))
                            .formParams(formParams)
                            .headers(headers)
                            .when()
                            .patch(invokingEndpoint);
                } else {
                    response = given()
                            .config(
                                    RestAssured.config()
                                            .encoderConfig(
                                                    encoderConfig()
                                                            .encodeContentTypeAs(VAR_API_MULTIPART_FORM_DATA, ContentType.TEXT)))
                            .formParams(formParams)
                            .header(AUTHORIZATION_HEADER_NAME, accessToken)
                            .headers(headers)
                            .when()
                            .patch(invokingEndpoint);
                }
                break;
        }

        saveStatusCode(response);
        saveApiResponseBody(response);
        printResponseTime(response);
        printResponse();
        printResponseHeaders(response);
        clearInvokedApiEndpointArtifacts();
    }
}
