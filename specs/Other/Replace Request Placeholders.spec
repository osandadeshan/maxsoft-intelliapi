# Replace Request Placeholders Specification

Project Name : MaxSoft-IntelliAPI
Developer    : Osanda Deshan
Version      : 1.0.0
Date         : 9/8/2018
Time         : 11:32 AM
Description  : This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.



## Saving values to Data Store

* And the user saves the values inside data stores as follows 

   |DataStore Type|Variable Name|Value To Be Stored|
   |--------------|-------------|------------------|
   |Scenario      |username     |Osanda12          |
   |Specification |username     |Osanda12          |
   |Specification |password     |Password1         |



## Replace request placeholders from values

* Given that a user needs to invoke "Get Auth Token"
* And the user set the request payload as follows <file:/resources/payloads/login_placeholders.txt>
* And the user set values to the request payload placeholders as follows 

   |Attribute Value In JSON Template|Attribute Value To Be Set|
   |--------------------------------|-------------------------|
   |#username                       |osanda12                 |
   |#password                       |Password1                |
* When the user invokes the API
* Then the status code for the request is "201"
* And the JSON Path Assertions for the response should be equal to the following 

   |JSON Path|Expected Result|
   |---------|---------------|
   |$.status |success        |



## Replace one request placeholders from values

* Given that a user needs to invoke "Get Auth Token"
* And the user set the request payload as follows <file:/resources/payloads/login_placeholder.txt>
* And the user set values to the request payload placeholders as follows 

   |Attribute Value In JSON Template|Attribute Value To Be Set|
   |--------------------------------|-------------------------|
   |#username                       |osanda12                 |
* When the user invokes the API
* Then the status code for the request is "201"
* And the JSON Path Assertions for the response should be equal to the following 

   |JSON Path|Expected Result|
   |---------|---------------|
   |$.status |success        |



## Replace request placeholders from data store values

* Given that a user needs to invoke "Get Auth Token"
* And the user set the request payload as follows <file:/resources/payloads/login_placeholders.txt>
* And the user set values to the request payload placeholders using data stores as follows 

   |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name|Attribute Value To Be Set|
   |--------------------------------|-------------------|---------------|------------------------|-------------------------|
   |#username                       |y                  |spec           |username                |                         |
   |#password                       |y                  |spec           |password                |                         |
* When the user invokes the API
* Then the status code for the request is "201"
* And the JSON Path Assertions for the response should be equal to the following 

   |JSON Path|Expected Result|
   |---------|---------------|
   |$.status |success        |



## Replace one request placeholder from data store values

* Given that a user needs to invoke "Get Auth Token"
* And the user set the request payload as follows <file:/resources/payloads/login_placeholders.txt>
* And the user set values to the request payload placeholders using data stores as follows 

   |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name|Attribute Value To Be Set|
   |--------------------------------|-------------------|---------------|------------------------|-------------------------|
   |#username                       |y                  |spec           |username                |                         |
   |#password                       |n                  |               |                        |Password1                |
* When the user invokes the API
* Then the status code for the request is "201"
* And the JSON Path Assertions for the response should be equal to the following 

   |JSON Path|Expected Result|
   |---------|---------------|
   |$.status |success        |
