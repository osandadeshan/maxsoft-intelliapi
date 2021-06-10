# Replace Request Placeholders Specification

Project Name : MaxSoft-IntelliAPI
Developer    : Osanda Deshan
Version      : 1.0.0
Date         : 9/8/2018
Time         : 11:32 AM
Description  : This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.

tags: request_placeholders, regression


## Saving values to Data Store

* And the user saves the values inside data stores as follows

   |DataStore Type|Variable Name|Value To Be Stored|
   |--------------|-------------|------------------|
   |Specification |varName      |Osanda            |
   |Specification |varGender    |Male              |
   |Specification |varStatus    |Active            |


## Replace all request placeholders in a text file from data store values

* Given that a user needs to invoke "Create a user"
* And the user set the request authentication configurations as follows

   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |Yes                |
   |Do you need to retrieve the access token from the text file?      |Yes                |
   |Provide the access token if you need to authorize the API manually|N/A                |
* And the user set the request payload as follows <file:./src/test/resources/payloads/create_a_user_with_all_fields.txt>
* And generate random email and save it in a data store as follows

   |Data Store Type|Data Store Variable Name|Domain Name   |
   |---------------|------------------------|--------------|
   |Scenario       |varEmail                |mailinator.com|
* And the user set the request attributes using data stores as follows

   |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name|Attibute Value To Be Set|
   |--------------------------------|-------------------|---------------|------------------------|------------------------|
   |#email                          |yes                |Scenario       |varEmail                |                        |
   |#name                           |yes                |Specification  |varName                 |                        |
   |#gender                         |yes                |Specification  |varGender               |                        |
   |#status                         |yes                |Specification  |varStatus               |                        |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the values inside the data stores

   |JSON Path    |Is Data Store Used?|Data Store Type|Data Store Variable Name|Expected Value|
   |-------------|-------------------|---------------|------------------------|--------------|
   |$.code       |no                 |               |                        |201           |
   |$.data.name  |yes                |Specification  |varName                 |              |
   |$.data.email |yes                |Scenario       |varEmail                |              |
   |$.data.gender|yes                |Specification  |varGender               |              |


## Replace one request placeholder in a text file from a data store value

* Given that a user needs to invoke "Create a user  (JSON request from text file)"
* And the user set the request authentication configurations as follows

   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |Yes                |
   |Do you need to retrieve the access token from the text file?      |Yes                |
   |Provide the access token if you need to authorize the API manually|N/A                |
* And the user set the request payload as follows <file:./src/test/resources/payloads/create_a_user_with_email.txt>
* And generate random email and save it in a data store as follows

   |Data Store Type|Data Store Variable Name|Domain Name   |
   |---------------|------------------------|--------------|
   |Scenario       |varEmail                |mailinator.com|
* And the user set the request attributes using data stores as follows

   |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name|Attibute Value To Be Set|
   |--------------------------------|-------------------|---------------|------------------------|------------------------|
   |#email                          |yes                |Scenario       |varEmail                |                        |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the values inside the data stores

   |JSON Path    |Is Data Store Used?|Data Store Type|Data Store Variable Name|Expected Value|
   |-------------|-------------------|---------------|------------------------|--------------|
   |$.code       |no                 |               |                        |201           |
   |$.data.name  |no                 |               |                        |Tester2       |
   |$.data.email |yes                |Scenario       |varEmail                |              |
   |$.data.gender|no                 |               |                        |Female        |
   |$.data.status|no                 |               |                        |Inactive      |


## Replace two request placeholders in API document from text file values

* Given that a user needs to invoke "Create a user"
* And the user set the request authentication configurations as follows

   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |Yes                |
   |Do you need to retrieve the access token from the text file?      |Yes                |
   |Provide the access token if you need to authorize the API manually|N/A                |
* And generate random email and save it in a data store as follows

   |Data Store Type|Data Store Variable Name|Domain Name   |
   |---------------|------------------------|--------------|
   |Scenario       |varEmail                |mailinator.com|
* And the user set the request attributes using data stores as follows

   |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name|Attibute Value To Be Set                       |
   |--------------------------------|-------------------|---------------|------------------------|-----------------------------------------------|
   |#email                          |yes                |Scenario       |varEmail                |                                               |
   |#name                           |yes                |Specification  |varName                 |                                               |
   |#gender                         |n                  |               |                        |<file:./src/test/resources/payloads/gender.txt>|
   |#status                         |n                  |               |                        |<file:./src/test/resources/payloads/status.txt>|
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the values inside the data stores

   |JSON Path    |Is Data Store Used?|Data Store Type|Data Store Variable Name|Expected Value|
   |-------------|-------------------|---------------|------------------------|--------------|
   |$.code       |no                 |               |                        |201           |
   |$.data.name  |yes                |Specification  |varName                 |              |
   |$.data.email |yes                |Scenario       |varEmail                |              |
   |$.data.gender|yes                |Specification  |varGender               |              |


## Replace API Endpoint placeholders

* Given that a user needs to invoke "Get metrics"
* And the user saves the values inside data stores as follows

   |DataStore Type|Variable Name|Value To Be Stored|
   |--------------|-------------|------------------|
   |Scenario      |version      |v2                |
   |Scenario      |jsonFile     |metrics.json      |
* And the user set values to the API endpoint placeholders using data stores as follows

   |Placeholder In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name|Replacement Text|
   |----------------------------|-------------------|---------------|------------------------|----------------|
   |#version                    |n                  |               |                        |v2              |
   |#jsonFile                   |y                  |Scenario       |jsonFile                |                |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Existence in the response should be equal to the following

   |JSON Path     |isExists?|
   |--------------|---------|
   |$.numAPIs     |true     |
   |$.numEndpoints|true     |
   |$.numSpecs    |true     |
