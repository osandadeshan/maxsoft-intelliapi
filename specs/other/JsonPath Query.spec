# JsonPath Query Specification

Project Name    : MaxSoft-IntelliAPI
Developer       : Osanda Deshan
Version         : 1.0.0
Date            : 28/04/2019
Time            : 20:09
Description     : This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.

tags: json_path, regression


## Check json path existence

* Given that a user needs to invoke "Get all users"
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Existence in the response should be equal to the following
   |JSON Path                 |isExists?            |
   |--------------------------|---------------------|
   |$.code                    |true                 |
   |$.status                  |false                |
   |$.data[?(@.id=='10')].name|true                 |


## Get camera model by userId

* Given that a user needs to invoke "Get photos"
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
   |JSON Path                             |Expected Result          |
   |--------------------------------------|-------------------------|
   |$.photos[?(@.user.id=='23896')].camera|["ILCA-99M2"]            |
