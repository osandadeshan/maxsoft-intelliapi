# Create Short Answer Type Question using Aggregation Service - Data Driven Positive Test Specification
Date Created    : 11/06/2017
Version   		: 1.0.0
Owner      		: Osanda Deshan
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.


tags: create_question, create_question_short_answer_type, create_question-positive_tests, positive


table: /resources/data_driven_test_csv/create_question/aggregation_service/create_question_short_answer_type-positive_tests.csv



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



## Create a question using a valid payload
* And the user set the request attributes using data stores as follows 

   |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name|Attribute Value To Be Set     |
   |--------------------------------|-------------------|---------------|------------------------|------------------------------|
   |#creatorId                      |n                  |               |                        |<creatorId>                   |
   |#creatorPlatform                |n                  |               |                        |<creatorPlatform>             |
   |#creatoredSource                |n                  |               |                        |<creatoredSource>             |
   |#creatoredType                  |n                  |               |                        |<creatoredType>               |
   |#deckId                         |y                  |scenario       |deckId                  |                              |
   |#isDeleted                      |n                  |               |                        |<isDeleted>                   |
   |#tempQuestionId                 |n                  |               |                        |<tempQuestionId>              |
   |#kind                           |n                  |               |                        |<kind>                        |
   |#learningObjectives             |n                  |               |                        |<learningObjectives>          |
   |#imageUrl                       |n                  |               |                        |<imageUrl>                    |
   |#media                          |n                  |               |                        |<media>                       |
   |#questionPrompt                 |n                  |               |                        |<prompt>                      |
   |#promptType                     |n                  |               |                        |<promptType>                  |
   |#timeout                        |n                  |               |                        |<timeout>                     |
   |#rationale                      |n                  |               |                        |<rationale>                   |
   |#boxId                          |n                  |               |                        |<boxId>                       |
   |#correctAttempts                |n                  |               |                        |<correctAttempts>             |
   |#inCorrectAttempts              |n                  |               |                        |<inCorrectAttempts>           |
   |#lastAswered                    |n                  |               |                        |<lastAswered>                 |
   |#questionId                     |n                  |               |                        |<questionId>                  |
   |#skips                          |n                  |               |                        |<skips>                       |
   |#userId                         |n                  |               |                        |<userId>                      |
   |#correctAnswerId                |n                  |               |                        |<correctAnswerId>             |
   |#correctAnswerValue             |n                  |               |                        |<correctAnswer>               |
   |#iscorrectAnswerCaseSensitive   |n                  |               |                        |<iscorrectAnswerCaseSensitive>|
   |#correctAnswerType              |n                  |               |                        |<correctAnswerType>           |
   |#tags                           |n                  |               |                        |<tags>                        |
* When the user invokes the API
* Then the status code for the request is "201"
* And the JSON Path Assertions for the response should be equal to the following 

   |JSON Path                 |Value                         |
   |--------------------------|------------------------------|
   |$.question.media          |<media>                       |
   |$.question.prompt         |<prompt>                      |
   |$.question.imageUrl       |<imageUrl>                    |
   |$.question.promptType     |<promptType>                  |
   |$.stats.questionId        |<questionId>                  |
   |$.stats.userId            |<userId>                      |
   |$.stats.boxId             |<boxId>                       |
   |$.stats.skips             |<skips>                       |
   |$.stats.inCorrectAttempts |<inCorrectAttempts>           |
   |$.stats.correctAttempts   |<correctAttempts>             |
   |$.learningObjectives      |<learningObjectives>          |
   |$.rationale               |<rationale>                   |
   |$.tags[0]                 |<tags>                        |
   |$.creatorId               |<creatorId>                   |
   |$.creatoredType           |<creatoredType>               |
   |$.creatorPlatform         |<creatorPlatform>             |
   |$.creatoredSource         |<creatoredSource>             |
   |$.deleted                 |<isDeleted>                   |
   |$.tempQuestionId          |<tempQuestionId>              |
   |$.answers[0].id           |<correctAnswerId>             |
   |$.answers[0].value        |<correctAnswer>               |
   |$.answers[0].caseSensitive|<iscorrectAnswerCaseSensitive>|
   |$.answers[0].type         |<correctAnswerType>           |
// Cannot assert lastAnswered since we can give it as ISO DateTime format and it returns epoch time
