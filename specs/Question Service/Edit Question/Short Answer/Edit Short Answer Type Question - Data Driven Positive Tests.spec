Edit Short Answer Type Question using Question Service - Data Driven Positive Test Specification
================================================================================================
Date Created    : 02/04/2018
Version   		: 1.0.0
Owner      		: Osanda Deshan
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.


tags: edit_question, edit_question_short_answer_type, edit_question-positive_tests, positive


table: /resources/data_driven_test_csv/edit_question/question_service/edit_question_short_answer_type-positive_tests.csv



* Create a short answer type question
* And save the JSON Path values in the response inside the data stores
    |DataStore Type |Variable Name  |Value To Be Stored     |
    |---------------|---------------|-----------------------|
    |scenario       |questionId     |$.id                   |
* Given that a user needs to invoke "Edit Short Answer Type Question using Question Service"
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |
* And the user set the path parameters using data stores as follows
    |Path Name      |Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value     |
    |---------------|-------------------|---------------|------------------------|---------------|
    |questionId     |y                  |scenario       |questionId              |N/A            |



Edit a question using a valid payload
-------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set               |
     |--------------------------------|----------------------------------------|
     |#creatorId                      |<creatorId>                             |
     |#creatorPlatform                |<creatorPlatform>                       |
     |#creatoredSource                |<creatoredSource>                       |
     |#creatoredType                  |<creatoredType>                         |
     |#deckId                         |<deckId>                                |
     |#isDeleted                      |<isDeleted>                             |
     |#tempQuestionId                 |<tempQuestionId>                        |
     |#kind                           |<kind>                                  |
     |#learningObjectives             |<learningObjectives>                    |
     |#imageUrl                       |<imageUrl>                              |
     |#media                          |<media>                                 |
     |#questionPrompt                 |<prompt>                                |
     |#promptType                     |<promptType>                            |
     |#timeout                        |<timeout>                               |
     |#rationale                      |<rationale>                             |
     |#boxId                          |<boxId>                                 |
     |#correctAttempts                |<correctAttempts>                       |
     |#inCorrectAttempts              |<inCorrectAttempts>                     |
     |#lastAswered                    |<lastAswered>                           |
     |#questionId                     |<questionId>                            |
     |#skips                          |<skips>                                 |
     |#userId                         |<userId>                                |
     |#correctAnswerId                |<correctAnswerId>                       |
     |#correctAnswerValue             |<correctAnswer>                         |
     |#iscorrectAnswerCaseSensitive   |<iscorrectAnswerCaseSensitive>          |
     |#correctAnswerType              |<correctAnswerType>                     |
     |#tags                           |<tags>                                  |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.question.media                          |<media>                                                  |
     |$.question.prompt                         |<prompt>                                                 |
     |$.question.imageUrl                       |<imageUrl>                                               |
     |$.question.promptType                     |<promptType>                                             |
     |$.stats.questionId                        |<questionId>                                             |
     |$.stats.userId                            |<userId>                                                 |
     |$.stats.boxId                             |<boxId>                                                  |
     |$.stats.skips                             |<skips>                                                  |
     |$.stats.inCorrectAttempts                 |<inCorrectAttempts>                                      |
     |$.stats.correctAttempts                   |<correctAttempts>                                        |
     |$.learningObjectives                      |<learningObjectives>                                     |
     |$.rationale                               |<rationale>                                              |
     |$.tags[0]                                 |<tags>                                                   |
     |$.creatorId                               |<creatorId>                                              |
     |$.creatoredType                           |<creatoredType>                                          |
     |$.creatorPlatform                         |<creatorPlatform>                                        |
     |$.creatoredSource                         |<creatoredSource>                                        |
     |$.deleted                                 |<isDeleted>                                              |
     |$.tempQuestionId                          |<tempQuestionId>                                         |
     |$.answers[0].id                           |<correctAnswerId>                                        |
     |$.answers[0].value                        |<correctAnswer>                                          |
     |$.answers[0].caseSensitive                |<iscorrectAnswerCaseSensitive>                           |
     |$.answers[0].type                         |<correctAnswerType>                                      |
// Cannot assert lastAnswered since we can give it as ISO DateTime format and it returns epoch time