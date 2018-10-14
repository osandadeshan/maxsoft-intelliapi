# Get Questions Count using Aggregation Service Specification
Date Created    : 03/26/2018
Version   		: 1.0.0
Owner      		: Osanda Deshan
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.


tags: get_questions_count, ci_ready



## Get questions count using a valid expert deckId with newly created questions
* Create an expert deck with all types of 9 questions
* Given that a user needs to invoke "Get Questions Count using Aggregation Service"
* And the user set the request authentication configurations as follows 

   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |Yes                |
   |Do you need to retrieve the access token from the text file?      |Yes                |
   |Provide the access token if you need to authorize the API manually|N/A                |
* And the user set the query parameters using data stores as follows 

   |Query Name|Is Data Store Used?|Data Store Type|Data Store Variable Name  |Query Value|
   |----------|-------------------|---------------|--------------------------|-----------|
   |deckId    |y                  |spec           |expertDeckIdWith9Questions|N/A        |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the values inside the data stores 

   |JSON Path      |Is Data Store Used?|Data Store Type|Data Store Variable Name  |Value|
   |---------------|-------------------|---------------|--------------------------|-----|
   |$.deckId       |y                  |spec           |expertDeckIdWith9Questions|     |
   |$.questionCount|n                  |               |                          |9    |



## Edit the last question of that expert deck
* Create an expert deck with all types of 9 questions
* Given that a user needs to invoke "Edit Short Answer Type Question using Aggregation Service"
* And the user set the request authentication configurations as follows 

   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |Yes                |
   |Do you need to retrieve the access token from the text file?      |Yes                |
   |Provide the access token if you need to authorize the API manually|N/A                |
* And the user set the path parameters using data stores as follows 

   |Path Name |Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value|
   |----------|-------------------|---------------|------------------------|----------|
   |questionId|y                  |scenario       |questionId              |N/A       |
* And the user set the request attributes using data stores as follows 

   |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name  |Attribute Value To Be Set                                                                                        |
   |--------------------------------|-------------------|---------------|--------------------------|-----------------------------------------------------------------------------------------------------------------|
   |#creatorId                      |n                  |               |                          |osanda12                                                                                                         |
   |#creatorPlatform                |n                  |               |                          |Web                                                                                                              |
   |#creatoredSource                |n                  |               |                          |App                                                                                                              |
   |#creatoredType                  |n                  |               |                          |Manual                                                                                                           |
   |#deckId                         |y                  |spec           |expertDeckIdWith9Questions|                                                                                                                 |
   |#isDeleted                      |n                  |               |                          |false                                                                                                            |
   |#tempQuestionId                 |n                  |               |                          |testId                                                                                                           |
   |#kind                           |n                  |               |                          |SHORT_ANSWER                                                                                                     |
   |#learningObjectives             |n                  |               |                          |                                                                                                                 |
   |#imageUrl                       |n                  |               |                          |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL|
   |#media                          |n                  |               |                          |TEXT                                                                                                             |
   |#questionPrompt                 |n                  |               |                          |What is Gauge?                                                                                                   |
   |#promptType                     |n                  |               |                          |TEXT                                                                                                             |
   |#timeout                        |n                  |               |                          |60                                                                                                               |
   |#rationale                      |n                  |               |                          |rationale                                                                                                        |
   |#boxId                          |n                  |               |                          |0                                                                                                                |
   |#correctAttempts                |n                  |               |                          |1                                                                                                                |
   |#inCorrectAttempts              |n                  |               |                          |0                                                                                                                |
   |#lastAswered                    |n                  |               |                          |2018-01-01T12:00:00+01:00                                                                                        |
   |#questionId                     |n                  |               |                          |0                                                                                                                |
   |#skips                          |n                  |               |                          |0                                                                                                                |
   |#userId                         |n                  |               |                          |0                                                                                                                |
   |#correctAnswerId                |n                  |               |                          |1                                                                                                                |
   |#correctAnswerValue             |n                  |               |                          |An Automation Framework                                                                                          |
   |#iscorrectAnswerCaseSensitive   |n                  |               |                          |false                                                                                                            |
   |#correctAnswerType              |n                  |               |                          |TEXT                                                                                                             |
   |#tags                           |n                  |               |                          |MaxSoft                                                                                                          |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following 

   |JSON Path            |Value                  |
   |---------------------|-----------------------|
   |$.question.prompt    |What is Gauge?         |
   |$.question.media     |TEXT                   |
   |$.question.promptType|TEXT                   |
   |$.kind               |SHORT_ANSWER           |
   |$.deleted            |false                  |
   |$.answers[0].value   |An Automation Framework|



