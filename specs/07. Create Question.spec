Create Question Specification
=============================
Date Created    : 11/06/2017
Version   		: 1.0.0
Owner      		: Osanda Deshan
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.


tags: create_question


table: /resources/data_driven_test_csv/create_question.csv



* Given that a user needs to invoke <api>



Create a question using a valid payload
---------------------------------------
* And the user set the request authentication configurations as follows
     |Configuration Property Name       |Configuration Property Value   |
     |----------------------------------|-------------------------------|
     |isAccessTokenIncluded             |True                           |
     |isAccessTokenRetrievedFromTextFile|True                           |
     |accessTokenString                 |N/A                            |
     |isHeadersInclueded                |False                          |
     |isJsonBodyIncluded                |True                           |
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set               |
     |--------------------------------|----------------------------------------|
     |#creatorId                      |<creatorId>                             |
     |#creatorPlatform                |<creatorPlatform>                       |
     |#creatoredSource                |<creatoredSource>                       |
     |#creatoredType                  |<creatoredType>                         |
     |#deckId                         |<deckId>                                |
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
     |#correctAnswer1                 |<correctAnswer1>                        |
     |#iscorrectAnswer1CaseSensitive  |<iscorrectAnswer1CaseSensitive>         |
     |#tags                           |<tags>                                  |
* When the user invokes the API
* Then the status code for the request is "201"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.question.prompt                         |<prompt>                                                 |
     |$.question.media                          |<media>                                                  |
     |$.question.promptType                     |<promptType>                                             |
     |$.kind                                    |<kind>                                                   |
     |$.correctAnswers[0].value                 |<correctAnswer1>                                         |