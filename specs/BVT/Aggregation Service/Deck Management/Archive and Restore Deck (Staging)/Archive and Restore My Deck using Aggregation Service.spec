# Archive and Restore My Deck using Aggregation Service Specification
Date Created    : 05/01/18
Version   		: 1.0.0
Owner      		: Osanda Deshan
Description  	: This specification covers archive deck scenarios from the aggregation service


tags: aggregation_service, deck_management, archive_my_deck, restore_my_deck, ci_ready



## Create a deck with archived false and add 4 MCQ questions
* Create a deck with 4 MCQ questions

## Counting the number of questions inside that deck
* Given that a user needs to invoke "Get Questions Count using Aggregation Service"
* And the user set the request authentication configurations as follows 

   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |Yes                |
   |Do you need to retrieve the access token from the text file?      |Yes                |
   |Provide the access token if you need to authorize the API manually|N/A                |
* And the user set the query parameters using data stores as follows 

   |Query Name|Is Data Store Used?|Data Store Type|Data Store Variable Name|Query Value|
   |----------|-------------------|---------------|------------------------|-----------|
   |deckId    |y                  |spec           |deckId                  |N/A        |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the values inside the data stores 

   |JSON Path      |Is Data Store Used?|Data Store Type|Data Store Variable Name|Value|
   |---------------|-------------------|---------------|------------------------|-----|
   |$.deckId       |y                  |spec           |deckId                  |     |
   |$.questionCount|n                  |               |                        |4    |



## Invoke PI API in Staging Environment using valid username and password and save the access token inside the text file

tags: get_pi_token, staging

* Given that a user needs to invoke "Get Staging PI Token"
* And the user set the request authentication configurations as follows 

   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |Yes                |
   |Do you need to retrieve the access token from the text file?      |Yes                |
   |Provide the access token if you need to authorize the API manually|N/A                |
* And the user set the request attributes as follows 

   |Attribute Value In JSON Template|Attribute Value To Be Set|
   |--------------------------------|-------------------------|
   |#username                       |sfc_system               |
   |#password                       |J6rfS39Js2xv49zZ         |
* When the user invokes the API
* Then the status code for the request is "201"
* And the JSON Path Assertions for the response should be equal to the following 

   |JSON Path|Expected Result|
   |---------|---------------|
   |$.status |success        |
* And save the access token in the response which is located inside the JSON Path of "$.data"

## Find that deck with archived false in PLA
* Given that a user needs to invoke "PLA Get Content API"
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
   |$.deckId |y                  |spec           |deckId                  |N/A           |



## Initially created cards are inside the deck in PLA
* Given that a user needs to invoke "PLA Get Content API"
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
* And the JSON Path values of the response should contains the values inside the data stores 

   |JSON Path|Is Data Store Used?|Data Store Type|Data Store Variable Name|Expected Value|
   |---------|-------------------|---------------|------------------------|--------------|
   |$.cards  |y                  |spec           |mcqCardId1              |N/A           |
   |$.cards  |y                  |spec           |mcqCardId2              |N/A           |
   |$.cards  |y                  |spec           |mcqCardId3              |N/A           |
   |$.cards  |y                  |spec           |mcqCardId4              |N/A           |



## Archive the deck
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
   |#description                    |"null"                                                                                                           |
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
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following 

   |JSON Path                                     |Value                                                                                                            |
   |----------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
   |$.title                                       |API Deck3                                                                                                        |
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



## Counting the number of questions inside that archived deck
* Given that a user needs to invoke "Get Questions Count using Aggregation Service"
* And the user set the request authentication configurations as follows 

   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |Yes                |
   |Do you need to retrieve the access token from the text file?      |Yes                |
   |Provide the access token if you need to authorize the API manually|N/A                |
* And the user set the query parameters using data stores as follows 

   |Query Name|Is Data Store Used?|Data Store Type|Data Store Variable Name|Query Value|
   |----------|-------------------|---------------|------------------------|-----------|
   |deckId    |y                  |spec           |deckId                  |N/A        |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the values inside the data stores 

   |JSON Path      |Is Data Store Used?|Data Store Type|Data Store Variable Name|Value|
   |---------------|-------------------|---------------|------------------------|-----|
   |$.deckId       |y                  |spec           |deckId                  |     |
   |$.questionCount|n                  |               |                        |4    |



