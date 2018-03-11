Delete A Deck using Aggregation Service - Negative Tests Specification
======================================================================
Date Created    : 01/09/2018
Version   		: 1.0.0
Owner      		: Osanda Deshan
Description  	: This specification covers delete a deck scenarios from the aggregation service


tags: aggregation_service, deck_management, delete_a_deck


* Given that a user needs to invoke "Delete a Deck using Aggregation Service"
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |



Delete a deck using already deleted deckId
------------------------------------------
* And the user set the path parameters as follows
     |Path Parameter |Path Value               |
     |---------------|-------------------------|
     |deckId         |5a570a5980a9ce1821e70b94 |
* When the user invokes the API
* Then the status code for the request is "404"



Delete a deck using an invalid deckId
-------------------------------------
* And the user set the path parameters as follows
     |Path Parameter |Path Value               |
     |---------------|-------------------------|
     |deckId         |this is not a deckId	   |
* When the user invokes the API
* Then the status code for the request is "404"



Delete a deck using an empty value as the deckId
------------------------------------------------
* And the user set the path parameters as follows
     |Path Parameter |Path Value               |
     |---------------|-------------------------|
     |deckId         |						   |
* When the user invokes the API
* Then the status code for the request is "400"



Delete a deck without deckId path parameter
-------------------------------------------
* When the user invokes the API
* Then the status code for the request is "405"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                  |Value                                                            |
     |---------------------------|-----------------------------------------------------------------|
     |$.status                   |405                                                              |
     |$.message                  |Request method 'DELETE' not supported                            |
     |$.exception                |org.springframework.web.HttpRequestMethodNotSupportedException   |
     |$.error                    |Method Not Allowed                                               |