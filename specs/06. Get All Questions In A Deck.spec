Get All Questions in a Deck Specification
=========================================
Date Created    : 11/06/2017
Version   		: 1.0.0
Owner      		: Osanda Deshan
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.


tags: get_all_questions_in_a_deck



* Given that a user needs to invoke "Get all Questions"



Get all questions of a deck using a valid deckId
------------------------------------------------
* And the user set the request authentication configurations as follows
     |Configuration Property Name       |Configuration Property Value   |
     |----------------------------------|-------------------------------|
     |isAccessTokenIncluded             |True                           |
     |isAccessTokenRetrievedFromTextFile|True                           |
     |accessTokenString                 |N/A                            |
* And the user set the query parameters as follows
     |Query Parameter|Query Value|
     |---------------|-----------|
     |deckId         |11         |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                         |Value                                              |
     |--------------------------------------------------|---------------------------------------------------|
     |$.questions.[0].question.media                    |TEXT                                               |
     |$.questions.[0].question.prompt                   |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _       |
     |$.questions.[0].question.imageUrl                 |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL|
     |$.questions.[0].question.promptType               |TEXT                                               |
     |$.questions.[0].kind                              |SHORT_ANSWER                                       |
     |$.questions.[0].learningObjectives                |[]                                                 |
     |$.questions.[0].tags[0]                           |UserCreated                                        |
     |$.questions.[0].creatorId                         |Instructor1                                        |
     |$.questions.[0].deckId                            |11                                                 |
     |$.questions.[0].creatoredType                     |Auto                                               |
     |$.questions.[0].creatorPlatform                   |Mobile                                             |
     |$.questions.[0].creatoredSource                   |Clipper                                            |
     |$.questions.[0].answers.[0].id                    |1                                                  |
     |$..questions.[0].answers.[0].value                |Osanda Deshan                                      |
     |$.questions.[0].answers.[0].caseSensitive         |false                                              |
     |$.questions.[0].answers.[0].type                  |TEXT                                               |



Get all questions of a deck using an invalid deckId
---------------------------------------------------
* And the user set the request authentication configurations as follows
     |Configuration Property Name       |Configuration Property Value   |
     |----------------------------------|-------------------------------|
     |isAccessTokenIncluded             |True                           |
     |isAccessTokenRetrievedFromTextFile|True                           |
     |accessTokenString                 |N/A                            |
* And the user set the query parameters as follows
     |Query Parameter|Query Value|
     |---------------|-----------|
     |deckId         |200        |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                  |Value                   |
     |---------------------------|------------------------|
     |$.questions                |[]                      |



Get all questions of a deck using empty deckId
----------------------------------------------
* And the user set the request authentication configurations as follows
     |Configuration Property Name       |Configuration Property Value   |
     |----------------------------------|-------------------------------|
     |isAccessTokenIncluded             |True                           |
     |isAccessTokenRetrievedFromTextFile|True                           |
     |accessTokenString                 |N/A                            |
* And the user set the query parameters as follows
     |Query Parameter|Query Value|
     |---------------|-----------|
     |deckId         |           |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                  |Value                                        |
     |---------------------------|---------------------------------------------|
     |$.message                  |deckId: Invalid value '' was given.          |
     |$.description              |null                                         |
     |$.fieldErrors              |null                                         |



Get all questions of a deck using a string as deckId
----------------------------------------------------
* And the user set the request authentication configurations as follows
     |Configuration Property Name       |Configuration Property Value   |
     |----------------------------------|-------------------------------|
     |isAccessTokenIncluded             |True                           |
     |isAccessTokenRetrievedFromTextFile|True                           |
     |accessTokenString                 |N/A                            |
* And the user set the query parameters as follows
     |Query Parameter|Query Value|
     |---------------|-----------|
     |deckId         |osanda12   |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                  |Value                                        |
     |---------------------------|---------------------------------------------|
     |$.message                  |deckId: Invalid value 'osanda12' was given.  |



