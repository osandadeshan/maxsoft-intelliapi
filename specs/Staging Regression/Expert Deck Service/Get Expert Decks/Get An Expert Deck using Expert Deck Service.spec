Get An Expert Deck using Expert Deck Service Specification
==========================================================
Date Created    : 01/19/2018
Version   		: 1.0.0
Owner      		: Yasith Edirisooriya
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.


tags: get_an_expert_decks



Get an expert deck using a valid id
-----------------------------------
* Create an expert deck
* Given that a user needs to invoke "Search Expert Decks using Expert Deck Service"
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                           |Expected Result                                        |
     |------------------------------------|-------------------------------------------------------|
     |$[-1:].title                        |Expert API Automation using MaxSoft ATA Framework      |
     |$[-1:].userId                       |osan                                                   |
     |$[-1:].book.bookTitle               |Expert API Deck3                                       |



Get an expert deck using an invalid id
--------------------------------------
* Given that a user needs to invoke "Search Expert Decks using Expert Deck Service"
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |
* And the user set the path parameters as follows
     |Path Parameter |Path Value                |
     |---------------|--------------------------|
     |id             |5a55a103559fee181b833a51  |
* When the user invokes the API
* Then the status code for the request is "404"



Get an expert deck using null value as the id
---------------------------------------------
* Given that a user needs to invoke "Search Expert Decks using Expert Deck Service"
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |
* And the user set the path parameters as follows
     |Path Parameter |Path Value                |
     |---------------|--------------------------|
     |id             |null                      |
* When the user invokes the API
* Then the status code for the request is "404"