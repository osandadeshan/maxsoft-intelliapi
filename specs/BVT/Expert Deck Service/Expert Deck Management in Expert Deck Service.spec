Expert Deck Management in Expert Deck Service Specification
===========================================================
Date Created    : 02/15/2018
Version         : 1.0.0
Owner      	    : Osanda Deshan
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.


tags: bvt, expert_deck_management, expert_deck_service



* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |



Create an Expert Deck using all the attributes in the contract
--------------------------------------------------------------
* Given that a user needs to invoke "Create An Expert Deck using Expert Deck Service"
* And the user set the request attributes as follows
     |Attribute Value In JSON Template   |Attribute Value To Be Set                                   |
     |-----------------------------------|------------------------------------------------------------|
     |#isArchived                        |true                                                        |
     |#bookAuthorName                    |Osanda Deshan                                               |
     |#bookTitle                         |API Deck3                                                   |
     |#tags                              |API tag1                                                    |
     |#time                              |08:00 AM                                                    |
     |#chapter                           |Ch. 02                                                      |
     |#subjectId                         |21312wrwe23423df                                            |
     |#cardPreview                       |true                                                        |
     |#categoryId                        |345345345345                                                |
     |#deckAuthorName                    |Osanda Nimalarathna                                         |
     |#deckAuthorId                      |234325345345                                                |
     |#description                       |Deck has been created via an automated script               |
     |#downloads                         |328                                                         |
     |#examDate                          |2018-01-19T07:10:20.943Z                                    |
     |#keywords                          |API                                                         |
     |#noOfCards                         |12                                                          |
     |#areNotificationsEnabled           |false                                                       |
     |#notificationFrequency             |3 times a day                                               |
     |#notificationTime                  |09.30 AM                                                    |
     |#parentDeckId                      |13123123dsfsd231                                            |
     |#progress                          |45                                                          |
     |#price                             |99                                                          |
     |#purchasedDate                     |2018-01-19T07:10:20.943Z                                    |
     |#sku                               |test.purchase1                                              |
     |#starred                           |false                                                       |
     |#status                            |In Progress                                                 |
     |#tags1                             |API tag                                                     |
     |#tempDeckId                        |3242dfs435fdgdfg34                                          |
     |#thumbnailUrl                      |http://somehost/someimg.jpg                                 |
     |#title                             |API Automation using MaxSoft ATA Framework                  |
     |#userId                            |osan                                                        |
* When the user invokes the API
* Then the status code for the request is "201"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path     |Expected Result                             |
     |--------------|--------------------------------------------|
     |$.title       |API Automation using MaxSoft ATA Framework  |
     |$.userId      |osan                                        |
* And save the JSON Path values in the response inside the data stores
    |DataStore Type |Variable Name  |Value To Be Stored     |
    |---------------|---------------|-----------------------|
    |spec           |deckId         |$.id                   |



Edit the previously created deck
--------------------------------
* Given that a user needs to invoke "Edit An Expert Deck using Expert Deck Service"
* And the user set the path parameters using data stores as follows
    |Path Name      |Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value     |
    |---------------|-------------------|---------------|------------------------|---------------|
    |deckId         |y                  |spec           |deckId                  |N/A            |
