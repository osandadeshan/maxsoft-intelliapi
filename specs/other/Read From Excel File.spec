# Read From Excel File Specification

Project Name : MaxSoft-IntelliAPI
Developer    : Osanda Deshan
Version      : 1.0.0
Date         : 6/17/2018
Time         : 2:06 PM
Description  : This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.

tags: excel, regression


## Invoke Create a user API using the test data in excel file

* Given that a user needs to invoke "Create a user"
* And the user saves test data inside excel file into data stores

   |DataStore Type|Variable Name|Excel Sheet Name|Key Name|
   |--------------|-------------|----------------|--------|
   |Scenario      |varName      |User_Test_Data  |name    |
   |Scenario      |varGender    |User_Test_Data  |gender  |
   |Scenario      |varStatus    |User_Test_Data  |status  |
* And generate random email and save it in a data store as follows

   |Data Store Type|Data Store Variable Name|Domain Name   |
   |---------------|------------------------|--------------|
   |Scenario       |varEmail                |mailinator.com|
* And the user set the request attributes using data stores as follows

   |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name|Attibute Value To Be Set|
   |--------------------------------|-------------------|---------------|------------------------|------------------------|
   |#email                          |yes                |Scenario       |varEmail                |                        |
   |#name                           |yes                |Scenario       |varName                 |                        |
   |#gender                         |yes                |Scenario       |varGender               |                        |
   |#status                         |yes                |Scenario       |varStatus               |                        |
* And the user set the request authentication configurations as follows

   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |Yes                |
   |Do you need to retrieve the access token from the text file?      |Yes                |
   |Provide the access token if you need to authorize the API manually|N/A                |
* When the user invokes the API
* Then the status code for the request is "200"
* And save the JSON Path values in the response inside the data stores

   |DataStore Type|Variable Name|Value To Be Stored|
   |--------------|-------------|------------------|
   |Scenario      |varUserId    |$.data.id         |
* And the JSON Path Assertions for the response should be equal to the values inside the data stores

   |JSON Path   |Is Data Store Used?|Data Store Type|Data Store Variable Name|Expected Value|
   |------------|-------------------|---------------|------------------------|--------------|
   |$.code      |no                 |               |                        |201           |
   |$.data.name |yes                |Scenario       |varName                 |              |
   |$.data.email|yes                |Scenario       |varEmail                |              |
* Delete a user by userId saved in "Scenario" type data store named "varUserId"
