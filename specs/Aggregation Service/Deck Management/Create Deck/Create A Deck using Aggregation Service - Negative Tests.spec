Create A Deck using Aggregation Service - Negative Tests Specification
======================================================================
Date Created    : 12/27/2017
Version         : 1.0.0
Owner      	    : Osanda Deshan
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.


tags: create_deck, create_deck-negative_tests, negative


* Given that a user needs to invoke "Create a Deck using Aggregation Service"
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |



Create a Deck using an empty value as the title
-----------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                                                                          |
     |--------------------------------|-------------------------------------------------------------------------------------------------------------------|
     |#title                          |                                                                                                                   |
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
     |#notificationTime               |08:00 AM                                                                                                           |
     |#notificationFrequency          |5                                                                                                                  |
     |#examDate                       |1512021142000                                                                                                      |
     |#userId                         |testUser                                                                                                           |
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
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path     |Expected Result                                                      |
     |--------------|---------------------------------------------------------------------|
     |$.status      |400                                                                  |
     |$.error       |Bad Request                                                          |
     |$.exception   |org.springframework.web.bind.MethodArgumentNotValidException         |



Create a Deck using a null value as the title
---------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                                                                          |
     |--------------------------------|-------------------------------------------------------------------------------------------------------------------|
     |#title                          |"null"                                                                                                             |
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
     |#notificationTime               |08:00 AM                                                                                                           |
     |#notificationFrequency          |5                                                                                                                  |
     |#examDate                       |1512021142000                                                                                                      |
     |#userId                         |testUser                                                                                                           |
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
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path     |Expected Result                                               |
     |--------------|--------------------------------------------------------------|
     |$.status      |400                                                           |
     |$.error       |Bad Request                                                   |
     |$.exception   |org.springframework.web.bind.MethodArgumentNotValidException  |


wewew

Description cannot be null
current : passed  as 200
actula should be : fail with message "Description cannot be null "



Create a Deck using an empty value as the subjectId
---------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                                                                          |
     |--------------------------------|-------------------------------------------------------------------------------------------------------------------|
     |#title                          |API Deck3                                                                                                          |
     |#description                    |Test description for API Deck3                                                                                     |
     |#tags1                          |API tag1                                                                                                           |
     |#subjectId                      |                                                                                                                   |
     |#subjectName                    |API Testing3                                                                                                       |
     |#bookTitle                      |Automation3                                                                                                        |
     |#bookAuthor                     |Osanda Nimalarathna                                                                                                |
     |#bookChapter                    |Chap. 04                                                                                                           |
     |#purchasedDate                  |1512021142001                                                                                                      |
     |#purchaseInformationPrice       |777                                                                                                                |
     |#purchaseInformationsku         |com.pearson.smartflashcards.test3                                                                                  |
     |#areNotificationsEnabled        |true                                                                                                               |
     |#notificationTime               |08:00 AM                                                                                                           |
     |#notificationFrequency          |5                                                                                                                  |
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
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path     |Expected Result                                                    |
     |--------------|-------------------------------------------------------------------|
     |$.status      |400                                                                |
     |$.error       |Bad Request                                                        |
     |$.exception   |org.springframework.http.converter.HttpMessageNotReadableException |



response repeat more than one time



Create a Deck using a null value as the subjectId
-------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                                                                          |
     |--------------------------------|-------------------------------------------------------------------------------------------------------------------|
     |#title                          |API Deck3                                                                                                          |
     |#description                    |Test description for API Deck3                                                                                     |
     |#tags1                          |API tag1                                                                                                           |
     |"#subjectId"                    |null                                                                                                               |
     |#subjectName                    |API Testing3                                                                                                       |
     |#bookTitle                      |Automation3                                                                                                        |
     |#bookAuthor                     |Osanda Nimalarathna                                                                                                |
     |#bookChapter                    |Chap. 04                                                                                                           |
     |#purchasedDate                  |1512021142001                                                                                                      |
     |#purchaseInformationPrice       |777                                                                                                                |
     |#purchaseInformationsku         |com.pearson.smartflashcards.test3                                                                                  |
     |#areNotificationsEnabled        |true                                                                                                               |
     |#notificationTime               |08:00 AM                                                                                                           |
     |#notificationFrequency          |5                                                                                                                  |
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
* And the user set the request headers as follows
     |Header Name                     |Header Value             |
     |--------------------------------|-------------------------|
     |X-Platform                      |Authoring                |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path     |Expected Result                                                            |
     |--------------|---------------------------------------------------------------------------|
     |$.status      |400                                                                        |
     |$.error       |Bad Request                                                                |
     |$.exception   |org.springframework.http.converter.HttpMessageNotReadableException         |



