Edit A Deck using Aggregation Service - Negative Tests Specification
====================================================================
Date Editd    : 01/08/2018
Version         : 1.0.0
Owner      	    : Osanda Deshan
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.


tags: edit_deck, edit_deck-negative_tests, negative



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



Edit a Deck using a null value as the title
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
     |JSON Path     |Expected Result                                                       |
     |--------------|----------------------------------------------------------------------|
     |$.status      |400                                                                   |
     |$.error       |Bad Request                                                           |
     |$.exception   |org.springframework.web.bind.MethodArgumentNotValidException          |


wewew

Description cannot be null
current : passed  as 200
actula should be : fail with message "Description cannot be null "



Edit a Deck using an empty value as the subjectId
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
     |JSON Path     |Expected Result                                                            |
     |--------------|---------------------------------------------------------------------------|
     |$.status      |400                                                                        |
     |$.error       |Bad Request                                                                |
     |$.exception   |org.springframework.http.converter.HttpMessageNotReadableException         |



response repeat more than one time



Edit a Deck using a null value as the subjectId
-------------------------------------------------
* And the user set the path parameters as follows
     |Path Parameter |Path Value                      |
     |---------------|--------------------------------|
     |deckId         |5a5eaafe2e02d86561172cda        |
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



Edit a Deck using a string value as the subjectId
---------------------------------------------------
* And the user set the path parameters as follows
     |Path Parameter |Path Value                      |
     |---------------|--------------------------------|
     |deckId         |5a5eaafe2e02d86561172cda        |
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




Edit a Deck using special character values as the subjectId
-------------------------------------------------------------
* And the user set the path parameters as follows
     |Path Parameter |Path Value                      |
     |---------------|--------------------------------|
     |deckId         |5a5eaafe2e02d86561172cda        |
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



Edit a Deck using a string value as the purchasedDate
-------------------------------------------------------
* And the user set the path parameters as follows
     |Path Parameter |Path Value                      |
     |---------------|--------------------------------|
     |deckId         |5a5eaafe2e02d86561172cda        |
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



Edit a Deck using special character values as the purchasedDate
-----------------------------------------------------------------
* And the user set the path parameters as follows
     |Path Parameter |Path Value                      |
     |---------------|--------------------------------|
     |deckId         |5a5eaafe2e02d86561172cda        |
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



Edit a Deck using an empty value as the purchaseInformationPrice
------------------------------------------------------------------
* And the user set the path parameters as follows
     |Path Parameter |Path Value                      |
     |---------------|--------------------------------|
     |deckId         |5a5eaafe2e02d86561172cda        |
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



Edit a Deck using a string value as the purchaseInformationPrice
------------------------------------------------------------------
* And the user set the path parameters as follows
     |Path Parameter |Path Value                      |
     |---------------|--------------------------------|
     |deckId         |5a5eaafe2e02d86561172cda        |
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



Edit a Deck using special character values as the purchaseInformationPrice
----------------------------------------------------------------------------
* And the user set the path parameters as follows
     |Path Parameter |Path Value                      |
     |---------------|--------------------------------|
     |deckId         |5a5eaafe2e02d86561172cda        |
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



Edit a Deck using an empty value as the areNotificationsEnabled
-----------------------------------------------------------------
* And the user set the path parameters as follows
     |Path Parameter |Path Value                      |
     |---------------|--------------------------------|
     |deckId         |5a5eaafe2e02d86561172cda        |
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



Edit a Deck using a string value as the areNotificationsEnabled
-----------------------------------------------------------------
* And the user set the path parameters as follows
     |Path Parameter |Path Value                      |
     |---------------|--------------------------------|
     |deckId         |5a5eaafe2e02d86561172cda        |
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





Edit a Deck using a string value as the examDate
--------------------------------------------------
* And the user set the path parameters as follows
     |Path Parameter |Path Value                      |
     |---------------|--------------------------------|
     |deckId         |5a5eaafe2e02d86561172cda        |
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




