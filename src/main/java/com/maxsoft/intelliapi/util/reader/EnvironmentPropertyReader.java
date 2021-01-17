package com.maxsoft.intelliapi.util.reader;

import java.security.InvalidParameterException;

import static com.maxsoft.intelliapi.common.Constants.*;

/**
 * Project Name    : MaxSoft-IntelliAPI
 * Developer       : Osanda Deshan
 * Version         : 1.0.0
 * Date            : 12/17/2020
 * Time            : 8:18 PM
 * Description     :
 **/

public class EnvironmentPropertyReader {

    public static String getBaseUrl() {
        String baseUrl;

        if (ENVIRONMENT == null) {
            throw new NullPointerException("Please add \"environment\" in the environment property file " +
                    "and assign an environment QA|DEV|UAT|PROD");
        }

        switch (ENVIRONMENT.toLowerCase()) {
            case DEV:
                baseUrl = System.getenv("dev_environment_base_url");
                break;
            case QA:
                baseUrl = System.getenv("qa_environment_base_url");
                break;
            case UAT:
                baseUrl = System.getenv("uat_environment_base_url");
                break;
            case PROD:
                baseUrl = System.getenv("prod_environment_base_url");
                break;
            default:
                throw new InvalidParameterException("Please assign an valid environment QA|DEV|UAT|PROD for " +
                        "\"environment\" in the environment property file");
        }

        if (baseUrl == null) {
            baseUrl = "";
        }
        return baseUrl;
    }

    public static String getApiDocumentFilePath() {
        String apiDocPath;

        if (ENVIRONMENT == null) {
            throw new NullPointerException("Please add \"environment\" in the property file " +
                    "and assign an environment QA|DEV|UAT|PROD");
        }

        switch (ENVIRONMENT.toLowerCase()) {
            case DEV:
                apiDocPath = System.getenv("dev_api_document_path");
                break;
            case QA:
                apiDocPath = System.getenv("qa_api_document_path");
                break;
            case UAT:
                apiDocPath = System.getenv("uat_api_document_path");
                break;
            case PROD:
                apiDocPath = System.getenv("prod_api_document_path");
                break;
            default:
                throw new InvalidParameterException("Please assign an valid environment QA|DEV|UAT|PROD for " +
                        "\"environment\" in the property file");
        }

        if (apiDocPath == null) {
            apiDocPath = "";
        }
        return CURRENT_DIRECTORY + FILE_SEPARATOR + apiDocPath;
    }
}
