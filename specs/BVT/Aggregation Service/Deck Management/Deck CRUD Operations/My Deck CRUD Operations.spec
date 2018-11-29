# My Deck CRUD Operations Specification
Date Created    : 06/11/2018
Version         : 1.0.0
Owner      	    : Osanda Deshan
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.


tags: create_my_deck, edit_my_deck, get_my_deck, get_my_decks, delete_my_deck



## Create a deck
* Given that a user needs to invoke "Create a Deck using Aggregation Service"
* And the user set the request authentication configurations as follows 

   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |Yes                |
   |Do you need to retrieve the access token from the text file?      |Yes                |
   |Provide the access token if you need to authorize the API manually|N/A                |
* And the user set the request attributes as follows 

   |Attribute Value In JSON Template|Attribute Value To Be Set                                                                                        |
   |--------------------------------|-----------------------------------------------------------------------------------------------------------------|
   |#title                          |API Deck3                                                                                                        |
   |#description                    |test description                                                                                                 |
   |#tags1                          |API tag1                                                                                                         |
   |#subjectId                      |2                                                                                                                |
   |#subjectName                    |API Testing3                                                                                                     |
   |#bookTitle                      |Automation3                                                                                                      |
   |#bookAuthor                     |Osanda Nimalarathna                                                                                              |
   |#bookChapter                    |Chap. 04                                                                                                         |
   |#purchasedDate                  |1512021142001                                                                                                    |
   |#purchaseInformationPrice       |777                                                                                                              |
   |#purchaseInformationsku         |com.pearson.smartflashcards.test3                                                                                |
   |#areNotificationsEnabled        |true                                                                                                             |
   |#notificationTime               |08:00                                                                                                            |
   |#notificationFrequency          |0                                                                                                                |
   |#examDate                       |1512021142000                                                                                                    |
   |#userId                         |34                                                                                                               |
   |#parentDeckId                   |5                                                                                                                |
   |#tempDeckId                     |999                                                                                                              |
   |#archived                       |true                                                                                                             |
   |#cardPreview                    |true                                                                                                             |
   |#noOfCards                      |2                                                                                                                |
   |#progress                       |3                                                                                                                |
   |#downloads                      |12                                                                                                               |
   |#deckAuthorName                 |Osanda                                                                                                           |
   |#deckAuthorId                   |6                                                                                                                |
   |#thumbnailUrl                   |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a154f35d5b71d1a8a54dd58/download/public?format=ORIGINAL|
   |#status                         |Closed                                                                                                           |
   |#starred                        |true                                                                                                             |
   |#categoryId                     |5a5db30a12ef181b0af109ba                                                                                         |
* When the user invokes the API
* Then the status code for the request is "201"
* And the JSON Path Assertions for the response should be equal to the following 

   |JSON Path                                     |Value                                                                                                            |
   |----------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
   |$.title                                       |API Deck3                                                                                                        |
   |$.description                                 |test description                                                                                                 |
   |$.tags[0]                                     |API tag1                                                                                                         |
   |$.book.bookTitle                              |Automation3                                                                                                      |
   |$.book.bookAuthor                             |Osanda Nimalarathna                                                                                              |
   |$.book.chapter                                |Chap. 04                                                                                                         |
   |$.purchaseInfo.price                          |777.0                                                                                                            |
   |$.notificationSettings.areNotificationsEnabled|true                                                                                                             |
   |$.notificationSettings.notificationTime       |08:00                                                                                                            |
   |$.notificationSettings.notificationFrequency  |0                                                                                                                |
   |$.examDate                                    |1512021142000                                                                                                    |
   |$.userId                                      |34                                                                                                               |
   |$.parentDeckId                                |5                                                                                                                |
   |$.tempDeckId                                  |999                                                                                                              |
   |$.archived                                    |true                                                                                                             |
   |$.cardPreview                                 |true                                                                                                             |
   |$.noOfCards                                   |2                                                                                                                |
   |$.progress                                    |3                                                                                                                |
   |$.downloads                                   |12                                                                                                               |
   |$.deckAuthor                                  |Osanda                                                                                                           |
   |$.deckAuthorId                                |6                                                                                                                |
   |$.thumbnailUrl                                |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a154f35d5b71d1a8a54dd58/download/public?format=ORIGINAL|
   |$.status                                      |Closed                                                                                                           |
   |$.expert                                      |false                                                                                                            |
   |$.starred                                     |true                                                                                                             |
   |$.categoryId                                  |5a5db30a12ef181b0af109ba                                                                                         |
