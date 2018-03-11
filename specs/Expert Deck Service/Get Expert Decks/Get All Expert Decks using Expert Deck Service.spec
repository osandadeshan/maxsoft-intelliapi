Get All Expert Decks using Expert Deck Service Specification
============================================================
Date Created    : 01/20/2017
Version   		: 1.0.0
Owner      		: Kinkini Gamage
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.


tags: get_all_expert_decks



Create an expert deck
---------------------
* Given that a user needs to invoke "Create An Expert Deck using Expert Deck Service"
* And the user set the request authentication configurations as follows
      |Configuration                                                     |Configuration Value|
      |------------------------------------------------------------------|-------------------|
      |Is authentication required?                                       |Yes                |
      |Do you need to retrieve the access token from the text file?      |Yes                |
      |Provide the access token if you need to authorize the API manually|N/A                |
* And the user set the request attributes as follows
      |Attribute Value In JSON Template|Attribute Value To Be Set|
      |--------------------------------|-------------------------|
      |#isArchived                     |true                     |
      |#bookAuthor                     |Dilanka                  |
      |#bookTitle                      |Networking               |
      |#chapter                        |1                        |
      |#cardPreview                    |true                     |
      |#categoryId                     |5a544b4d41c1102b72930ea7 |
      |#createdAt                      |2018-01-30T04:03:33.042Z |
      |#deckAuthor                     |Dilanka                  |
      |#deckAuthorId                   |1                        |
      |#description                    |Computer networking      |
      |#downloads                      |0                        |
      |#time                           |12.00                    |
      |#id                             |1                        |
      |#keywords                       |Networking               |
      |#noOfCards                      |0                        |
      |#areNotificationsEnabled        |true                     |
      |#notificationFrequency          |1                        |
      |#notificationTime               |12.00                    |
      |#parentDeckId                   |Parent                   |
      |#progress                       |0                        |
      |#price                          |0                        |
      |#sku                            |0                        |
      |#starred                        |true                     |
      |#status                         |available                |
      |#subjectId                      |IT                       |
      |#tags                           |networking               |
      |#tempDeckId                     |1                        |
      |#thumbnailUrl                   |www.google.com           |
      |#title                          |Networking               |
      |#userId                         |dila                     |
* When the user invokes the API
* Then the status code for the request is "201"
* And the JSON Path Assertions for the response should be equal to the following
      |JSON Path                           |Expected Result       |
      |------------------------------------|----------------------|
      |$.title                             |Networking            |
      |$.userId                            |dila                  |
      |$.archived                          |true                  |
      |$.book.bookTitle                    |Networking            |



Get all expert decks
--------------------
tags: get_all_expert_decks, positive

* Given that a user needs to invoke "Search Expert Decks using Expert Deck Service"
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path           |Expected Result                    |
     |--------------------|-----------------------------------|
     |$[-1:].title        |Networking                         |
     |$[-1:].description  |Computer networking                |
     |$[-1:].subjectId    |IT                                 |
     |$[-1:].categoryId   |5a544b4d41c1102b72930ea7           |










