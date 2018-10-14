# Copy Decks using Aggregation Service Specification
Date Created    : 01/08/2018
Version   		: 1.0.0
Owner      		: Osanda Deshan
Description  	: This specification covers copy decks scenarios from the aggregation service


tags: aggregation_service, deck_management, copy_decks, ci_ready



## Copy questions from My Deck to My Deck

tags: copy_decks, positive

* Create a deck
* And save the JSON Path values in the response inside the data stores 

   |DataStore Type|Variable Name|Value To Be Stored|
   |--------------|-------------|------------------|
   |spec          |deckId       |$.id              |
* Create a deck with 4 questions
* Given that a user needs to invoke "Copy Decks using Aggregation Service"
* And the user set the request authentication configurations as follows 

   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |Yes                |
   |Do you need to retrieve the access token from the text file?      |Yes                |
   |Provide the access token if you need to authorize the API manually|N/A                |
* And the user set the query parameters using data stores as follows 

   |Query Parameter|Is Data Store Used?|Data Store Type|Data Store Variable Name|Query Value|
   |---------------|-------------------|---------------|------------------------|-----------|
   |sourceId       |y                  |spec           |deckIdWith4Questions    |           |
   |destinationId  |y                  |spec           |deckId                  |           |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following 

   |JSON Path           |Value|
   |--------------------|-----|
   |$.questions.length()|4    |



## Validate the previously copied questions from My Deck
* Given that a user needs to invoke "Get Questions using Aggregation Service"
* And the user set the request authentication configurations as follows 

   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |Yes                |
   |Do you need to retrieve the access token from the text file?      |Yes                |
   |Provide the access token if you need to authorize the API manually|N/A                |
* And the user set the query parameters using data stores as follows 

   |Query Parameter|Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value|
   |---------------|-------------------|---------------|------------------------|----------|
   |deckId         |y                  |spec           |deckId                  |          |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following 

   |JSON Path           |Value|
   |--------------------|-----|
   |$.questions.length()|4    |



## Validate the question count in above my deck copied from another my deck using question count API
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



## Copy questions from Expert Deck to My Deck

tags: copy_decks, positive

* Create a deck
* And save the JSON Path values in the response inside the data stores 

   |DataStore Type|Variable Name|Value To Be Stored|
   |--------------|-------------|------------------|
   |spec          |deckId2      |$.id              |
* Create an expert deck with 4 questions
* Given that a user needs to invoke "Copy Decks using Aggregation Service"
* And the user set the request authentication configurations as follows 

   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |Yes                |
   |Do you need to retrieve the access token from the text file?      |Yes                |
   |Provide the access token if you need to authorize the API manually|N/A                |
* And the user set the query parameters using data stores as follows 

   |Query Parameter|Is Data Store Used?|Data Store Type|Data Store Variable Name  |Query Value|
   |---------------|-------------------|---------------|--------------------------|-----------|
   |sourceId       |y                  |spec           |expertDeckIdWith4Questions|           |
   |destinationId  |y                  |spec           |deckId2                   |           |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following 

   |JSON Path           |Value|
   |--------------------|-----|
   |$.questions.length()|4    |



## Validate the previously copied questions from Expert Deck
* Given that a user needs to invoke "Get Questions using Aggregation Service"
* And the user set the request authentication configurations as follows 

   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |Yes                |
   |Do you need to retrieve the access token from the text file?      |Yes                |
   |Provide the access token if you need to authorize the API manually|N/A                |
* And the user set the query parameters using data stores as follows 

   |Query Parameter|Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value|
   |---------------|-------------------|---------------|------------------------|----------|
   |deckId         |y                  |spec           |deckId2                 |          |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following 

   |JSON Path           |Value|
   |--------------------|-----|
   |$.questions.length()|4    |



## Validate the question count in above my deck copied from an expert deck using question count API
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
   |deckId    |y                  |spec           |deckId2                 |N/A        |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the values inside the data stores 

   |JSON Path      |Is Data Store Used?|Data Store Type|Data Store Variable Name|Value|
   |---------------|-------------------|---------------|------------------------|-----|
   |$.deckId       |y                  |spec           |deckId2                 |     |
   |$.questionCount|n                  |               |                        |4    |



## Delete the previously created expert deck with 4 questions
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

## Copy all types of questions from Expert Deck to My Deck

tags: copy_decks, positive

* Create a deck
* And save the JSON Path values in the response inside the data stores 

   |DataStore Type|Variable Name|Value To Be Stored|
   |--------------|-------------|------------------|
   |spec          |myDeckId     |$.id              |
* Create an expert deck with all types of 9 questions
* Given that a user needs to invoke "Copy Decks using Aggregation Service"
* And the user set the request authentication configurations as follows 

   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |Yes                |
   |Do you need to retrieve the access token from the text file?      |Yes                |
   |Provide the access token if you need to authorize the API manually|N/A                |
* And the user set the query parameters using data stores as follows 

   |Query Parameter|Is Data Store Used?|Data Store Type|Data Store Variable Name  |Query Value|
   |---------------|-------------------|---------------|--------------------------|-----------|
   |sourceId       |y                  |spec           |expertDeckIdWith9Questions|           |
   |destinationId  |y                  |spec           |myDeckId                  |           |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following 

   |JSON Path           |Value|
   |--------------------|-----|
   |$.questions.length()|9    |



## Validate the previously copied all types of questions from Expert Deck
* Given that a user needs to invoke "Get Questions using Aggregation Service"
* And the user set the request authentication configurations as follows 

   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |Yes                |
   |Do you need to retrieve the access token from the text file?      |Yes                |
   |Provide the access token if you need to authorize the API manually|N/A                |
* And the user set the query parameters using data stores as follows 

   |Query Parameter|Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value|
   |---------------|-------------------|---------------|------------------------|----------|
   |deckId         |y                  |spec           |myDeckId                |          |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following 

   |JSON Path           |Value|
   |--------------------|-----|
   |$.questions.length()|9    |



## Validate the all types of question count in above my deck copied from an expert deck using question count API
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
   |deckId    |y                  |spec           |myDeckId                |N/A        |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the values inside the data stores 

   |JSON Path      |Is Data Store Used?|Data Store Type|Data Store Variable Name|Value|
   |---------------|-------------------|---------------|------------------------|-----|
   |$.deckId       |y                  |spec           |myDeckId                |     |
   |$.questionCount|n                  |               |                        |9    |



## Delete the previously created expert deck with 9 questions
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
   |deckId   |y                  |spec           |expertDeckIdWith9Questions|N/A       |
* When the user invokes the API
* Then the status code for the request is "204"