* And save the JSON Path values in the response inside the data stores 

   |DataStore Type|Variable Name|Value To Be Stored|
   |--------------|-------------|------------------|
   |spec          |deckId       |$.id              |
   |spec          |userId       |$.userId          |
   |spec          |title        |$.title           |



## Edit a deck
* Given that a user needs to invoke "Edit a Deck using Aggregation Service"
* And the user set the request authentication configurations as follows 

   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |Yes                |
   |Do you need to retrieve the access token from the text file?      |Yes                |
   |Provide the access token if you need to authorize the API manually|N/A                |
* And the user set the path parameters using data stores as follows 

   |Path Name|Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value|
   |---------|-------------------|---------------|------------------------|----------|
   |deckId   |y                  |spec           |deckId                  |N/A       |
* And the user set the request attributes as follows 

   |Attribute Value In JSON Template|Attribute Value To Be Set                                                                                        |
   |--------------------------------|-----------------------------------------------------------------------------------------------------------------|
   |#title                          |API Deck3                                                                                                        |
   |#description                    |Test description for API Deck3                                                                                   |
   |#tags1                          |API tag1                                                                                                         |
   |#subjectId                      |2                                                                                                                |
   |#subjectName                    |API Testing3                                                                                                     |
   |#bookAuthor                     |Osanda Nimalarathna                                                                                              |
   |#bookTitle                      |                                                                                                                 |
   |#bookChapter                    |Chap. 04                                                                                                         |
   |#purchasedDate                  |1512021142001                                                                                                    |
   |#purchaseInformationPrice       |777                                                                                                              |
   |#purchaseInformationsku         |com.pearson.smartflashcards.test3                                                                                |
   |#areNotificationsEnabled        |true                                                                                                             |
   |#notificationTime               |08:00                                                                                                            |
   |#notificationFrequency          |1                                                                                                                |
   |#examDate                       |1512021142000                                                                                                    |
   |#userId                         |34                                                                                                               |
   |#parentDeckId                   |5                                                                                                                |
   |#tempDeckId                     |999                                                                                                              |
   |#archived                       |false                                                                                                            |
   |#cardPreview                    |true                                                                                                             |
   |#noOfCards                      |2                                                                                                                |
   |#progress                       |3                                                                                                                |
   |#downloads                      |12                                                                                                               |
   |#deckAuthorName                 |Osanda                                                                                                           |
   |#deckAuthorId                   |6                                                                                                                |
   |#thumbnailUrl                   |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a154f35d5b71d1a8a54dd58/download/public?format=ORIGINAL|
   |#status                         |Closed                                                                                                           |
   |#starred                        |true                                                                                                             |
   |#categoryId                     |5a5db30a12ef181b0af109ba                                                                                         |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following 

   |JSON Path                                     |Value                                                                                                            |
   |----------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
   |$.title                                       |API Deck3                                                                                                        |
   |$.description                                 |Test description for API Deck3                                                                                   |
   |$.tags[0]                                     |API tag1                                                                                                         |
   |$.book.bookAuthor                             |Osanda Nimalarathna                                                                                              |
   |$.book.chapter                                |Chap. 04                                                                                                         |
   |$.notificationSettings.areNotificationsEnabled|true                                                                                                             |
   |$.notificationSettings.notificationTime       |08:00                                                                                                            |
   |$.notificationSettings.notificationFrequency  |1                                                                                                                |
   |$.examDate                                    |1512021142000                                                                                                    |
   |$.userId                                      |34                                                                                                               |
   |$.parentDeckId                                |5                                                                                                                |
   |$.tempDeckId                                  |999                                                                                                              |
   |$.archived                                    |false                                                                                                            |
   |$.cardPreview                                 |true                                                                                                             |
   |$.noOfCards                                   |2                                                                                                                |
   |$.progress                                    |3                                                                                                                |
   |$.downloads                                   |12                                                                                                               |
   |$.deckAuthor                                  |Osanda                                                                                                           |
   |$.deckAuthorId                                |6                                                                                                                |
   |$.thumbnailUrl                                |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a154f35d5b71d1a8a54dd58/download/public?format=ORIGINAL|
   |$.status                                      |Closed                                                                                                           |
   |$.expert                                      |false                                                                                                            |
   |$.starred                                     |true                                                                                                             |
   |$.purchaseInfo.price                          |777.0                                                                                                            |
   |$.categoryId                                  |5a5db30a12ef181b0af109ba                                                                                         |



