Create MCQ Type Question using Question Service - Data Driven Positive Test Specification
=========================================================================================
Date Created    : 11/06/2017
Version   		: 1.0.0
Owner      		: Osanda Deshan
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.


tags: create_question, create_question_mcq_type, create_question-positive_tests, positive


table: /resources/data_driven_test_csv/create_question/question_service/create_question_mcq_type-positive_tests.csv



* Given that a user needs to invoke <api>
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |



Create a question using a valid payload
---------------------------------------
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
     |#correctAnswerList              |<correctAnswerList>                     |
     |#answer1Id                      |<answer1Id>                             |
     |#answer1Value                   |<answer1Value>                          |
     |#answer1Type                    |<answer1Type>                           |
     |#answer1CaseSensitive           |<answer1CaseSensitive>                  |
     |#answer2Id                      |<answer2Id>                             |
     |#answer2Value                   |<answer2Value>                          |
     |#answer2Type                    |<answer2Type>                           |
     |#answer2CaseSensitive           |<answer2CaseSensitive>                  |
     |#answer3Id                      |<answer3Id>                             |
     |#answer3Value                   |<answer3Value>                          |
     |#answer3Type                    |<answer3Type>                           |
     |#answer3CaseSensitive           |<answer3CaseSensitive>                  |
     |#answer4Id                      |<answer4Id>                             |
     |#answer4Value                   |<answer4Value>                          |
     |#answer4Type                    |<answer4Type>                           |
     |#answer4CaseSensitive           |<answer4CaseSensitive>                  |
     |#answer5Id                      |<answer5Id>                             |
     |#answer5Value                   |<answer5Value>                          |
     |#answer5Type                    |<answer5Type>                           |
     |#answer5CaseSensitive           |<answer5CaseSensitive>                  |
     |#tags                           |<tags>                                  |
* When the user invokes the API
* Then the status code for the request is "201"
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
     |$.tags                                    |<tags>                                                   |
     |$.creatorId                               |<creatorId>                                              |
     |$.creatoredType                           |<creatoredType>                                          |
     |$.creatorPlatform                         |<creatorPlatform>                                        |
     |$.creatoredSource                         |<creatoredSource>                                        |
     |$.correctAnswers[0]                       |<correctAnswerList>                                      |
     |$.deleted                                 |<isDeleted>                                              |
     |$.tempQuestionId                          |<tempQuestionId>                                         |
//     |$.answers[0].id                           |<answer1Id>                                              |
//     |$.answers[0].value                        |<answer1Value>                                           |
//     |$.answers[0].type                         |<answer1Type>                                            |
//     |$.answers[0].caseSensitive                |<answer1CaseSensitive>                                   |
//     |$.answers[1].id                           |<answer2Id>                                              |
//     |$.answers[1].value                        |<answer2Value>                                           |
//     |$.answers[1].type                         |<answer2Type>                                            |
//     |$.answers[1].caseSensitive                |<answer2CaseSensitive>                                   |
//     |$.answers[2].id                           |<answer3Id>                                              |
//     |$.answers[2].value                        |<answer3Value>                                           |
//     |$.answers[2].type                         |<answer3Type>                                            |
//     |$.answers[2].caseSensitive                |<answer3CaseSensitive>                                   |
//     |$.answers[3].id                           |<answer4Id>                                              |
//     |$.answers[3].value                        |<answer4Value>                                           |
//     |$.answers[3].type                         |<answer4Type>                                            |
//     |$.answers[3].caseSensitive                |<answer4CaseSensitive>                                   |
