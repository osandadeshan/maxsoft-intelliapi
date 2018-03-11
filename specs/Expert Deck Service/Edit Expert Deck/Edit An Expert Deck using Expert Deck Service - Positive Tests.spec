Edit An Expert Deck using Expert Deck Service - Positive Tests Specification
============================================================================
Date Created    : 01/20/2018
Version         : 1.0.0
Owner      	    : Osanda Deshan
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.


tags: edit_expert_deck, edit_expert_deck-positive_tests, positive



* Create an expert deck
* And save the JSON Path values in the response inside the data stores
    |DataStore Type |Variable Name  |Value To Be Stored     |
    |---------------|---------------|-----------------------|
    |scenario       |expertDeckId   |$.id                   |
* Given that a user needs to invoke "Edit An Expert Deck using Expert Deck Service"
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |
* And the user set the path parameters using data stores as follows
    |Path Name      |Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value     |
    |---------------|-------------------|---------------|------------------------|---------------|
    |expertDeckId   |y                  |scenario       |expertDeckId            |N/A            |




Edit an Expert Deck using all the attributes in the contract
------------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template   |Attribute Value To Be Set                                   |
     |-----------------------------------|------------------------------------------------------------|
     |#isArchived                        |true                                                        |
     |#bookAuthorName                    |Osanda Deshan                                               |
     |#bookTitle                         |API Deck3                                                   |
     |#chapter                           |Ch. 02                                                      |
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
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path     |Expected Result                             |
     |--------------|--------------------------------------------|
     |$.title       |API Automation using MaxSoft ATA Framework  |
     |$.userId      |osan                                        |



Edit an Expert Deck only using deck title and userId
----------------------------------------------------
* And the user set the request payload as follows <file:/resources/payloads/create_expert_deck_only_using_deck_title_and_userId.txt>
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path     |Expected Result                             |
     |--------------|--------------------------------------------|
     |$.title       |Expert Deck using only userId and title     |
     |$.userId      |osan                                        |
