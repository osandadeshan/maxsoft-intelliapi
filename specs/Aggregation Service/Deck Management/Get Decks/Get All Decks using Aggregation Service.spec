Get All Decks using Aggregation Service Specification
=====================================================
Date Created    : 12/21/17
Version   		: 1.0.0
Owner      		: Dilp Wickramasinghe
Description  	: This specification covers get decks scenarios from the aggrigation service


tags: aggregation_service, deck_management, get_all_decks



Get all decks for a user using valid userId
-------------------------------------------
tags: get_all_decks, positive

* Create a deck
* And save the JSON Path values in the response inside the data stores
    |DataStore Type |Variable Name        |Value To Be Stored     |
    |---------------|---------------------|-----------------------|
    |scenario       |userId               |$.userId               |
    |scenario       |deckId               |$.id                   |
    |scenario       |title                |$.title                |
* Given that a user needs to invoke "Get all Decks using Aggregation service"
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |
* And the user set the path parameters using data stores as follows
    |Path Name      |Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value     |
    |---------------|-------------------|---------------|------------------------|---------------|
    |$.userId       |y                  |scenario       |userId                  |N/A            |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the values inside the data stores
    |JSON Path     |Is Data Store Used?|Data Store Type|Data Store Variable Name|Expected Value |
    |--------------|-------------------|---------------|------------------------|---------------|
    |$[-1].id      |y                  |scenario       |deckId                  |N/A            |
    |$[-1].title   |y                  |scenario       |title                   |success        |
    |$[-1].userId  |y                  |scenario       |userId                  |success        |




Get all decks for a user using empty userId
-------------------------------------------
tags: get_all_decks, negative

* Given that a user needs to invoke "Get all Decks using Aggregation service"
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |
* And the user set the path parameters as follows
     |Path Parameter |Path Value               |
     |---------------|-------------------------|
     |User           |                         |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                         |Value                                                   |
     |--------------------------------------------------|--------------------------------------------------------|
     |$.status                                          |400                                                     |
     |$.error                                           |Bad Request                                             |
     |$.exception                                       |org.springframework.web.client.ResourceAccessException  |



Get all decks for a user using invalid userId
---------------------------------------------
tags: get_all_decks, negative

* Given that a user needs to invoke "Get all Decks using Aggregation service"
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |
* And the user set the path parameters as follows
     |Path Parameter |Path Value               |
     |---------------|-------------------------|
     |User           |sdsdsdsds                |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                         |Value                                                                                     |
     |--------------------------------------------------|------------------------------------------------------------------------------------------|
     |$                                                 |[]                                                                                        |