Edit a Deck using special character values as the examDate
------------------------------------------------------------
* And the user set the path parameters as follows
     |Path Parameter |Path Value                      |
     |---------------|--------------------------------|
     |deckId         |5a5eaafe2e02d86561172cda        |
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
     |JSON Path     |Expected Result                                                            |
     |--------------|---------------------------------------------------------------------------|
     |$.status      |400                                                                        |
     |$.error       |Bad Request                                                                |
     |$.exception   |org.springframework.http.converter.HttpMessageNotReadableException         |



Edit a Deck using an empty value as the userId
----------------------------------------------
* And the user set the path parameters as follows
     |Path Parameter |Path Value                      |
     |---------------|--------------------------------|
     |deckId         |5a5eaafe2e02d86561172cda        |
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
     |JSON Path     |Expected Result                                                            |
     |--------------|---------------------------------------------------------------------------|
     |$.status      |400                                                                        |
     |$.error       |Bad Request                                                                |
     |$.exception   |org.springframework.web.bind.MethodArgumentNotValidException               |



Edit a Deck using an empty value as the archived
--------------------------------------------------
* And the user set the path parameters as follows
     |Path Parameter |Path Value                      |
     |---------------|--------------------------------|
     |deckId         |5a5eaafe2e02d86561172cda        |
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
     |JSON Path     |Expected Result                                                            |
     |--------------|---------------------------------------------------------------------------|
     |$.status      |400                                                                        |
     |$.error       |Bad Request                                                                |
     |$.exception   |org.springframework.http.converter.HttpMessageNotReadableException         |




Edit a Deck using a string value as the archived
--------------------------------------------------
* And the user set the path parameters as follows
     |Path Parameter |Path Value                      |
     |---------------|--------------------------------|
     |deckId         |5a5eaafe2e02d86561172cda        |
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
     |JSON Path     |Expected Result                                                            |
     |--------------|---------------------------------------------------------------------------|
     |$.status      |400                                                                        |
     |$.error       |Bad Request                                                                |
     |$.exception   |org.springframework.http.converter.HttpMessageNotReadableException         |



Edit a Deck using an empty value as the cardPreview
-----------------------------------------------------
* And the user set the path parameters as follows
     |Path Parameter |Path Value                      |
     |---------------|--------------------------------|
     |deckId         |5a5eaafe2e02d86561172cda        |
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
     |JSON Path     |Expected Result                                                            |
     |--------------|---------------------------------------------------------------------------|
     |$.status      |400                                                                        |
     |$.error       |Bad Request                                                                |
     |$.exception   |org.springframework.http.converter.HttpMessageNotReadableException         |


Edit a Deck using a string value as the cardPreview
-----------------------------------------------------
* And the user set the path parameters as follows
     |Path Parameter |Path Value                      |
     |---------------|--------------------------------|
     |deckId         |5a5eaafe2e02d86561172cda        |
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
     |JSON Path     |Expected Result                                                            |
     |--------------|---------------------------------------------------------------------------|
     |$.status      |400                                                                        |
     |$.error       |Bad Request                                                                |
     |$.exception   |org.springframework.http.converter.HttpMessageNotReadableException         |



Edit a Deck using a string value as the noOfCards
---------------------------------------------------
* And the user set the path parameters as follows
     |Path Parameter |Path Value                      |
     |---------------|--------------------------------|
     |deckId         |5a5eaafe2e02d86561172cda        |
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
     |JSON Path     |Expected Result                                                            |
     |--------------|---------------------------------------------------------------------------|
     |$.status      |400                                                                        |
     |$.error       |Bad Request                                                                |
     |$.exception   |org.springframework.http.converter.HttpMessageNotReadableException         |




Edit a Deck using special character value as the noOfCards
------------------------------------------------------------
* And the user set the path parameters as follows
     |Path Parameter |Path Value                      |
     |---------------|--------------------------------|
     |deckId         |5a5eaafe2e02d86561172cda        |
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
     |JSON Path     |Expected Result                                                            |
     |--------------|---------------------------------------------------------------------------|
     |$.status      |400                                                                        |
     |$.error       |Bad Request                                                                |
     |$.exception   |org.springframework.http.converter.HttpMessageNotReadableException         |




