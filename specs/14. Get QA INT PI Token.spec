Get QA INT PI Token Specification
=================================
Date Created    : 11/29/2017
Version   		: 1.0.0
Owner      		: Osanda Deshan
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.


tags: get_pi_token



Invoke PI API in QA INT Environment using valid username and password and save the access token inside the text file
--------------------------------------------------------------------------------------------------------------------
tags: get_pi_token, qa_int

* Given that a user needs to invoke "Get QA PI Token"
* And the user set the request authentication configurations as follows
     |Configuration Property Name       |Configuration Property Value   |
     |----------------------------------|-------------------------------|
     |isAccessTokenIncluded             |N/A                            |
     |isAccessTokenRetrievedFromTextFile|N/A                            |
     |accessTokenString                 |N/A                            |
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set      |
     |--------------------------------|-------------------------------|
     |#username                       |smartflashcards_system         |
     |#password                       |klbV2BBe2Jh8CWGuiHTf29WEYu00S8R|
* When the user invokes the API
* Then the status code for the request is "201"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path     |Expected Result|
     |--------------|---------------|
     |$.status      |success        |
* And save the access token in the response which is located inside the JSON Path of "$.data"