# Save Auth Token To A Text File Specification

<pre>
Project Name    : MaxSoft-IntelliAPI
Developer       : Osanda Deshan
Version         : 1.0.0
Date            : 28/04/2019
Time            : 13:49
Description     : This is an executable specification file
</pre>



## Invoke Auth API using valid username and password using payload text file and save the token in a text file

tags: get_auth_token

* Given that a user needs to invoke "Get Auth Token"
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
