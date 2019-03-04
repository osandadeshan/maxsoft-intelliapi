# Run GET API using Endpoint in Data Store Specification

<pre>
Project Name    : MaxSoft-IntelliAPI
Developer       : Osanda Deshan
Version         : 1.0.0
Date            : 04/03/2019
Time            : 21:45
Description     : This is an executable specification file
</pre>


    
## Run GET API using Endpoint in Data Store
* Given that a user needs to invoke "Get Staging PI Token"
* And the user set the request payload as follows <file:/resources/payloads/login.txt>
* When the user invokes the API
* Then the status code for the request is "201"
* And the JSON Path Assertions for the response should be equal to the following

   |JSON Path|Expected Result|
   |---------|---------------|
   |$.status |success        |
* And save the access token in the response which is located inside the JSON Path of "$.data"

* And the user saves the values inside data stores as follows

   |DataStore Type|Variable Name       |Value To Be Stored                                                                                                          |
   |--------------|--------------------|----------------------------------------------------------------------------------------------------------------------------|
   |Scenario      |invokingEndpoint    |http://aggregationservice-pearson-prep-us1-stg-blue.bite.pearsondev.tech/api/questions?deckId=5badc2027246d600100fe269      |

* Given that a user needs to invoke GET API using data stores

   |DataStore Type|Variable Name      |
   |--------------|-------------------|
   |Scenario      |invokingEndpoint   |
* And the user set the request authentication configurations as follows

   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |Yes                |
   |Do you need to retrieve the access token from the text file?      |Yes                |
   |Provide the access token if you need to authorize the API manually|N/A                |
* When the user invokes GET API

   |DataStore Type|Variable Name      |
   |--------------|-------------------|
   |Scenario      |invokingEndpoint   |
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following

   |JSON Path   |Expected Result|
   |------------|---------------|
   |$.questions |[]             |