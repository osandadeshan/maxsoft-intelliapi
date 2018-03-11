Get A Deck using Deck Service Specification
===========================================
Date Created    : 12/21/17
Version   		: 1.0.0
Owner      		: Dilp Wickramasinghe
Description  	: This specification covers get decks scenarios from the aggregation service


tags: aggregation_service, deck_management, get_a_deck



Get a deck using valid deckId
-----------------------------
tags: get_a_deck, positive

* Create a deck
* And save the JSON Path values in the response inside the data stores
    |DataStore Type |Variable Name        |Value To Be Stored     |
    |---------------|---------------------|-----------------------|
    |scenario       |deckId               |$.id                   |
* Given that a user needs to invoke "Get a Deck using Deck Service"
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
     |JSON Path                                         |Is Data Store Used?|Data Store Type|Data Store Variable Name|Value                                                                                                            |
     |--------------------------------------------------|-------------------|---------------|------------------------|-----------------------------------------------------------------------------------------------------------------|
     |$.id                                              |y                  |scenario       |deckId                  |                                                                                                                 |
     |$.title                                           |n                  |               |                        |API Deck3                                                                                                        |
     |$.description                                     |n                  |               |                        |test description                                                                                                 |
     |$.tags[0]                                         |n                  |               |                        |API tag1                                                                                                         |
     |$.book.bookTitle                                  |n                  |               |                        |Automation3                                                                                                      |
     |$.book.bookAuthor                                 |n                  |               |                        |Osanda Nimalarathna                                                                                              |
     |$.book.chapter                                    |n                  |               |                        |Chap. 04                                                                                                         |
     |$.purchaseInfo.price                              |n                  |               |                        |0                                                                                                                |
     |$.notificationSettings.areNotificationsEnabled    |n                  |               |                        |true                                                                                                             |
     |$.notificationSettings.notificationTime           |n                  |               |                        |08:00 AM                                                                                                         |
     |$.notificationSettings.notificationFrequency      |n                  |               |                        |5                                                                                                                |
     |$.examDate                                        |n                  |               |                        |1512021142000                                                                                                    |
     |$.userId                                          |n                  |               |                        |34                                                                                                               |
     |$.parentDeckId                                    |n                  |               |                        |5                                                                                                                |
     |$.archived                                        |n                  |               |                        |true                                                                                                             |
     |$.cardPreview                                     |n                  |               |                        |true                                                                                                             |
     |$.noOfCards                                       |n                  |               |                        |2                                                                                                                |
     |$.progress                                        |n                  |               |                        |3                                                                                                                |
     |$.downloads                                       |n                  |               |                        |12                                                                                                               |
     |$.deckAuthor                                      |n                  |               |                        |Osanda                                                                                                           |
     |$.deckAuthorId                                    |n                  |               |                        |6                                                                                                                |
     |$.thumbnailUrl                                    |n                  |               |                        |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a154f35d5b71d1a8a54dd58/download/public?format=ORIGINAL|
     |$.status                                          |n                  |               |                        |Closed                                                                                                           |
     |$.expert                                          |n                  |               |                        |false                                                                                                            |
     |$.userDeck                                        |n                  |               |                        |true                                                                                                             |
     |$.starred                                         |n                  |               |                        |true                                                                                                             |



Get a deck without deckId
-------------------------
tags: get_a_deck, negative

* Given that a user needs to invoke "Get a Deck using Deck Service"
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |
* And the user set the path parameters as follows
       |Path Parameter |Path Value               |
       |---------------|-------------------------|
       |DeckId         |                         |
* When the user invokes the API
* Then the status code for the request is "405"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                         |Value                                                                                                            |
     |--------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
     |$.status                                          |405                                                                                                              |
     |$.error                                           |Method Not Allowed                                                                                               |
     |$.exception                                       |org.springframework.web.HttpRequestMethodNotSupportedException                                                   |
     |$.message                                         |Request method 'GET' not supported                                                                               |
     |$.path                                            |/api/decks/                                                                                                      |



Get a deck using invalid DeckId
-------------------------------
tags: get_a_deck, negative

* Given that a user needs to invoke "Get a Deck using Deck Service"
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |
* And the user set the path parameters as follows
     |Path Parameter |Path Value               |
     |---------------|-------------------------|
     |DeckId         |  34347                  |
* When the user invokes the API
* Then the status code for the request is "404"



Get a deck using invalid DeckId format
--------------------------------------
tags: get_a_deck, negative

* Given that a user needs to invoke "Get a Deck using Deck Service"
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |
* And the user set the path parameters as follows
     |Path Parameter |Path Value               |
     |---------------|-------------------------|
     |DeckId         |erere34347               |
* When the user invokes the API
* Then the status code for the request is "404"