Create a Deck using a string value as the subjectId
---------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                                                                          |
     |--------------------------------|-------------------------------------------------------------------------------------------------------------------|
     |#title                          |API Deck3                                                                                                          |
     |#description                    |Test description for API Deck3                                                                                     |
     |#tags1                          |API tag1                                                                                                           |
     |#subjectId                      |sdsdsds                                                                                                            |
     |#subjectName                    |API Testing3                                                                                                       |
     |#bookTitle                      |Automation3                                                                                                        |
     |#bookAuthor                     |Osanda Nimalarathna                                                                                                |
     |#bookChapter                    |Chap. 04                                                                                                           |
     |#purchasedDate                  |1512021142001                                                                                                      |
     |#purchaseInformationPrice       |777                                                                                                                |
     |#purchaseInformationsku         |com.pearson.smartflashcards.test3                                                                                  |
     |#areNotificationsEnabled        |true                                                                                                               |
     |#notificationTime               |08:00 AM                                                                                                           |
     |#notificationFrequency          |5                                                                                                                  |
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
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path     |Expected Result                                                            |
     |--------------|---------------------------------------------------------------------------|
     |$.status      |400                                                                        |
     |$.error       |Bad Request                                                                |
     |$.exception   |org.springframework.http.converter.HttpMessageNotReadableException         |




Create a Deck using special character values as the subjectId
-------------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                                                                          |
     |--------------------------------|-------------------------------------------------------------------------------------------------------------------|
     |#title                          |API Deck3                                                                                                          |
     |#description                    |Test description for API Deck3                                                                                     |
     |#tags1                          |API tag1                                                                                                           |
     |#subjectId                      |!@#                                                                                                                |
     |#subjectName                    |API Testing3                                                                                                       |
     |#bookTitle                      |Automation3                                                                                                        |
     |#bookAuthor                     |Osanda Nimalarathna                                                                                                |
     |#bookChapter                    |Chap. 04                                                                                                           |
     |#purchasedDate                  |1512021142001                                                                                                      |
     |#purchaseInformationPrice       |777                                                                                                                |
     |#purchaseInformationsku         |com.pearson.smartflashcards.test3                                                                                  |
     |#areNotificationsEnabled        |true                                                                                                               |
     |#notificationTime               |08:00 AM                                                                                                           |
     |#notificationFrequency          |5                                                                                                                  |
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
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path     |Expected Result                                                            |
     |--------------|---------------------------------------------------------------------------|
     |$.status      |400                                                                        |
     |$.error       |Bad Request                                                                |
     |$.exception   |org.springframework.http.converter.HttpMessageNotReadableException         |




//some feilds are having null in response
//how to send arry object




Create a Deck using a null value as the notificationTime
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
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path           |Value                                                                |
     |--------------------|---------------------------------------------------------------------|
     |$.status            |400                                                                  |
     |$.message           |Text '2017-11-25 null' could not be parsed at index 11               |
     |$.error             |Bad Request                                                          |
     |$.exception         |com.pearson.question.aggregator.exceptions.BaseException             |




Create a Deck using an empty value as the notificationTime
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
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path           |Value                                                                |
     |--------------------|---------------------------------------------------------------------|
     |$.status            |400                                                                  |
     |$.message           |Text '2017-11-25 null' could not be parsed at index 11               |
     |$.error             |Bad Request                                                          |
     |$.exception         |com.pearson.question.aggregator.exceptions.BaseException             |



