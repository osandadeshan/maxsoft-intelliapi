# Get Auth Token Specification

Project Name : MaxSoft-IntelliAPI
Developer    : Osanda Deshan
Version      : 1.0.0
Date         : 12/24/2020
Time         : 9:33 AM
Description  : This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.

tags: get_auth_token, regression


## Invoke Auth API and save the access token inside the text file

* Given that a user needs to invoke "Get auth token"
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following

   |JSON Path|Expected Result|
   |---------|---------------|
   |$.status |success        |
* And save the access token in the response which is located inside the JSON Path of "$.token"