Edit a Deck using an empty value as the progress
--------------------------------------------------
* And the user set the path parameters as follows
     |Path Parameter |Path Value                      |
     |---------------|--------------------------------|
     |deckId         |5a5eaafe2e02d86561172cda        |
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
     |JSON Path     |Expected Result                                                            |
     |--------------|---------------------------------------------------------------------------|
     |$.status      |400                                                                        |
     |$.error       |Bad Request                                                                |
     |$.exception   |org.springframework.http.converter.HttpMessageNotReadableException         |




Edit a Deck using a string value as the progress
--------------------------------------------------
* And the user set the path parameters as follows
     |Path Parameter |Path Value                      |
     |---------------|--------------------------------|
     |deckId         |5a5eaafe2e02d86561172cda        |
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
     |JSON Path     |Expected Result                                                            |
     |--------------|---------------------------------------------------------------------------|
     |$.status      |400                                                                        |
     |$.error       |Bad Request                                                                |
     |$.exception   |org.springframework.http.converter.HttpMessageNotReadableException         |




Edit a Deck using special character values as the progress
------------------------------------------------------------
* And the user set the path parameters as follows
     |Path Parameter |Path Value                      |
     |---------------|--------------------------------|
     |deckId         |5a5eaafe2e02d86561172cda        |
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
     |JSON Path     |Expected Result                                                            |
     |--------------|---------------------------------------------------------------------------|
     |$.status      |400                                                                        |
     |$.error       |Bad Request                                                                |
     |$.exception   |org.springframework.http.converter.HttpMessageNotReadableException         |



Edit a Deck using an empty value as the downloads
---------------------------------------------------
* And the user set the path parameters as follows
     |Path Parameter |Path Value                      |
     |---------------|--------------------------------|
     |deckId         |5a5eaafe2e02d86561172cda        |
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
     |JSON Path     |Expected Result                                                            |
     |--------------|---------------------------------------------------------------------------|
     |$.status      |400                                                                        |
     |$.error       |Bad Request                                                                |
     |$.exception   |org.springframework.http.converter.HttpMessageNotReadableException         |



Edit a Deck using a string value as the downloads
---------------------------------------------------
* And the user set the path parameters as follows
     |Path Parameter |Path Value                      |
     |---------------|--------------------------------|
     |deckId         |5a5eaafe2e02d86561172cda        |
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
     |JSON Path     |Expected Result                                                            |
     |--------------|---------------------------------------------------------------------------|
     |$.status      |400                                                                        |
     |$.error       |Bad Request                                                                |
     |$.exception   |org.springframework.http.converter.HttpMessageNotReadableException         |




Edit a Deck using a special character value as the downloads
--------------------------------------------------------------
* And the user set the path parameters as follows
     |Path Parameter |Path Value                      |
     |---------------|--------------------------------|
     |deckId         |5a5eaafe2e02d86561172cda        |
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
     |JSON Path     |Expected Result                                                            |
     |--------------|---------------------------------------------------------------------------|
     |$.status      |400                                                                        |
     |$.error       |Bad Request                                                                |
     |$.exception   |org.springframework.http.converter.HttpMessageNotReadableException         |



Edit a Deck using an empty value as the starred
-------------------------------------------------
* And the user set the path parameters as follows
     |Path Parameter |Path Value                      |
     |---------------|--------------------------------|
     |deckId         |5a5eaafe2e02d86561172cda        |
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
     |JSON Path     |Expected Result                                                            |
     |--------------|---------------------------------------------------------------------------|
     |$.status      |400                                                                        |
     |$.error       |Bad Request                                                                |
     |$.exception   |org.springframework.http.converter.HttpMessageNotReadableException         |



