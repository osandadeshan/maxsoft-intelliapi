Add Expert Deck To My Deck using Aggregation Service Specification
==================================================================
Date Created    : 02/28/2018
Version         : 1.0.0
Owner      	    : Osanda Deshan
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.


tags: add_expert_deck_to_my_deck, ci_ready



Add an expert deck to my deck
-----------------------------
* Create an expert deck with 4 questions
* Given that a user needs to invoke "Add Expert Deck To My Deck using Aggregation Service"
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |
* And the user set the path parameters using data stores as follows
       |Path Parameter  |Is Data Store Used?|Data Store Type|Data Store Variable Name   |Path Value                |
       |----------------|-------------------|---------------|---------------------------|--------------------------|
       |deckId          |y                  |spec           |expertDeckIdWith4Questions |                          |
       |users           |n                  |               |                           |users                     |
       |userId          |n                  |               |                           |osan                      |
* When the user invokes the API
* Then the status code for the request is "201"



Verify all the questions are in the newly added deck
----------------------------------------------------
* Given that a user needs to invoke "Get all Questions using Aggregation Service"
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |
* And the user set the query parameters using data stores as follows
    |Query Name     |Is Data Store Used?|Data Store Type|Data Store Variable Name   |Query Value    |
    |---------------|-------------------|---------------|---------------------------|---------------|
    |deckId         |y                  |spec           |expertDeckIdWith4Questions |N/A            |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the values inside the data stores
    |JSON Path               |Is Data Store Used?|Data Store Type|Data Store Variable Name     |Expected Value |
    |------------------------|-------------------|---------------|-----------------------------|---------------|
    |$.questions[0].deckId   |y                  |spec           |expertDeckIdWith4Questions   |N/A            |
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                   |Value                                     |
     |----------------------------|------------------------------------------|
     |$.questions.length()        |4                                         |



Delete the previously created expert deck
-----------------------------------------
* Given that a user needs to invoke "Delete Expert Deck by ID using Expert Deck Service"
* And the user set the path parameters using data stores as follows
    |Path Name      |Is Data Store Used?|Data Store Type|Data Store Variable Name   |Path Value     |
    |---------------|-------------------|---------------|---------------------------|---------------|
    |deckId         |y                  |spec           |expertDeckIdWith4Questions |N/A            |
* When the user invokes the API
* Then the status code for the request is "204"