## Find the above archived deck in PLA
* Given that a user needs to invoke "PLA Get Content API"
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
   |$.deckId |y                  |spec           |deckId                  |N/A           |



## Initially created cards are inside the above archived deck in PLA
* Given that a user needs to invoke "PLA Get Content API"
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
* And the JSON Path values of the response should contains the values inside the data stores 

   |JSON Path|Is Data Store Used?|Data Store Type|Data Store Variable Name|Expected Value|
   |---------|-------------------|---------------|------------------------|--------------|
   |$.cards  |y                  |spec           |mcqCardId1              |N/A           |
   |$.cards  |y                  |spec           |mcqCardId2              |N/A           |
   |$.cards  |y                  |spec           |mcqCardId3              |N/A           |
   |$.cards  |y                  |spec           |mcqCardId4              |N/A           |



## Restore the deck
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
   |#description                    |"null"                                                                                                           |
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
   |$.categoryId                                  |5a5db30a12ef181b0af109ba                                                                                         |



## Verify all the questions are in the restored deck
* Given that a user needs to invoke "Get all Questions using Aggregation Service"
* And the user set the request authentication configurations as follows 

   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |Yes                |
   |Do you need to retrieve the access token from the text file?      |Yes                |
   |Provide the access token if you need to authorize the API manually|N/A                |
* And the user set the query parameters using data stores as follows 

   |Query Name|Is Data Store Used?|Data Store Type|Data Store Variable Name|Query Value|
   |----------|-------------------|---------------|------------------------|-----------|
   |deckId    |y                  |spec           |deckId                  |N/A        |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the values inside the data stores 

   |JSON Path            |Is Data Store Used?|Data Store Type|Data Store Variable Name|Expected Value|
   |---------------------|-------------------|---------------|------------------------|--------------|
   |$.questions[0].deckId|y                  |spec           |deckId                  |N/A           |
* And the JSON Path Assertions for the response should be equal to the following 

   |JSON Path           |Value|
   |--------------------|-----|
   |$.questions.length()|4    |



## Counting the number of questions inside that restored deck
* Given that a user needs to invoke "Get Questions Count using Aggregation Service"
* And the user set the request authentication configurations as follows 

   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |Yes                |
   |Do you need to retrieve the access token from the text file?      |Yes                |
   |Provide the access token if you need to authorize the API manually|N/A                |
* And the user set the query parameters using data stores as follows 

   |Query Name|Is Data Store Used?|Data Store Type|Data Store Variable Name|Query Value|
   |----------|-------------------|---------------|------------------------|-----------|
   |deckId    |y                  |spec           |deckId                  |N/A        |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the values inside the data stores 

   |JSON Path      |Is Data Store Used?|Data Store Type|Data Store Variable Name|Value|
   |---------------|-------------------|---------------|------------------------|-----|
   |$.deckId       |y                  |spec           |deckId                  |     |
   |$.questionCount|n                  |               |                        |4    |



## Find that restored deck in PLA
* Given that a user needs to invoke "PLA Get Content API"
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
   |$.deckId |y                  |spec           |deckId                  |N/A           |



## Above created cards are inside the restored deck in PLA
* Given that a user needs to invoke "PLA Get Content API"
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
* And the JSON Path values of the response should contains the values inside the data stores 

   |JSON Path|Is Data Store Used?|Data Store Type|Data Store Variable Name|Expected Value|
   |---------|-------------------|---------------|------------------------|--------------|
   |$.cards  |y                  |spec           |mcqCardId1              |N/A           |
   |$.cards  |y                  |spec           |mcqCardId2              |N/A           |
   |$.cards  |y                  |spec           |mcqCardId3              |N/A           |
   |$.cards  |y                  |spec           |mcqCardId4              |N/A           |