## Get questions count using a valid expert deckId with newly created questions and edited question
* Given that a user needs to invoke "Get Questions Count using Aggregation Service"
* And the user set the request authentication configurations as follows 

   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |Yes                |
   |Do you need to retrieve the access token from the text file?      |Yes                |
   |Provide the access token if you need to authorize the API manually|N/A                |
* And the user set the query parameters using data stores as follows 

   |Query Name|Is Data Store Used?|Data Store Type|Data Store Variable Name  |Query Value|
   |----------|-------------------|---------------|--------------------------|-----------|
   |deckId    |y                  |spec           |expertDeckIdWith9Questions|N/A        |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the values inside the data stores 

   |JSON Path      |Is Data Store Used?|Data Store Type|Data Store Variable Name  |Value|
   |---------------|-------------------|---------------|--------------------------|-----|
   |$.deckId       |y                  |spec           |expertDeckIdWith9Questions|     |
   |$.questionCount|n                  |               |                          |9    |



## Delete a question in that expert deck
* Create an expert deck with all types of 9 questions
* Given that a user needs to invoke "Delete a Question using Aggregation Service"
* And the user set the request authentication configurations as follows 

   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |Yes                |
   |Do you need to retrieve the access token from the text file?      |Yes                |
   |Provide the access token if you need to authorize the API manually|N/A                |
* And the user set the path parameters using data stores as follows 

   |Path Name |Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value|
   |----------|-------------------|---------------|------------------------|----------|
   |questionId|y                  |scenario       |questionId              |N/A       |
* When the user invokes the API
* Then the status code for the request is "204"

## Get questions count using a valid expert deckId with newly created questions and deleted question
* Given that a user needs to invoke "Get Questions Count using Aggregation Service"
* And the user set the request authentication configurations as follows 

   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |Yes                |
   |Do you need to retrieve the access token from the text file?      |Yes                |
   |Provide the access token if you need to authorize the API manually|N/A                |
* And the user set the query parameters using data stores as follows 

   |Query Name|Is Data Store Used?|Data Store Type|Data Store Variable Name  |Query Value|
   |----------|-------------------|---------------|--------------------------|-----------|
   |deckId    |y                  |spec           |expertDeckIdWith9Questions|N/A        |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the values inside the data stores 

   |JSON Path      |Is Data Store Used?|Data Store Type|Data Store Variable Name  |Value|
   |---------------|-------------------|---------------|--------------------------|-----|
   |$.deckId       |y                  |spec           |expertDeckIdWith9Questions|     |
   |$.questionCount|n                  |               |                          |8    |



## Delete the previously created expert deck with 8 questions
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

## Get questions count using a valid my deckId with newly created questions
* Create a my deck with all types of 9 questions
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
   |deckId    |y                  |spec           |myDeckIdWith9Questions  |N/A        |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the values inside the data stores 

   |JSON Path      |Is Data Store Used?|Data Store Type|Data Store Variable Name|Value|
   |---------------|-------------------|---------------|------------------------|-----|
   |$.deckId       |y                  |spec           |myDeckIdWith9Questions  |     |
   |$.questionCount|n                  |               |                        |9    |



## Edit the last question of that my deck
* Create a my deck with all types of 9 questions
* Given that a user needs to invoke "Edit Short Answer Type Question using Aggregation Service"
* And the user set the request authentication configurations as follows 

   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |Yes                |
   |Do you need to retrieve the access token from the text file?      |Yes                |
   |Provide the access token if you need to authorize the API manually|N/A                |
* And the user set the path parameters using data stores as follows 

   |Path Name |Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value|
   |----------|-------------------|---------------|------------------------|----------|
   |questionId|y                  |scenario       |questionId              |N/A       |
