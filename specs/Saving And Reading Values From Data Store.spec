Saving And Reading Values From Data Store Specification
=======================================================
Date Created    : 01/07/2018
Version   		: 1.0.0
Owner      		: Osanda Deshan
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.



Saving values to Data Store
---------------------------
* And the user save the values inside data stores as follows
    |DataStore Type |Variable Name  |Value To Be Stored     |
    |---------------|---------------|-----------------------|
    |Scenario       |variable1      |Osanda Deshan          |
    |Specification  |variable2      |Osanda Nimalarathna    |
    |Scenario       |variable3      |Software Automation    |



Reading values from Data Store
------------------------------
* And the user read the values from data stores as follows
    |DataStore Type |Variable Name  |
    |---------------|---------------|
    |Scenario       |variable1      |
    |Specification  |variable2      |
    |Scenario       |variable3      |



Invoke PI API in Staging Environment using valid username and password
----------------------------------------------------------------------
tags: get_pi_token, staging

* Given that a user needs to invoke "Get Staging PI Token"
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |No                             |
     |Do you need to retrieve the access token from the text file?      |N/A                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |
* And the user set the request payload as follows <file:/resources/payloads/login.txt>
* When the user invokes the API
* Then the status code for the request is "201"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path     |Expected Result|
     |--------------|---------------|
     |$.status      |success        |
* And the JSON Path Existence in the response should be equal to the following
     |JSON Path     |isExists       |
     |--------------|---------------|
     |$.status      |true           |
     |$.fuck        |false          |
* And save the access token in the response which is located inside the JSON Path of "$.data"
* And save the JSON Path values in the response inside the data stores
    |DataStore Type |Variable Name  |Value To Be Stored     |
    |---------------|---------------|-----------------------|
    |Scenario       |variable1      |$.status               |
    |Specification  |variable2      |$.data                 |
* And the user read the values from data stores as follows
    |DataStore Type |Variable Name  |
    |---------------|---------------|
    |Scenario       |variable1      |
    |Specification  |variable2      |



Invoke PI API in Staging Environment using valid username and password and save the access token inside the text file
---------------------------------------------------------------------------------------------------------------------
tags: get_pi_token, staging

* Given that a user needs to invoke "Get Staging PI Token"
* And the user save the values inside data stores as follows
    |DataStore Type |Variable Name  |Value To Be Stored     |
    |---------------|---------------|-----------------------|
    |Scenario       |username       |osanda12               |
    |Specification  |variable2      |Osanda Nimalarathna    |
    |Scenario       |variable3      |Software Automation    |
* And the user set the request attributes using data stores as follows
    |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name|Attribute Value To Be Set|
    |--------------------------------|-------------------|---------------|------------------------|-------------------------|
    |#username                       |y                  |scenario       |username                |N/A                      |
    |#password                       |n                  |N/A            |N/A                     |Password1                |
* When the user invokes the API
* Then the status code for the request is "201"
* And the JSON Path values of the response should contains the following
     |JSON Path     |isContains     |
     |--------------|---------------|
     |$.status      |success        |
* And the JSON Path values of the response should not contains the following
     |JSON Path     |notContains    |
     |--------------|---------------|
     |$.status      |fail           |
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path     |Expected Result|
     |--------------|---------------|
     |$.status      |success        |
* And the JSON Path Assertions for the response should not be equal to the following
     |JSON Path     |Expected Result|
     |--------------|---------------|
     |$.status      |fail           |
* And save the JSON Path values in the response inside the data stores
    |DataStore Type |Variable Name  |Value To Be Stored     |
    |---------------|---------------|-----------------------|
    |Scenario       |status         |$.status               |
* And the JSON Path Assertions for the response should be equal to the values inside the data stores
    |JSON Path      |Is Data Store Used?|Data Store Type|Data Store Variable Name|Expected Value |
    |---------------|-------------------|---------------|------------------------|---------------|
    |$.status       |y                  |scenario       |status                  |N/A            |
    |$.status       |n                  |N/A            |N/A                     |success        |
* And the JSON Path Assertions for the response should not be equal to the values inside the data stores
    |JSON Path      |Is Data Store Used?|Data Store Type|Data Store Variable Name|Expected Value |
    |---------------|-------------------|---------------|------------------------|---------------|
    |$.status       |n                  |N/A            |N/A                     |fail           |
* And save the access token in the response which is located inside the JSON Path of "$.data"
* And the JSON Path Existence in the response should be equal to the following
     |JSON Path     |isExists       |
     |--------------|---------------|
     |$.status      |true           |
     |$.fuck        |false          |
* And the user set the query parameters using data stores as follows
    |Query Name     |Is Data Store Used?|Data Store Type|Data Store Variable Name|Query Value|
    |---------------|-------------------|---------------|------------------------|-----------|
    |username       |y                  |scenario       |username                |N/A        |
    |password       |n                  |N/A            |N/A                     |Password1  |
* And the user set the path parameters using data stores as follows
    |Path Name      |Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value |
    |---------------|-------------------|---------------|------------------------|-----------|
    |#username      |y                  |scenario       |username                |N/A        |
    |#password      |n                  |N/A            |N/A                     |Password1  |