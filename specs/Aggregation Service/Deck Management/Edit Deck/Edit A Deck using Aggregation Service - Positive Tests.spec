Edit A Deck using Aggregation Service - Positive Tests Specification
====================================================================
Date Created    : 01/02/2018
Version         : 1.0.0
Owner      	    : Osanda Deshan
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.


tags: edit_deck, edit_deck-positive_tests, positive


* Create a deck
* And save the JSON Path values in the response inside the data stores
    |DataStore Type |Variable Name        |Value To Be Stored     |
    |---------------|---------------------|-----------------------|
    |scenario       |deckId               |$.id                   |
* Given that a user needs to invoke "Edit a Deck using Aggregation Service"
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



Edit a Deck only using deck title and userId
----------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template                      |Attribute Value To Be Set                                                                                          |
     |------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
     |#title                                                |API Deck3                                                                                                          |
     |"description": "#description",                        |                                                                                                                   |
     |"tags": [                                             |                                                                                                                   |
     |"#tags1"                                              |                                                                                                                   |
     |"subject": {                                          |                                                                                                                   |
     |"id": #subjectId,                                     |                                                                                                                   |
     |"name": "#subjectName"                                |                                                                                                                   |
     |"book": {                                             |                                                                                                                   |
     |"bookTitle": "#bookTitle",                            |                                                                                                                   |
     |"bookAuthor": "#bookAuthor",                          |                                                                                                                   |
     |"chapter": "#bookChapter"                             |                                                                                                                   |
     |"purchaseInformation": {                              |                                                                                                                   |
     |"purchasedDate": #purchasedDate,                      |                                                                                                                   |
     |"price": #purchaseInformationPrice,                   |                                                                                                                   |
     |"sku": "#purchaseInformationsku"                      |                                                                                                                   |
     |"notificationSettings": {                             |                                                                                                                   |
     |"areNotificationsEnabled": #areNotificationsEnabled,  |                                                                                                                   |
     |"notificationTime": "#notificationTime",              |                                                                                                                   |
     |"notificationFrequency": "#notificationFrequency"     |                                                                                                                   |
     |"examDate": #examDate,                                |                                                                                                                   |
     |"#userId",                                            |"Osanda Deshan"                                                                                                    |
     |"parentDeckId": "#parentDeckId",                      |                                                                                                                   |
     |"tempDeckId": "#tempDeckId",                          |                                                                                                                   |
     |"archived": #archived,                                |                                                                                                                   |
     |"cardPreview": #cardPreview,                          |                                                                                                                   |
     |"noOfCards": #noOfCards,                              |                                                                                                                   |
     |"categoryId": "#categoryId",                          |                                                                                                                   |
     |"progress": #progress,                                |                                                                                                                   |
     |"downloads": #downloads,                              |                                                                                                                   |
     |"deckAuthor": "#deckAuthorName",                      |                                                                                                                   |
     |"deckAuthorId": "#deckAuthorId",                      |                                                                                                                   |
     |"thumbnailUrl": "#thumbnailUrl",                      |                                                                                                                   |
     |"status": "#status",                                  |                                                                                                                   |
     |"starred": #starred                                   |                                                                                                                   |
     |],                                                    |                                                                                                                   |
     |},                                                    |                                                                                                                   |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path     |Value                            |
     |--------------|--------------------------------------------|
     |$.title       |API Deck3                                   |
     |$.userId      |Osanda Deshan                               |



Edit a Deck using a null value as the description
---------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                                                                          |
     |--------------------------------|-------------------------------------------------------------------------------------------------------------------|
     |#title                          |API Deck3                                                                                                          |
     |#description                    |"null"                                                                                                             |
     |#tags1                          |API tag1                                                                                                           |
     |#subjectId                      |2                                                                                                                  |
     |#subjectName                    |API Testing3                                                                                                       |
     |#bookTitle                      |Automation3                                                                                                        |
     |#bookAuthor                     |Osanda Nimalarathna                                                                                                |
     |#bookChapter                    |Chap. 04                                                                                                           |
     |#purchasedDate                  |1512021142001                                                                                                      |
     |#purchaseInformationPrice       |777                                                                                                                |
     |#purchaseInformationsku         |com.pearson.smartflashcards.test3                                                                                  |
     |#areNotificationsEnabled        |true                                                                                                               |
     |#notificationTime               |08:00                                                                                                           |
     |#notificationFrequency          |0                                                                                                                  |
     |#examDate                       |1512021142000                                                                                                      |
     |#userId                         |34                                                                                                                 |
     |#parentDeckId                   |5                                                                                                                  |
     |#tempDeckId                     |999                                                                                                                |
     |#archived                       |true                                                                                                               |
     |#cardPreview                    |true                                                                                                               |
     |#noOfCards                      |2                                                                                                                  |
     |#progress                       |3                                                                                                                  |
     |#downloads                      |12                                                                                                                 |
     |#deckAuthorName                 |Osanda                                                                                                             |
     |#deckAuthorId                   |6                                                                                                                  |
     |#thumbnailUrl                   |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a154f35d5b71d1a8a54dd58/download/public?format=ORIGINAL  |
     |#status                         |Closed                                                                                                             |
     |#starred                        |true                                                                                                               |
     |#categoryId                     |5a5db30a12ef181b0af109ba                                                                                           |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                         |Value                                                                                                                           |
     |--------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
     |$.title                                           |API Deck3                                                                                                                       |
     |$.tags[0]                                         |API tag1                                                                                                                        |
     |$.book.bookTitle                                  |Automation3                                                                                                                     |
     |$.book.bookAuthor                                 |Osanda Nimalarathna                                                                                                             |
     |$.book.chapter                                    |Chap. 04                                                                                                                        |
     |$.purchaseInfo.price                              |0                                                                                                                               |
     |$.notificationSettings.areNotificationsEnabled    |true                                                                                                                            |
     |$.notificationSettings.notificationTime           |08:00                                                                                                                        |
     |$.notificationSettings.notificationFrequency      |0                                                                                                                               |
     |$.examDate                                        |1512021142000                                                                                                                   |
     |$.userId                                          |34                                                                                                                              |
     |$.parentDeckId                                    |5                                                                                                                               |
     |$.tempDeckId                                      |999                                                                                                                             |
     |$.archived                                        |true                                                                                                                            |
     |$.cardPreview                                     |true                                                                                                                            |
     |$.noOfCards                                       |2                                                                                                                               |
     |$.progress                                        |3                                                                                                                               |
     |$.downloads                                       |12                                                                                                                              |
     |$.deckAuthor                                      |Osanda                                                                                                                          |
     |$.deckAuthorId                                    |6                                                                                                                               |
     |$.thumbnailUrl                                    |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a154f35d5b71d1a8a54dd58/download/public?format=ORIGINAL               |
     |$.status                                          |Closed                                                                                                                          |
     |$.expert                                          |false                                                                                                                           |
     |$.starred                                         |true                                                                                                                            |
     |$.categoryId                                      |5a5db30a12ef181b0af109ba                                                                                                        |



Edit a Deck using an empty value as the bookTitle
---------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                                                                          |
     |--------------------------------|-------------------------------------------------------------------------------------------------------------------|
     |#title                          |API Deck3                                                                                                          |
     |#description                    |Test description for API Deck3                                                                                     |
     |#tags1                          |API tag1                                                                                                           |
     |#subjectId                      |2                                                                                                                  |
     |#subjectName                    |API Testing3                                                                                                       |
     |#bookAuthor                     |Osanda Nimalarathna                                                                                                |
     |#bookTitle                      |                                                                                                                   |
     |#bookChapter                    |Chap. 04                                                                                                           |
     |#purchasedDate                  |1512021142001                                                                                                      |
     |#purchaseInformationPrice       |777                                                                                                                |
     |#purchaseInformationsku         |com.pearson.smartflashcards.test3                                                                                  |
     |#areNotificationsEnabled        |true                                                                                                               |
     |#notificationTime               |08:00                                                                                                           |
     |#notificationFrequency          |1                                                                                                                  |
     |#examDate                       |1512021142000                                                                                                      |
     |#userId                         |34                                                                                                                 |
     |#parentDeckId                   |5                                                                                                                  |
     |#tempDeckId                     |999                                                                                                                |
     |#archived                       |true                                                                                                               |
     |#cardPreview                    |true                                                                                                               |
     |#noOfCards                      |2                                                                                                                  |
     |#progress                       |3                                                                                                                  |
     |#downloads                      |12                                                                                                                 |
     |#deckAuthorName                 |Osanda                                                                                                             |
     |#deckAuthorId                   |6                                                                                                                  |
     |#thumbnailUrl                   |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a154f35d5b71d1a8a54dd58/download/public?format=ORIGINAL  |
     |#status                         |Closed                                                                                                             |
     |#starred                        |true                                                                                                               |
     |#categoryId                     |5a5db30a12ef181b0af109ba                                                                                           |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                         |Value                                                                                                                           |
     |--------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
     |$.title                                           |API Deck3                                                                                                                       |
     |$.description                                     |Test description for API Deck3                                                                                                  |
     |$.tags[0]                                         |API tag1                                                                                                                        |
     |$.book.bookAuthor                                 |Osanda Nimalarathna                                                                                                             |
     |$.book.chapter                                    |Chap. 04                                                                                                                        |
     |$.notificationSettings.areNotificationsEnabled    |true                                                                                                                            |
     |$.notificationSettings.notificationTime           |08:00                                                                                                                        |
     |$.notificationSettings.notificationFrequency      |1                                                                                                                               |
     |$.examDate                                        |1512021142000                                                                                                                   |
     |$.userId                                          |34                                                                                                                              |
     |$.parentDeckId                                    |5                                                                                                                               |
	 |$.tempDeckId                                      |999                                                                                                                             |
     |$.archived                                        |true                                                                                                                            |
     |$.cardPreview                                     |true                                                                                                                            |
     |$.noOfCards                                       |2                                                                                                                               |
     |$.progress                                        |3                                                                                                                               |
     |$.downloads                                       |12                                                                                                                              |
     |$.deckAuthor                                      |Osanda                                                                                                                          |
     |$.deckAuthorId                                    |6                                                                                                                               |
     |$.thumbnailUrl                                    |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a154f35d5b71d1a8a54dd58/download/public?format=ORIGINAL               |
     |$.status                                          |Closed                                                                                                                          |
     |$.expert                                          |false                                                                                                                           |
     |$.starred                                         |true                                                                                                                            |
     |$.purchaseInfo.price                              |0                                                                                                                               |
     |$.categoryId                                      |5a5db30a12ef181b0af109ba                                                                                                        |



Edit a Deck using a null value as the bookTitle
-------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                                                                          |
     |--------------------------------|-------------------------------------------------------------------------------------------------------------------|
     |#title                          |API Deck3                                                                                                          |
     |#description                    |Test description for API Deck3                                                                                     |
     |#tags1                          |API tag1                                                                                                           |
     |#subjectId                      |2                                                                                                                  |
     |#subjectName                    |API Testing3                                                                                                       |
     |#bookTitle                      |"null"                                                                                                             |
     |#bookAuthor                     |Osanda Nimalarathna                                                                                                |
     |#bookChapter                    |Chap. 04                                                                                                           |
     |#purchasedDate                  |1512021142001                                                                                                      |
     |#purchaseInformationPrice       |777                                                                                                                |
     |#purchaseInformationsku         |com.pearson.smartflashcards.test3                                                                                  |
     |#areNotificationsEnabled        |true                                                                                                               |
     |#notificationTime               |08:00                                                                                                           |
     |#notificationFrequency          |2                                                                                                                  |
     |#examDate                       |1512021142000                                                                                                      |
     |#userId                         |34                                                                                                                 |
     |#parentDeckId                   |5                                                                                                                  |
     |#tempDeckId                     |999                                                                                                                |
     |#archived                       |true                                                                                                               |
     |#cardPreview                    |true                                                                                                               |
     |#noOfCards                      |2                                                                                                                  |
     |#progress                       |3                                                                                                                  |
     |#downloads                      |12                                                                                                                 |
     |#deckAuthorName                 |Osanda                                                                                                             |
     |#deckAuthorId                   |6                                                                                                                  |
     |#thumbnailUrl                   |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a154f35d5b71d1a8a54dd58/download/public?format=ORIGINAL  |
     |#status                         |Closed                                                                                                             |
     |#starred                        |true                                                                                                               |
     |#categoryId                     |5a5db30a12ef181b0af109ba                                                                                           |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                         |Value                                                                                                                           |
     |--------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
     |$.title                                           |API Deck3                                                                                                                       |
     |$.description                                     |Test description for API Deck3                                                                                                  |
     |$.tags[0]                                         |API tag1                                                                                                                        |
     |$.book.bookAuthor                                 |Osanda Nimalarathna                                                                                                             |
     |$.book.chapter                                    |Chap. 04                                                                                                                        |
     |$.notificationSettings.areNotificationsEnabled    |true                                                                                                                            |
     |$.notificationSettings.notificationTime           |08:00                                                                                                                        |
     |$.notificationSettings.notificationFrequency      |2                                                                                                                               |
     |$.examDate                                        |1512021142000                                                                                                                   |
     |$.userId                                          |34                                                                                                                              |
     |$.parentDeckId                                    |5                                                                                                                               |
	 |$.tempDeckId                                      |999                                                                                                                             |
     |$.archived                                        |true                                                                                                                            |
     |$.cardPreview                                     |true                                                                                                                            |
     |$.noOfCards                                       |2                                                                                                                               |
     |$.progress                                        |3                                                                                                                               |
     |$.downloads                                       |12                                                                                                                              |
     |$.deckAuthor                                      |Osanda                                                                                                                          |
     |$.deckAuthorId                                    |6                                                                                                                               |
     |$.thumbnailUrl                                    |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a154f35d5b71d1a8a54dd58/download/public?format=ORIGINAL               |
     |$.status                                          |Closed                                                                                                                          |
     |$.expert                                          |false                                                                                                                           |
     |$.starred                                         |true                                                                                                                            |
     |$.purchaseInfo.price                              |0                                                                                                                               |
     |$.categoryId                                      |5a5db30a12ef181b0af109ba                                                                                                        |




Edit a Deck using an empty value as the bookAuthor
----------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                                                                          |
     |--------------------------------|-------------------------------------------------------------------------------------------------------------------|
     |#title                          |API Deck3                                                                                                          |
     |#description                    |Test description for API Deck3                                                                                     |
     |#tags1                          |API tag1                                                                                                           |
     |#subjectId                      |2                                                                                                                  |
     |#subjectName                    |API Testing3                                                                                                       |
     |#bookTitle                      |Automation3                                                                                                        |
     |#bookAuthor                     |                                                                                                                   |
     |#bookChapter                    |Chap. 04                                                                                                           |
     |#purchasedDate                  |1512021142001                                                                                                      |
     |#purchaseInformationPrice       |777                                                                                                                |
     |#purchaseInformationsku         |com.pearson.smartflashcards.test3                                                                                  |
     |#areNotificationsEnabled        |true                                                                                                               |
     |#notificationTime               |08:00                                                                                                           |
     |#notificationFrequency          |3                                                                                                                  |
     |#examDate                       |1512021142000                                                                                                      |
     |#userId                         |34                                                                                                                 |
     |#parentDeckId                   |5                                                                                                                  |
     |#tempDeckId                     |999                                                                                                                |
     |#archived                       |true                                                                                                               |
     |#cardPreview                    |true                                                                                                               |
     |#noOfCards                      |2                                                                                                                  |
     |#progress                       |3                                                                                                                  |
     |#downloads                      |12                                                                                                                 |
     |#deckAuthorName                 |Osanda                                                                                                             |
     |#deckAuthorId                   |6                                                                                                                  |
     |#thumbnailUrl                   |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a154f35d5b71d1a8a54dd58/download/public?format=ORIGINAL  |
     |#status                         |Closed                                                                                                             |
     |#starred                        |true                                                                                                               |
     |#categoryId                     |5a5db30a12ef181b0af109ba                                                                                           |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                         |Value                                                                                                                           |
     |--------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
     |$.title                                           |API Deck3                                                                                                                       |
     |$.description                                     |Test description for API Deck3                                                                                                  |
     |$.tags[0]                                         |API tag1                                                                                                                        |
     |$.book.bookTitle                                  |Automation3                                                                                                                     |
     |$.book.chapter                                    |Chap. 04                                                                                                                        |
     |$.notificationSettings.areNotificationsEnabled    |true                                                                                                                            |
     |$.notificationSettings.notificationTime           |08:00                                                                                                                        |
     |$.notificationSettings.notificationFrequency      |3                                                                                                                               |
     |$.examDate                                        |1512021142000                                                                                                                   |
     |$.userId                                          |34                                                                                                                              |
     |$.parentDeckId                                    |5                                                                                                                               |
	 |$.tempDeckId                                      |999                                                                                                                             |
     |$.archived                                        |true                                                                                                                            |
     |$.cardPreview                                     |true                                                                                                                            |
     |$.noOfCards                                       |2                                                                                                                               |
     |$.progress                                        |3                                                                                                                               |
     |$.downloads                                       |12                                                                                                                              |
     |$.deckAuthor                                      |Osanda                                                                                                                          |
     |$.deckAuthorId                                    |6                                                                                                                               |
     |$.thumbnailUrl                                    |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a154f35d5b71d1a8a54dd58/download/public?format=ORIGINAL               |
     |$.status                                          |Closed                                                                                                                          |
     |$.expert                                          |false                                                                                                                           |
     |$.starred                                         |true                                                                                                                            |
     |$.purchaseInfo.price                              |0                                                                                                                               |
     |$.categoryId                                      |5a5db30a12ef181b0af109ba                                                                                                        |




Edit a Deck using a null value as the bookAuthor
--------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                                                                          |
     |--------------------------------|-------------------------------------------------------------------------------------------------------------------|
     |#title                          |API Deck3                                                                                                          |
     |#description                    |Test description for API Deck3                                                                                     |
     |#tags1                          |API tag1                                                                                                           |
     |#subjectId                      |2                                                                                                                  |
     |#subjectName                    |API Testing3                                                                                                       |
     |#bookTitle                      |Automation3                                                                                                        |
     |#bookAuthor                     |"null"                                                                                                             |
     |#bookChapter                    |Chap. 04                                                                                                           |
     |#purchasedDate                  |1512021142001                                                                                                      |
     |#purchaseInformationPrice       |777                                                                                                                |
     |#purchaseInformationsku         |com.pearson.smartflashcards.test3                                                                                  |
     |#areNotificationsEnabled        |true                                                                                                               |
     |#notificationTime               |08:00                                                                                                           |
     |#notificationFrequency          |1                                                                                                                  |
     |#examDate                       |1512021142000                                                                                                      |
     |#userId                         |34                                                                                                                 |
     |#parentDeckId                   |5                                                                                                                  |
     |#tempDeckId                     |999                                                                                                                |
     |#archived                       |true                                                                                                               |
     |#cardPreview                    |true                                                                                                               |
     |#noOfCards                      |2                                                                                                                  |
     |#progress                       |3                                                                                                                  |
     |#downloads                      |12                                                                                                                 |
     |#deckAuthorName                 |Osanda                                                                                                             |
     |#deckAuthorId                   |6                                                                                                                  |
     |#thumbnailUrl                   |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a154f35d5b71d1a8a54dd58/download/public?format=ORIGINAL  |
     |#status                         |Closed                                                                                                             |
     |#starred                        |true                                                                                                               |
     |#categoryId                     |5a5db30a12ef181b0af109ba                                                                                           |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                         |Value                                                                                                                           |
     |--------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
     |$.title                                           |API Deck3                                                                                                                       |
     |$.description                                     |Test description for API Deck3                                                                                                  |
     |$.tags[0]                                         |API tag1                                                                                                                        |
     |$.book.bookTitle                                  |Automation3                                                                                                                     |
     |$.book.chapter                                    |Chap. 04                                                                                                                        |
     |$.notificationSettings.areNotificationsEnabled    |true                                                                                                                            |
     |$.notificationSettings.notificationTime           |08:00                                                                                                                        |
     |$.notificationSettings.notificationFrequency      |1                                                                                                                               |
     |$.examDate                                        |1512021142000                                                                                                                   |
     |$.userId                                          |34                                                                                                                              |
     |$.parentDeckId                                    |5                                                                                                                               |
	 |$.tempDeckId                                      |999                                                                                                                             |
     |$.archived                                        |true                                                                                                                            |
     |$.cardPreview                                     |true                                                                                                                            |
     |$.noOfCards                                       |2                                                                                                                               |
     |$.progress                                        |3                                                                                                                               |
     |$.downloads                                       |12                                                                                                                              |
     |$.deckAuthor                                      |Osanda                                                                                                                          |
     |$.deckAuthorId                                    |6                                                                                                                               |
     |$.thumbnailUrl                                    |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a154f35d5b71d1a8a54dd58/download/public?format=ORIGINAL               |
     |$.status                                          |Closed                                                                                                                          |
     |$.expert                                          |false                                                                                                                           |
     |$.starred                                         |true                                                                                                                            |
     |$.purchaseInfo.price                              |0                                                                                                                               |
     |$.categoryId                                      |5a5db30a12ef181b0af109ba                                                                                                        |




Edit a Deck using an empty value as the bookChapter
-----------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                                                                          |
     |--------------------------------|-------------------------------------------------------------------------------------------------------------------|
     |#title                          |API Deck3                                                                                                          |
     |#description                    |Test description for API Deck3                                                                                     |
     |#tags1                          |API tag1                                                                                                           |
     |#subjectId                      |2                                                                                                                  |
     |#subjectName                    |API Testing3                                                                                                       |
     |#bookTitle                      |Automation3                                                                                                        |
     |#bookAuthor                     |Osanda Nimalarathna                                                                                                |
     |#bookChapter                    |                                                                                                                   |
     |#purchasedDate                  |1512021142001                                                                                                      |
     |#purchaseInformationPrice       |777                                                                                                                |
     |#purchaseInformationsku         |com.pearson.smartflashcards.test3                                                                                  |
     |#areNotificationsEnabled        |true                                                                                                               |
     |#notificationTime               |08:00                                                                                                           |
     |#notificationFrequency          |2                                                                                                                  |
     |#examDate                       |1512021142000                                                                                                      |
     |#userId                         |34                                                                                                                 |
     |#parentDeckId                   |5                                                                                                                  |
     |#tempDeckId                     |999                                                                                                                |
     |#archived                       |true                                                                                                               |
     |#cardPreview                    |true                                                                                                               |
     |#noOfCards                      |2                                                                                                                  |
     |#progress                       |3                                                                                                                  |
     |#downloads                      |12                                                                                                                 |
     |#deckAuthorName                 |Osanda                                                                                                             |
     |#deckAuthorId                   |6                                                                                                                  |
     |#thumbnailUrl                   |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a154f35d5b71d1a8a54dd58/download/public?format=ORIGINAL  |
     |#status                         |Closed                                                                                                             |
     |#starred                        |true                                                                                                               |
     |#categoryId                     |5a5db30a12ef181b0af109ba                                                                                           |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                         |Value                                                                                                                           |
     |--------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
     |$.title                                           |API Deck3                                                                                                                       |
     |$.description                                     |Test description for API Deck3                                                                                                  |
     |$.tags[0]                                         |API tag1                                                                                                                        |
     |$.book.bookTitle                                  |Automation3                                                                                                                     |
     |$.book.bookAuthor                                 |Osanda Nimalarathna                                                                                                             |
     |$.notificationSettings.areNotificationsEnabled    |true                                                                                                                            |
     |$.notificationSettings.notificationTime           |08:00                                                                                                                        |
     |$.notificationSettings.notificationFrequency      |2                                                                                                                               |
     |$.examDate                                        |1512021142000                                                                                                                   |
     |$.userId                                          |34                                                                                                                              |
     |$.parentDeckId                                    |5                                                                                                                               |
	 |$.tempDeckId                                      |999                                                                                                                             |
     |$.archived                                        |true                                                                                                                            |
     |$.cardPreview                                     |true                                                                                                                            |
     |$.noOfCards                                       |2                                                                                                                               |
     |$.progress                                        |3                                                                                                                               |
     |$.downloads                                       |12                                                                                                                              |
     |$.deckAuthor                                      |Osanda                                                                                                                          |
     |$.deckAuthorId                                    |6                                                                                                                               |
     |$.thumbnailUrl                                    |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a154f35d5b71d1a8a54dd58/download/public?format=ORIGINAL               |
     |$.status                                          |Closed                                                                                                                          |
     |$.expert                                          |false                                                                                                                           |
     |$.starred                                         |true                                                                                                                            |
     |$.purchaseInfo.price                              |0                                                                                                                               |
     |$.categoryId                                      |5a5db30a12ef181b0af109ba                                                                                                        |




Edit a Deck using a null value as the bookChapter
---------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                                                                          |
     |--------------------------------|-------------------------------------------------------------------------------------------------------------------|
     |#title                          |API Deck3                                                                                                          |
     |#description                    |Test description for API Deck3                                                                                     |
     |#tags1                          |API tag1                                                                                                           |
     |#subjectId                      |2                                                                                                                  |
     |#subjectName                    |API Testing3                                                                                                       |
     |#bookTitle                      |Automation3                                                                                                        |
     |#bookAuthor                     |Osanda Nimalarathna                                                                                                |
     |#bookChapter                    |"null"                                                                                                             |
     |#purchasedDate                  |1512021142001                                                                                                      |
     |#purchaseInformationPrice       |777                                                                                                                |
     |#purchaseInformationsku         |com.pearson.smartflashcards.test3                                                                                  |
     |#areNotificationsEnabled        |true                                                                                                               |
     |#notificationTime               |08:00                                                                                                           |
     |#notificationFrequency          |3                                                                                                                  |
     |#examDate                       |1512021142000                                                                                                      |
     |#userId                         |34                                                                                                                 |
     |#parentDeckId                   |5                                                                                                                  |
     |#tempDeckId                     |999                                                                                                                |
     |#archived                       |true                                                                                                               |
     |#cardPreview                    |true                                                                                                               |
     |#noOfCards                      |2                                                                                                                  |
     |#progress                       |3                                                                                                                  |
     |#downloads                      |12                                                                                                                 |
     |#deckAuthorName                 |Osanda                                                                                                             |
     |#deckAuthorId                   |6                                                                                                                  |
     |#thumbnailUrl                   |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a154f35d5b71d1a8a54dd58/download/public?format=ORIGINAL  |
     |#status                         |Closed                                                                                                             |
     |#starred                        |true                                                                                                               |
     |#categoryId                     |5a5db30a12ef181b0af109ba                                                                                           |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                         |Value                                                                                                                           |
     |--------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
     |$.title                                           |API Deck3                                                                                                                       |
     |$.description                                     |Test description for API Deck3                                                                                                  |
     |$.tags[0]                                         |API tag1                                                                                                                        |
     |$.book.bookTitle                                  |Automation3                                                                                                                     |
     |$.book.bookAuthor                                 |Osanda Nimalarathna                                                                                                             |
     |$.notificationSettings.areNotificationsEnabled    |true                                                                                                                            |
     |$.notificationSettings.notificationTime           |08:00                                                                                                                        |
     |$.notificationSettings.notificationFrequency      |3                                                                                                                               |
     |$.examDate                                        |1512021142000                                                                                                                   |
     |$.userId                                          |34                                                                                                                              |
     |$.parentDeckId                                    |5                                                                                                                               |
	 |$.tempDeckId                                      |999                                                                                                                             |
     |$.archived                                        |true                                                                                                                            |
     |$.cardPreview                                     |true                                                                                                                            |
     |$.noOfCards                                       |2                                                                                                                               |
     |$.progress                                        |3                                                                                                                               |
     |$.downloads                                       |12                                                                                                                              |
     |$.deckAuthor                                      |Osanda                                                                                                                          |
     |$.deckAuthorId                                    |6                                                                                                                               |
     |$.thumbnailUrl                                    |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a154f35d5b71d1a8a54dd58/download/public?format=ORIGINAL               |
     |$.status                                          |Closed                                                                                                                          |
     |$.expert                                          |false                                                                                                                           |
     |$.starred                                         |true                                                                                                                            |
     |$.purchaseInfo.price                              |0                                                                                                                               |
     |$.categoryId                                      |5a5db30a12ef181b0af109ba                                                                                                        |




Edit a Deck using an empty value as the purchasedDate
-------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                                                                          |
     |--------------------------------|-------------------------------------------------------------------------------------------------------------------|
     |#title                          |API Deck3                                                                                                          |
     |#description                    |Test description for API Deck3                                                                                     |
     |#tags1                          |API tag1                                                                                                           |
     |#subjectId                      |2                                                                                                                  |
     |#subjectName                    |API Testing3                                                                                                       |
     |#bookTitle                      |Automation3                                                                                                        |
     |#bookAuthor                     |Osanda Nimalarathna                                                                                                |
     |#bookChapter                    |Chap. 04                                                                                                           |
     |#purchasedDate                  |""                                                                                                                 |
     |#purchaseInformationPrice       |777                                                                                                                |
     |#purchaseInformationsku         |com.pearson.smartflashcards.test3                                                                                  |
     |#areNotificationsEnabled        |true                                                                                                               |
     |#notificationTime               |08:00                                                                                                           |
     |#notificationFrequency          |1                                                                                                                  |
     |#examDate                       |1512021142000                                                                                                      |
     |#userId                         |34                                                                                                                 |
     |#parentDeckId                   |5                                                                                                                  |
     |#tempDeckId                     |999                                                                                                                |
     |#archived                       |true                                                                                                               |
     |#cardPreview                    |true                                                                                                               |
     |#noOfCards                      |2                                                                                                                  |
     |#progress                       |3                                                                                                                  |
     |#downloads                      |12                                                                                                                 |
     |#deckAuthorName                 |Osanda                                                                                                             |
     |#deckAuthorId                   |6                                                                                                                  |
     |#thumbnailUrl                   |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a154f35d5b71d1a8a54dd58/download/public?format=ORIGINAL  |
     |#status                         |Closed                                                                                                             |
     |#starred                        |true                                                                                                               |
     |#categoryId                     |5a5db30a12ef181b0af109ba                                                                                           |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                         |Value                                                                                                                           |
     |--------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
     |$.title                                           |API Deck3                                                                                                                       |
     |$.description                                     |Test description for API Deck3                                                                                                  |
     |$.tags[0]                                         |API tag1                                                                                                                        |
     |$.book.bookTitle                                  |Automation3                                                                                                                     |
     |$.book.bookAuthor                                 |Osanda Nimalarathna                                                                                                             |
     |$.notificationSettings.areNotificationsEnabled    |true                                                                                                                            |
     |$.notificationSettings.notificationTime           |08:00                                                                                                                        |
     |$.notificationSettings.notificationFrequency      |1                                                                                                                               |
     |$.examDate                                        |1512021142000                                                                                                                   |
     |$.userId                                          |34                                                                                                                              |
     |$.parentDeckId                                    |5                                                                                                                               |
	 |$.tempDeckId                                      |999                                                                                                                             |
     |$.archived                                        |true                                                                                                                            |
     |$.cardPreview                                     |true                                                                                                                            |
     |$.noOfCards                                       |2                                                                                                                               |
     |$.progress                                        |3                                                                                                                               |
     |$.downloads                                       |12                                                                                                                              |
     |$.deckAuthor                                      |Osanda                                                                                                                          |
     |$.deckAuthorId                                    |6                                                                                                                               |
     |$.thumbnailUrl                                    |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a154f35d5b71d1a8a54dd58/download/public?format=ORIGINAL               |
     |$.status                                          |Closed                                                                                                                          |
     |$.expert                                          |false                                                                                                                           |
     |$.starred                                         |true                                                                                                                            |
     |$.purchaseInfo.price                              |0                                                                                                                               |
     |$.categoryId                                      |5a5db30a12ef181b0af109ba                                                                                                        |


pugrchase date validation



Edit a Deck using a null value as the purchaseInformationSku
--------------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                                                                          |
     |--------------------------------|-------------------------------------------------------------------------------------------------------------------|
     |#title                          |API Deck3                                                                                                          |
     |#description                    |Test description for API Deck3                                                                                     |
     |#tags1                          |API tag1                                                                                                           |
     |#subjectId                      |2                                                                                                                  |
     |#subjectName                    |API Testing3                                                                                                       |
     |#bookTitle                      |Automation3                                                                                                        |
     |#bookAuthor                     |Osanda Nimalarathna                                                                                                |
     |#bookChapter                    |"null"                                                                                                             |
     |#purchasedDate                  |1512021142001                                                                                                      |
     |#purchaseInformationPrice       |777                                                                                                                |
     |#purchaseInformationsku         |"null"                                                                                                             |
     |#areNotificationsEnabled        |true                                                                                                               |
     |#notificationTime               |08:00                                                                                                           |
     |#notificationFrequency          |2                                                                                                                  |
     |#examDate                       |1512021142000                                                                                                      |
     |#userId                         |34                                                                                                                 |
     |#parentDeckId                   |5                                                                                                                  |
     |#tempDeckId                     |999                                                                                                                |
     |#archived                       |true                                                                                                               |
     |#cardPreview                    |true                                                                                                               |
     |#noOfCards                      |2                                                                                                                  |
     |#progress                       |3                                                                                                                  |
     |#downloads                      |12                                                                                                                 |
     |#deckAuthorName                 |Osanda                                                                                                             |
     |#deckAuthorId                   |6                                                                                                                  |
     |#thumbnailUrl                   |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a154f35d5b71d1a8a54dd58/download/public?format=ORIGINAL  |
     |#status                         |Closed                                                                                                             |
     |#starred                        |true                                                                                                               |
     |#categoryId                     |5a5db30a12ef181b0af109ba                                                                                           |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                         |Value                                                                                                                           |
     |--------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
     |$.title                                           |API Deck3                                                                                                                       |
     |$.description                                     |Test description for API Deck3                                                                                                  |
     |$.tags[0]                                         |API tag1                                                                                                                        |
     |$.book.bookTitle                                  |Automation3                                                                                                                     |
     |$.book.bookAuthor                                 |Osanda Nimalarathna                                                                                                             |
     |$.notificationSettings.areNotificationsEnabled    |true                                                                                                                            |
     |$.notificationSettings.notificationTime           |08:00                                                                                                                        |
     |$.notificationSettings.notificationFrequency      |2                                                                                                                               |
     |$.examDate                                        |1512021142000                                                                                                                   |
     |$.userId                                          |34                                                                                                                              |
     |$.parentDeckId                                    |5                                                                                                                               |
	 |$.tempDeckId                                      |999                                                                                                                             |
     |$.archived                                        |true                                                                                                                            |
     |$.cardPreview                                     |true                                                                                                                            |
     |$.noOfCards                                       |2                                                                                                                               |
     |$.progress                                        |3                                                                                                                               |
     |$.downloads                                       |12                                                                                                                              |
     |$.deckAuthor                                      |Osanda                                                                                                                          |
     |$.deckAuthorId                                    |6                                                                                                                               |
     |$.thumbnailUrl                                    |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a154f35d5b71d1a8a54dd58/download/public?format=ORIGINAL               |
     |$.status                                          |Closed                                                                                                                          |
     |$.expert                                          |false                                                                                                                           |
     |$.starred                                         |true                                                                                                                            |
     |$.purchaseInfo.price                              |0                                                                                                                               |
     |$.categoryId                                      |5a5db30a12ef181b0af109ba                                                                                                        |




Edit a Deck using a null value as the areNotificationsEnabled
---------------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                                                                          |
     |--------------------------------|-------------------------------------------------------------------------------------------------------------------|
     |#title                          |API Deck3                                                                                                          |
     |#description                    |Test description for API Deck3                                                                                     |
     |#tags1                          |API tag1                                                                                                           |
     |#subjectId                      |2                                                                                                                  |
     |#subjectName                    |API Testing3                                                                                                       |
     |#bookTitle                      |Automation3                                                                                                        |
     |#bookAuthor                     |Osanda Nimalarathna                                                                                                |
     |#bookChapter                    |Chap. 04                                                                                                           |
     |#purchasedDate                  |1512021142001                                                                                                      |
     |#purchaseInformationPrice       |777                                                                                                                |
     |#purchaseInformationsku         |com.pearson.smartflashcards.test3                                                                                  |
     |#areNotificationsEnabled        |null                                                                                                               |
     |#notificationTime               |08:00                                                                                                           |
     |#notificationFrequency          |2                                                                                                                  |
     |#examDate                       |1512021142000                                                                                                      |
     |#userId                         |34                                                                                                                 |
     |#parentDeckId                   |5                                                                                                                  |
     |#tempDeckId                     |999                                                                                                                |
     |#archived                       |true                                                                                                               |
     |#cardPreview                    |true                                                                                                               |
     |#noOfCards                      |2                                                                                                                  |
     |#progress                       |3                                                                                                                  |
     |#downloads                      |12                                                                                                                 |
     |#deckAuthorName                 |Osanda                                                                                                             |
     |#deckAuthorId                   |6                                                                                                                  |
     |#thumbnailUrl                   |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a154f35d5b71d1a8a54dd58/download/public?format=ORIGINAL  |
     |#status                         |Closed                                                                                                             |
     |#starred                        |true                                                                                                               |
     |#categoryId                     |5a5db30a12ef181b0af109ba                                                                                           |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                         |Value                                                                                                                           |
     |--------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
     |$.title                                           |API Deck3                                                                                                                       |
     |$.description                                     |Test description for API Deck3                                                                                                  |
     |$.tags[0]                                         |API tag1                                                                                                                        |
     |$.book.bookTitle                                  |Automation3                                                                                                                     |
     |$.book.bookAuthor                                 |Osanda Nimalarathna                                                                                                             |
     |$.book.chapter                                    |Chap. 04                                                                                                                        |
     |$.notificationSettings.areNotificationsEnabled    |false                                                                                                                           |
     |$.notificationSettings.notificationTime           |08:00                                                                                                                        |
     |$.notificationSettings.notificationFrequency      |2                                                                                                                               |
     |$.examDate                                        |1512021142000                                                                                                                   |
     |$.userId                                          |34                                                                                                                              |
     |$.parentDeckId                                    |5                                                                                                                               |
	 |$.tempDeckId                                      |999                                                                                                                             |
     |$.archived                                        |true                                                                                                                            |
     |$.cardPreview                                     |true                                                                                                                            |
     |$.noOfCards                                       |2                                                                                                                               |
     |$.progress                                        |3                                                                                                                               |
     |$.downloads                                       |12                                                                                                                              |
     |$.deckAuthor                                      |Osanda                                                                                                                          |
     |$.deckAuthorId                                    |6                                                                                                                               |
     |$.thumbnailUrl                                    |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a154f35d5b71d1a8a54dd58/download/public?format=ORIGINAL               |
     |$.status                                          |Closed                                                                                                                          |
     |$.expert                                          |false                                                                                                                           |
     |$.starred                                         |true                                                                                                                            |
     |$.purchaseInfo.price                              |0                                                                                                                               |
     |$.categoryId                                      |5a5db30a12ef181b0af109ba                                                                                                        |




Edit a Deck using a null value as the notificationTime
--------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                                                                          |
     |--------------------------------|-------------------------------------------------------------------------------------------------------------------|
     |#title                          |API Deck3                                                                                                          |
     |#description                    |Test description for API Deck3                                                                                     |
     |#tags1                          |API tag1                                                                                                           |
     |#subjectId                      |2                                                                                                                  |
     |#subjectName                    |API Testing3                                                                                                       |
     |#bookTitle                      |Automation3                                                                                                        |
     |#bookAuthor                     |Osanda Nimalarathna                                                                                                |
     |#bookChapter                    |Chap. 04                                                                                                           |
     |#purchasedDate                  |1512021142001                                                                                                      |
     |#purchaseInformationPrice       |777                                                                                                                |
     |#purchaseInformationsku         |com.pearson.smartflashcards.test3                                                                                  |
     |#areNotificationsEnabled        |true                                                                                                               |
     |#notificationTime               |"null"                                                                                                             |
     |#notificationFrequency          |1                                                                                                                  |
     |#examDate                       |1512021142000                                                                                                      |
     |#userId                         |34                                                                                                                 |
     |#parentDeckId                   |5                                                                                                                  |
     |#tempDeckId                     |999                                                                                                                |
     |#archived                       |true                                                                                                               |
     |#cardPreview                    |true                                                                                                               |
     |#noOfCards                      |2                                                                                                                  |
     |#progress                       |3                                                                                                                  |
     |#downloads                      |12                                                                                                                 |
     |#deckAuthorName                 |Osanda                                                                                                             |
     |#deckAuthorId                   |6                                                                                                                  |
     |#thumbnailUrl                   |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a154f35d5b71d1a8a54dd58/download/public?format=ORIGINAL  |
     |#status                         |Closed                                                                                                             |
     |#starred                        |true                                                                                                               |
     |#categoryId                     |5a5db30a12ef181b0af109ba                                                                                           |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                         |Value                                                                                                                           |
     |--------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
     |$.title                                           |API Deck3                                                                                                                       |
     |$.description                                     |Test description for API Deck3                                                                                                  |
     |$.tags[0]                                         |API tag1                                                                                                                        |
     |$.book.bookTitle                                  |Automation3                                                                                                                     |
     |$.book.bookAuthor                                 |Osanda Nimalarathna                                                                                                             |
     |$.book.chapter                                    |Chap. 04                                                                                                                        |
     |$.notificationSettings.areNotificationsEnabled    |true                                                                                                                            |
     |$.notificationSettings.notificationFrequency      |1                                                                                                                               |
     |$.examDate                                        |1512021142000                                                                                                                   |
     |$.userId                                          |34                                                                                                                              |
     |$.parentDeckId                                    |5                                                                                                                               |
	 |$.tempDeckId                                      |999                                                                                                                             |
     |$.archived                                        |true                                                                                                                            |
     |$.cardPreview                                     |true                                                                                                                            |
     |$.noOfCards                                       |2                                                                                                                               |
     |$.progress                                        |3                                                                                                                               |
     |$.downloads                                       |12                                                                                                                              |
     |$.deckAuthor                                      |Osanda                                                                                                                          |
     |$.deckAuthorId                                    |6                                                                                                                               |
     |$.thumbnailUrl                                    |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a154f35d5b71d1a8a54dd58/download/public?format=ORIGINAL               |
     |$.status                                          |Closed                                                                                                                          |
     |$.expert                                          |false                                                                                                                           |
     |$.starred                                         |true                                                                                                                            |
     |$.purchaseInfo.price                              |0                                                                                                                               |
     |$.categoryId                                      |5a5db30a12ef181b0af109ba                                                                                                        |




Edit a Deck using an empty value as the notificationTime
-----------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                                                                          |
     |--------------------------------|-------------------------------------------------------------------------------------------------------------------|
     |#title                          |API Deck3                                                                                                          |
     |#description                    |Test description for API Deck3                                                                                     |
     |#tags1                          |API tag1                                                                                                           |
     |#subjectId                      |2                                                                                                                  |
     |#subjectName                    |API Testing3                                                                                                       |
     |#bookTitle                      |Automation3                                                                                                        |
     |#bookAuthor                     |Osanda Nimalarathna                                                                                                |
     |#bookChapter                    |Chap. 04                                                                                                           |
     |#purchasedDate                  |1512021142001                                                                                                      |
     |#purchaseInformationPrice       |777                                                                                                                |
     |#purchaseInformationsku         |com.pearson.smartflashcards.test3                                                                                  |
     |#areNotificationsEnabled        |true                                                                                                               |
     |#notificationTime               |                                                                                                                   |
     |#notificationFrequency          |2                                                                                                                  |
     |#examDate                       |1512021142000                                                                                                      |
     |#userId                         |34                                                                                                                 |
     |#parentDeckId                   |5                                                                                                                  |
     |#tempDeckId                     |999                                                                                                                |
     |#archived                       |true                                                                                                               |
     |#cardPreview                    |true                                                                                                               |
     |#noOfCards                      |2                                                                                                                  |
     |#progress                       |3                                                                                                                  |
     |#downloads                      |12                                                                                                                 |
     |#deckAuthorName                 |Osanda                                                                                                             |
     |#deckAuthorId                   |6                                                                                                                  |
     |#thumbnailUrl                   |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a154f35d5b71d1a8a54dd58/download/public?format=ORIGINAL  |
     |#status                         |Closed                                                                                                             |
     |#starred                        |true                                                                                                               |
     |#categoryId                     |5a5db30a12ef181b0af109ba                                                                                           |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                         |Value                                                                                                                           |
     |--------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
     |$.title                                           |API Deck3                                                                                                                       |
     |$.description                                     |Test description for API Deck3                                                                                                  |
     |$.tags[0]                                         |API tag1                                                                                                                        |
     |$.book.bookTitle                                  |Automation3                                                                                                                     |
     |$.book.bookAuthor                                 |Osanda Nimalarathna                                                                                                             |
     |$.book.chapter                                    |Chap. 04                                                                                                                        |
     |$.notificationSettings.areNotificationsEnabled    |true                                                                                                                            |
     |$.notificationSettings.notificationFrequency      |2                                                                                                                               |
     |$.examDate                                        |1512021142000                                                                                                                   |
     |$.userId                                          |34                                                                                                                              |
     |$.parentDeckId                                    |5                                                                                                                               |
	 |$.tempDeckId                                      |999                                                                                                                             |
     |$.archived                                        |true                                                                                                                            |
     |$.cardPreview                                     |true                                                                                                                            |
     |$.noOfCards                                       |2                                                                                                                               |
     |$.progress                                        |3                                                                                                                               |
     |$.downloads                                       |12                                                                                                                              |
     |$.deckAuthor                                      |Osanda                                                                                                                          |
     |$.deckAuthorId                                    |6                                                                                                                               |
     |$.thumbnailUrl                                    |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a154f35d5b71d1a8a54dd58/download/public?format=ORIGINAL               |
     |$.status                                          |Closed                                                                                                                          |
     |$.expert                                          |false                                                                                                                           |
     |$.starred                                         |true                                                                                                                            |
     |$.purchaseInfo.price                              |0                                                                                                                               |
     |$.categoryId                                      |5a5db30a12ef181b0af109ba                                                                                                        |




Edit a Deck using an empty value as the examDate
--------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                                                                          |
     |--------------------------------|-------------------------------------------------------------------------------------------------------------------|
     |#title                          |API Deck3                                                                                                          |
     |#description                    |Test description for API Deck3                                                                                     |
     |#tags1                          |API tag1                                                                                                           |
     |#subjectId                      |2                                                                                                                  |
     |#subjectName                    |API Testing3                                                                                                       |
     |#bookTitle                      |Automation3                                                                                                        |
     |#bookAuthor                     |Osanda Nimalarathna                                                                                                |
     |#bookChapter                    |Chap. 04                                                                                                           |
     |#purchasedDate                  |1512021142001                                                                                                      |
     |#purchaseInformationPrice       |777                                                                                                                |
     |#purchaseInformationsku         |com.pearson.smartflashcards.test3                                                                                  |
     |#areNotificationsEnabled        |true                                                                                                               |
     |#notificationTime               |08:00                                                                                                           |
     |#notificationFrequency          |1                                                                                                                  |
     |#examDate                       |""                                                                                                                 |
     |#userId                         |34                                                                                                                 |
     |#parentDeckId                   |5                                                                                                                  |
     |#tempDeckId                     |999                                                                                                                |
     |#archived                       |true                                                                                                               |
     |#cardPreview                    |true                                                                                                               |
     |#noOfCards                      |2                                                                                                                  |
     |#progress                       |3                                                                                                                  |
     |#downloads                      |12                                                                                                                 |
     |#deckAuthorName                 |Osanda                                                                                                             |
     |#deckAuthorId                   |6                                                                                                                  |
     |#thumbnailUrl                   |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a154f35d5b71d1a8a54dd58/download/public?format=ORIGINAL  |
     |#status                         |Closed                                                                                                             |
     |#starred                        |true                                                                                                               |
     |#categoryId                     |5a5db30a12ef181b0af109ba                                                                                           |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                         |Value                                                                                                                           |
     |--------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
     |$.title                                           |API Deck3                                                                                                                       |
     |$.description                                     |Test description for API Deck3                                                                                                  |
     |$.tags[0]                                         |API tag1                                                                                                                        |
     |$.book.bookTitle                                  |Automation3                                                                                                                     |
     |$.book.bookAuthor                                 |Osanda Nimalarathna                                                                                                             |
     |$.book.chapter                                    |Chap. 04                                                                                                                        |
     |$.notificationSettings.areNotificationsEnabled    |true                                                                                                                            |
     |$.notificationSettings.notificationTime           |08:00                                                                                                                        |
     |$.notificationSettings.notificationFrequency      |1                                                                                                                               |
     |$.userId                                          |34                                                                                                                              |
     |$.parentDeckId                                    |5                                                                                                                               |
	 |$.tempDeckId                                      |999                                                                                                                             |
     |$.archived                                        |true                                                                                                                            |
     |$.cardPreview                                     |true                                                                                                                            |
     |$.noOfCards                                       |2                                                                                                                               |
     |$.progress                                        |3                                                                                                                               |
     |$.downloads                                       |12                                                                                                                              |
     |$.deckAuthor                                      |Osanda                                                                                                                          |
     |$.deckAuthorId                                    |6                                                                                                                               |
     |$.thumbnailUrl                                    |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a154f35d5b71d1a8a54dd58/download/public?format=ORIGINAL               |
     |$.status                                          |Closed                                                                                                                          |
     |$.expert                                          |false                                                                                                                           |
     |$.starred                                         |true                                                                                                                            |
     |$.purchaseInfo.price                              |0                                                                                                                               |
     |$.categoryId                                      |5a5db30a12ef181b0af109ba                                                                                                        |




Edit a Deck using an null value as the examDate
-------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                                                                          |
     |--------------------------------|-------------------------------------------------------------------------------------------------------------------|
     |#title                          |API Deck3                                                                                                          |
     |#description                    |Test description for API Deck3                                                                                     |
     |#tags1                          |API tag1                                                                                                           |
     |#subjectId                      |2                                                                                                                  |
     |#subjectName                    |API Testing3                                                                                                       |
     |#bookTitle                      |Automation3                                                                                                        |
     |#bookAuthor                     |Osanda Nimalarathna                                                                                                |
     |#bookChapter                    |Chap. 04                                                                                                           |
     |#purchasedDate                  |1512021142001                                                                                                      |
     |#purchaseInformationPrice       |777                                                                                                                |
     |#purchaseInformationsku         |com.pearson.smartflashcards.test3                                                                                  |
     |#areNotificationsEnabled        |true                                                                                                               |
     |#notificationTime               |08:00                                                                                                           |
     |#notificationFrequency          |2                                                                                                                  |
     |#examDate                       |null                                                                                                               |
     |#userId                         |34                                                                                                                 |
     |#parentDeckId                   |5                                                                                                                  |
     |#tempDeckId                     |999                                                                                                                |
     |#archived                       |true                                                                                                               |
     |#cardPreview                    |true                                                                                                               |
     |#noOfCards                      |2                                                                                                                  |
     |#progress                       |3                                                                                                                  |
     |#downloads                      |12                                                                                                                 |
     |#deckAuthorName                 |Osanda                                                                                                             |
     |#deckAuthorId                   |6                                                                                                                  |
     |#thumbnailUrl                   |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a154f35d5b71d1a8a54dd58/download/public?format=ORIGINAL  |
     |#status                         |Closed                                                                                                             |
     |#starred                        |true                                                                                                               |
     |#categoryId                     |5a5db30a12ef181b0af109ba                                                                                           |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                         |Value                                                                                                                           |
     |--------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
     |$.title                                           |API Deck3                                                                                                                       |
     |$.description                                     |Test description for API Deck3                                                                                                  |
     |$.tags[0]                                         |API tag1                                                                                                                        |
     |$.book.bookTitle                                  |Automation3                                                                                                                     |
     |$.book.bookAuthor                                 |Osanda Nimalarathna                                                                                                             |
     |$.book.chapter                                    |Chap. 04                                                                                                                        |
     |$.notificationSettings.areNotificationsEnabled    |true                                                                                                                            |
     |$.notificationSettings.notificationTime           |08:00                                                                                                                        |
     |$.notificationSettings.notificationFrequency      |2                                                                                                                               |
     |$.userId                                          |34                                                                                                                              |
     |$.parentDeckId                                    |5                                                                                                                               |
	 |$.tempDeckId                                      |999                                                                                                                             |
     |$.archived                                        |true                                                                                                                            |
     |$.cardPreview                                     |true                                                                                                                            |
     |$.noOfCards                                       |2                                                                                                                               |
     |$.progress                                        |3                                                                                                                               |
     |$.downloads                                       |12                                                                                                                              |
     |$.deckAuthor                                      |Osanda                                                                                                                          |
     |$.deckAuthorId                                    |6                                                                                                                               |
     |$.thumbnailUrl                                    |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a154f35d5b71d1a8a54dd58/download/public?format=ORIGINAL               |
     |$.status                                          |Closed                                                                                                                          |
     |$.expert                                          |false                                                                                                                           |
     |$.starred                                         |true                                                                                                                            |
     |$.purchaseInfo.price                              |0                                                                                                                               |
     |$.categoryId                                      |5a5db30a12ef181b0af109ba                                                                                                        |




Edit a Deck using a null value as the parentDeckId
----------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                                                                          |
     |--------------------------------|-------------------------------------------------------------------------------------------------------------------|
     |#title                          |API Deck3                                                                                                          |
     |#description                    |Test description for API Deck3                                                                                     |
     |#tags1                          |API tag1                                                                                                           |
     |#subjectId                      |2                                                                                                                  |
     |#subjectName                    |API Testing3                                                                                                       |
     |#bookTitle                      |Automation3                                                                                                        |
     |#bookAuthor                     |Osanda Nimalarathna                                                                                                |
     |#bookChapter                    |Chap. 04                                                                                                           |
     |#purchasedDate                  |1512021142001                                                                                                      |
     |#purchaseInformationPrice       |777                                                                                                                |
     |#purchaseInformationsku         |com.pearson.smartflashcards.test3                                                                                  |
     |#areNotificationsEnabled        |true                                                                                                               |
     |#notificationTime               |08:00                                                                                                           |
     |#notificationFrequency          |3                                                                                                                  |
     |#examDate                       |1512021142000                                                                                                      |
     |#userId                         |34                                                                                                                 |
     |#parentDeckId                   |"null"                                                                                                             |
     |#tempDeckId                     |999                                                                                                                |
     |#archived                       |true                                                                                                               |
     |#cardPreview                    |true                                                                                                               |
     |#noOfCards                      |2                                                                                                                  |
     |#progress                       |3                                                                                                                  |
     |#downloads                      |12                                                                                                                 |
     |#deckAuthorName                 |Osanda                                                                                                             |
     |#deckAuthorId                   |6                                                                                                                  |
     |#thumbnailUrl                   |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a154f35d5b71d1a8a54dd58/download/public?format=ORIGINAL  |
     |#status                         |Closed                                                                                                             |
     |#starred                        |true                                                                                                               |
     |#categoryId                     |5a5db30a12ef181b0af109ba                                                                                           |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                         |Value                                                                                                                           |
     |--------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
     |$.title                                           |API Deck3                                                                                                                       |
     |$.description                                     |Test description for API Deck3                                                                                                  |
     |$.tags[0]                                         |API tag1                                                                                                                        |
     |$.book.bookTitle                                  |Automation3                                                                                                                     |
     |$.book.bookAuthor                                 |Osanda Nimalarathna                                                                                                             |
     |$.book.chapter                                    |Chap. 04                                                                                                                        |
     |$.notificationSettings.areNotificationsEnabled    |true                                                                                                                            |
     |$.notificationSettings.notificationTime           |08:00                                                                                                                        |
     |$.notificationSettings.notificationFrequency      |3                                                                                                                               |
     |$.examDate                                        |1512021142000                                                                                                                   |
     |$.userId                                          |34                                                                                                                              |
	 |$.tempDeckId                                      |999                                                                                                                             |
     |$.archived                                        |true                                                                                                                            |
     |$.cardPreview                                     |true                                                                                                                            |
     |$.noOfCards                                       |2                                                                                                                               |
     |$.progress                                        |3                                                                                                                               |
     |$.downloads                                       |12                                                                                                                              |
     |$.deckAuthor                                      |Osanda                                                                                                                          |
     |$.deckAuthorId                                    |6                                                                                                                               |
     |$.thumbnailUrl                                    |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a154f35d5b71d1a8a54dd58/download/public?format=ORIGINAL               |
     |$.status                                          |Closed                                                                                                                          |
     |$.expert                                          |false                                                                                                                           |
     |$.starred                                         |true                                                                                                                            |
     |$.purchaseInfo.price                              |0                                                                                                                               |
     |$.categoryId                                      |5a5db30a12ef181b0af109ba                                                                                                        |




Edit a Deck using a null value as the archived
------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                                                                          |
     |--------------------------------|-------------------------------------------------------------------------------------------------------------------|
     |#title                          |API Deck3                                                                                                          |
     |#description                    |Test description for API Deck3                                                                                     |
     |#tags1                          |API tag1                                                                                                           |
     |#subjectId                      |2                                                                                                                  |
     |#subjectName                    |API Testing3                                                                                                       |
     |#bookTitle                      |Automation3                                                                                                        |
     |#bookAuthor                     |Osanda Nimalarathna                                                                                                |
     |#bookChapter                    |Chap. 04                                                                                                           |
     |#purchasedDate                  |1512021142001                                                                                                      |
     |#purchaseInformationPrice       |777                                                                                                                |
     |#purchaseInformationsku         |com.pearson.smartflashcards.test3                                                                                  |
     |#areNotificationsEnabled        |true                                                                                                               |
     |#notificationTime               |08:00                                                                                                           |
     |#notificationFrequency          |1                                                                                                                  |
     |#examDate                       |1512021142000                                                                                                      |
     |#userId                         |34                                                                                                                 |
     |#parentDeckId                   |5                                                                                                                  |
     |#tempDeckId                     |999                                                                                                                |
     |#archived                       |null                                                                                                               |
     |#cardPreview                    |true                                                                                                               |
     |#noOfCards                      |2                                                                                                                  |
     |#progress                       |3                                                                                                                  |
     |#downloads                      |12                                                                                                                 |
     |#deckAuthorName                 |Osanda                                                                                                             |
     |#deckAuthorId                   |6                                                                                                                  |
     |#thumbnailUrl                   |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a154f35d5b71d1a8a54dd58/download/public?format=ORIGINAL  |
     |#status                         |Closed                                                                                                             |
     |#starred                        |true                                                                                                               |
     |#categoryId                     |5a5db30a12ef181b0af109ba                                                                                           |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                         |Value                                                                                                                           |
     |--------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
     |$.title                                           |API Deck3                                                                                                                       |
     |$.description                                     |Test description for API Deck3                                                                                                  |
     |$.tags[0]                                         |API tag1                                                                                                                        |
     |$.book.bookTitle                                  |Automation3                                                                                                                     |
     |$.book.bookAuthor                                 |Osanda Nimalarathna                                                                                                             |
     |$.book.chapter                                    |Chap. 04                                                                                                                        |
     |$.notificationSettings.areNotificationsEnabled    |true                                                                                                                            |
     |$.notificationSettings.notificationTime           |08:00                                                                                                                        |
     |$.notificationSettings.notificationFrequency      |1                                                                                                                               |
     |$.examDate                                        |1512021142000                                                                                                                   |
     |$.userId                                          |34                                                                                                                              |
     |$.parentDeckId                                    |5                                                                                                                               |
	 |$.tempDeckId                                      |999                                                                                                                             |
     |$.archived                                        |false                                                                                                                           |
     |$.cardPreview                                     |true                                                                                                                            |
     |$.noOfCards                                       |2                                                                                                                               |
     |$.progress                                        |3                                                                                                                               |
     |$.downloads                                       |12                                                                                                                              |
     |$.deckAuthor                                      |Osanda                                                                                                                          |
     |$.deckAuthorId                                    |6                                                                                                                               |
     |$.thumbnailUrl                                    |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a154f35d5b71d1a8a54dd58/download/public?format=ORIGINAL               |
     |$.status                                          |Closed                                                                                                                          |
     |$.expert                                          |false                                                                                                                           |
     |$.starred                                         |true                                                                                                                            |
     |$.purchaseInfo.price                              |0                                                                                                                               |
     |$.categoryId                                      |5a5db30a12ef181b0af109ba                                                                                                        |




Edit a Deck using a null value as the cardPreview
---------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                                                                          |
     |--------------------------------|-------------------------------------------------------------------------------------------------------------------|
     |#title                          |API Deck3                                                                                                          |
     |#description                    |Test description for API Deck3                                                                                     |
     |#tags1                          |API tag1                                                                                                           |
     |#subjectId                      |2                                                                                                                  |
     |#subjectName                    |API Testing3                                                                                                       |
     |#bookTitle                      |Automation3                                                                                                        |
     |#bookAuthor                     |Osanda Nimalarathna                                                                                                |
     |#bookChapter                    |Chap. 04                                                                                                           |
     |#purchasedDate                  |1512021142001                                                                                                      |
     |#purchaseInformationPrice       |777                                                                                                                |
     |#purchaseInformationsku         |com.pearson.smartflashcards.test3                                                                                  |
     |#areNotificationsEnabled        |true                                                                                                               |
     |#notificationTime               |08:00                                                                                                           |
     |#notificationFrequency          |2                                                                                                                  |
     |#examDate                       |1512021142000                                                                                                      |
     |#userId                         |34                                                                                                                 |
     |#parentDeckId                   |2                                                                                                                  |
     |#tempDeckId                     |999                                                                                                                |
     |#archived                       |true                                                                                                               |
     |#cardPreview                    |null                                                                                                               |
     |#noOfCards                      |2                                                                                                                  |
     |#progress                       |3                                                                                                                  |
     |#downloads                      |12                                                                                                                 |
     |#deckAuthorName                 |Osanda                                                                                                             |
     |#deckAuthorId                   |6                                                                                                                  |
     |#thumbnailUrl                   |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a154f35d5b71d1a8a54dd58/download/public?format=ORIGINAL  |
     |#status                         |Closed                                                                                                             |
     |#starred                        |true                                                                                                               |
     |#categoryId                     |5a5db30a12ef181b0af109ba                                                                                           |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                         |Value                                                                                                                           |
     |--------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
     |$.title                                           |API Deck3                                                                                                                       |
     |$.description                                     |Test description for API Deck3                                                                                                  |
     |$.tags[0]                                         |API tag1                                                                                                                        |
     |$.book.bookTitle                                  |Automation3                                                                                                                     |
     |$.book.bookAuthor                                 |Osanda Nimalarathna                                                                                                             |
     |$.book.chapter                                    |Chap. 04                                                                                                                        |
     |$.notificationSettings.areNotificationsEnabled    |true                                                                                                                            |
     |$.notificationSettings.notificationTime           |08:00                                                                                                                        |
     |$.notificationSettings.notificationFrequency      |2                                                                                                                               |
     |$.examDate                                        |1512021142000                                                                                                                   |
     |$.userId                                          |34                                                                                                                              |
     |$.parentDeckId                                    |2                                                                                                                               |
	 |$.tempDeckId                                      |999                                                                                                                             |
     |$.archived                                        |true                                                                                                                            |
     |$.cardPreview                                     |false                                                                                                                           |
     |$.noOfCards                                       |2                                                                                                                               |
     |$.progress                                        |3                                                                                                                               |
     |$.downloads                                       |12                                                                                                                              |
     |$.deckAuthor                                      |Osanda                                                                                                                          |
     |$.deckAuthorId                                    |6                                                                                                                               |
     |$.thumbnailUrl                                    |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a154f35d5b71d1a8a54dd58/download/public?format=ORIGINAL               |
     |$.status                                          |Closed                                                                                                                          |
     |$.expert                                          |false                                                                                                                           |
     |$.starred                                         |true                                                                                                                            |
     |$.purchaseInfo.price                              |0                                                                                                                               |
     |$.categoryId                                      |5a5db30a12ef181b0af109ba                                                                                                        |





Edit a Deck using an empty value as the noOfCards
---------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                                                                          |
     |--------------------------------|-------------------------------------------------------------------------------------------------------------------|
     |#title                          |API Deck3                                                                                                          |
     |#description                    |Test description for API Deck3                                                                                     |
     |#tags1                          |API tag1                                                                                                           |
     |#subjectId                      |2                                                                                                                  |
     |#subjectName                    |API Testing3                                                                                                       |
     |#bookTitle                      |Automation3                                                                                                        |
     |#bookAuthor                     |Osanda Nimalarathna                                                                                                |
     |#bookChapter                    |Chap. 04                                                                                                           |
     |#purchasedDate                  |1512021142001                                                                                                      |
     |#purchaseInformationPrice       |777                                                                                                                |
     |#purchaseInformationsku         |com.pearson.smartflashcards.test3                                                                                  |
     |#areNotificationsEnabled        |true                                                                                                               |
     |#notificationTime               |08:00                                                                                                           |
     |#notificationFrequency          |1                                                                                                                  |
     |#examDate                       |1512021142000                                                                                                      |
     |#userId                         |34                                                                                                                 |
     |#parentDeckId                   |5                                                                                                                  |
     |#tempDeckId                     |999                                                                                                                |
     |#archived                       |true                                                                                                               |
     |#cardPreview                    |true                                                                                                               |
     |#noOfCards                      |""                                                                                                                 |
     |#progress                       |3                                                                                                                  |
     |#downloads                      |12                                                                                                                 |
     |#deckAuthorName                 |Osanda                                                                                                             |
     |#deckAuthorId                   |6                                                                                                                  |
     |#thumbnailUrl                   |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a154f35d5b71d1a8a54dd58/download/public?format=ORIGINAL  |
     |#status                         |Closed                                                                                                             |
     |#starred                        |true                                                                                                               |
     |#categoryId                     |5a5db30a12ef181b0af109ba                                                                                           |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                         |Value                                                                                                                           |
     |--------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
     |$.title                                           |API Deck3                                                                                                                       |
     |$.description                                     |Test description for API Deck3                                                                                                  |
     |$.tags[0]                                         |API tag1                                                                                                                        |
     |$.book.bookTitle                                  |Automation3                                                                                                                     |
     |$.book.bookAuthor                                 |Osanda Nimalarathna                                                                                                             |
     |$.book.chapter                                    |Chap. 04                                                                                                                        |
     |$.notificationSettings.areNotificationsEnabled    |true                                                                                                                            |
     |$.notificationSettings.notificationTime           |08:00                                                                                                                        |
     |$.notificationSettings.notificationFrequency      |1                                                                                                                               |
     |$.examDate                                        |1512021142000                                                                                                                   |
     |$.userId                                          |34                                                                                                                              |
     |$.parentDeckId                                    |5                                                                                                                               |
	 |$.tempDeckId                                      |999                                                                                                                             |
     |$.archived                                        |true                                                                                                                            |
     |$.cardPreview                                     |true                                                                                                                            |
     |$.noOfCards                                       |0                                                                                                                               |
     |$.progress                                        |3                                                                                                                               |
     |$.downloads                                       |12                                                                                                                              |
     |$.deckAuthor                                      |Osanda                                                                                                                          |
     |$.deckAuthorId                                    |6                                                                                                                               |
     |$.thumbnailUrl                                    |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a154f35d5b71d1a8a54dd58/download/public?format=ORIGINAL               |
     |$.status                                          |Closed                                                                                                                          |
     |$.expert                                          |false                                                                                                                           |
     |$.starred                                         |true                                                                                                                            |
     |$.purchaseInfo.price                              |0                                                                                                                               |
     |$.categoryId                                      |5a5db30a12ef181b0af109ba                                                                                                        |



Edit a Deck using a null value as the progress
------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                                                                          |
     |--------------------------------|-------------------------------------------------------------------------------------------------------------------|
     |#title                          |API Deck3                                                                                                          |
     |#description                    |Test description for API Deck3                                                                                     |
     |#tags1                          |API tag1                                                                                                           |
     |#subjectId                      |2                                                                                                                  |
     |#subjectName                    |API Testing3                                                                                                       |
     |#bookTitle                      |Automation3                                                                                                        |
     |#bookAuthor                     |Osanda Nimalarathna                                                                                                |
     |#bookChapter                    |Chap. 04                                                                                                           |
     |#purchasedDate                  |1512021142001                                                                                                      |
     |#purchaseInformationPrice       |777                                                                                                                |
     |#purchaseInformationsku         |com.pearson.smartflashcards.test3                                                                                  |
     |#areNotificationsEnabled        |true                                                                                                               |
     |#notificationTime               |08:00                                                                                                           |
     |#notificationFrequency          |1                                                                                                                  |
     |#examDate                       |1512021142000                                                                                                      |
     |#userId                         |34                                                                                                                 |
     |#parentDeckId                   |5                                                                                                                  |
     |#tempDeckId                     |999                                                                                                                |
     |#archived                       |true                                                                                                               |
     |#cardPreview                    |true                                                                                                               |
     |#noOfCards                      |2                                                                                                                  |
     |#progress                       |null                                                                                                               |
     |#downloads                      |12                                                                                                                 |
     |#deckAuthorName                 |Osanda                                                                                                             |
     |#deckAuthorId                   |6                                                                                                                  |
     |#thumbnailUrl                   |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a154f35d5b71d1a8a54dd58/download/public?format=ORIGINAL  |
     |#status                         |Closed                                                                                                             |
     |#starred                        |true                                                                                                               |
     |#categoryId                     |5a5db30a12ef181b0af109ba                                                                                           |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                         |Value                                                                                                                           |
     |--------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
     |$.title                                           |API Deck3                                                                                                                       |
     |$.description                                     |Test description for API Deck3                                                                                                  |
     |$.tags[0]                                         |API tag1                                                                                                                        |
     |$.book.bookTitle                                  |Automation3                                                                                                                     |
     |$.book.bookAuthor                                 |Osanda Nimalarathna                                                                                                             |
     |$.book.chapter                                    |Chap. 04                                                                                                                        |
     |$.notificationSettings.areNotificationsEnabled    |true                                                                                                                            |
     |$.notificationSettings.notificationTime           |08:00                                                                                                                        |
     |$.notificationSettings.notificationFrequency      |1                                                                                                                               |
     |$.examDate                                        |1512021142000                                                                                                                   |
     |$.userId                                          |34                                                                                                                              |
     |$.parentDeckId                                    |5                                                                                                                               |
	 |$.tempDeckId                                      |999                                                                                                                             |
     |$.archived                                        |true                                                                                                                            |
     |$.cardPreview                                     |true                                                                                                                            |
     |$.noOfCards                                       |2                                                                                                                               |
     |$.progress                                        |0                                                                                                                               |
     |$.downloads                                       |12                                                                                                                              |
     |$.deckAuthor                                      |Osanda                                                                                                                          |
     |$.deckAuthorId                                    |6                                                                                                                               |
     |$.thumbnailUrl                                    |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a154f35d5b71d1a8a54dd58/download/public?format=ORIGINAL               |
     |$.status                                          |Closed                                                                                                                          |
     |$.expert                                          |false                                                                                                                           |
     |$.starred                                         |true                                                                                                                            |
     |$.purchaseInfo.price                              |0                                                                                                                               |
     |$.categoryId                                      |5a5db30a12ef181b0af109ba                                                                                                        |




Edit a Deck using a null value as the downloads
-------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                                                                          |
     |--------------------------------|-------------------------------------------------------------------------------------------------------------------|
     |#title                          |API Deck3                                                                                                          |
     |#description                    |Test description for API Deck3                                                                                     |
     |#tags1                          |API tag1                                                                                                           |
     |#subjectId                      |2                                                                                                                  |
     |#subjectName                    |API Testing3                                                                                                       |
     |#bookTitle                      |Automation3                                                                                                        |
     |#bookAuthor                     |Osanda Nimalarathna                                                                                                |
     |#bookChapter                    |Chap. 04                                                                                                           |
     |#purchasedDate                  |1512021142001                                                                                                      |
     |#purchaseInformationPrice       |777                                                                                                                |
     |#purchaseInformationsku         |com.pearson.smartflashcards.test3                                                                                  |
     |#areNotificationsEnabled        |true                                                                                                               |
     |#notificationTime               |08:00                                                                                                           |
     |#notificationFrequency          |2                                                                                                                  |
     |#examDate                       |1512021142000                                                                                                      |
     |#userId                         |34                                                                                                                 |
     |#parentDeckId                   |5                                                                                                                  |
     |#tempDeckId                     |999                                                                                                                |
     |#archived                       |true                                                                                                               |
     |#cardPreview                    |true                                                                                                               |
     |#noOfCards                      |2                                                                                                                  |
     |#progress                       |3                                                                                                                  |
     |#downloads                      |null                                                                                                               |
     |#deckAuthorName                 |Osanda                                                                                                             |
     |#deckAuthorId                   |6                                                                                                                  |
     |#thumbnailUrl                   |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a154f35d5b71d1a8a54dd58/download/public?format=ORIGINAL  |
     |#status                         |Closed                                                                                                             |
     |#starred                        |true                                                                                                               |
     |#categoryId                     |5a5db30a12ef181b0af109ba                                                                                           |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                         |Value                                                                                                                           |
     |--------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
     |$.title                                           |API Deck3                                                                                                                       |
     |$.description                                     |Test description for API Deck3                                                                                                  |
     |$.tags[0]                                         |API tag1                                                                                                                        |
     |$.book.bookTitle                                  |Automation3                                                                                                                     |
     |$.book.bookAuthor                                 |Osanda Nimalarathna                                                                                                             |
     |$.book.chapter                                    |Chap. 04                                                                                                                        |
     |$.notificationSettings.areNotificationsEnabled    |true                                                                                                                            |
     |$.notificationSettings.notificationTime           |08:00                                                                                                                        |
     |$.notificationSettings.notificationFrequency      |2                                                                                                                               |
     |$.examDate                                        |1512021142000                                                                                                                   |
     |$.userId                                          |34                                                                                                                              |
     |$.parentDeckId                                    |5                                                                                                                               |
	 |$.tempDeckId                                      |999                                                                                                                             |
     |$.archived                                        |true                                                                                                                            |
     |$.cardPreview                                     |true                                                                                                                            |
     |$.noOfCards                                       |2                                                                                                                               |
     |$.progress                                        |3                                                                                                                               |
     |$.downloads                                       |0                                                                                                                               |
     |$.deckAuthor                                      |Osanda                                                                                                                          |
     |$.deckAuthorId                                    |6                                                                                                                               |
     |$.thumbnailUrl                                    |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a154f35d5b71d1a8a54dd58/download/public?format=ORIGINAL               |
     |$.status                                          |Closed                                                                                                                          |
     |$.expert                                          |false                                                                                                                           |
     |$.starred                                         |true                                                                                                                            |
     |$.purchaseInfo.price                              |0                                                                                                                               |
     |$.categoryId                                      |5a5db30a12ef181b0af109ba                                                                                                        |




Edit a Deck using a null value as the deckAuthorName
------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                                                                          |
     |--------------------------------|-------------------------------------------------------------------------------------------------------------------|
     |#title                          |API Deck3                                                                                                          |
     |#description                    |Test description for API Deck3                                                                                     |
     |#tags1                          |API tag1                                                                                                           |
     |#subjectId                      |2                                                                                                                  |
     |#subjectName                    |API Testing3                                                                                                       |
     |#bookTitle                      |Automation3                                                                                                        |
     |#bookAuthor                     |Osanda Nimalarathna                                                                                                |
     |#bookChapter                    |Chap. 04                                                                                                           |
     |#purchasedDate                  |1512021142001                                                                                                      |
     |#purchaseInformationPrice       |777                                                                                                                |
     |#purchaseInformationsku         |com.pearson.smartflashcards.test3                                                                                  |
     |#areNotificationsEnabled        |true                                                                                                               |
     |#notificationTime               |08:00                                                                                                           |
     |#notificationFrequency          |3                                                                                                                  |
     |#examDate                       |1512021142000                                                                                                      |
     |#userId                         |34                                                                                                                 |
     |#parentDeckId                   |5                                                                                                                  |
     |#tempDeckId                     |999                                                                                                                |
     |#archived                       |true                                                                                                               |
     |#cardPreview                    |true                                                                                                               |
     |#noOfCards                      |2                                                                                                                  |
     |#progress                       |3                                                                                                                  |
     |#downloads                      |12                                                                                                                 |
     |#deckAuthorName                 |"null"                                                                                                             |
     |#deckAuthorId                   |6                                                                                                                  |
     |#thumbnailUrl                   |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a154f35d5b71d1a8a54dd58/download/public?format=ORIGINAL  |
     |#status                         |Closed                                                                                                             |
     |#starred                        |true                                                                                                               |
     |#categoryId                     |5a5db30a12ef181b0af109ba                                                                                           |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                         |Value                                                                                                                           |
     |--------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
     |$.title                                           |API Deck3                                                                                                                       |
     |$.description                                     |Test description for API Deck3                                                                                                  |
     |$.tags[0]                                         |API tag1                                                                                                                        |
     |$.book.bookTitle                                  |Automation3                                                                                                                     |
     |$.book.bookAuthor                                 |Osanda Nimalarathna                                                                                                             |
     |$.book.chapter                                    |Chap. 04                                                                                                                        |
     |$.notificationSettings.areNotificationsEnabled    |true                                                                                                                            |
     |$.notificationSettings.notificationTime           |08:00                                                                                                                        |
     |$.notificationSettings.notificationFrequency      |3                                                                                                                               |
     |$.examDate                                        |1512021142000                                                                                                                   |
     |$.userId                                          |34                                                                                                                              |
     |$.parentDeckId                                    |5                                                                                                                               |
	 |$.tempDeckId                                      |999                                                                                                                             |
     |$.archived                                        |true                                                                                                                            |
     |$.cardPreview                                     |true                                                                                                                            |
     |$.noOfCards                                       |2                                                                                                                               |
     |$.progress                                        |3                                                                                                                               |
     |$.downloads                                       |12                                                                                                                              |
     |$.deckAuthorId                                    |6                                                                                                                               |
     |$.thumbnailUrl                                    |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a154f35d5b71d1a8a54dd58/download/public?format=ORIGINAL               |
     |$.status                                          |Closed                                                                                                                          |
     |$.expert                                          |false                                                                                                                           |
     |$.starred                                         |true                                                                                                                            |
     |$.purchaseInfo.price                              |0                                                                                                                               |
     |$.categoryId                                      |5a5db30a12ef181b0af109ba                                                                                                        |




Edit a Deck using a null value as the deckAuthorId
----------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                                                                          |
     |--------------------------------|-------------------------------------------------------------------------------------------------------------------|
     |#title                          |API Deck3                                                                                                          |
     |#description                    |Test description for API Deck3                                                                                     |
     |#tags1                          |API tag1                                                                                                           |
     |#subjectId                      |2                                                                                                                  |
     |#subjectName                    |API Testing3                                                                                                       |
     |#bookTitle                      |Automation3                                                                                                        |
     |#bookAuthor                     |Osanda Nimalarathna                                                                                                |
     |#bookChapter                    |Chap. 04                                                                                                           |
     |#purchasedDate                  |1512021142001                                                                                                      |
     |#purchaseInformationPrice       |777                                                                                                                |
     |#purchaseInformationsku         |com.pearson.smartflashcards.test3                                                                                  |
     |#areNotificationsEnabled        |true                                                                                                               |
     |#notificationTime               |08:00                                                                                                           |
     |#notificationFrequency          |1                                                                                                                  |
     |#examDate                       |1512021142000                                                                                                      |
     |#userId                         |34                                                                                                                 |
     |#parentDeckId                   |5                                                                                                                  |
     |#tempDeckId                     |999                                                                                                                |
     |#archived                       |true                                                                                                               |
     |#cardPreview                    |true                                                                                                               |
     |#noOfCards                      |2                                                                                                                  |
     |#progress                       |3                                                                                                                  |
     |#downloads                      |12                                                                                                                 |
     |#deckAuthorName                 |Osanda                                                                                                             |
     |#deckAuthorId                   |"null"                                                                                                             |
     |#thumbnailUrl                   |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a154f35d5b71d1a8a54dd58/download/public?format=ORIGINAL  |
     |#status                         |Closed                                                                                                             |
     |#starred                        |true                                                                                                               |
     |#categoryId                     |5a5db30a12ef181b0af109ba                                                                                           |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                         |Value                                                                                                                           |
     |--------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
     |$.title                                           |API Deck3                                                                                                                       |
     |$.description                                     |Test description for API Deck3                                                                                                  |
     |$.tags[0]                                         |API tag1                                                                                                                        |
     |$.book.bookTitle                                  |Automation3                                                                                                                     |
     |$.book.bookAuthor                                 |Osanda Nimalarathna                                                                                                             |
     |$.book.chapter                                    |Chap. 04                                                                                                                        |
     |$.notificationSettings.areNotificationsEnabled    |true                                                                                                                            |
     |$.notificationSettings.notificationTime           |08:00                                                                                                                        |
     |$.notificationSettings.notificationFrequency      |1                                                                                                                               |
     |$.examDate                                        |1512021142000                                                                                                                   |
     |$.userId                                          |34                                                                                                                              |
     |$.parentDeckId                                    |5                                                                                                                               |
	 |$.tempDeckId                                      |999                                                                                                                             |
     |$.archived                                        |true                                                                                                                            |
     |$.cardPreview                                     |true                                                                                                                            |
     |$.noOfCards                                       |2                                                                                                                               |
     |$.progress                                        |3                                                                                                                               |
     |$.downloads                                       |12                                                                                                                              |
     |$.deckAuthor                                      |Osanda                                                                                                                          |
     |$.thumbnailUrl                                    |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a154f35d5b71d1a8a54dd58/download/public?format=ORIGINAL               |
     |$.status                                          |Closed                                                                                                                          |
     |$.expert                                          |false                                                                                                                           |
     |$.starred                                         |true                                                                                                                            |
     |$.purchaseInfo.price                              |0                                                                                                                               |
     |$.categoryId                                      |5a5db30a12ef181b0af109ba                                                                                                        |




Edit a Deck using a null value as the thumbnailUrl
----------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                                                                          |
     |--------------------------------|-------------------------------------------------------------------------------------------------------------------|
     |#title                          |API Deck3                                                                                                          |
     |#description                    |Test description for API Deck3                                                                                     |
     |#tags1                          |API tag1                                                                                                           |
     |#subjectId                      |2                                                                                                                  |
     |#subjectName                    |API Testing3                                                                                                       |
     |#bookTitle                      |Automation3                                                                                                        |
     |#bookAuthor                     |Osanda Nimalarathna                                                                                                |
     |#bookChapter                    |Chap. 04                                                                                                           |
     |#purchasedDate                  |1512021142001                                                                                                      |
     |#purchaseInformationPrice       |777                                                                                                                |
     |#purchaseInformationsku         |com.pearson.smartflashcards.test3                                                                                  |
     |#areNotificationsEnabled        |true                                                                                                               |
     |#notificationTime               |08:00                                                                                                           |
     |#notificationFrequency          |1                                                                                                                  |
     |#examDate                       |1512021142000                                                                                                      |
     |#userId                         |34                                                                                                                 |
     |#parentDeckId                   |5                                                                                                                  |
     |#tempDeckId                     |999                                                                                                                |
     |#archived                       |true                                                                                                               |
     |#cardPreview                    |true                                                                                                               |
     |#noOfCards                      |2                                                                                                                  |
     |#progress                       |3                                                                                                                  |
     |#downloads                      |12                                                                                                                 |
     |#deckAuthorName                 |Osanda                                                                                                             |
     |#deckAuthorId                   |6                                                                                                                  |
     |#thumbnailUrl                   |"null"                                                                                                             |
     |#status                         |Closed                                                                                                             |
     |#starred                        |true                                                                                                               |
     |#categoryId                     |5a5db30a12ef181b0af109ba                                                                                           |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                         |Value                                                                                                                           |
     |--------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
     |$.title                                           |API Deck3                                                                                                                       |
     |$.description                                     |Test description for API Deck3                                                                                                  |
     |$.tags[0]                                         |API tag1                                                                                                                        |
     |$.book.bookTitle                                  |Automation3                                                                                                                     |
     |$.book.bookAuthor                                 |Osanda Nimalarathna                                                                                                             |
     |$.book.chapter                                    |Chap. 04                                                                                                                        |
     |$.notificationSettings.areNotificationsEnabled    |true                                                                                                                            |
     |$.notificationSettings.notificationTime           |08:00                                                                                                                        |
     |$.notificationSettings.notificationFrequency      |1                                                                                                                               |
     |$.examDate                                        |1512021142000                                                                                                                   |
     |$.userId                                          |34                                                                                                                              |
     |$.parentDeckId                                    |5                                                                                                                               |
	 |$.tempDeckId                                      |999                                                                                                                             |
     |$.archived                                        |true                                                                                                                            |
     |$.cardPreview                                     |true                                                                                                                            |
     |$.noOfCards                                       |2                                                                                                                               |
     |$.progress                                        |3                                                                                                                               |
     |$.downloads                                       |12                                                                                                                              |
     |$.deckAuthor                                      |Osanda                                                                                                                          |
     |$.deckAuthorId                                    |6                                                                                                                               |
     |$.status                                          |Closed                                                                                                                          |
     |$.expert                                          |false                                                                                                                           |
     |$.starred                                         |true                                                                                                                            |
     |$.purchaseInfo.price                              |0                                                                                                                               |
     |$.categoryId                                      |5a5db30a12ef181b0af109ba                                                                                                        |




Edit a Deck using a null value as the status
----------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                                                                          |
     |--------------------------------|-------------------------------------------------------------------------------------------------------------------|
     |#title                          |API Deck3                                                                                                          |
     |#description                    |Test description for API Deck3                                                                                     |
     |#tags1                          |API tag1                                                                                                           |
     |#subjectId                      |2                                                                                                                  |
     |#subjectName                    |API Testing3                                                                                                       |
     |#bookTitle                      |Automation3                                                                                                        |
     |#bookAuthor                     |Osanda Nimalarathna                                                                                                |
     |#bookChapter                    |Chap. 04                                                                                                           |
     |#purchasedDate                  |1512021142001                                                                                                      |
     |#purchaseInformationPrice       |777                                                                                                                |
     |#purchaseInformationsku         |com.pearson.smartflashcards.test3                                                                                  |
     |#areNotificationsEnabled        |true                                                                                                               |
     |#notificationTime               |08:00                                                                                                           |
     |#notificationFrequency          |1                                                                                                                  |
     |#examDate                       |1512021142000                                                                                                      |
     |#userId                         |34                                                                                                                 |
     |#parentDeckId                   |5                                                                                                                  |
     |#tempDeckId                     |999                                                                                                                |
     |#archived                       |true                                                                                                               |
     |#cardPreview                    |true                                                                                                               |
     |#noOfCards                      |2                                                                                                                  |
     |#progress                       |3                                                                                                                  |
     |#downloads                      |12                                                                                                                 |
     |#deckAuthorName                 |Osanda                                                                                                             |
     |#deckAuthorId                   |6                                                                                                                  |
     |#thumbnailUrl                   |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a154f35d5b71d1a8a54dd58/download/public?format=ORIGINAL  |
     |#status                         |"null"                                                                                                             |
     |#starred                        |true                                                                                                               |
     |#categoryId                     |5a5db30a12ef181b0af109ba                                                                                           |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                         |Value                                                                                                                           |
     |--------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
     |$.title                                           |API Deck3                                                                                                                       |
     |$.description                                     |Test description for API Deck3                                                                                                  |
     |$.tags[0]                                         |API tag1                                                                                                                        |
     |$.book.bookTitle                                  |Automation3                                                                                                                     |
     |$.book.bookAuthor                                 |Osanda Nimalarathna                                                                                                             |
     |$.book.chapter                                    |Chap. 04                                                                                                                        |
     |$.notificationSettings.areNotificationsEnabled    |true                                                                                                                            |
     |$.notificationSettings.notificationTime           |08:00                                                                                                                        |
     |$.notificationSettings.notificationFrequency      |1                                                                                                                               |
     |$.examDate                                        |1512021142000                                                                                                                   |
     |$.userId                                          |34                                                                                                                              |
     |$.parentDeckId                                    |5                                                                                                                               |
	 |$.tempDeckId                                      |999                                                                                                                             |
     |$.archived                                        |true                                                                                                                            |
     |$.cardPreview                                     |true                                                                                                                            |
     |$.noOfCards                                       |2                                                                                                                               |
     |$.progress                                        |3                                                                                                                               |
     |$.downloads                                       |12                                                                                                                              |
     |$.deckAuthor                                      |Osanda                                                                                                                          |
     |$.deckAuthorId                                    |6                                                                                                                               |
     |$.thumbnailUrl                                    |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a154f35d5b71d1a8a54dd58/download/public?format=ORIGINAL               |
     |$.expert                                          |false                                                                                                                           |
     |$.starred                                         |true                                                                                                                            |
     |$.purchaseInfo.price                              |0                                                                                                                               |
     |$.categoryId                                      |5a5db30a12ef181b0af109ba                                                                                                        |




Edit a Deck using a null value as the starred
-----------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                                                                          |
     |--------------------------------|-------------------------------------------------------------------------------------------------------------------|
     |#title                          |API Deck3                                                                                                          |
     |#description                    |Test description for API Deck3                                                                                     |
     |#tags1                          |API tag1                                                                                                           |
     |#subjectId                      |2                                                                                                                  |
     |#subjectName                    |API Testing3                                                                                                       |
     |#bookTitle                      |Automation3                                                                                                        |
     |#bookAuthor                     |Osanda Nimalarathna                                                                                                |
     |#bookChapter                    |Chap. 04                                                                                                           |
     |#purchasedDate                  |1512021142001                                                                                                      |
     |#purchaseInformationPrice       |777                                                                                                                |
     |#purchaseInformationsku         |com.pearson.smartflashcards.test3                                                                                  |
     |#areNotificationsEnabled        |true                                                                                                               |
     |#notificationTime               |08:00                                                                                                           |
     |#notificationFrequency          |2                                                                                                                  |
     |#examDate                       |1512021142000                                                                                                      |
     |#userId                         |34                                                                                                                 |
     |#parentDeckId                   |5                                                                                                                  |
     |#tempDeckId                     |999                                                                                                                |
     |#archived                       |true                                                                                                               |
     |#cardPreview                    |true                                                                                                               |
     |#noOfCards                      |2                                                                                                                  |
     |#progress                       |3                                                                                                                  |
     |#downloads                      |12                                                                                                                 |
     |#deckAuthorName                 |Osanda                                                                                                             |
     |#deckAuthorId                   |6                                                                                                                  |
     |#thumbnailUrl                   |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a154f35d5b71d1a8a54dd58/download/public?format=ORIGINAL  |
     |#status                         |Closed                                                                                                             |
     |#starred                        |null                                                                                                               |
     |#categoryId                     |5a5db30a12ef181b0af109ba                                                                                           |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                         |Value                                                                                                                           |
     |--------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
     |$.title                                           |API Deck3                                                                                                                       |
     |$.description                                     |Test description for API Deck3                                                                                                  |
     |$.tags[0]                                         |API tag1                                                                                                                        |
     |$.book.bookTitle                                  |Automation3                                                                                                                     |
     |$.book.bookAuthor                                 |Osanda Nimalarathna                                                                                                             |
     |$.book.chapter                                    |Chap. 04                                                                                                                        |
     |$.notificationSettings.areNotificationsEnabled    |true                                                                                                                            |
     |$.notificationSettings.notificationTime           |08:00                                                                                                                        |
     |$.notificationSettings.notificationFrequency      |2                                                                                                                               |
     |$.examDate                                        |1512021142000                                                                                                                   |
     |$.userId                                          |34                                                                                                                              |
     |$.parentDeckId                                    |5                                                                                                                               |
	 |$.tempDeckId                                      |999                                                                                                                             |
     |$.archived                                        |true                                                                                                                            |
     |$.cardPreview                                     |true                                                                                                                            |
     |$.noOfCards                                       |2                                                                                                                               |
     |$.progress                                        |3                                                                                                                               |
     |$.downloads                                       |12                                                                                                                              |
     |$.deckAuthor                                      |Osanda                                                                                                                          |
     |$.deckAuthorId                                    |6                                                                                                                               |
     |$.thumbnailUrl                                    |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a154f35d5b71d1a8a54dd58/download/public?format=ORIGINAL               |
     |$.status                                          |Closed                                                                                                                          |
     |$.expert                                          |false                                                                                                                           |
     |$.starred                                         |false                                                                                                                           |
     |$.purchaseInfo.price                              |0                                                                                                                               |
     |$.categoryId                                      |5a5db30a12ef181b0af109ba                                                                                                        |




Edit a Deck using an integer value as the starred
---------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                                                                          |
     |--------------------------------|-------------------------------------------------------------------------------------------------------------------|
     |#title                          |API Deck3                                                                                                          |
     |#description                    |Test description for API Deck3                                                                                     |
     |#tags1                          |API tag1                                                                                                           |
     |#subjectId                      |2                                                                                                                  |
     |#subjectName                    |API Testing3                                                                                                       |
     |#bookTitle                      |Automation3                                                                                                        |
     |#bookAuthor                     |Osanda Nimalarathna                                                                                                |
     |#bookChapter                    |Chap. 04                                                                                                           |
     |#purchasedDate                  |1512021142001                                                                                                      |
     |#purchaseInformationPrice       |777                                                                                                                |
     |#purchaseInformationsku         |com.pearson.smartflashcards.test3                                                                                  |
     |#areNotificationsEnabled        |true                                                                                                               |
     |#notificationTime               |08:00                                                                                                           |
     |#notificationFrequency          |2                                                                                                                 |
     |#examDate                       |1512021142000                                                                                                      |
     |#userId                         |34                                                                                                                 |
     |#parentDeckId                   |5                                                                                                                  |
     |#tempDeckId                     |999                                                                                                                |
     |#archived                       |true                                                                                                               |
     |#cardPreview                    |true                                                                                                               |
     |#noOfCards                      |2                                                                                                                  |
     |#progress                       |3                                                                                                                  |
     |#downloads                      |12                                                                                                                 |
     |#deckAuthorName                 |Osanda                                                                                                             |
     |#deckAuthorId                   |6                                                                                                                  |
     |#thumbnailUrl                   |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a154f35d5b71d1a8a54dd58/download/public?format=ORIGINAL  |
     |#status                         |Closed                                                                                                             |
     |#starred                        |123                                                                                                                |
     |#categoryId                     |5a5db30a12ef181b0af109ba                                                                                           |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                         |Value                                                                                                                           |
     |--------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
     |$.title                                           |API Deck3                                                                                                                       |
     |$.description                                     |Test description for API Deck3                                                                                                  |
     |$.tags[0]                                         |API tag1                                                                                                                        |
     |$.book.bookTitle                                  |Automation3                                                                                                                     |
     |$.book.bookAuthor                                 |Osanda Nimalarathna                                                                                                             |
     |$.book.chapter                                    |Chap. 04                                                                                                                        |
     |$.notificationSettings.areNotificationsEnabled    |true                                                                                                                            |
     |$.notificationSettings.notificationTime           |08:00                                                                                                                        |
     |$.notificationSettings.notificationFrequency      |2                                                                                                                               |
     |$.examDate                                        |1512021142000                                                                                                                   |
     |$.userId                                          |34                                                                                                                              |
     |$.parentDeckId                                    |5                                                                                                                               |
	 |$.tempDeckId                                      |999                                                                                                                             |
     |$.archived                                        |true                                                                                                                            |
     |$.cardPreview                                     |null                                                                                                                            |
     |$.noOfCards                                       |2                                                                                                                               |
     |$.progress                                        |3                                                                                                                               |
     |$.downloads                                       |12                                                                                                                              |
     |$.deckAuthor                                      |Osanda                                                                                                                          |
     |$.deckAuthorId                                    |6                                                                                                                               |
     |$.thumbnailUrl                                    |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a154f35d5b71d1a8a54dd58/download/public?format=ORIGINAL               |
     |$.status                                          |Closed                                                                                                                          |
     |$.expert                                          |false                                                                                                                           |
     |$.starred                                         |false                                                                                                                           |
     |$.purchaseInfo.price                              |0                                                                                                                               |
     |$.categoryId                                      |5a5db30a12ef181b0af109ba                                                                                                        |




Edit a Deck using an empty value as the tempDeckId
--------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                                                                          |
     |--------------------------------|-------------------------------------------------------------------------------------------------------------------|
     |#title                          |API Deck3                                                                                                          |
     |#description                    |Test description for API Deck3                                                                                     |
     |#tags1                          |API tag1                                                                                                           |
     |#subjectId                      |2                                                                                                                  |
     |#subjectName                    |API Testing3                                                                                                       |
     |#bookTitle                      |Automation3                                                                                                        |
     |#bookAuthor                     |Osanda Nimalarathna                                                                                                |
     |#bookChapter                    |Chap. 04                                                                                                           |
     |#purchasedDate                  |1512021142001                                                                                                      |
     |#purchaseInformationPrice       |777                                                                                                                |
     |#purchaseInformationsku         |com.pearson.smartflashcards.test3                                                                                  |
     |#areNotificationsEnabled        |true                                                                                                               |
     |#notificationTime               |08:00                                                                                                           |
     |#notificationFrequency          |1                                                                                                                  |
     |#examDate                       |1512021142000                                                                                                      |
     |#userId                         |34                                                                                                                 |
     |#parentDeckId                   |5                                                                                                                  |
     |#tempDeckId                     |                                                                                                                   |
     |#archived                       |true                                                                                                               |
     |#cardPreview                    |true                                                                                                               |
     |#noOfCards                      |2                                                                                                                  |
     |#progress                       |3                                                                                                                  |
     |#downloads                      |12                                                                                                                 |
     |#deckAuthorName                 |Osanda                                                                                                             |
     |#deckAuthorId                   |6                                                                                                                  |
     |#thumbnailUrl                   |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a154f35d5b71d1a8a54dd58/download/public?format=ORIGINAL  |
     |#status                         |Closed                                                                                                             |
     |#starred                        |false                                                                                                              |
     |#categoryId                     |5a5db30a12ef181b0af109ba                                                                                           |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                         |Value                                                                                                                           |
     |--------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
     |$.title                                           |API Deck3                                                                                                                       |
     |$.description                                     |Test description for API Deck3                                                                                                  |
     |$.tags[0]                                         |API tag1                                                                                                                        |
     |$.book.bookTitle                                  |Automation3                                                                                                                     |
     |$.book.bookAuthor                                 |Osanda Nimalarathna                                                                                                             |
     |$.book.chapter                                    |Chap. 04                                                                                                                        |
     |$.notificationSettings.areNotificationsEnabled    |true                                                                                                                            |
     |$.notificationSettings.notificationTime           |08:00                                                                                                                        |
     |$.notificationSettings.notificationFrequency      |1                                                                                                                               |
     |$.examDate                                        |1512021142000                                                                                                                   |
     |$.userId                                          |34                                                                                                                              |
     |$.parentDeckId                                    |5                                                                                                                               |
	 |$.tempDeckId                                      |                                                                                                                                |
     |$.archived                                        |true                                                                                                                            |
     |$.cardPreview                                     |true                                                                                                                            |
     |$.noOfCards                                       |2                                                                                                                               |
     |$.progress                                        |3                                                                                                                               |
     |$.downloads                                       |12                                                                                                                              |
     |$.deckAuthor                                      |Osanda                                                                                                                          |
     |$.deckAuthorId                                    |6                                                                                                                               |
     |$.thumbnailUrl                                    |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a154f35d5b71d1a8a54dd58/download/public?format=ORIGINAL               |
     |$.status                                          |Closed                                                                                                                          |
     |$.expert                                          |false                                                                                                                           |
     |$.starred                                         |false                                                                                                                           |
     |$.purchaseInfo.price                              |0                                                                                                                               |
     |$.categoryId                                      |5a5db30a12ef181b0af109ba                                                                                                        |




Edit a Deck using a null value as the tempDeckId
------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                                                                          |
     |--------------------------------|-------------------------------------------------------------------------------------------------------------------|
     |#title                          |API Deck3                                                                                                          |
     |#description                    |Test description for API Deck3                                                                                     |
     |#tags1                          |API tag1                                                                                                           |
     |#subjectId                      |2                                                                                                                  |
     |#subjectName                    |API Testing3                                                                                                       |
     |#bookTitle                      |Automation3                                                                                                        |
     |#bookAuthor                     |Osanda Nimalarathna                                                                                                |
     |#bookChapter                    |Chap. 04                                                                                                           |
     |#purchasedDate                  |1512021142001                                                                                                      |
     |#purchaseInformationPrice       |777                                                                                                                |
     |#purchaseInformationsku         |com.pearson.smartflashcards.test3                                                                                  |
     |#areNotificationsEnabled        |true                                                                                                               |
     |#notificationTime               |08:00                                                                                                           |
     |#notificationFrequency          |1                                                                                                                  |
     |#examDate                       |1512021142000                                                                                                      |
     |#userId                         |34                                                                                                                 |
     |#parentDeckId                   |5                                                                                                                  |
     |#tempDeckId                     |"null"                                                                                                             |
     |#archived                       |true                                                                                                               |
     |#cardPreview                    |true                                                                                                               |
     |#noOfCards                      |2                                                                                                                  |
     |#progress                       |3                                                                                                                  |
     |#downloads                      |12                                                                                                                 |
     |#deckAuthorName                 |Osanda                                                                                                             |
     |#deckAuthorId                   |6                                                                                                                  |
     |#thumbnailUrl                   |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a154f35d5b71d1a8a54dd58/download/public?format=ORIGINAL  |
     |#status                         |Closed                                                                                                             |
     |#starred                        |false                                                                                                              |
     |#categoryId                     |5a5db30a12ef181b0af109ba                                                                                           |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                         |Value                                                                                                                           |
     |--------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
     |$.title                                           |API Deck3                                                                                                                       |
     |$.description                                     |Test description for API Deck3                                                                                                  |
     |$.tags[0]                                         |API tag1                                                                                                                        |
     |$.book.bookTitle                                  |Automation3                                                                                                                     |
     |$.book.bookAuthor                                 |Osanda Nimalarathna                                                                                                             |
     |$.book.chapter                                    |Chap. 04                                                                                                                        |
     |$.notificationSettings.areNotificationsEnabled    |true                                                                                                                            |
     |$.notificationSettings.notificationTime           |08:00                                                                                                                        |
     |$.notificationSettings.notificationFrequency      |1                                                                                                                               |
     |$.examDate                                        |1512021142000                                                                                                                   |
     |$.userId                                          |34                                                                                                                              |
     |$.parentDeckId                                    |5                                                                                                                               |
     |$.archived                                        |true                                                                                                                            |
     |$.cardPreview                                     |true                                                                                                                            |
     |$.noOfCards                                       |2                                                                                                                               |
     |$.progress                                        |3                                                                                                                               |
     |$.downloads                                       |12                                                                                                                              |
     |$.deckAuthor                                      |Osanda                                                                                                                          |
     |$.deckAuthorId                                    |6                                                                                                                               |
     |$.thumbnailUrl                                    |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a154f35d5b71d1a8a54dd58/download/public?format=ORIGINAL               |
     |$.status                                          |Closed                                                                                                                          |
     |$.expert                                          |false                                                                                                                           |
     |$.starred                                         |false                                                                                                                           |
     |$.purchaseInfo.price                              |0                                                                                                                               |
     |$.categoryId                                      |5a5db30a12ef181b0af109ba                                                                                                        |
