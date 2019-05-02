# Form-Data Example Specification

Project Name : MaxSoft-IntelliAPI
Developer    : Osanda Deshan
Version      : 1.0.0
Date         : 6/2/2018
Time         : 3:02 PM
Description  : This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.



## Get Google OAuth Access token

* Given that a user needs to invoke "Get OAuth Access Token from Refresh Token"
* And the user set the form-data key value pairs as follows 

   |Key          |Value                      |
   |-------------|---------------------------|
   |grant_type   |refresh_token              |
   |client_id    |<file:C:/client_id.txt>    |
   |client_secret|<file:C:/client_secret.txt>|
   |refresh_token|<file:C:/refresh_token.txt>|
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following 

   |JSON Path   |Expected Result|
   |------------|---------------|
   |$.expires_in|3600           |
   |$.token_type|Bearer         |



## Upload file

* Create a deck
* And save the JSON Path values in the response inside the data stores 

   |DataStore Type|Variable Name|Value To Be Stored|
   |--------------|-------------|------------------|
   |Scenario      |varDeckId    |$.id              |

* Given that a user needs to invoke "File Upload"
* And the user set the request authentication configurations as follows 

   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |Yes                |
   |Do you need to retrieve the access token from the text file?      |Yes                |
   |Provide the access token if you need to authorize the API manually|N/A                |
* And the user set the form-data key value pairs using data stores as follows 

   |Key            |Is Data Store Used?|Data Store Type|Data Store Variable Name|Value    |
   |---------------|-------------------|---------------|------------------------|---------|
   |title          |n                  |               |                        |DOCX file|
   |creatorId      |n                  |               |                        |tester1  |
   |creatorPlatform|n                  |               |                        |Web      |
   |creatoredSource|n                  |               |                        |File     |
   |creatoredType  |n                  |               |                        |Auto     |
   |deckId         |y                  |Scenario       |varDeckId               |         |
   |isExpert       |n                  |               |                        |false    |
   |examDate       |n                  |               |                        |         |
   |userId         |n                  |               |                        |tester1  |
* And the user set the multipart file key value pairs as follows 

   |Key |File Path                            |Mime Type                                                              |
   |----|-------------------------------------|-----------------------------------------------------------------------|
   |file|/resources/docx_files/DOCX file1.docx|application/vnd.openxmlformats-officedocument.wordprocessingml.document|
* When the user invokes the API
* Then the status code for the request is "201"
* And the JSON Path Assertions for the response should be equal to the following 

   |JSON Path |Expected Result|
   |----------|---------------|
   |$.length()|15             |

* Delete deck by deckId saved in "Scenario" type data store named "varDeckId"
