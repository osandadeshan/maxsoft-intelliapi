Create A Deck using Aggregation Service - Data Driven Positive Tests Specification
==================================================================================
Date Created    : 12/27/2017
Version         : 1.0.0
Owner      	    : Osanda Deshan
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.


tags: create_deck, create_deck-positive_tests, positive


table: /resources/data_driven_test_csv/create_deck/create_new_deck_using_aggregation_service.csv


* Given that a user needs to invoke <api>
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |



Create a Deck using valid payload
---------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set               |
     |--------------------------------|----------------------------------------|
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
* When the user invokes the API
* Then the status code for the request is "201"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                         |Value                                   |
     |--------------------------------------------------|----------------------------------------|
     |$.title                                           |<title>                                 |
     |$.description                                     |<description>                           |
     |$.tags[0]                                         |<tags1>                                 |
     |$.book.bookTitle                                  |<bookTitle>                             |
     |$.book.bookAuthor                                 |<bookAuthor>                            |
     |$.book.chapter                                    |<bookChapter>                           |
     |$.notificationSettings.areNotificationsEnabled    |<areNotificationsEnabled>               |
     |$.notificationSettings.notificationTime           |<notificationTime>                      |
     |$.notificationSettings.notificationFrequency      |<notificationFrequency>                 |
     |$.examDate                                        |<examDate>                              |
     |$.userId                                          |<userId>                                |
     |$.parentDeckId                                    |<parentDeckId>                          |
     |$.archived                                        |<archived>                              |
     |$.cardPreview                                     |<cardPreview>                           |
     |$.noOfCards                                       |<noOfCards>                             |
     |$.progress                                        |<progress>                              |
     |$.downloads                                       |<downloads>                             |
     |$.deckAuthor                                      |<deckAuthorName>                        |
     |$.deckAuthorId                                    |<deckAuthorId>                          |
     |$.thumbnailUrl                                    |<thumbnailUrl>                          |
     |$.status                                          |<status>                                |
     |$.expert                                          |false                                   |
     |$.purchaseInfo.price                              |0                                       |
     |$.starred                                         |<starred>                               |
     |$.categoryId                                      |<categoryId>                            |