Create a Deck using a string value as the purchasedDate
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
     |#purchasedDate                  |abc                                                                                                                |
     |#purchaseInformationPrice       |777                                                                                                                |
     |#purchaseInformationsku         |com.pearson.smartflashcards.test3                                                                                  |
     |#areNotificationsEnabled        |true                                                                                                               |
     |#notificationTime               |08:00 AM                                                                                                           |
     |#notificationFrequency          |5                                                                                                                  |
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
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path     |Expected Result                                                            |
     |--------------|---------------------------------------------------------------------------|
     |$.status      |400                                                                        |
     |$.error       |Bad Request                                                                |
     |$.exception   |org.springframework.http.converter.HttpMessageNotReadableException         |



null save when user send null for pdate
pdate format validation



Create a Deck using special character values as the purchasedDate
-----------------------------------------------------------------
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
     |#purchasedDate                  |!@#                                                                                                                |
     |#purchaseInformationPrice       |777                                                                                                                |
     |#purchaseInformationsku         |com.pearson.smartflashcards.test3                                                                                  |
     |#areNotificationsEnabled        |true                                                                                                               |
     |#notificationTime               |08:00 AM                                                                                                           |
     |#notificationFrequency          |5                                                                                                                  |
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
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path     |Expected Result                                                            |
     |--------------|---------------------------------------------------------------------------|
     |$.status      |400                                                                        |
     |$.error       |Bad Request                                                                |
     |$.exception   |org.springframework.http.converter.HttpMessageNotReadableException         |



Create a Deck using an empty value as the purchaseInformationPrice
------------------------------------------------------------------
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
     |#purchaseInformationPrice       |                                                                                                                   |
     |#purchaseInformationsku         |com.pearson.smartflashcards.test3                                                                                  |
     |#areNotificationsEnabled        |true                                                                                                               |
     |#notificationTime               |08:00 AM                                                                                                           |
     |#notificationFrequency          |5                                                                                                                  |
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
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path     |Expected Result                                                            |
     |--------------|---------------------------------------------------------------------------|
     |$.status      |400                                                                        |
     |$.error       |Bad Request                                                                |
     |$.exception   |org.springframework.http.converter.HttpMessageNotReadableException         |



Create a Deck using a string value as the purchaseInformationPrice
------------------------------------------------------------------
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
     |#purchaseInformationPrice       |abc                                                                                                                |
     |#purchaseInformationsku         |com.pearson.smartflashcards.test3                                                                                  |
     |#areNotificationsEnabled        |true                                                                                                               |
     |#notificationTime               |08:00 AM                                                                                                           |
     |#notificationFrequency          |5                                                                                                                  |
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
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path     |Expected Result                                                            |
     |--------------|---------------------------------------------------------------------------|
     |$.status      |400                                                                        |
     |$.error       |Bad Request                                                                |
     |$.exception   |org.springframework.http.converter.HttpMessageNotReadableException         |



Create a Deck using special character values as the purchaseInformationPrice
----------------------------------------------------------------------------
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
     |#purchaseInformationPrice       |!@#                                                                                                                |
     |#purchaseInformationsku         |com.pearson.smartflashcards.test3                                                                                  |
     |#areNotificationsEnabled        |true                                                                                                               |
     |#notificationTime               |08:00 AM                                                                                                           |
     |#notificationFrequency          |5                                                                                                                  |
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
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path     |Expected Result                                                            |
     |--------------|---------------------------------------------------------------------------|
     |$.status      |400                                                                        |
     |$.error       |Bad Request                                                                |
     |$.exception   |org.springframework.http.converter.HttpMessageNotReadableException         |


save purchaase infromation value as null
Bug



Create a Deck using an empty value as the areNotificationsEnabled
-----------------------------------------------------------------
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
     |#areNotificationsEnabled        |                                                                                                                   |
     |#notificationTime               |08:00 AM                                                                                                           |
     |#notificationFrequency          |5                                                                                                                  |
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
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path     |Expected Result                                                            |
     |--------------|---------------------------------------------------------------------------|
     |$.status      |400                                                                        |
     |$.error       |Bad Request                                                                |
     |$.exception   |org.springframework.http.converter.HttpMessageNotReadableException         |



