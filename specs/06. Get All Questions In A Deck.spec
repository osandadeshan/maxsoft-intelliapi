Get All Questions in a Deck Specification
=========================================
Date Created    : 11/06/2017
Version   		: 1.0.0
Owner      		: Osanda Deshan
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.


tags: get_all_questions_in_a_deck



* Given that a user needs to invoke "Get all Questions"



Get all questions using a valid userId and valid filter
--------------------------------------------------------
* And the user set the request authentication configurations as follows
     |Configuration Property Name       |Configuration Property Value   |
     |----------------------------------|-------------------------------|
     |isAccessTokenIncluded             |True                           |
     |isAccessTokenRetrievedFromTextFile|True                           |
     |accessTokenString                 |N/A                            |
     |isHeadersInclueded                |True                           |
     |isJsonBodyIncluded                |False                          |
* And the user set the query parameters as follows
     |Query Parameter|Query Value|
     |---------------|-----------|
     |deckId         |1479       |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                              |
     |------------------------------------------|-----------------------------------|
     |$.questions[-1:].question.prompt[0]       |QE Test3                           |
     |$.[:1].subject.name                       |SUB 1                              |
     |$.[:1].userId                             |Osanda                             |