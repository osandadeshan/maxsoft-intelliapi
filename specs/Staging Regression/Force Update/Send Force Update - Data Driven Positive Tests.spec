Send Force Update - Data Driven Positive Tests Specification
============================================================
Date Created    : 03/06/2018
Version         : 1.0.0
Owner      	    : Osanda Deshan
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.


tags: force_update, force_update-positive_tests, positive


table: /resources/data_driven_test_csv/send_force_update/send_force_update.csv



* Given that a user needs to invoke <api>
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set               |
     |--------------------------------|----------------------------------------|
     |#version                        |<version>                               |
     |#androidVersionCode             |<androidVersionCode>                    |
     |#appName                        |<appName>                               |
     |#platform                       |<platform>                              |
     |#allowforceUpdate               |<allowforceUpdate>                      |
* When the user invokes the API
* Then the status code for the request is "201"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                          |Value                                   |
     |-----------------------------------|----------------------------------------|
     |$.status                           |Success                                 |
     |$.code                             |201                                     |
     |$.message.n                        |1                                       |
     |$.message.ok                       |1                                       |



Get a force update to mobile app
--------------------------------
* Given that a user needs to invoke "Get Force Update Latest Version"
*  And the user set the query parameters as follows
     |Query Parameter|Query Value                     |
     |---------------|--------------------------------|
     |appName        |<appName>                       |
     |platform       |<platform>                      |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                          |Value                                   |
     |-----------------------------------|----------------------------------------|
     |$.appName                          |<appName>                               |
     |$.platform                         |<platform>                              |
     |$.forceUpdate                      |<allowforceUpdate>                      |