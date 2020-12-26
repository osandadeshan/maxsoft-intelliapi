# Saving And Reading Values From Data Stores Specification

Project Name : MaxSoft-IntelliAPI
Developer    : Osanda Deshan
Version      : 1.0.0
Date         : 12/24/2020
Time         : 10:52 AM
Description  : This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.

tags: data_store, regression


## Get configurations of the testing environment

* Configurations of the testing environment


## Saving values to Data Store

* And the user saves the values inside data stores as follows 
   |DataStore Type|Variable Name|Value To Be Stored |
   |--------------|-------------|-------------------|
   |Scenario      |variable1    |Osanda Deshan      |
   |Specification |variable2    |Osanda Nimalarathna|
   |Scenario      |variable3    |Software Automation|
   |Specification |variable6    |Osa                |
* And the user saves the values inside data stores as follows
   |DataStore Type|Variable Name|Value To Be Stored|
   |--------------|-------------|------------------|
   |Specification |varName      |Osanda            |
   |Specification |varGender    |Male              |
   |Specification |varStatus    |Active            |


## Reading values from Data Store

* And the user read the values from data stores as follows 
   |DataStore Type|Variable Name|
   |--------------|-------------|
   |Scenario      |variable1    |
   |Specification |variable2    |
   |Scenario      |variable3    |


## Invoke Create user API using valid payload text file

* Given that a user needs to invoke "Create a user"
* And the user set the request authentication configurations as follows
   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |Yes                |
   |Do you need to retrieve the access token from the text file?      |Yes                |
   |Provide the access token if you need to authorize the API manually|N/A                |
* And the user set the request payload as follows <file:./src/test/resources/payloads/create_a_user_with_all_fields.txt>
* And generate random email and save it in a data store as follows
   |Data Store Type|Data Store Variable Name|Domain Name     |
   |---------------|------------------------|----------------|
   |Scenario       |varEmail                |mailinator.com  |
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
* And the JSON Path Existence in the response should be equal to the following 
   |JSON Path|isExists|
   |---------|--------|
   |$.code   |true    |
   |$.osa    |false   |
* And save the JSON Path values in the response inside the data stores 
   |DataStore Type|Variable Name|Value To Be Stored|
   |--------------|-------------|------------------|
   |Scenario      |variable4    |$.code            |
   |Specification |variable5    |$.data.name       |
* And the user read the values from data stores as follows 
   |DataStore Type|Variable Name|
   |--------------|-------------|
   |Scenario      |variable4    |
   |Specification |variable5    |
* And the JSON Path values of the response should contains the following
   |JSON Path   |isContains|
   |------------|----------|
   |$.data.name |Osa       |
* And the JSON Path values of the response should contains the values inside the data stores
   |JSON Path  |Is Data Store Used?|Data Store Type|Data Store Variable Name|Expected Value|
   |-----------|-------------------|---------------|------------------------|--------------|
   |$.data.name|y                  |Specification  |variable6               |              |
* And the JSON Path values of the response should not contains the following
   |JSON Path  |notContains|
   |-----------|-----------|
   |$.data.name|Deshan     |
* And the JSON Path values of the response should not contains the values inside the data stores
   |JSON Path  |Is Data Store Used?|Data Store Type|Data Store Variable Name|Expected Value|
   |-----------|-------------------|---------------|------------------------|--------------|
   |$.data.name|y                  |Specification  |variable2               |              |
* And the JSON Path Assertions for the response should be equal to the following
   |JSON Path  |Expected Result|
   |-----------|---------------|
   |$.data.name|Osanda         |
* And the JSON Path Assertions for the response should not be equal to the following
   |JSON Path  |Expected Result|
   |-----------|---------------|
   |$.data.name|Deshan         |
* And the JSON Path Assertions for the response should be equal to the values inside the data stores
   |JSON Path  |Is Data Store Used?|Data Store Type|Data Store Variable Name|Expected Value|
   |-----------|-------------------|---------------|------------------------|--------------|
   |$.data.name|y                  |Specification  |varName                 |              |
   |$.code     |n                  |               |                        |201           |
* And the JSON Path Assertions for the response should not be equal to the values inside the data stores
   |JSON Path     |Is Data Store Used?|Data Store Type|Data Store Variable Name|Expected Value|
   |--------------|-------------------|---------------|------------------------|--------------|
   |$.data.name   |y                  |Specification  |varGender               |              |
   |$.data.status |n                  |               |                        |Inactive      |
* And the JSON Path Existence in the response should be equal to the following
   |JSON Path     |isExists|
   |--------------|--------|
   |$.data.status |true    |
   |$.osa         |false   |