Get all questions of a deck using special characters as deckId
--------------------------------------------------------------
* And the user set the request authentication configurations as follows
     |Configuration Property Name       |Configuration Property Value   |
     |----------------------------------|-------------------------------|
     |isAccessTokenIncluded             |True                           |
     |isAccessTokenRetrievedFromTextFile|True                           |
     |accessTokenString                 |N/A                            |
* And the user set the query parameters as follows
     |Query Parameter|Query Value|
     |---------------|-----------|
     |deckId         |@#$%^*     |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                  |Value                                        |
     |---------------------------|---------------------------------------------|
     |$.message                  |deckId: Invalid value '@#$%^*' was given.    |
     |$.description              |null                                         |
     |$.fieldErrors              |null                                         |



Get all questions of a deck using an invalid query parameter
------------------------------------------------------------
* And the user set the request authentication configurations as follows
     |Configuration Property Name       |Configuration Property Value   |
     |----------------------------------|-------------------------------|
     |isAccessTokenIncluded             |True                           |
     |isAccessTokenRetrievedFromTextFile|True                           |
     |accessTokenString                 |N/A                            |
* And the user set the query parameters as follows
     |Query Parameter|Query Value|
     |---------------|-----------|
     |deck           |2          |
* When the user invokes the API
* Then the status code for the request is "500"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                  |Value                                        |
     |---------------------------|---------------------------------------------|
     |$.message                  |error.internalServerError                    |
     |$.description              |Internal server error                        |
     |$.fieldErrors              |null                                         |



Get all questions of a deck using two valid query parameters
------------------------------------------------------------
* And the user set the request authentication configurations as follows
     |Configuration Property Name       |Configuration Property Value   |
     |----------------------------------|-------------------------------|
     |isAccessTokenIncluded             |True                           |
     |isAccessTokenRetrievedFromTextFile|True                           |
     |accessTokenString                 |N/A                            |
* And the user set the query parameters as follows
     |Query Parameter|Query Value|
     |---------------|-----------|
     |deckId         |11         |
     |deckId         |3          |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                         |Value                                              |
     |--------------------------------------------------|---------------------------------------------------|
     |$.questions.[0].question.media                    |TEXT                                               |
     |$.questions.[0].question.prompt                   |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _       |
     |$.questions.[0].question.imageUrl                 |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL|
     |$.questions.[0].question.promptType               |TEXT                                               |
     |$.questions.[0].kind                              |SHORT_ANSWER                                       |
     |$.questions.[0].learningObjectives                |[]                                                 |
     |$.questions.[0].tags[0]                           |UserCreated                                        |
     |$.questions.[0].creatorId                         |Instructor1                                        |
     |$.questions.[0].deckId                            |11                                                 |
     |$.questions.[0].creatoredType                     |Auto                                               |
     |$.questions.[0].creatorPlatform                   |Mobile                                             |
     |$.questions.[0].creatoredSource                   |Clipper                                            |
     |$.questions.[0].answers.[0].id                    |1                                                  |
     |$..questions.[0].answers.[0].value                |Osanda Deshan                                      |
     |$.questions.[0].answers.[0].caseSensitive         |false                                              |
     |$.questions.[0].answers.[0].type                  |TEXT                                               |



Get all questions of a deck using one valid and one invalid query parameters
----------------------------------------------------------------------------
* And the user set the request authentication configurations as follows
     |Configuration Property Name       |Configuration Property Value   |
     |----------------------------------|-------------------------------|
     |isAccessTokenIncluded             |True                           |
     |isAccessTokenRetrievedFromTextFile|True                           |
     |accessTokenString                 |N/A                            |
* And the user set the query parameters as follows
     |Query Parameter|Query Value|
     |---------------|-----------|
     |deckId         |200        |
     |deckId         |2          |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                  |Value                                        |
     |---------------------------|---------------------------------------------|
     |$.questions                |[]                                           |



