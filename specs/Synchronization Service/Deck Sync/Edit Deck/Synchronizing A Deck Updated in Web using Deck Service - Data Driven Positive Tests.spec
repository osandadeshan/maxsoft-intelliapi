Synchronizing A Deck Updated in Web using Deck Service - Data Driven Positive Tests Specification
=================================================================================================
Date Created    : 02/07/2018
Version         : 1.0.0
Owner      	    : Osanda Deshan
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.


tags: sync_edit_an_existing_deck_updated_in_web, sync_edit_an_existing_deck_updated_in_web-positive_tests, positive


table: /resources/data_driven_test_csv/sync_deck/sync_edit_an_existing_deck_using_deck_service.csv



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



Synchronize edit an existing deck which has already edited in web
-----------------------------------------------------------------
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
     |#serverDate                      |n                   |                |                         |2018-02-06T09:40:26.456Z                |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                            |Value                                   |
     |-----------------------------------------------------|----------------------------------------|
     |$                                                    |[]                                      |


