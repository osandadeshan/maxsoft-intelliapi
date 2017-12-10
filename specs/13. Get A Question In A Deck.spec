Get A Question Specification
============================
Date Created    : 11/14/2017
Version   		: 1.0.0
Owner      		: Osanda Deshan
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.


tags: get_a_question



* Given that a user needs to invoke "Get a Question"



Get a question using a valid existing cardId
--------------------------------------------
* And the user set the request authentication configurations as follows
     |Configuration Property Name       |Configuration Property Value   |
     |----------------------------------|-------------------------------|
     |isAccessTokenIncluded             |True                           |
     |isAccessTokenRetrievedFromTextFile|True                           |
     |accessTokenString                 |N/A                            |
* And the user set the path parameters as follows
     |Path Parameter |Path Value               |
     |---------------|-------------------------|
     |Id             |5a0926575ed274e204b95547 |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                           |Value                                              |
     |------------------------------------|---------------------------------------------------|
     |$.question.media                    |TEXT                                               |
     |$.question.prompt                   |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _       |
     |$.question.imageUrl                 |www.maxsoft.com/image2                             |
     |$.question.promptType               |TEXT                                               |
     |$.kind                              |SHORT_ANSWER                                       |
     |$.learningObjectives[0]             |objective2                                         |
     |$.tags[0]                           |MaxSoft                                            |
     |$.creatorId                         |osanda12                                           |
     |$.deckId                            |3                                                  |
     |$.creatoredType                     |Manual                                             |
     |$.creatorPlatform                   |Web                                                |
     |$.creatoredSource                   |App                                                |
     |$.answers.[0].value                 |Osanda Deshan                                       |
     |$.answers.[0].caseSensitive         |false                                              |
     |$.answers.[0].type                  |null                                               |



Get a question using an already deleted cardId
----------------------------------------------
* And the user set the request authentication configurations as follows
     |Configuration Property Name       |Configuration Property Value   |
     |----------------------------------|-------------------------------|
     |isAccessTokenIncluded             |True                           |
     |isAccessTokenRetrievedFromTextFile|True                           |
     |accessTokenString                 |N/A                            |
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
* And the user set the request authentication configurations as follows
     |Configuration Property Name       |Configuration Property Value   |
     |----------------------------------|-------------------------------|
     |isAccessTokenIncluded             |True                           |
     |isAccessTokenRetrievedFromTextFile|True                           |
     |accessTokenString                 |N/A                            |
* And the user set the path parameters as follows
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
* And the user set the request authentication configurations as follows
     |Configuration Property Name       |Configuration Property Value   |
     |----------------------------------|-------------------------------|
     |isAccessTokenIncluded             |True                           |
     |isAccessTokenRetrievedFromTextFile|True                           |
     |accessTokenString                 |N/A                            |
* And the user set the path parameters as follows
     |Path Parameter |Path Value               |
     |---------------|-------------------------|
     |Id             |                         |
* When the user invokes the API
* Then the status code for the request is "500"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                  |Value                                                      |
     |---------------------------|-----------------------------------------------------------|
     |$.message                  |error.internalServerError                                  |
     |$.description              |Internal server error                                      |
     |$.fieldErrors              |null                                                       |



Get a question without cardId path parameter
--------------------------------------------
* And the user set the request authentication configurations as follows
     |Configuration Property Name       |Configuration Property Value   |
     |----------------------------------|-------------------------------|
     |isAccessTokenIncluded             |True                           |
     |isAccessTokenRetrievedFromTextFile|True                           |
     |accessTokenString                 |N/A                            |
* When the user invokes the API
* Then the status code for the request is "500"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                  |Value                                                      |
     |---------------------------|-----------------------------------------------------------|
     |$.message                  |error.internalServerError                                  |
     |$.description              |Internal server error                                      |
     |$.fieldErrors              |null                                                       |