Create a Deck using a string value as the areNotificationsEnabled
-----------------------------------------------------------------
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
     |#areNotificationsEnabled        |abc                                                                                                                |
     |#notificationTime               |08:00 AM                                                                                                           |
     |#notificationFrequency          |5                                                                                                                  |
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
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path     |Expected Result                                                            |
     |--------------|---------------------------------------------------------------------------|
     |$.status      |400                                                                        |
     |$.error       |Bad Request                                                                |
     |$.exception   |org.springframework.http.converter.HttpMessageNotReadableException         |





Create a Deck using a string value as the examDate
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
     |#notificationTime               |08:00 AM                                                                                                           |
     |#notificationFrequency          |5                                                                                                                  |
     |#examDate                       |abc                                                                                                                |
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
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path     |Expected Result                                                            |
     |--------------|---------------------------------------------------------------------------|
     |$.status      |400                                                                        |
     |$.error       |Bad Request                                                                |
     |$.exception   |org.springframework.http.converter.HttpMessageNotReadableException         |




Create a Deck using special character values as the examDate
------------------------------------------------------------
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
     |#notificationTime               |08:00 AM                                                                                                           |
     |#notificationFrequency          |5                                                                                                                  |
     |#examDate                       |!@#                                                                                                                |
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
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
         |JSON Path     |Expected Result                                                    |
         |--------------|-------------------------------------------------------------------|
         |$.status      |400                                                                |
         |$.error       |Bad Request                                                        |
         |$.exception   |org.springframework.http.converter.HttpMessageNotReadableException |



Create a Deck using an empty value the userId
---------------------------------------------
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
     |#notificationTime               |08:00 AM                                                                                                           |
     |#notificationFrequency          |5                                                                                                                  |
     |#examDate                       |1512021142000                                                                                                      |
     |#userId                         |                                                                                                                   |
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
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path     |Expected Result                                                    |
     |--------------|-------------------------------------------------------------------|
     |$.status      |400                                                                |
     |$.error       |Bad Request                                                        |
     |$.exception   |org.springframework.web.bind.MethodArgumentNotValidException       |



Create a Deck using an empty value as the archived
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
     |#notificationTime               |08:00 AM                                                                                                           |
     |#notificationFrequency          |5                                                                                                                  |
     |#examDate                       |1512021142000                                                                                                      |
     |#userId                         |34                                                                                                                 |
     |#parentDeckId                   |5                                                                                                                  |
     |#tempDeckId                     |999                                                                                                                |
     |#archived                       |                                                                                                                   |
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
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
         |JSON Path     |Expected Result                                                    |
         |--------------|-------------------------------------------------------------------|
         |$.status      |400                                                                |
         |$.error       |Bad Request                                                        |
         |$.exception   |org.springframework.http.converter.HttpMessageNotReadableException |




Create a Deck using a string value as the archived
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
     |#notificationTime               |08:00 AM                                                                                                           |
     |#notificationFrequency          |5                                                                                                                  |
     |#examDate                       |1512021142000                                                                                                      |
     |#userId                         |34                                                                                                                 |
     |#parentDeckId                   |5                                                                                                                  |
     |#tempDeckId                     |999                                                                                                                |
     |#archived                       |abc                                                                                                                |
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
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
         |JSON Path     |Expected Result                                                    |
         |--------------|-------------------------------------------------------------------|
         |$.status      |400                                                                |
         |$.error       |Bad Request                                                        |
         |$.exception   |org.springframework.http.converter.HttpMessageNotReadableException |



Create a Deck using an empty value as the cardPreview
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
     |#bookChapter                    |Chap. 04                                                                                                           |
     |#purchasedDate                  |1512021142001                                                                                                      |
     |#purchaseInformationPrice       |777                                                                                                                |
     |#purchaseInformationsku         |com.pearson.smartflashcards.test3                                                                                  |
     |#areNotificationsEnabled        |true                                                                                                               |
     |#notificationTime               |08:00 AM                                                                                                           |
     |#notificationFrequency          |5                                                                                                                  |
     |#examDate                       |1512021142000                                                                                                      |
     |#userId                         |34                                                                                                                 |
     |#parentDeckId                   |5                                                                                                                  |
     |#tempDeckId                     |999                                                                                                                |
     |#archived                       |true                                                                                                               |
     |#cardPreview                    |                                                                                                                   |
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
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
         |JSON Path     |Expected Result                                                    |
         |--------------|-------------------------------------------------------------------|
         |$.status      |400                                                                |
         |$.error       |Bad Request                                                        |
         |$.exception   |org.springframework.http.converter.HttpMessageNotReadableException |


