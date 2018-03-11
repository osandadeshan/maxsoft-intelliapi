Get A Deck using Aggregation Service Specification
==================================================
Date Created    : 12/21/17
Version   		: 1.0.0
Owner      		: Dilp Wickramasinghe
Description  	: This specification covers get decks scenarios from the aggregation service


tags: aggregation_service, deck_management, get_a_deck



* Given that a user needs to invoke "Get a Deck using Aggregation service"
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |



Get a deck using valid deckId
-----------------------------
tags: get_a_deck, positive

* Create a deck
* And save the JSON Path values in the response inside the data stores
    |DataStore Type |Variable Name        |Value To Be Stored     |
    |---------------|---------------------|-----------------------|
    |scenario       |deckId               |$.id                   |
* Given that a user needs to invoke "Get a Deck using Aggregation service"
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |
* And the user set the path parameters using data stores as follows
    |Path Name      |Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value     |
    |---------------|-------------------|---------------|------------------------|---------------|
    |deckId         |y                  |scenario       |deckId                  |N/A            |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the values inside the data stores
    |JSON Path      |Is Data Store Used?|Data Store Type|Data Store Variable Name|Expected Value |
    |---------------|-------------------|---------------|------------------------|---------------|
    |$.id           |y                  |scenario       |deckId                  |N/A            |



Get a deck without deckId
-------------------------
tags: get_a_deck, negative

* And the user set the path parameters as follows
       |Path Parameter |Path Value               |
       |---------------|-------------------------|
       |DeckId         |                         |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                         |Value                                                                                                            |
     |--------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
     |$.status                                          |400                                                                                                              |
     |$.error                                           |Bad Request                                                                                                      |
     |$.exception                                       |org.springframework.web.HttpRequestMethodNotSupportedException                                                   |



Get a deck using invalid DeckId
-------------------------------
tags: get_a_deck, negative

* And the user set the path parameters as follows
     |Path Parameter |Path Value               |
     |---------------|-------------------------|
     |DeckId         |  34347                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                         |Value                                                   |
     |--------------------------------------------------|--------------------------------------------------------|
     |$.status                                          |400                                                     |
     |$.error                                           |Bad Request                                             |
     |$.exception                                       |org.springframework.web.client.ResourceAccessException  |



Get a deck using invalid DeckId format
--------------------------------------
tags: get_a_deck, negative
* And the user set the path parameters as follows
     |Path Parameter |Path Value               |
     |---------------|-------------------------|
     |DeckId         |  erere34347             |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                         |Value                                                   |
     |--------------------------------------------------|--------------------------------------------------------|
     |$.status                                          |400                                                     |
     |$.error                                           |Bad Request                                             |
     |$.exception                                       |org.springframework.web.client.ResourceAccessException  |
//Verfiy duplicate response






