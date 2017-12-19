Edit Short Answer Type Question - Negative Test Specification
=============================================================
Date Created    : 11/15/2017
Version   		: 1.0.0
Owner      		: Osanda Deshan
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.


tags: edit_question, edit_question-negative_tests, negative



* Given that a user needs to invoke "Edit Short Answer Type Question"



Edit a question using an invalid creatorId
--------------------------------------------
* And the user set the request authentication configurations as follows
     |Configuration Property Name       |Configuration Property Value   |
     |----------------------------------|-------------------------------|
     |isAccessTokenIncluded             |True                           |
     |isAccessTokenRetrievedFromTextFile|True                           |
     |accessTokenString                 |N/A                            |
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda                                                   |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |51                                                       |
     |#kind                           |SHORT_ANSWER                                             |
     |#learningObjectives             |learningObjective1                                       |
     |#imageUrl                       |www.maxsoft.com/image                                    |
     |#media                          |TEXT                                                     |
     |#questionPrompt                 |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |TEXT                                                     |
     |#timeout                        |60                                                       |
     |#rationale                      |rationale                                                |
     |#boxId                          |0                                                        |
     |#correctAttempts                |1                                                        |
     |#inCorrectAttempts              |0                                                        |
     |#lastAswered                    |11/8/2017                                                |
     |#questionId                     |0                                                        |
     |#skips                          |0                                                        |
     |#userId                         |0                                                        |
     |#correctAnswerId                |1                                                        |
     |#correctAnswerValue             |Osanda Deshan                                            |
     |#iscorrectAnswerCaseSensitive   |false                                                    |
     |#correctAnswerType              |TEXT                                                     |
     |#tags                           |MaxSoft                                                  |
* And the user set the path parameters as follows
     |Path Parameter |Path Value               |
     |---------------|-------------------------|
     |Id             |5a0974b75ed274e204b9554c |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.question.prompt                         |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |$.question.media                          |TEXT                                                     |
     |$.question.promptType                     |TEXT                                                     |
     |$.kind                                    |SHORT_ANSWER                                             |
     |$.answers[0].value                        |Osanda Deshan                                            |