# Archive and Restore Expert Deck using Aggregation Service Specification
Date Created    : 05/01/18
Version   		: 1.0.0
Owner      		: Osanda Deshan
Description  	: This specification covers archive deck scenarios from the aggregation service


tags: aggregation_service, deck_management, archive_expert_deck, restore_expert_deck, ci_ready



## Add an expert deck to my deck
* Create an expert deck with 4 questions
* Given that a user needs to invoke "Add Expert Deck To My Deck using Aggregation Service"
* And the user set the request authentication configurations as follows 

   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |Yes                |
   |Do you need to retrieve the access token from the text file?      |Yes                |
   |Provide the access token if you need to authorize the API manually|N/A                |
* And the user set the path parameters using data stores as follows 

   |Path Parameter|Is Data Store Used?|Data Store Type|Data Store Variable Name  |Path Value|
   |--------------|-------------------|---------------|--------------------------|----------|
   |deckId        |y                  |spec           |expertDeckIdWith4Questions|          |
   |users         |n                  |               |                          |users     |
   |userId        |n                  |               |                          |osan      |
* When the user invokes the API
* Then the status code for the request is "201"
* And save the JSON Path values in the response inside the data stores 

   |DataStore Type|Variable Name        |Value To Be Stored|
   |--------------|---------------------|------------------|
   |spec          |purchasedExpertDeckId|$.id              |



## Verify all the questions are in the newly added deck
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
   |deckId    |y                  |spec           |purchasedExpertDeckId   |N/A        |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the values inside the data stores 

   |JSON Path            |Is Data Store Used?|Data Store Type|Data Store Variable Name|Expected Value|
   |---------------------|-------------------|---------------|------------------------|--------------|
   |$.questions[0].deckId|y                  |spec           |purchasedExpertDeckId   |N/A           |
* And the JSON Path Assertions for the response should be equal to the following 

   |JSON Path           |Value|
   |--------------------|-----|
   |$.questions.length()|4    |
* And save the JSON Path values in the response inside the data stores 

   |DataStore Type|Variable Name|Value To Be Stored|
   |--------------|-------------|------------------|
   |spec          |mcqCardId1   |$.questions[0].id |
   |spec          |mcqCardId2   |$.questions[1].id |
   |spec          |mcqCardId3   |$.questions[2].id |
   |spec          |mcqCardId4   |$.questions[3].id |



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
   |deckId    |y                  |spec           |purchasedExpertDeckId   |N/A        |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the values inside the data stores 

   |JSON Path      |Is Data Store Used?|Data Store Type|Data Store Variable Name|Value|
   |---------------|-------------------|---------------|------------------------|-----|
   |$.deckId       |y                  |spec           |purchasedExpertDeckId   |     |
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
   |deckId   |y                  |spec           |purchasedExpertDeckId   |N/A       |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the values inside the data stores 

   |JSON Path|Is Data Store Used?|Data Store Type|Data Store Variable Name|Expected Value|
   |---------|-------------------|---------------|------------------------|--------------|
   |$.deckId |y                  |spec           |purchasedExpertDeckId   |N/A           |



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
   |deckId   |y                  |spec           |purchasedExpertDeckId   |N/A       |
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
   |deckId   |y                  |spec           |purchasedExpertDeckId   |N/A       |
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
   |deckId    |y                  |spec           |purchasedExpertDeckId   |N/A        |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the values inside the data stores 

   |JSON Path      |Is Data Store Used?|Data Store Type|Data Store Variable Name|Value|
   |---------------|-------------------|---------------|------------------------|-----|
   |$.deckId       |y                  |spec           |purchasedExpertDeckId   |     |
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
   |deckId   |y                  |spec           |purchasedExpertDeckId   |N/A       |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the values inside the data stores 

   |JSON Path|Is Data Store Used?|Data Store Type|Data Store Variable Name|Expected Value|
   |---------|-------------------|---------------|------------------------|--------------|
   |$.deckId |y                  |spec           |purchasedExpertDeckId   |N/A           |



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
   |deckId   |y                  |spec           |purchasedExpertDeckId   |N/A       |
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
   |deckId   |y                  |spec           |purchasedExpertDeckId   |N/A       |
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
   |deckId    |y                  |spec           |purchasedExpertDeckId   |N/A        |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the values inside the data stores 

   |JSON Path            |Is Data Store Used?|Data Store Type|Data Store Variable Name|Expected Value|
   |---------------------|-------------------|---------------|------------------------|--------------|
   |$.questions[0].deckId|y                  |spec           |purchasedExpertDeckId   |N/A           |
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
   |deckId    |y                  |spec           |purchasedExpertDeckId   |N/A        |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the values inside the data stores 

   |JSON Path      |Is Data Store Used?|Data Store Type|Data Store Variable Name|Value|
   |---------------|-------------------|---------------|------------------------|-----|
   |$.deckId       |y                  |spec           |purchasedExpertDeckId   |     |
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
   |deckId   |y                  |spec           |purchasedExpertDeckId   |N/A       |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the values inside the data stores 

   |JSON Path|Is Data Store Used?|Data Store Type|Data Store Variable Name|Expected Value|
   |---------|-------------------|---------------|------------------------|--------------|
   |$.deckId |y                  |spec           |purchasedExpertDeckId   |N/A           |



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
   |deckId   |y                  |spec           |purchasedExpertDeckId   |N/A       |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path values of the response should contains the values inside the data stores 

   |JSON Path|Is Data Store Used?|Data Store Type|Data Store Variable Name|Expected Value|
   |---------|-------------------|---------------|------------------------|--------------|
   |$.cards  |y                  |spec           |mcqCardId1              |N/A           |
   |$.cards  |y                  |spec           |mcqCardId2              |N/A           |
   |$.cards  |y                  |spec           |mcqCardId3              |N/A           |
   |$.cards  |y                  |spec           |mcqCardId4              |N/A           |



## Delete the previously created expert deck
* Given that a user needs to invoke "Delete Expert Deck by ID using Expert Deck Service"
* And the user set the request authentication configurations as follows 

   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |Yes                |
   |Do you need to retrieve the access token from the text file?      |Yes                |
   |Provide the access token if you need to authorize the API manually|N/A                |
* And the user set the path parameters using data stores as follows 

   |Path Name|Is Data Store Used?|Data Store Type|Data Store Variable Name  |Path Value|
   |---------|-------------------|---------------|--------------------------|----------|
   |deckId   |y                  |spec           |expertDeckIdWith4Questions|N/A       |
* When the user invokes the API
* Then the status code for the request is "204"

