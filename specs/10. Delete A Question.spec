Delete a Question Specification
===============================
Date Created    : 11/14/2017
Version   		: 1.0.0
Owner      		: Osanda Deshan
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.


tags: delete_a_question



* Given that a user needs to invoke "Delete a Question"
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |



Delete a question using a valid cardId
--------------------------------------
* And the user set the path parameters as follows
     |Path Parameter |Path Value               |
     |---------------|-------------------------|
     |Id             |5a099fbe796245186514ccb0 |
* When the user invokes the API
* Then the status code for the request is "204"



Delete a question using already deleted cardId
----------------------------------------------
* And the user set the path parameters as follows
     |Path Parameter |Path Value               |
     |---------------|-------------------------|
     |Id             |5a0a7bce5ed274e204b95568 |
* When the user invokes the API
* Then the status code for the request is "404"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                  |Value                                                      |
     |---------------------------|-----------------------------------------------------------|
     |$.message                  |Couldn't find question with id - 5a0a7bce5ed274e204b95568  |
     |$.description              |null                                                       |
     |$.fieldErrors              |null                                                       |



Delete a question using an invalid cardId
-----------------------------------------
* And the user set the path parameters as follows
     |Path Parameter |Path Value               |
     |---------------|-------------------------|
     |Id             |safkjashfjashjkfahsjkf   |
* When the user invokes the API
* Then the status code for the request is "404"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                  |Value                                                      |
     |---------------------------|-----------------------------------------------------------|
     |$.message                  |Couldn't find question with id - safkjashfjashjkfahsjkf    |
     |$.description              |null                                                       |
     |$.fieldErrors              |null                                                       |



Delete a question using an empty value as the cardId
----------------------------------------------------
* And the user set the path parameters as follows
     |Path Parameter |Path Value               |
     |---------------|-------------------------|
     |Id             |                         |
* When the user invokes the API
* Then the status code for the request is "405"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                  |Value                                                      |
     |---------------------------|-----------------------------------------------------------|
     |$.message                  |error.methodNotSupported                                   |
     |$.description              |Request method 'DELETE' not supported                      |
     |$.fieldErrors              |null                                                       |



Delete a question without cardId path parameter
-----------------------------------------------
* When the user invokes the API
* Then the status code for the request is "405"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                  |Value                                                      |
     |---------------------------|-----------------------------------------------------------|
     |$.message                  |error.methodNotSupported                                   |
     |$.description              |Request method 'DELETE' not supported                      |
     |$.fieldErrors              |null                                                       |