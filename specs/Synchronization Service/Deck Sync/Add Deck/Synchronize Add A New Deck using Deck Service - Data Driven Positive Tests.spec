Synchronize Add A New Deck using Deck Service - Data Driven Positive Tests Specification
========================================================================================
Date Created    : 02/07/2018
Version         : 1.0.0
Owner      	    : Osanda Deshan
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.


tags: sync_add_new_deck, sync_add_new_deck-positive_tests, positive


table: /resources/data_driven_test_csv/sync_deck/sync_add_a_new_deck_using_deck_service.csv


* Given that a user needs to invoke <api>
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |
 * And replace the row values in "tempDeckId" column of the CSV "\\resources\\data_driven_test_csv\\sync_deck\\sync_add_a_new_deck_using_deck_service.csv" into the "dd.MM.yyyy HH:mm:ss:SSSSSS" timestamp pattern



Synchronize add a new deck using valid payload
----------------------------------------------
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
     |$[0].title                                           |<title>                                 |
     |$[0].description                                     |<description>                           |
     |$[0].tags[0]                                         |<tags1>                                 |
     |$[0].book.bookTitle                                  |<bookTitle>                             |
     |$[0].book.bookAuthor                                 |<bookAuthor>                            |
     |$[0].book.chapter                                    |<bookChapter>                           |
     |$[0].notificationSettings.areNotificationsEnabled    |<areNotificationsEnabled>               |
     |$[0].notificationSettings.notificationTime           |<notificationTime>                      |
     |$[0].notificationSettings.notificationFrequency      |<notificationFrequency>                 |
     |$[0].examDate                                        |<examDate>                              |
     |$[0].userId                                          |<userId>                                |
     |$[0].parentDeckId                                    |<parentDeckId>                          |
     |$[0].archived                                        |<archived>                              |
     |$[0].cardPreview                                     |<cardPreview>                           |
     |$[0].noOfCards                                       |<noOfCards>                             |
     |$[0].progress                                        |<progress>                              |
     |$[0].downloads                                       |<downloads>                             |
     |$[0].deckAuthor                                      |<deckAuthorName>                        |
     |$[0].deckAuthorId                                    |<deckAuthorId>                          |
     |$[0].thumbnailUrl                                    |<thumbnailUrl>                          |
     |$[0].status                                          |<status>                                |
     |$[0].expert                                          |false                                   |
     |$[0].purchaseInfo.price                              |0                                       |
     |$[0].userDeck                                        |true                                    |
     |$[0].starred                                         |<starred>                               |
     |$[0].categoryId                                      |<categoryId>                            |
     |$[0].tempDeckId                                      |<tempDeckId>                            |
* And the JSON Path Assertions for the response should not be equal to the following
     |JSON Path                                            |Value                                   |
     |-----------------------------------------------------|----------------------------------------|
     |$[0].id                                              |<tempDeckId>                            |