Create a Deck using a string value as the cardPreview
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
     |#bookChapter                    |Chap. 04                                                                                                           |
     |#purchasedDate                  |1512021142001                                                                                                      |
     |#purchaseInformationPrice       |777                                                                                                                |
     |#purchaseInformationsku         |com.pearson.smartflashcards.test3                                                                                  |
     |#areNotificationsEnabled        |true                                                                                                               |
     |#notificationTime               |08:00 AM                                                                                                           |
     |#notificationFrequency          |5                                                                                                                  |
     |#examDate                       |1512021142000                                                                                                      |
     |#userId                         |34                                                                                                                 |
     |#parentDeckId                   |5                                                                                                                  |
     |#tempDeckId                     |999                                                                                                                |
     |#archived                       |true                                                                                                               |
     |#cardPreview                    |abc                                                                                                                |
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
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
         |JSON Path     |Expected Result                                                    |
         |--------------|-------------------------------------------------------------------|
         |$.status      |400                                                                |
         |$.error       |Bad Request                                                        |
         |$.exception   |org.springframework.http.converter.HttpMessageNotReadableException |



Create a Deck using a string value as the noOfCards
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
     |#notificationTime               |08:00 AM                                                                                                           |
     |#notificationFrequency          |5                                                                                                                  |
     |#examDate                       |1512021142000                                                                                                      |
     |#userId                         |34                                                                                                                 |
     |#parentDeckId                   |5                                                                                                                  |
     |#tempDeckId                     |999                                                                                                                |
     |#archived                       |true                                                                                                               |
     |#cardPreview                    |true                                                                                                               |
     |#noOfCards                      |abc                                                                                                                |
     |#progress                       |3                                                                                                                  |
     |#downloads                      |12                                                                                                                 |
     |#deckAuthorName                 |Osanda                                                                                                             |
     |#deckAuthorId                   |6                                                                                                                  |
     |#thumbnailUrl                   |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a154f35d5b71d1a8a54dd58/download/public?format=ORIGINAL  |
     |#status                         |Closed                                                                                                             |
     |#starred                        |true                                                                                                               |
     |#categoryId                     |5a5db30a12ef181b0af109ba                                                                                           |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
         |JSON Path     |Expected Result                                                    |
         |--------------|-------------------------------------------------------------------|
         |$.status      |400                                                                |
         |$.error       |Bad Request                                                        |
         |$.exception   |org.springframework.http.converter.HttpMessageNotReadableException |




Create a Deck using special character value as the noOfCards
------------------------------------------------------------
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
     |#notificationTime               |08:00 AM                                                                                                           |
     |#notificationFrequency          |5                                                                                                                  |
     |#examDate                       |1512021142000                                                                                                      |
     |#userId                         |34                                                                                                                 |
     |#parentDeckId                   |5                                                                                                                  |
     |#tempDeckId                     |999                                                                                                                |
     |#archived                       |true                                                                                                               |
     |#cardPreview                    |true                                                                                                               |
     |#noOfCards                      |!@#                                                                                                                |
     |#progress                       |3                                                                                                                  |
     |#downloads                      |12                                                                                                                 |
     |#deckAuthorName                 |Osanda                                                                                                             |
     |#deckAuthorId                   |6                                                                                                                  |
     |#thumbnailUrl                   |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a154f35d5b71d1a8a54dd58/download/public?format=ORIGINAL  |
     |#status                         |Closed                                                                                                             |
     |#starred                        |true                                                                                                               |
     |#categoryId                     |5a5db30a12ef181b0af109ba                                                                                           |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path     |Expected Result                                                    |
     |--------------|-------------------------------------------------------------------|
     |$.status      |400                                                                |
     |$.error       |Bad Request                                                        |
     |$.exception   |org.springframework.http.converter.HttpMessageNotReadableException |




