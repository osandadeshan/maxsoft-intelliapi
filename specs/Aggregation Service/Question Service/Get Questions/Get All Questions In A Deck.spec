Get All Questions In A Deck using Aggregation Service Specification
===================================================================
Date Created    : 11/06/2017
Version   		: 1.0.0
Owner      		: Osanda Deshan
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.


tags: get_all_questions_in_a_deck, ci_ready



Get all questions of a deck using a valid deckId
------------------------------------------------
* Given that a user needs to invoke "Get all Questions using Aggregation Service"
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |
*  And the user set the query parameters as follows
     |Query Parameter|Query Value                     |
     |---------------|--------------------------------|
     |deckId         |5a603af62e02d86561172dac        |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                           |Value                                              |
     |----------------------------------------------------|---------------------------------------------------|
     |$.questions.[-1:].question.media                    |TEXT                                               |
     |$.questions.[-1:].question.promptType               |TEXT                                               |
     |$.questions.[-1:].kind                              |SHORT_ANSWER                                       |
     |$.questions.[-1:].creatoredSource                   |App                                                |
     |$..questions.[-1:].answers.[0].value                |Osanda Deshan                                      |
     |$.questions.[-1:].answers.[0].type                  |TEXT                                               |



Get all questions of a deck using an invalid deckId
---------------------------------------------------
* Given that a user needs to invoke "Get all Questions using Aggregation Service"
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |
*  And the user set the query parameters as follows
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
* Given that a user needs to invoke "Get all Questions using Aggregation Service"
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |
*  And the user set the query parameters as follows
     |Query Parameter|Query Value|
     |---------------|-----------|
     |deckId         |           |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                  |Value                                        |
     |---------------------------|---------------------------------------------|
     |$.description              |null                                         |
     |$.fieldErrors              |null                                         |



Get all questions of a deck using a string as deckId
----------------------------------------------------
* Given that a user needs to invoke "Get all Questions using Aggregation Service"
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |
*  And the user set the query parameters as follows
     |Query Parameter|Query Value|
     |---------------|-----------|
     |deckId         |osanda12   |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path         |Value                    |
     |------------------|-------------------------|
     |$.questions       |[]                       |



Get all questions of a deck using special characters as deckId
--------------------------------------------------------------
* Given that a user needs to invoke "Get all Questions using Aggregation Service"
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |
* And the user set the query parameters as follows
     |Query Parameter|Query Value|
     |---------------|-----------|
     |deckId         |@#$%^*     |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path         |Value                    |
     |------------------|-------------------------|
     |$.questions       |[]                       |



Get all questions of a deck using an invalid query parameter
------------------------------------------------------------
* Given that a user needs to invoke "Get all Questions using Aggregation Service"
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |
* And the user set the query parameters as follows
     |Query Parameter|Query Value               |
     |---------------|--------------------------|
     |deck           |5a603af62e02d86561172dac  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                  |Value                                                                |
     |---------------------------|---------------------------------------------------------------------|
     |$.status                   |400                                                                  |
     |$.message                  |Required String parameter 'deckId' is not present                    |
     |$.error                    |Bad Request                                                          |
     |$.exception                |org.springframework.web.bind.MissingServletRequestParameterException |



Get all questions of a deck using two valid query parameters
------------------------------------------------------------
* Given that a user needs to invoke "Get all Questions using Aggregation Service"
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |
* And the user set the query parameters as follows
     |Query Parameter|Query Value              |
     |---------------|-------------------------|
     |deckId         |5a603af62e02d86561172dac |
     |deckId         |5a603af62e02d86561172dac |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path         |Value                    |
     |------------------|-------------------------|
     |$.questions       |[]                       |



Get all questions of a deck using one valid and one invalid query parameters
----------------------------------------------------------------------------
* Given that a user needs to invoke "Get all Questions using Aggregation Service"
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |
* And the user set the query parameters as follows
     |Query Parameter|Query Value              |
     |---------------|-------------------------|
     |deckId         |5a603af62e02d86561172dac |
     |deckId         |5a603af62e02d8           |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                  |Value                                        |
     |---------------------------|---------------------------------------------|
     |$.questions                |[]                                           |



Get all questions of a deck without query parameters
----------------------------------------------------
* Given that a user needs to invoke "Get all Questions using Aggregation Service"
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                  |Value                                                                |
     |---------------------------|---------------------------------------------------------------------|
     |$.status                   |400                                                                  |
     |$.message                  |Required String parameter 'deckId' is not present                    |
     |$.error                    |Bad Request                                                          |
     |$.exception                |org.springframework.web.bind.MissingServletRequestParameterException |



Get all questions of a deck without access token
------------------------------------------------
* Given that a user needs to invoke "Get all Questions using Aggregation Service"
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |No                             |
     |Do you need to retrieve the access token from the text file?      |N/A                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |
* And the user set the query parameters as follows
     |Query Parameter|Query Value              |
     |---------------|-------------------------|
     |deckId         |5a603af62e02d86561172dac |
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
* Given that a user needs to invoke "Get all Questions using Aggregation Service"
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |No                             |
     |Provide the access token if you need to authorize the API manually|dsfsdfsdfqe32423rdasfas        |
* And the user set the query parameters as follows
     |Query Parameter|Query Value              |
     |---------------|-------------------------|
     |deckId         |5a603af62e02d86561172dac |
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
* Given that a user needs to invoke "Get all Questions using Aggregation Service"
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |No                             |
     |Provide the access token if you need to authorize the API manually|eyJhbGciOiJSUzUxMiIsImtpZCI6ImsxMDY5NDgxOTAifQ.eyJleHAiOjE1MTA1NTI5OTEsInN1YiI6ImZmZmZmZmZmNTllODg2YjRlNGIwMWNlZDI4M2YwNjU1Iiwic2Vzc2lkIjoiZGJiYjA4YmItNWJlOS00ZmRjLWFiYTUtOGMzZDZhNGExNTA2IiwiaGNjIjoiVVMiLCJ0eXBlIjoiYXQiLCJpYXQiOjE1MTA1NDIxOTB9.StnchZ2j7Jpfl27spA9lC-qsxRkEjxEC_rq7O9dSlWPpRmOQYCS2MzvAVyN5uAFDb9mYEOm7TXeuNFcS8XlQ8Q0k1vhAqKpxadfv9QHFOBnwAhYoDXUmjl9rBfDG5Topblqfm7JG2Z5gEEup4R_Nk_cw-aO74qYZTjRXcVxiRmE |
* And the user set the query parameters as follows
     |Query Parameter|Query Value              |
     |---------------|-------------------------|
     |deckId         |5a603af62e02d86561172dac |
* When the user invokes the API
* Then the status code for the request is "401"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                  |Value                                        |
     |---------------------------|---------------------------------------------|
     |$.status                   |Error                                        |
     |$.code                     |401                                          |
     |$.message                  |Unauthorized Request                         |