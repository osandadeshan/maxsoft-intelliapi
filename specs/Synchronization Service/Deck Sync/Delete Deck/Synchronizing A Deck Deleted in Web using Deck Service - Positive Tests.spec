Synchronizing A Deck Deleted in Web using Deck Service - Positive Tests Specification
=====================================================================================
Date Created    : 02/07/2018
Version         : 1.0.0
Owner      	    : Osanda Deshan
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.


tags: sync_an_existing_deck_deleted_in_web, sync_an_existing_deck_deleted_in_web-positive_tests, positive



* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |



Synchronize delete an existing deck which has already deleted in web
--------------------------------------------------------------------
* Create a deck
* And save the JSON Path values in the response inside the data stores
    |DataStore Type |Variable Name  |Value To Be Stored     |
    |---------------|---------------|-----------------------|
    |spec           |deckId         |$.id                   |
* Given that a user needs to invoke "Delete a Deck using Deck Service"
* And the user set the path parameters using data stores as follows
    |Path Name      |Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value     |
    |---------------|-------------------|---------------|------------------------|---------------|
    |deckId         |y                  |spec           |deckId                  |N/A            |
* When the user invokes the API
* Then the status code for the request is "200"
* Given that a user needs to invoke "Sync API"
* And the user set the request attributes using data stores as follows
    |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name|Attribute Value To Be Set                                                                                        |
    |--------------------------------|-------------------|---------------|------------------------|-----------------------------------------------------------------------------------------------------------------|
    |#deckId                         |y                  |spec           |deckId                  |N/A                                                                                                              |
    |#title                          |n                  |               |                        |API Deck3                                                                                                        |
    |#description                    |n                  |               |                        |test description                                                                                                 |
    |#tags1                          |n                  |               |                        |API tag1                                                                                                         |
    |#subjectId                      |n                  |               |                        |2                                                                                                                |
    |#subjectName                    |n                  |               |                        |API Testing3                                                                                                     |
    |#bookTitle                      |n                  |               |                        |Automation3                                                                                                      |
    |#bookAuthor                     |n                  |               |                        |Osanda Nimalarathna                                                                                              |
    |#bookChapter                    |n                  |               |                        |Chap. 04                                                                                                         |
    |#purchasedDate                  |n                  |               |                        |1512021142001                                                                                                    |
    |#purchaseInformationPrice       |n                  |               |                        |777                                                                                                              |
    |#purchaseInformationsku         |n                  |               |                        |com.pearson.smartflashcards.test3                                                                                |
    |#areNotificationsEnabled        |n                  |               |                        |true                                                                                                             |
    |#notificationTime               |n                  |               |                        |08:00 AM                                                                                                         |
    |#notificationFrequency          |n                  |               |                        |5                                                                                                                |
    |#examDate                       |n                  |               |                        |1512021142000                                                                                                    |
    |#userId                         |n                  |               |                        |34                                                                                                               |
    |#parentDeckId                   |n                  |               |                        |5                                                                                                                |
    |#tempDeckId                     |n                  |               |                        |999                                                                                                              |
    |#archived                       |n                  |               |                        |true                                                                                                             |
    |#cardPreview                    |n                  |               |                        |true                                                                                                             |
    |#noOfCards                      |n                  |               |                        |2                                                                                                                |
    |#progress                       |n                  |               |                        |3                                                                                                                |
    |#downloads                      |n                  |               |                        |12                                                                                                               |
    |#deckAuthorName                 |n                  |               |                        |Osanda                                                                                                           |
    |#deckAuthorId                   |n                  |               |                        |6                                                                                                                |
    |#thumbnailUrl                   |n                  |               |                        |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a154f35d5b71d1a8a54dd58/download/public?format=ORIGINAL|
    |#status                         |n                  |               |                        |Closed                                                                                                           |
    |#starred                        |n                  |               |                        |true                                                                                                             |
    |#categoryId                     |n                  |               |                        |5a5db30a12ef181b0af109ba                                                                                         |
    |#serverDate                     |n                  |               |                        |2018-08-06T09:40:26.456Z                                                                                         |
    |#activityId                     |n                  |               |                        |act1                                                                                                             |
    |#activityType                   |n                  |               |                        |delete                                                                                                           |
* When the user invokes the API
* Then the status code for the request is "404"
* And the JSON Path Assertions for the response should be equal to the following
    |JSON Path                                     |Value                               |
    |----------------------------------------------|------------------------------------|
    |$.status                                      |404                                 |
    |$.error                                       |Not Found                           |
    |$.message                                     |No message available                |
