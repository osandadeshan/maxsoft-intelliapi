Get A Question using Aggregation Service Specification
======================================================
Date Created    : 11/14/2017
Version   		: 1.0.0
Owner      		: Osanda Deshan
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.


tags: get_a_question



Get a question using a valid existing cardId
--------------------------------------------
* Create a short answer type question
* And save the JSON Path values in the response inside the data stores
    |DataStore Type |Variable Name  |Value To Be Stored     |
    |---------------|---------------|-----------------------|
    |scenario       |questionId     |$.id                   |
* Given that a user needs to invoke "Get a Question using Aggregation Service"
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
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                           |Value                                              |
     |------------------------------------|---------------------------------------------------|
     |$.question.media                    |TEXT                                               |
     |$.question.prompt                   |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _       |
     |$.question.imageUrl                 |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL|
     |$.question.promptType               |TEXT                                               |
     |$.kind                              |SHORT_ANSWER                                       |
     |$.learningObjectives[0]             |                                                   |
     |$.tags[0]                           |MaxSoft                                            |
     |$.creatorId                         |osanda12                                           |
     |$.deckId                            |5a603af62e02d86561172dac                           |
     |$.creatoredType                     |Manual                                             |
     |$.creatorPlatform                   |Web                                                |
     |$.creatoredSource                   |App                                                |
     |$.answers.[0].value                 |Osanda Deshan                                      |
     |$.answers.[0].caseSensitive         |false                                              |
     |$.answers.[0].type                  |TEXT                                               |



Get a question using an already deleted cardId
----------------------------------------------
* Given that a user needs to invoke "Get a Question using Aggregation Service"
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
     |JSON Path                  |Value                                                             |
     |---------------------------|------------------------------------------------------------------|
     |$.message                  |Couldn't find a question for given id : 5a0a7bce5ed274e204b95568  |
     |$.description              |null                                                              |
     |$.fieldErrors              |null                                                              |



Get a question using an invalid cardId
--------------------------------------
* Given that a user needs to invoke "Get a Question using Aggregation Service"
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |
*  And the user set the path parameters as follows
     |Path Parameter |Path Value               |
     |---------------|-------------------------|
     |Id             |sfsgsgfsgfsgsgsgfsgfsfgs |
* When the user invokes the API
* Then the status code for the request is "404"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                  |Value                                                             |
     |---------------------------|------------------------------------------------------------------|
     |$.message                  |Couldn't find a question for given id : sfsgsgfsgfsgsgsgfsgfsfgs  |
     |$.description              |null                                                              |
     |$.fieldErrors              |null                                                              |



Get a question using the cardId as empty
----------------------------------------
* Given that a user needs to invoke "Get a Question using Aggregation Service"
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |
*  And the user set the path parameters as follows
     |Path Parameter |Path Value               |
     |---------------|-------------------------|
     |Id             |                         |
* When the user invokes the API
* Then the status code for the request is "404"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                  |Value                                                      |
     |---------------------------|-----------------------------------------------------------|
     |$.message                  |error.internalServerError                                  |
     |$.description              |Internal server error                                      |
     |$.fieldErrors              |null                                                       |



Get a question without cardId path parameter
--------------------------------------------
* Given that a user needs to invoke "Get a Question using Aggregation Service"
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |
* When the user invokes the API
* Then the status code for the request is "404"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                  |Value                                                      |
     |---------------------------|-----------------------------------------------------------|
     |$.message                  |error.internalServerError                                  |
     |$.description              |Internal server error                                      |
     |$.fieldErrors              |null                                                       |