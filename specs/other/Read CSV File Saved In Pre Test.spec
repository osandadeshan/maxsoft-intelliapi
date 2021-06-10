# Read CSV File Saved In Pre Test Specification

Project Name    : MaxSoft-IntelliAPI
Developer       : Osanda Deshan
Version         : 1.0.0
Date            : 28/04/2019
Time            : 19:36
Description     : This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.

tags: csv, regression

table: ./src/test/resources/csv/userIds.csv


## Delete users by uderId which was saved in a CSV file from the pre test

* Given that a user needs to invoke "Delete a user"
* And the user set the request authentication configurations as follows

   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |Yes                |
   |Do you need to retrieve the access token from the text file?      |Yes                |
   |Provide the access token if you need to authorize the API manually|N/A                |
* And the user set the path parameters as follows

   |Path Parameter|Path Value|
   |--------------|----------|
   |userId        |<userId>  |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following

   |JSON Path|Expected Result|
   |---------|---------------|
   |$.code   |204            |
