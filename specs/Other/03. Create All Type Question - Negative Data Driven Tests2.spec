# Create All Type Question using Question Service - Negative Data Driven Test Specification2
Date Created    : 19/06/2018
Version   		: 1.0.0
Owner      		: Tharukie Jayasinghe
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.


tags: create_question, create_question_all_type, create_question-negative_tests, negative


table: ./resources/data_driven_test_csv/create_question/question_service/create_question_all_type-negative_tests_2.csv



* Create a deck
* And save the JSON Path values in the response inside the data stores 

   |DataStore Type|Variable Name|Value To Be Stored|
   |--------------|-------------|------------------|
   |scenario      |deckId       |$.id              |
* Given that a user needs to invoke <api>
* And the user set the request authentication configurations as follows 

   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |Yes                |
   |Do you need to retrieve the access token from the text file?      |Yes                |
   |Provide the access token if you need to authorize the API manually|N/A                |



## Create a question negative tests
* And the user set the request attributes using data stores as follows 

   |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name|Attribute Value To Be Set|
   |--------------------------------|-------------------|---------------|------------------------|-------------------------|
   |#creatorId                      |n                  |               |                        |<creatorId>              |
   |#creatorPlatform                |n                  |               |                        |<creatorPlatform>        |
   |#creatoredSource                |n                  |               |                        |<creatoredSource>        |
   |#creatoredType                  |n                  |               |                        |<creatoredType>          |
   |#deckId                         |y                  |scenario       |deckId                  |                         |
   |#kind                           |n                  |               |                        |<kind>                   |
   |#isDeleted                      |n                  |               |                        |<isDeleted>              |
   |#tempQuestionId                 |n                  |               |                        |<tempQuestionId>         |
   |#learningObjectives             |n                  |               |                        |<learningObjectives>     |
   |#imageUrl                       |n                  |               |                        |<imageUrl>               |
   |#media                          |n                  |               |                        |<media>                  |
   |#questionPrompt                 |n                  |               |                        |<prompt>                 |
   |#promptType                     |n                  |               |                        |<promptType>             |
   |#timeout                        |n                  |               |                        |<timeout>                |
   |#rationale                      |n                  |               |                        |<rationale>              |
   |#boxId                          |n                  |               |                        |<boxId>                  |
   |#correctAttempts                |n                  |               |                        |<correctAttempts>        |
   |#inCorrectAttempts              |n                  |               |                        |<inCorrectAttempts>      |
   |#lastAswered                    |n                  |               |                        |<lastAswered>            |
   |#questionId                     |n                  |               |                        |<questionId>             |
   |#skips                          |n                  |               |                        |<skips>                  |
   |#userId                         |n                  |               |                        |<userId>                 |
   |#correctAnswerList              |n                  |               |                        |<correctAnswerList>      |
   |#answer1Id                      |n                  |               |                        |<answer1Id>              |
   |#answer1Value                   |n                  |               |                        |<answer1Value>           |
   |#answer1Type                    |n                  |               |                        |<answer1Type>            |
   |#answer1CaseSensitive           |n                  |               |                        |<answer1CaseSensitive>   |
   |#answer2Id                      |n                  |               |                        |<answer2Id>              |
   |#answer2Value                   |n                  |               |                        |<answer2Value>           |
   |#answer2Type                    |n                  |               |                        |<answer2Type>            |
   |#answer2CaseSensitive           |n                  |               |                        |<answer2CaseSensitive>   |
   |#answer3Id                      |n                  |               |                        |<answer3Id>              |
   |#answer3Value                   |n                  |               |                        |<answer3Value>           |
   |#answer3Type                    |n                  |               |                        |<answer3Type>            |
   |#answer3CaseSensitive           |n                  |               |                        |<answer3CaseSensitive>   |
   |#answer4Id                      |n                  |               |                        |<answer4Id>              |
   |#answer4Value                   |n                  |               |                        |<answer4Value>           |
   |#answer4Type                    |n                  |               |                        |<answer4Type>            |
   |#answer4CaseSensitive           |n                  |               |                        |<answer4CaseSensitive>   |
   |#answer5Id                      |n                  |               |                        |<answer5Id>              |
   |#answer5Value                   |n                  |               |                        |<answer5Value>           |
   |#answer5Type                    |n                  |               |                        |<answer5Type>            |
   |#answer5CaseSensitive           |n                  |               |                        |<answer5CaseSensitive>   |
   |#tags                           |n                  |               |                        |<tags>                   |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path values of the response should contains the following 

   |JSON Path    |Value        |
   |-------------|-------------|
   |$.message    |<message>    |
   |$.description|<description>|
   |$.fieldErrors|<fieldErrors>|