Create a Deck using an empty value as the progress
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
     |#notificationTime               |08:00 AM                                                                                                           |
     |#notificationFrequency          |5                                                                                                                  |
     |#examDate                       |1512021142000                                                                                                      |
     |#userId                         |34                                                                                                                 |
     |#parentDeckId                   |5                                                                                                                  |
     |#tempDeckId                     |999                                                                                                                |
     |#archived                       |true                                                                                                               |
     |#cardPreview                    |true                                                                                                               |
     |#noOfCards                      |2                                                                                                                  |
     |#progress                       |                                                                                                                   |
     |#downloads                      |12                                                                                                                 |
     |#deckAuthorName                 |Osanda                                                                                                             |
     |#deckAuthorId                   |6                                                                                                                  |
     |#thumbnailUrl                   |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a154f35d5b71d1a8a54dd58/download/public?format=ORIGINAL  |
     |#status                         |Closed                                                                                                             |
     |#starred                        |true                                                                                                               |
     |#categoryId                     |5a5db30a12ef181b0af109ba                                                                                           |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
         |JSON Path     |Expected Result                                                    |
         |--------------|-------------------------------------------------------------------|
         |$.status      |400                                                                |
         |$.error       |Bad Request                                                        |
         |$.exception   |org.springframework.http.converter.HttpMessageNotReadableException |




Create a Deck using a string value as the progress
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
     |#notificationTime               |08:00 AM                                                                                                           |
     |#notificationFrequency          |5                                                                                                                  |
     |#examDate                       |1512021142000                                                                                                      |
     |#userId                         |34                                                                                                                 |
     |#parentDeckId                   |5                                                                                                                  |
     |#tempDeckId                     |999                                                                                                                |
     |#archived                       |true                                                                                                               |
     |#cardPreview                    |true                                                                                                               |
     |#noOfCards                      |2                                                                                                                  |
     |#progress                       |abc                                                                                                                |
     |#downloads                      |12                                                                                                                 |
     |#deckAuthorName                 |Osanda                                                                                                             |
     |#deckAuthorId                   |6                                                                                                                  |
     |#thumbnailUrl                   |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a154f35d5b71d1a8a54dd58/download/public?format=ORIGINAL  |
     |#status                         |Closed                                                                                                             |
     |#starred                        |true                                                                                                               |
     |#categoryId                     |5a5db30a12ef181b0af109ba                                                                                           |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
         |JSON Path     |Expected Result                                                    |
         |--------------|-------------------------------------------------------------------|
         |$.status      |400                                                                |
         |$.error       |Bad Request                                                        |
         |$.exception   |org.springframework.http.converter.HttpMessageNotReadableException |




Create a Deck using special character values as the progress
------------------------------------------------------------
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
     |#notificationTime               |08:00 AM                                                                                                           |
     |#notificationFrequency          |5                                                                                                                  |
     |#examDate                       |1512021142000                                                                                                      |
     |#userId                         |34                                                                                                                 |
     |#parentDeckId                   |5                                                                                                                  |
     |#tempDeckId                     |999                                                                                                                |
     |#archived                       |true                                                                                                               |
     |#cardPreview                    |true                                                                                                               |
     |#noOfCards                      |2                                                                                                                  |
     |#progress                       |!@#                                                                                                                |
     |#downloads                      |12                                                                                                                 |
     |#deckAuthorName                 |Osanda                                                                                                             |
     |#deckAuthorId                   |6                                                                                                                  |
     |#thumbnailUrl                   |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a154f35d5b71d1a8a54dd58/download/public?format=ORIGINAL  |
     |#status                         |Closed                                                                                                             |
     |#starred                        |true                                                                                                               |
     |#categoryId                     |5a5db30a12ef181b0af109ba                                                                                           |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
         |JSON Path     |Expected Result                                                    |
         |--------------|-------------------------------------------------------------------|
         |$.status      |400                                                                |
         |$.error       |Bad Request                                                        |
         |$.exception   |org.springframework.http.converter.HttpMessageNotReadableException |



