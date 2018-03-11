Synchronize Edit A Non Existing using Deck Service - Data Driven Positive Tests Specification
=============================================================================================
Date Created    : 02/07/2018
Version         : 1.0.0
Owner      	    : Osanda Deshan
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.


tags: sync_edit_a_non_existing_deck, sync_edit_a_non_existing_deck-positive_tests, positive


table: /resources/data_driven_test_csv/sync_deck/sync_edit_a_non_existing_deck_using_deck_service.csv



* Given that a user needs to invoke <api>
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |



Synchronize edit a non existing deck using valid payload
--------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set               |
     |--------------------------------|----------------------------------------|
     |#activityId                     |<activityId>                            |
     |#activityType                   |<activityType>                          |
     |#title                          |<title>                                 |
     |#description                    |<description>                           |
     |#tags1                          |<tags1>                                 |
     |#subjectId                      |<subjectId>                             |
     |#subjectName                    |<subjectName>                           |
     |#bookTitle                      |<bookTitle>                             |
     |#bookAuthor                     |<bookAuthor>                            |
     |#bookChapter                    |<bookChapter>                           |
     |#purchasedDate                  |<purchasedDate>                         |
     |#purchaseInformationPrice       |<purchaseInformationPrice>              |
     |#purchaseInformationsku         |<purchaseInformationsku>                |
     |#areNotificationsEnabled        |<areNotificationsEnabled>               |
     |#notificationTime               |<notificationTime>                      |
     |#notificationFrequency          |<notificationFrequency>                 |
     |#examDate                       |<examDate>                              |
     |#categoryId                     |<categoryId>                            |
     |#userId                         |<userId>                                |
     |#parentDeckId                   |<parentDeckId>                          |
     |#tempDeckId                     |<tempDeckId>                            |
     |#archived                       |<archived>                              |
     |#cardPreview                    |<cardPreview>                           |
     |#noOfCards                      |<noOfCards>                             |
     |#progress                       |<progress>                              |
     |#downloads                      |<downloads>                             |
     |#deckAuthorName                 |<deckAuthorName>                        |
     |#deckAuthorId                   |<deckAuthorId>                          |
     |#thumbnailUrl                   |<thumbnailUrl>                          |
     |#status                         |<status>                                |
     |#starred                        |<starred>                               |
     |#deckId                         |<tempDeckId>                            |
     |#serverDate                     |<serverDate>                            |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                            |Value                                   |
     |-----------------------------------------------------|----------------------------------------|
     |$                                                    |[]                                      |
