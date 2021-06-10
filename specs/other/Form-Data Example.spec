# Form-Data Example Specification

Project Name : MaxSoft-IntelliAPI
Developer    : Osanda Deshan
Version      : 1.0.0
Date         : 6/2/2018
Time         : 3:02 PM
Description  : This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.

tags: form_data, regression


## Get Google OAuth Access token

* Given that a user needs to invoke "Get oauth access token from refresh token"
* And the user set the form-data key value pairs using data stores as follows

   |Key          |Is Data Store Used?|Data Store Type|Data Store Variable Name|Value                                                 |
   |-------------|-------------------|---------------|------------------------|------------------------------------------------------|
   |grant_type   |no                 |               |                        |refresh_token                                         |
   |client_id    |no                 |               |                        |540975095521-nb0mhgret5drjc.apps.googleusercontent.com|
   |client_secret|no                 |               |                        |D1z3sdgsgsdgBF-0sgsgsdgsdg                            |
   |refresh_token|no                 |               |                        |1//0glZRx4PeVuDvCgYIARAAGBASNwF-L9IrQc4XYnC-WH        |
* When the user invokes the API
* Then the status code for the request is "401"
* And the JSON Path Assertions for the response should be equal to the following

   |JSON Path          |Expected Result                |
   |-------------------|-------------------------------|
   |$.error            |invalid_client                 |
   |$.error_description|The OAuth client was not found.|


## Upload file

* Given that a user needs to invoke "File upload"
* And the user set the multipart file key value pairs as follows

   |Key     |File Path                                        |Mime Type                                                        |
   |--------|-------------------------------------------------|-----------------------------------------------------------------|
   |filename|/src/test/resources/api_document/dev_api_doc.xlsx|application/vnd.openxmlformats-officedocument.spreadsheetml.sheet|
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Existence in the response should be equal to the following

   |JSON Path |isExists|
   |----------|--------|
   |$.FileId  |true    |
   |$.FileSize|false   |
* And the JSON Path Assertions for the response should be equal to the following

   |JSON Path |Expected Result |
   |----------|----------------|
   |$.FileName|dev_api_doc.xlsx|
   |$.FileExt |xlsx            |
