Synchronize Delete An Existing Deck using Deck Service - Data Driven Positive Tests Specification
=================================================================================================
Date Created    : 02/07/2018
Version         : 1.0.0
Owner      	    : Osanda Deshan
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.


tags: sync_delete_an_existing_deck, sync_delete_an_existing_deck-positive_tests, positive


table: /resources/data_driven_test_csv/sync_deck/sync_delete_an_existing_deck_using_deck_service.csv



* Create a deck
* And save the JSON Path values in the response inside the data stores
    |DataStore Type |Variable Name  |Value To Be Stored     |
    |---------------|---------------|-----------------------|
    |scenario       |deckId         |$.id                   |
* Given that a user needs to invoke <api>
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |



Synchronize delete an existing deck using valid payload
-------------------------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template |Is Data Store Used? |Data Store Type |Data Store Variable Name |Attribute Value To Be Set               |
     |---------------------------------|--------------------|----------------|-------------------------|----------------------------------------|
     |#activityId                      |n                   |                |                         |<activityId>                            |
     |#activityType                    |n                   |                |                         |<activityType>                          |
     |#title                           |n                   |                |                         |<title>                                 |
     |#description                     |n                   |                |                         |<description>                           |
     |#tags1                           |n                   |                |                         |<tags1>                                 |
     |#subjectId                       |n                   |                |                         |<subjectId>                             |
     |#subjectName                     |n                   |                |                         |<subjectName>                           |
     |#bookTitle                       |n                   |                |                         |<bookTitle>                             |
     |#bookAuthor                      |n                   |                |                         |<bookAuthor>                            |
     |#bookChapter                     |n                   |                |                         |<bookChapter>                           |
     |#purchasedDate                   |n                   |                |                         |<purchasedDate>                         |
     |#purchaseInformationPrice        |n                   |                |                         |<purchaseInformationPrice>              |
     |#purchaseInformationsku          |n                   |                |                         |<purchaseInformationsku>                |
     |#areNotificationsEnabled         |n                   |                |                         |<areNotificationsEnabled>               |
     |#notificationTime                |n                   |                |                         |<notificationTime>                      |
     |#notificationFrequency           |n                   |                |                         |<notificationFrequency>                 |
     |#examDate                        |n                   |                |                         |<examDate>                              |
     |#categoryId                      |n                   |                |                         |<categoryId>                            |
     |#userId                          |n                   |                |                         |<userId>                                |
     |#parentDeckId                    |n                   |                |                         |<parentDeckId>                          |
     |#tempDeckId                      |n                   |                |                         |<tempDeckId>                            |
     |#archived                        |n                   |                |                         |<archived>                              |
     |#cardPreview                     |n                   |                |                         |<cardPreview>                           |
     |#noOfCards                       |n                   |                |                         |<noOfCards>                             |
     |#progress                        |n                   |                |                         |<progress>                              |
     |#downloads                       |n                   |                |                         |<downloads>                             |
     |#deckAuthorName                  |n                   |                |                         |<deckAuthorName>                        |
     |#deckAuthorId                    |n                   |                |                         |<deckAuthorId>                          |
     |#thumbnailUrl                    |n                   |                |                         |<thumbnailUrl>                          |
     |#status                          |n                   |                |                         |<status>                                |
     |#starred                         |n                   |                |                         |<starred>                               |
     |#deckId                          |y                   |scenario        |deckId                   |                                        |
     |#serverDate                      |n                   |                |                         |<serverDate>                            |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the values inside the data stores
     |JSON Path                                            |Is Data Store Used? |Data Store Type |Data Store Variable Name |Value                                   |
     |-----------------------------------------------------|--------------------|----------------|-------------------------|----------------------------------------|
     |$[0].id                                              |y                   |scenario        |deckId                   |                                        |
     |$[0].title                                           |n                   |                |                         |API Deck3                               |
     |$[0].description                                     |n                   |                |                         |test description                        |
     |$[0].tags[0]                                         |n                   |                |                         |API tag1                                |
     |$[0].book.bookTitle                                  |n                   |                |                         |Automation3                             |
     |$[0].book.bookAuthor                                 |n                   |                |                         |Osanda Nimalarathna                     |
     |$[0].book.chapter                                    |n                   |                |                         |Chap. 04                                |
     |$[0].notificationSettings.areNotificationsEnabled    |n                   |                |                         |true                                    |
     |$[0].notificationSettings.notificationTime           |n                   |                |                         |08:00 AM                                |
     |$[0].notificationSettings.notificationFrequency      |n                   |                |                         |5                                       |
     |$[0].examDate                                        |n                   |                |                         |1512021142000                           |
     |$[0].userId                                          |n                   |                |                         |34                                      |
     |$[0].parentDeckId                                    |n                   |                |                         |5                                       |
     |$[0].archived                                        |n                   |                |                         |true                                    |
     |$[0].cardPreview                                     |n                   |                |                         |true                                    |
     |$[0].noOfCards                                       |n                   |                |                         |2                                       |
     |$[0].progress                                        |n                   |                |                         |3                                       |
     |$[0].downloads                                       |n                   |                |                         |12                                      |
     |$[0].deckAuthor                                      |n                   |                |                         |Osanda                                  |
     |$[0].deckAuthorId                                    |n                   |                |                         |6                                       |
     |$[0].status                                          |n                   |                |                         |Closed                                  |
     |$[0].expert                                          |n                   |                |                         |false                                   |
     |$[0].purchaseInfo.price                              |n                   |                |                         |0                                       |
     |$[0].userDeck                                        |n                   |                |                         |true                                    |
     |$[0].starred                                         |n                   |                |                         |true                                    |
     |$[0].categoryId                                      |n                   |                |                         |5a5db30a12ef181b0af109ba                |
     |$[0].tempDeckId                                      |n                   |                |                         |999                                     |