Create a Deck using an empty value as the downloads
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
     |#notificationTime               |08:00 AM                                                                                                           |
     |#notificationFrequency          |5                                                                                                                  |
     |#examDate                       |1512021142000                                                                                                      |
     |#userId                         |34                                                                                                                 |
     |#parentDeckId                   |5                                                                                                                  |
     |#tempDeckId                     |999                                                                                                                |
     |#archived                       |true                                                                                                               |
     |#cardPreview                    |true                                                                                                               |
     |#noOfCards                      |2                                                                                                                  |
     |#progress                       |3                                                                                                                  |
     |#downloads                      |                                                                                                                   |
     |#deckAuthorName                 |Osanda                                                                                                             |
     |#deckAuthorId                   |6                                                                                                                  |
     |#thumbnailUrl                   |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a154f35d5b71d1a8a54dd58/download/public?format=ORIGINAL  |
     |#status                         |Closed                                                                                                             |
     |#starred                        |true                                                                                                               |
     |#categoryId                     |5a5db30a12ef181b0af109ba                                                                                           |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
         |JSON Path     |Expected Result                                                    |
         |--------------|-------------------------------------------------------------------|
         |$.status      |400                                                                |
         |$.error       |Bad Request                                                        |
         |$.exception   |org.springframework.http.converter.HttpMessageNotReadableException |



Create a Deck using a string value as the downloads
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
     |#notificationTime               |08:00 AM                                                                                                           |
     |#notificationFrequency          |5                                                                                                                  |
     |#examDate                       |1512021142000                                                                                                      |
     |#userId                         |34                                                                                                                 |
     |#parentDeckId                   |5                                                                                                                  |
     |#tempDeckId                     |999                                                                                                                |
     |#archived                       |true                                                                                                               |
     |#cardPreview                    |true                                                                                                               |
     |#noOfCards                      |2                                                                                                                  |
     |#progress                       |3                                                                                                                  |
     |#downloads                      |abc                                                                                                                |
     |#deckAuthorName                 |Osanda                                                                                                             |
     |#deckAuthorId                   |6                                                                                                                  |
     |#thumbnailUrl                   |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a154f35d5b71d1a8a54dd58/download/public?format=ORIGINAL  |
     |#status                         |Closed                                                                                                             |
     |#starred                        |true                                                                                                               |
     |#categoryId                     |5a5db30a12ef181b0af109ba                                                                                           |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
         |JSON Path     |Expected Result                                                    |
         |--------------|-------------------------------------------------------------------|
         |$.status      |400                                                                |
         |$.error       |Bad Request                                                        |
         |$.exception   |org.springframework.http.converter.HttpMessageNotReadableException |




Create a Deck using a special character value as the downloads
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
     |#bookChapter                    |Chap. 04                                                                                                           |
     |#purchasedDate                  |1512021142001                                                                                                      |
     |#purchaseInformationPrice       |777                                                                                                                |
     |#purchaseInformationsku         |com.pearson.smartflashcards.test3                                                                                  |
     |#areNotificationsEnabled        |true                                                                                                               |
     |#notificationTime               |08:00 AM                                                                                                           |
     |#notificationFrequency          |5                                                                                                                  |
     |#examDate                       |1512021142000                                                                                                      |
     |#userId                         |34                                                                                                                 |
     |#parentDeckId                   |5                                                                                                                  |
     |#tempDeckId                     |999                                                                                                                |
     |#archived                       |true                                                                                                               |
     |#cardPreview                    |true                                                                                                               |
     |#noOfCards                      |2                                                                                                                  |
     |#progress                       |3                                                                                                                  |
     |#downloads                      |!@#                                                                                                                |
     |#deckAuthorName                 |Osanda                                                                                                             |
     |#deckAuthorId                   |6                                                                                                                  |
     |#thumbnailUrl                   |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a154f35d5b71d1a8a54dd58/download/public?format=ORIGINAL  |
     |#status                         |Closed                                                                                                             |
     |#starred                        |true                                                                                                               |
     |#categoryId                     |5a5db30a12ef181b0af109ba                                                                                           |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
         |JSON Path     |Expected Result                                                    |
         |--------------|-------------------------------------------------------------------|
         |$.status      |400                                                                |
         |$.error       |Bad Request                                                        |
         |$.exception   |org.springframework.http.converter.HttpMessageNotReadableException |



