Aggregated Text Questions Specification
=======================================
Date Created    : 11/22/2017
Version   		: 1.0.0
Owner      		: Osanda Deshan
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.


tags: aggregated_question, aggregated_question-positive_tests, positive


table: /resources/data_driven_test_csv/aggregated_questions/aggregated_questions-text-positive_tests.csv



* Given that a user needs to invoke <api>



Aggregate a text question using a valid payload
-----------------------------------------------
* Given that a user needs to invoke "Aggregated Text Questions"
* And the user set the request authentication configurations as follows
     |Configuration Property Name       |Configuration Property Value   |
     |----------------------------------|-------------------------------|
     |isAccessTokenIncluded             |True                           |
     |isAccessTokenRetrievedFromTextFile|True                           |
     |accessTokenString                 |N/A                            |
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#deckId                         |<deckId>                                                 |
     |#timeout                        |<timeout>                                                |
     |#media                          |<media>                                                  |
     |#imageUrl                       |<imageUrl>                                               |
     |#promptType                     |<promptType>                                             |
     |#questionId                     |<questionId>                                             |
     |#userId                         |<userId>                                                 |
     |#boxId                          |<boxId>                                                  |
     |#skips                          |<skips>                                                  |
     |#lastAswered                    |<lastAswered>                                            |
     |#correctAttempts                |<correctAttempts>                                        |
     |#inCorrectAttempts              |<inCorrectAttempts>                                      |
     |#creatorId                      |<creatorId>                                              |
     |#creatorPlatform                |<creatorPlatform>                                          |
     |#creatoredSource                |<creatoredSource>                                        |
     |#creatoredType                  |<creatoredType>                                          |
     |#title                          |<title>                                                  |
     |#user                           |<user>                                                   |
     |#isExpert                       |<isExpert>                                               |
     |#questionText                   |<questionText>                                           |
     |#examDate                       |                                                         |
     |#points                         |2                                                        |
* When the user invokes the API
* Then the status code for the request is "201"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                    |Value                                                    |
     |---------------------------------------------|---------------------------------------------------------|
     |$[0].question.media                          |<media>                                                  |
     |$[0].question.prompt                         |<prompt>                                                 |
     |$[0].question.imageUrl                       |<imageUrl>                                               |
     |$[0].question.promptType                     |<promptType>                                             |
     |$[0].question.timeout                        |<timeout>                                                |
     |$[0].stats.questionId                        |<questionId>                                             |
     |$[0].stats.userId                            |<userId>                                                 |
     |$[0].stats.boxId                             |<boxId>                                                  |
     |$[0].stats.skips                             |<skips>                                                  |
     |$[0].stats.lastAswered                       |<lastAswered>                                            |
     |$[0].stats.inCorrectAttempts                 |<inCorrectAttempts>                                      |
     |$[0].stats.correctAttempts                   |<correctAttempts>                                        |
     |$[0].kind                                    |<kind>                                                   |
     |$[0].learningObjectives                      |<learningObjectives>                                     |
     |$[0].rationale                               |<rationale>                                              |
     |$[0].creatorId                               |<creatorId>                                              |
     |$[0].creatoredType                           |<creatoredType>                                          |
     |$[0].creatorPlatform                         |<creatorPlatform>                                        |
     |$[0].creatoredSource                         |<creatoredSource>                                        |
     |$[0].correctAnswers[0].value                 |<correctAnswer1>                                         |
     |$[0].correctAnswers[0].caseSensitive         |<iscorrectAnswer1CaseSensitive>                          |
     |$[0].correctAnswers[0].type                  |<correctAnswer1Type>                                     |