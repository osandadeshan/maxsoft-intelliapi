package com.maxsoft.intelliapi.api;

import io.restassured.http.ContentType;
import io.restassured.http.Headers;
import io.restassured.response.Response;

import static com.maxsoft.intelliapi.api.ApiResponseProcessor.*;
import static com.maxsoft.intelliapi.Constants.AUTHORIZATION_HEADER_NAME;
import static io.restassured.RestAssured.given;

/**
 * Project Name    : MaxSoft-IntelliAPI
 * Developer       : Osanda Deshan
 * Version         : 1.0.0
 * Date            : 12/11/2020
 * Time            : 9:23 PM
 * Description     :
 **/

public class JsonRequestProcessor {

    public static void getApiWithAuthMultipleHeaders(String invokingEndpoint, String accessToken, Headers headers) {
        Response response;

        if (accessToken == null || accessToken.equals("")) {
            response = given()
                    .contentType(ContentType.JSON)
                    .headers(headers)
                    .when()
                    .get(invokingEndpoint);
        } else {
            response = given()
                    .contentType(ContentType.JSON)
                    .header(AUTHORIZATION_HEADER_NAME, accessToken)
                    .headers(headers)
                    .when()
                    .get(invokingEndpoint);
        }

        saveStatusCode(response);
        saveApiResponseBody(response);
        printResponseTime(response);
        printResponse();
        printResponseHeaders(response);
        clearInvokedApiEndpointArtifacts();
    }

    public static void postApiWithAuthMultipleHeaders(String invokingEndpoint, String jsonPayload, String accessToken, Headers headers) {
        Response response;

        if (accessToken == null || accessToken.equals("")) {
            response = given()
                    .contentType(ContentType.JSON)
                    .headers(headers)
                    .body(jsonPayload)
                    .when()
                    .post(invokingEndpoint);
        } else {
            response = given()
                    .contentType(ContentType.JSON)
                    .header(AUTHORIZATION_HEADER_NAME, accessToken)
                    .headers(headers)
                    .body(jsonPayload)
                    .when()
                    .post(invokingEndpoint);
        }

        saveStatusCode(response);
        saveApiResponseBody(response);
        printResponseTime(response);
        printResponse();
        printResponseHeaders(response);
        clearInvokedApiEndpointArtifacts();
    }

    public static void putApiWithAuthMultipleHeaders(String invokingEndpoint, String jsonPayload, String accessToken, Headers headers) {
        Response response;

        if (accessToken == null || accessToken.equals("")) {
            response = given()
                    .contentType(ContentType.JSON)
                    .headers(headers)
                    .body(jsonPayload)
                    .when()
                    .put(invokingEndpoint);
        } else {
            response = given()
                    .contentType(ContentType.JSON)
                    .header(AUTHORIZATION_HEADER_NAME, accessToken)
                    .headers(headers)
                    .body(jsonPayload)
                    .when()
                    .put(invokingEndpoint);
        }

        saveStatusCode(response);
        saveApiResponseBody(response);
        printResponseTime(response);
        printResponse();
        printResponseHeaders(response);
        clearInvokedApiEndpointArtifacts();
    }

    public static void patchApiWithAuthMultipleHeaders(String invokingEndpoint, String jsonPayload, String accessToken, Headers headers) {
        Response response;

        if (accessToken == null || accessToken.equals("")) {
            response = given()
                    .contentType(ContentType.JSON)
                    .headers(headers)
                    .body(jsonPayload)
                    .when()
                    .patch(invokingEndpoint);
        } else {
            response = given()
                    .contentType(ContentType.JSON)
                    .header(AUTHORIZATION_HEADER_NAME, accessToken)
                    .headers(headers)
                    .body(jsonPayload)
                    .when()
                    .patch(invokingEndpoint);
        }

        saveStatusCode(response);
        saveApiResponseBody(response);
        printResponseTime(response);
        printResponse();
        printResponseHeaders(response);
        clearInvokedApiEndpointArtifacts();
    }

    public static void deleteApiWithAuthMultipleHeaders(String invokingEndpoint, String accessToken, Headers headers) {
        Response response;

        if (accessToken == null || accessToken.equals("")) {
            response = given()
                    .contentType(ContentType.JSON)
                    .headers(headers)
                    .when()
                    .delete(invokingEndpoint);
        } else {
            response = given()
                    .contentType(ContentType.JSON)
                    .header(AUTHORIZATION_HEADER_NAME, accessToken)
                    .headers(headers)
                    .when()
                    .delete(invokingEndpoint);

            saveStatusCode(response);
            saveApiResponseBody(response);
            printResponseTime(response);
            printResponse();
            printResponseHeaders(response);
            clearInvokedApiEndpointArtifacts();
        }
    }
}