Create a Deck using an empty value as the starred
-------------------------------------------------
* And the user set the request authentication configurations as follows
     |Configuration Property Name       |Configuration Property Value   |
     |----------------------------------|-------------------------------|
     |isAccessTokenIncluded             |True                           |
     |isAccessTokenRetrievedFromTextFile|True                           |
     |accessTokenString                 |N/A                            |
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
     |#notificationTime               |08:00 AM                                                                                                           |
     |#notificationFrequency          |5                                                                                                                  |
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
     |#starred                        |                                                                                                                   |
     |#categoryId                     |5a5db30a12ef181b0af109ba                                                                                           |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
         |JSON Path     |Expected Result                                                    |
         |--------------|-------------------------------------------------------------------|
         |$.status      |400                                                                |
         |$.error       |Bad Request                                                        |
         |$.exception   |org.springframework.http.converter.HttpMessageNotReadableException |



Create a Deck using a string value as the starred
-------------------------------------------------
* And the user set the request authentication configurations as follows
     |Configuration Property Name       |Configuration Property Value   |
     |----------------------------------|-------------------------------|
     |isAccessTokenIncluded             |True                           |
     |isAccessTokenRetrievedFromTextFile|True                           |
     |accessTokenString                 |N/A                            |
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
     |#notificationTime               |08:00 AM                                                                                                           |
     |#notificationFrequency          |5                                                                                                                  |
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
     |#starred                        |abc                                                                                                                |
     |#categoryId                     |5a5db30a12ef181b0af109ba                                                                                           |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
         |JSON Path     |Expected Result                                                    |
         |--------------|-------------------------------------------------------------------|
         |$.status      |400                                                                |
         |$.error       |Bad Request                                                        |
         |$.exception   |org.springframework.http.converter.HttpMessageNotReadableException |



Create a Deck using special character values as the starred
-----------------------------------------------------------
* And the user set the request authentication configurations as follows
     |Configuration Property Name       |Configuration Property Value   |
     |----------------------------------|-------------------------------|
     |isAccessTokenIncluded             |True                           |
     |isAccessTokenRetrievedFromTextFile|True                           |
     |accessTokenString                 |N/A                            |
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
     |#notificationTime               |08:00 AM                                                                                                           |
     |#notificationFrequency          |5                                                                                                                  |
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
     |#starred                        |!@#                                                                                                                |
     |#categoryId                     |5a5db30a12ef181b0af109ba                                                                                           |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
         |JSON Path     |Expected Result                                                    |
         |--------------|-------------------------------------------------------------------|
         |$.status      |400                                                                |
         |$.error       |Bad Request                                                        |
         |$.exception   |org.springframework.http.converter.HttpMessageNotReadableException |



Create a Deck using invalid notification frequency
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
     |#notificationTime               |08:00 AM                                                                                                           |
     |#notificationFrequency          |5                                                                                                                  |
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
* Then the status code for the request is "400"



Create a Deck using a string value as the notificationFrequency
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
     |#areNotificationsEnabled        |true                                                                                                               |
     |#notificationTime               |08:00 AM                                                                                                           |
     |#notificationFrequency          |string                                                                                                                   |
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
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path     |Expected Result                                                      |
     |--------------|---------------------------------------------------------------------|
     |$.status      |400                                                                  |
     |$.message     |For input string: \"string\                                          |
     |$.error       |Bad Request                                                          |
     |$.exception   |com.pearson.question.aggregator.exceptions.BaseException             |



Create a Deck using an empty value as the notificationFrequency
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
     |#areNotificationsEnabled        |true                                                                                                               |
     |#notificationTime               |08:00 AM                                                                                                           |
     |#notificationFrequency          |                                                                                                                   |
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
* Then the status code for the request is "400"



Create a Deck using an null value as the notificationFrequency
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
     |#areNotificationsEnabled        |true                                                                                                               |
     |#notificationTime               |08:00 AM                                                                                                           |
     |#notificationFrequency          |null                                                                                                                   |
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
* Then the status code for the request is "400"