* And the user set the request attributes as follows
     |Attribute Value In JSON Template   |Attribute Value To Be Set                                   |
     |-----------------------------------|------------------------------------------------------------|
     |#isArchived                        |true                                                        |
     |#bookAuthorName                    |Osanda Deshan                                               |
     |#bookTitle                         |API Deck3                                                   |
     |#tags                              |API tag1                                                    |
     |#time                              |08:00 AM                                                    |
     |#chapter                           |Ch. 02                                                      |
     |#subjectId                         |21312wrwe23423df                                            |
     |#chapter                           |Ch. 02                                                      |
     |#cardPreview                       |true                                                        |
     |#categoryId                        |345345345345                                                |
     |#deckAuthorName                    |Osanda Nimalarathna                                         |
     |#deckAuthorId                      |234325345345                                                |
     |#description                       |Deck has been created via an automated script               |
     |#downloads                         |328                                                         |
     |#examDate                          |2018-01-19T07:10:20.943Z                                    |
     |#keywords                          |API                                                         |
     |#noOfCards                         |12                                                          |
     |#areNotificationsEnabled           |false                                                       |
     |#notificationFrequency             |3 times a day                                               |
     |#notificationTime                  |09.30 AM                                                    |
     |#parentDeckId                      |13123123dsfsd231                                            |
     |#progress                          |45                                                          |
     |#price                             |99                                                          |
     |#purchasedDate                     |2018-01-19T07:10:20.943Z                                    |
     |#sku                               |test.purchase1                                              |
     |#starred                           |false                                                       |
     |#status                            |In Progress                                                 |
     |#tags1                             |API tag                                                     |
     |#tempDeckId                        |3242dfs435fdgdfg34                                          |
     |#thumbnailUrl                      |http://somehost/someimg.jpg                                 |
     |#title                             |API Automation using MaxSoft ATA Framework                  |
     |#userId                            |osan                                                        |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path     |Expected Result                             |
     |--------------|--------------------------------------------|
     |$.title       |API Automation using MaxSoft ATA Framework  |
     |$.userId      |osan                                        |



Get the previously created deck
-------------------------------
* Given that a user needs to invoke "Search Expert Decks using Expert Deck Service"
* And the user set the path parameters using data stores as follows
    |Path Name      |Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value     |
    |---------------|-------------------|---------------|------------------------|---------------|
    |deckId         |y                  |spec           |deckId                  |N/A            |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                         |Value                                                                                                                           |
     |--------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
     |$.title                                           |API Automation using MaxSoft ATA Framework                                                                                      |
     |$.tags[0]                                         |API tag1                                                                                                                        |
     |$.book.bookTitle                                  |API Deck3                                                                                                                       |
     |$.book.bookAuthor                                 |Osanda Deshan                                                                                                                   |
     |$.book.chapter                                    |Ch. 02                                                                                                                          |
     |$.purchaseInfo.price                              |99                                                                                                                              |
     |$.notificationSettings.areNotificationsEnabled    |false                                                                                                                           |
     |$.notificationSettings.notificationTime           |09.30 AM                                                                                                                        |
     |$.notificationSettings.notificationFrequency      |3 times a day                                                                                                                   |
     |$.examDate                                        |1517285013042                                                                                                                   |
     |$.userId                                          |osan                                                                                                                            |
     |$.parentDeckId                                    |13123123dsfsd231                                                                                                                |
     |$.tempDeckId                                      |3242dfs435fdgdfg34                                                                                                              |
     |$.archived                                        |true                                                                                                                            |
     |$.cardPreview                                     |true                                                                                                                            |
     |$.noOfCards                                       |12                                                                                                                              |
     |$.progress                                        |45                                                                                                                              |
     |$.downloads                                       |328                                                                                                                             |
     |$.deckAuthor                                      |Osanda Nimalarathna                                                                                                             |
     |$.deckAuthorId                                    |234325345345                                                                                                                    |
     |$.thumbnailUrl                                    |http://somehost/someimg.jpg                                                                                                     |
     |$.status                                          |In Progress                                                                                                                     |
     |$.expert                                          |true                                                                                                                            |
     |$.starred                                         |false                                                                                                                           |
     |$.categoryId                                      |345345345345                                                                                                                    |



Delete the previously created deck
----------------------------------
* Given that a user needs to invoke "Delete Expert Deck by ID using Expert Deck Service"
* And the user set the path parameters using data stores as follows
    |Path Name      |Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value     |
    |---------------|-------------------|---------------|------------------------|---------------|
    |deckId         |y                  |spec           |deckId                  |N/A            |
* When the user invokes the API
* Then the status code for the request is "200"