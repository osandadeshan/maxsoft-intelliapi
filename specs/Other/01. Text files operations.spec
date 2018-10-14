# Text Files Operations Specification
Project Name : MaxSoft-IntelliAPI
Developer    : Osanda Deshan
Version      : 1.0.0
Date         : 6/17/2018
Time         : 2:06 PM
Description  : This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.



## Invoke PI API in Staging Environment using valid username and password using payload text file

tags: get_pi_token, staging

* Given that a user needs to invoke "Get Staging PI Token"
* And the user set the request payload as follows <file:/resources/payloads/login.txt>
* When the user invokes the API
* Then the status code for the request is "201"
* And the JSON Path Assertions for the response should be equal to the following 

   |JSON Path|Expected Result|
   |---------|---------------|
   |$.status |success        |
* And the JSON Path Existence in the response should be equal to the following 

   |JSON Path|isExists|
   |---------|--------|
   |$.status |true    |
   |$.osa    |false   |
* And save the access token in the response which is located inside the JSON Path of "$.data"
* And save the JSON Path values of the response into text files 

   |JSON Path|Text File Path                                |
   |---------|----------------------------------------------|
   |$.status |/resources/text_files/response_data/status.txt|
   |$.data   |/resources/text_files/response_data/token.txt |



## Get a category
* Given that a user needs to invoke "Get All Categories in Deck Service"
* And the user set the request authentication configurations as follows 

   |Configuration                                                     |Configuration Value                                 |
   |------------------------------------------------------------------|----------------------------------------------------|
   |Is authentication required?                                       |Yes                                                 |
   |Do you need to retrieve the access token from the text file?      |No                                                  |
   |Provide the access token if you need to authorize the API manually|<file:/resources/text_files/response_data/token.txt>|
* When the user invokes the API
* Then the status code for the request is "200"