Edit a Deck using a string value as the starred
-------------------------------------------------
* And the user set the path parameters as follows
     |Path Parameter |Path Value                      |
     |---------------|--------------------------------|
     |deckId         |5a5eaafe2e02d86561172cda        |
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
     |JSON Path     |Expected Result                                                            |
     |--------------|---------------------------------------------------------------------------|
     |$.status      |400                                                                        |
     |$.error       |Bad Request                                                                |
     |$.exception   |org.springframework.http.converter.HttpMessageNotReadableException         |

Edit a Deck using special character values as the starred
-----------------------------------------------------------
* And the user set the path parameters as follows
     |Path Parameter |Path Value                      |
     |---------------|--------------------------------|
     |deckId         |5a5eaafe2e02d86561172cda        |
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
     |JSON Path     |Expected Result                                                            |
     |--------------|---------------------------------------------------------------------------|
     |$.status      |400                                                                        |
     |$.error       |Bad Request                                                                |
     |$.exception   |org.springframework.http.converter.HttpMessageNotReadableException         |




Edit a Deck using a null value as the noOfCards
-------------------------------------------------
* And the user set the path parameters as follows
     |Path Parameter |Path Value                      |
     |---------------|--------------------------------|
     |deckId         |5a5eaafe2e02d86561172cda        |
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                                                                    |
     |--------------------------------|-------------------------------------------------------------------------------------------------------------|
     |#id                             |5                                                                                                            |
     |#title                          |API Deck3                                                                                                    |
     |#description                    |Test description for API Deck3                                                                               |
     |#tags1                          |API tag                                                                                                      |
     |#subjectId                      |5                                                                                                            |
     |#subjectName                    |API Testing3                                                                                                 |
     |#bookTitle                      |Automation3                                                                                                  |
     |#bookAuthor                     |Osanda3                                                                                                      |
     |#bookChapter                    |Chap. 03                                                                                                     |
     |#purchasedDate                  |1512021142001                                                                                                |
     |#purchaseInformationPrice       |3                                                                                                            |
     |#purchaseInformationsku         |com.pearson.smartflashcards.test3                                                                            |
     |#areNotificationsEnabled        |false                                                                                                        |
     |#notificationTime               |string3                                                                                                      |
     |#notificationFrequency          |string3                                                                                                      |
     |#examDate                       |1512021142000                                                                                                |
     |#userId                         |osan                                                                                                         |
     |#parentDeckId                   |3                                                                                                            |
     |#tempDeckId                     |999                                                                                                          |
     |#archived                       |false                                                                                                        |
     |#cardPreview                    |false                                                                                                        |
     |#noOfCards                      |null                                                                                                         |
     |#progress                       |3                                                                                                            |
     |#downloads                      |3                                                                                                            |
     |#deckAuthorName                 |Osanda                                                                                                       |
     |#deckAuthorId                   |3                                                                                                            |
     |#thumbnailUrl                   |C://documentservice-qa.stg-prsn.com/api/v1/documents/5a154f35d5b71d1a8a54dd58/download/public?format=ORIGINAL|
     |#status                         |Closed                                                                                                       |
     |#starred                        |false                                                                                                        |
     |#categoryId                     |5a5db30a12ef181b0af109ba                                                                                     |
* And the user set the request headers as follows
     |Header Name                     |Header Value             |
     |--------------------------------|-------------------------|
     |X-Platform                      |Authoring                |
* When the user invokes the API
* Then the status code for the request is "400"


Edit a Deck using an empty value as the notificationFrequency
---------------------------------------------------------------
* And the user set the path parameters as follows
     |Path Parameter |Path Value                      |
     |---------------|--------------------------------|
     |deckId         |5a5eaafe2e02d86561172cda        |
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




Edit a Deck using a null value as the notificationFrequency
-------------------------------------------------------------
* And the user set the path parameters as follows
     |Path Parameter |Path Value                      |
     |---------------|--------------------------------|
     |deckId         |5a5eaafe2e02d86561172cda        |
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
     |#notificationFrequency          |"null"                                                                                                             |
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