## Get a deck
* Given that a user needs to invoke "Get a Deck using Aggregation service"
* And the user set the request authentication configurations as follows 

   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |Yes                |
   |Do you need to retrieve the access token from the text file?      |Yes                |
   |Provide the access token if you need to authorize the API manually|N/A                |
* And the user set the path parameters using data stores as follows 

   |Path Name|Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value|
   |---------|-------------------|---------------|------------------------|----------|
   |deckId   |y                  |spec           |deckId                  |N/A       |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the values inside the data stores 

   |JSON Path|Is Data Store Used?|Data Store Type|Data Store Variable Name|Expected Value|
   |---------|-------------------|---------------|------------------------|--------------|
   |$.id     |y                  |spec           |deckId                  |N/A           |
* And the JSON Path Assertions for the response should be equal to the following 

   |JSON Path                                     |Value                                                                                                            |
   |----------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
   |$.title                                       |API Deck3                                                                                                        |
   |$.description                                 |Test description for API Deck3                                                                                   |
   |$.tags[0]                                     |API tag1                                                                                                         |
   |$.book.bookAuthor                             |Osanda Nimalarathna                                                                                              |
   |$.book.chapter                                |Chap. 04                                                                                                         |
   |$.notificationSettings.areNotificationsEnabled|true                                                                                                             |
   |$.notificationSettings.notificationTime       |08:00                                                                                                            |
   |$.notificationSettings.notificationFrequency  |1                                                                                                                |
   |$.examDate                                    |1512021142000                                                                                                    |
   |$.userId                                      |34                                                                                                               |
   |$.parentDeckId                                |5                                                                                                                |
   |$.tempDeckId                                  |999                                                                                                              |
   |$.archived                                    |false                                                                                                            |
   |$.cardPreview                                 |true                                                                                                             |
   |$.noOfCards                                   |2                                                                                                                |
   |$.progress                                    |3                                                                                                                |
   |$.downloads                                   |12                                                                                                               |
   |$.deckAuthor                                  |Osanda                                                                                                           |
   |$.deckAuthorId                                |6                                                                                                                |
   |$.thumbnailUrl                                |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a154f35d5b71d1a8a54dd58/download/public?format=ORIGINAL|
   |$.status                                      |Closed                                                                                                           |
   |$.expert                                      |false                                                                                                            |
   |$.starred                                     |true                                                                                                             |
   |$.purchaseInfo.price                          |777.0                                                                                                            |
   |$.categoryId                                  |5a5db30a12ef181b0af109ba                                                                                         |



## Get all decks for a user
* Given that a user needs to invoke "Get all Decks using Aggregation service"
* And the user set the request authentication configurations as follows 

   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |Yes                |
   |Do you need to retrieve the access token from the text file?      |Yes                |
   |Provide the access token if you need to authorize the API manually|N/A                |
* And the user set the path parameters using data stores as follows 

   |Path Name|Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value|
   |---------|-------------------|---------------|------------------------|----------|
   |$.userId |y                  |spec           |userId                  |N/A       |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the values inside the data stores 

   |JSON Path   |Is Data Store Used?|Data Store Type|Data Store Variable Name|Expected Value|
   |------------|-------------------|---------------|------------------------|--------------|
   |$[-1].id    |y                  |spec           |deckId                  |N/A           |
   |$[-1].title |y                  |spec           |title                   |N/A           |
   |$[-1].userId|y                  |spec           |userId                  |N/A           |



## Delete a deck
* Given that a user needs to invoke "Delete a Deck using Aggregation Service"
* And the user set the request authentication configurations as follows 

   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |Yes                |
   |Do you need to retrieve the access token from the text file?      |Yes                |
   |Provide the access token if you need to authorize the API manually|N/A                |
* And the user set the path parameters using data stores as follows 

   |Path Name|Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value|
   |---------|-------------------|---------------|------------------------|----------|
   |deckId   |y                  |spec           |deckId                  |N/A       |
* When the user invokes the API
* Then the status code for the request is "204"
