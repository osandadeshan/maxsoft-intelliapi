# Data Store Comparison Specification

Project Name : MaxSoft-IntelliAPI
Developer    : Osanda Deshan
Version      : 1.0.0
Date         : 12/24/2020
Time         : 10:21 AM
Description  : This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.

tags: data_store, regression


* Given that a user needs to invoke "Create a user"
* And the user set the request payload as follows <file:./src/test/resources/payloads/create_a_user.txt>
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
   |Scenario      |varStatusCode|$.code            |
* And the JSON Path Assertions for the response should be equal to the values inside the data stores

   |JSON Path   |Is Data Store Used?|Data Store Type|Data Store Variable Name|Expected Value  |
   |------------|-------------------|---------------|------------------------|----------------|
   |$.code      |no                 |               |                        |201             |
   |$.data.email|no                 |               |                        |osa92@google.com|
* And the user saves the values inside data stores as follows

   |DataStore Type|Variable Name |Value To Be Stored|
   |--------------|--------------|------------------|
   |Scenario      |username      |osanda12          |
   |Scenario      |mobileUserName|osanda12          |


## Equality of data store values with hard coded values

* And the values inside the data stores equal to the following

   |DataStore Type|Variable Name|Expected Value|
   |--------------|-------------|--------------|
   |Scenario      |username     |osanda12      |
   |Scenario      |varStatusCode|201           |


## Equality of data store values with another data store values

* And the values inside two data stores should be equal

   |DataStore 1 Type|Variable 1 Name|DataStore 2 Type|Variable 2 Name|
   |----------------|---------------|----------------|---------------|
   |Scenario        |username       |Scenario        |mobileUserName |


## Inequality of data store values with hard coded values

* And the values inside the data stores not equal to the following

   |DataStore Type|Variable Name|Expected Value|
   |--------------|-------------|--------------|
   |Scenario      |username     |osanda        |
   |Scenario      |varStatusCode|succes        |


## Inequality of data store values with another data store values

* And the values inside two data stores should not be equal

   |DataStore 1 Type|Variable 1 Name|DataStore 2 Type|Variable 2 Name|
   |----------------|---------------|----------------|---------------|
   |Scenario        |username       |Scenario        |varStatusCode  |


## Contains of data store values with hard coded values

* And the values inside the data stores contain the following

   |DataStore Type|Variable Name|Expected Value|
   |--------------|-------------|--------------|
   |Scenario      |username     |osanda        |
   |Scenario      |varStatusCode|20            |


## Contains of data store values with another data store values

* And the value inside a data store should contain the value of the other data store

   |DataStore 1 Type|Variable 1 Name|DataStore 2 Type|Variable 2 Name|
   |----------------|---------------|----------------|---------------|
   |Scenario        |username       |Scenario        |mobileUserName |


## Not contains of data store values with hard coded values

* And the values inside the data stores not contain the following

   |DataStore Type|Variable Name|Expected Value|
   |--------------|-------------|--------------|
   |Scenario      |username     |deshan        |
   |Scenario      |varStatusCode|fail          |


## Not contains of data store values with another data store values

* And the value inside a data store should not contain the value of the other data store

   |DataStore 1 Type|Variable 1 Name|DataStore 2 Type|Variable 2 Name|
   |----------------|---------------|----------------|---------------|
   |Scenario        |username       |Scenario        |varStatusCode  |


_______________________________________________________________________________
* Delete a user by userId saved in "Scenario" type data store named "varUserId"