Get all questions of a deck without query parameters
----------------------------------------------------
* And the user set the request authentication configurations as follows
     |Configuration Property Name       |Configuration Property Value   |
     |----------------------------------|-------------------------------|
     |isAccessTokenIncluded             |True                           |
     |isAccessTokenRetrievedFromTextFile|True                           |
     |accessTokenString                 |N/A                            |
* When the user invokes the API
* Then the status code for the request is "500"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                  |Value                                        |
     |---------------------------|---------------------------------------------|
     |$.message                  |error.internalServerError                    |
     |$.description              |Internal server error                        |
     |$.fieldErrors              |null                                         |



Get all questions of a deck without access token
------------------------------------------------
* And the user set the request authentication configurations as follows
     |Configuration Property Name       |Configuration Property Value   |
     |----------------------------------|-------------------------------|
     |isAccessTokenIncluded             |False                          |
     |isAccessTokenRetrievedFromTextFile|N/A                            |
     |accessTokenString                 |N/A                            |
* And the user set the query parameters as follows
     |Query Parameter|Query Value|
     |---------------|-----------|
     |deckId         |2          |
* When the user invokes the API
* Then the status code for the request is "401"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                  |Value                                        |
     |---------------------------|---------------------------------------------|
     |$.status                   |Error                                        |
     |$.code                     |401                                          |
     |$.message                  |Unauthorized Request                         |



Get all questions of a deck using invalid access token
------------------------------------------------------
* And the user set the request authentication configurations as follows
     |Configuration Property Name       |Configuration Property Value   |
     |----------------------------------|-------------------------------|
     |isAccessTokenIncluded             |False                          |
     |isAccessTokenRetrievedFromTextFile|False                          |
     |accessTokenString                 |osanda12accesstoken            |
* And the user set the query parameters as follows
     |Query Parameter|Query Value|
     |---------------|-----------|
     |deckId         |2          |
* When the user invokes the API
* Then the status code for the request is "401"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                  |Value                                        |
     |---------------------------|---------------------------------------------|
     |$.status                   |Error                                        |
     |$.code                     |401                                          |
     |$.message                  |Unauthorized Request                         |



Get all questions of a deck using an expired access token
---------------------------------------------------------
* And the user set the request authentication configurations as follows
     |Configuration Property Name       |Configuration Property Value   |
     |----------------------------------|-------------------------------|
     |isAccessTokenIncluded             |False                          |
     |isAccessTokenRetrievedFromTextFile|False                          |
     |accessTokenString                 |eyJhbGciOiJSUzUxMiIsImtpZCI6ImsxMDY5NDgxOTAifQ.eyJleHAiOjE1MTA1NTI5OTEsInN1YiI6ImZmZmZmZmZmNTllODg2YjRlNGIwMWNlZDI4M2YwNjU1Iiwic2Vzc2lkIjoiZGJiYjA4YmItNWJlOS00ZmRjLWFiYTUtOGMzZDZhNGExNTA2IiwiaGNjIjoiVVMiLCJ0eXBlIjoiYXQiLCJpYXQiOjE1MTA1NDIxOTB9.StnchZ2j7Jpfl27spA9lC-qsxRkEjxEC_rq7O9dSlWPpRmOQYCS2MzvAVyN5uAFDb9mYEOm7TXeuNFcS8XlQ8Q0k1vhAqKpxadfv9QHFOBnwAhYoDXUmjl9rBfDG5Topblqfm7JG2Z5gEEup4R_Nk_cw-aO74qYZTjRXcVxiRmE   |
* And the user set the query parameters as follows
     |Query Parameter|Query Value|
     |---------------|-----------|
     |deckId         |2          |
* When the user invokes the API
* Then the status code for the request is "401"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                  |Value                                        |
     |---------------------------|---------------------------------------------|
     |$.status                   |Error                                        |
     |$.code                     |401                                          |
     |$.message                  |Unauthorized Request                         |