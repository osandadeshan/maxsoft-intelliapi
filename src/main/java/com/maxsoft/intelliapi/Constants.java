package com.maxsoft.intelliapi;

import java.io.File;

/**
 * Project Name    : MaxSoft-IntelliAPI
 * Developer       : Osanda Deshan
 * Version         : 1.0.0
 * Date            : 12/7/2020
 * Time            : 7:03 PM
 * Description     :
 **/

public class Constants {

    // Environment Constants
    public static final String DEV = "dev";
    public static final String QA = "qa";
    public static final String UAT = "uat";
    public static final String PROD = "prod";
    public static final String ENVIRONMENT = System.getenv("environment");

    // Operating System/Machine Constants
    public static final String CURRENT_DIRECTORY = System.getProperty("user.dir");
    public static final String FILE_SEPARATOR = File.separator;
    public static final String OS = System.getProperty("os.name");

    // Data Store Types
    public static final String SPEC = "spec";
    public static final String SPECIFICATION = "specification";
    public static final String SCENARIO = "scenario";
    public static final String SUITE = "suite";

    // File Syntax Constants
    public static final String FILE_SYNTAX_PREFIX = "<file:";
    public static final int FILE_SYNTAX_CHARACTER_COUNT = FILE_SYNTAX_PREFIX.length();

    // API Document Constants
    public static final String VAR_API_NAME = "apiName";
    public static final String VAR_API_ENDPOINT = "apiEndpoint";
    public static final String VAR_API_HTTP_METHOD = "apiHttpMethod";
    public static final String VAR_API_REQUEST_BODY_TYPE = "apiBodyType";
    public static final String VAR_API_JSON_REQUEST_BODY = "apiJsonRequestBody";

    // Authentication Token Constants
    public static final String IS_AUTHENTICATION_REQUIRED = "Is authentication required?";
    public static final String RETRIEVE_TOKEN_FROM_TEXT_FILE = "Do you need to retrieve the access token from the text file?";
    public static final String MANUAL_TOKEN = "Provide the access token if you need to authorize the API manually";
    public static final String AUTHORIZATION_HEADER_NAME = System.getenv("header_name_for_authorization");
    public static String AUTHENTICATION_FIRST_VALUE = System.getenv("authentication_first_value");
    public static final String ACCESS_TOKEN_FILE_PATH = CURRENT_DIRECTORY + FILE_SEPARATOR + System.getenv("access_token_file_path");

    // Form-Data Constants
    public static final String VAR_API_FORM_DATA_KEYS_LIST = "keysList";
    public static final String VAR_API_FORM_DATA_VALUES_LIST = "valuesList";
    public static final String VAR_API_MULTIPART_FORM_DATA = "multipart/form-data";
    public static final String VAR_API_FORM_DATA_MULTIPART_FILE_KEY = "fileKey";
    public static final String VAR_API_FORM_DATA_MULTIPART_FILE_PATH = "filePath";
    public static final String VAR_API_FORM_DATA_MULTIPART_MIME_TYPE = "mimeType";
    public static final String VAR_API_FORM_DATA_MULTIPART_FILES_COUNT = "noOfRows";

    // API Payload Constants
    public static final String VAR_API_HEADER_NAMES_LIST = "headersNamesList";
    public static final String VAR_API_HEADER_VALUES_LIST = "headersValuesList";
    public static final String VAR_API_QUERY_PARAMS = "queryParams";
    public static final String VAR_API_PATH_PARAMS = "pathParams";

    // API Response Constants
    public static final String VAR_API_RESPONSE_STATUS_CODE = "statusCode";
    public static final String VAR_API_RESPONSE_BODY = "response";

    // MySQL Constants
    public static final String MYSQL_DRIVER = "com.mysql.jdbc.Driver";
    public static final String MYSQL_DATABASE_URL = System.getenv("mysql_database_url");
    public static final String MYSQL_USERNAME = "username";
    public static final String MYSQL_PASSWORD = "password";
    public static final String MYSQL_DATABASE_NAME = "databaseName";
    public static final String MYSQL_QUERY = "query";

    // Mongo Constants
    public static final String MONGO_DB_SERVER_HOST = System.getenv("mongo_database_host");
    public static final int MONGO_DB_PORT = Integer.parseInt(System.getenv("mongo_database_port"));
    public static final String MONGO_DATABASE_NAME = "databaseName";
    public static final String MONGO_COLLECTION_NAME = "collectionName";
    public static final String IS_MONGO_NEED_AUTHENTICATION = "Is authentication credentials required?";
    public static final String MONGO_USERNAME = "Username";
    public static final String MONGO_SOURCE = "Source";
    public static final String MONGO_PASSWORD = "Password";

    // Random Data Generation Constants
    public static final String FIRST_NAME = "firstname";
    public static final String LAST_NAME = "lastname";
    public static final String FULL_NAME = "fullname";
    public static final String ADDRESS = "address";
}
