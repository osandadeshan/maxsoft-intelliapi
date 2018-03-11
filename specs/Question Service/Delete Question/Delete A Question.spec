Delete a Question using Question Service Specification
======================================================
Date Created    : 11/14/2017
Version   		: 1.0.0
Owner      		: Osanda Deshan
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.


tags: delete_a_question



Delete a short answer type question using valid question id
-----------------------------------------------------------
* Create a short answer type question
* And save the JSON Path values in the response inside the data stores
    |DataStore Type |Variable Name  |Value To Be Stored     |
    |---------------|---------------|-----------------------|
    |scenario       |questionId     |$.id                   |
* Given that a user needs to invoke "Delete a Question using Question Service"
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |
* And the user set the path parameters using data stores as follows
    |Path Name      |Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value     |
    |---------------|-------------------|---------------|------------------------|---------------|
    |questionId     |y                  |scenario       |questionId              |N/A            |
* When the user invokes the API
* Then the status code for the request is "204"



Delete a MCQ question using valid question id
---------------------------------------------
* Create a MCQ question
* And save the JSON Path values in the response inside the data stores
    |DataStore Type |Variable Name  |Value To Be Stored     |
    |---------------|---------------|-----------------------|
    |scenario       |questionId     |$.id                   |
* Given that a user needs to invoke "Delete a Question using Question Service"
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |
* And the user set the path parameters using data stores as follows
    |Path Name      |Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value     |
    |---------------|-------------------|---------------|------------------------|---------------|
    |questionId     |y                  |scenario       |questionId              |N/A            |
* When the user invokes the API
* Then the status code for the request is "204"



Delete a question using already deleted cardId
----------------------------------------------
* Given that a user needs to invoke "Delete a Question using Question Service"
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |
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
* Given that a user needs to invoke "Delete a Question using Question Service"
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |
*  And the user set the path parameters as follows
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
* Given that a user needs to invoke "Delete a Question using Question Service"
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |
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
* Given that a user needs to invoke "Delete a Question using Question Service"
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |
*  When the user invokes the API
* Then the status code for the request is "405"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                  |Value                                                      |
     |---------------------------|-----------------------------------------------------------|
     |$.message                  |error.methodNotSupported                                   |
     |$.description              |Request method 'DELETE' not supported                      |
     |$.fieldErrors              |null                                                       |