* And the user set the request attributes using data stores as follows 

   |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name|Attribute Value To Be Set                                                                                        |
   |--------------------------------|-------------------|---------------|------------------------|-----------------------------------------------------------------------------------------------------------------|
   |#creatorId                      |n                  |               |                        |osanda12                                                                                                         |
   |#creatorPlatform                |n                  |               |                        |Web                                                                                                              |
   |#creatoredSource                |n                  |               |                        |App                                                                                                              |
   |#creatoredType                  |n                  |               |                        |Manual                                                                                                           |
   |#deckId                         |y                  |spec           |myDeckIdWith9Questions  |                                                                                                                 |
   |#isDeleted                      |n                  |               |                        |false                                                                                                            |
   |#tempQuestionId                 |n                  |               |                        |testId                                                                                                           |
   |#kind                           |n                  |               |                        |SHORT_ANSWER                                                                                                     |
   |#learningObjectives             |n                  |               |                        |                                                                                                                 |
   |#imageUrl                       |n                  |               |                        |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL|
   |#media                          |n                  |               |                        |TEXT                                                                                                             |
   |#questionPrompt                 |n                  |               |                        |What is Gauge?                                                                                                   |
   |#promptType                     |n                  |               |                        |TEXT                                                                                                             |
   |#timeout                        |n                  |               |                        |60                                                                                                               |
   |#rationale                      |n                  |               |                        |rationale                                                                                                        |
   |#boxId                          |n                  |               |                        |0                                                                                                                |
   |#correctAttempts                |n                  |               |                        |1                                                                                                                |
   |#inCorrectAttempts              |n                  |               |                        |0                                                                                                                |
   |#lastAswered                    |n                  |               |                        |2018-01-01T12:00:00+01:00                                                                                        |
   |#questionId                     |n                  |               |                        |0                                                                                                                |
   |#skips                          |n                  |               |                        |0                                                                                                                |
   |#userId                         |n                  |               |                        |0                                                                                                                |
   |#correctAnswerId                |n                  |               |                        |1                                                                                                                |
   |#correctAnswerValue             |n                  |               |                        |An Automation Framework                                                                                          |
   |#iscorrectAnswerCaseSensitive   |n                  |               |                        |false                                                                                                            |
   |#correctAnswerType              |n                  |               |                        |TEXT                                                                                                             |
   |#tags                           |n                  |               |                        |MaxSoft                                                                                                          |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following 

   |JSON Path            |Value                  |
   |---------------------|-----------------------|
   |$.question.prompt    |What is Gauge?         |
   |$.question.media     |TEXT                   |
   |$.question.promptType|TEXT                   |
   |$.kind               |SHORT_ANSWER           |
   |$.deleted            |false                  |
   |$.answers[0].value   |An Automation Framework|



## Get questions count using a valid my deckId with newly created questions and edited question
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
   |deckId    |y                  |spec           |myDeckIdWith9Questions  |N/A        |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the values inside the data stores 

   |JSON Path      |Is Data Store Used?|Data Store Type|Data Store Variable Name|Value|
   |---------------|-------------------|---------------|------------------------|-----|
   |$.deckId       |y                  |spec           |myDeckIdWith9Questions  |     |
   |$.questionCount|n                  |               |                        |9    |



## Delete a question in that my deck
* Create a my deck with all types of 9 questions
* Given that a user needs to invoke "Delete a Question using Aggregation Service"
* And the user set the request authentication configurations as follows 

   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |Yes                |
   |Do you need to retrieve the access token from the text file?      |Yes                |
   |Provide the access token if you need to authorize the API manually|N/A                |
* And the user set the path parameters using data stores as follows 

   |Path Name |Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value|
   |----------|-------------------|---------------|------------------------|----------|
   |questionId|y                  |scenario       |questionId              |N/A       |
* When the user invokes the API
* Then the status code for the request is "204"

## Get questions count using a valid my deckId with newly created questions and deleted question
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
   |deckId    |y                  |spec           |myDeckIdWith9Questions  |N/A        |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the values inside the data stores 

   |JSON Path      |Is Data Store Used?|Data Store Type|Data Store Variable Name|Value|
   |---------------|-------------------|---------------|------------------------|-----|
   |$.deckId       |y                  |spec           |myDeckIdWith9Questions  |     |
   |$.questionCount|n                  |               |                        |8    |



## Delete the previously created my deck with 8 questions
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
   |deckId   |y                  |spec           |myDeckIdWith9Questions  |N/A       |
* When the user invokes the API
* Then the status code for the request is "204"
