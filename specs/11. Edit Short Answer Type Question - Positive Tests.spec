Edit Short Answer Type Question - Positive Test Specification
=============================================================
Date Created    : 11/15/2017
Version   		: 1.0.0
Owner      		: Osanda Deshan
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.


tags: edit_question, edit_question-positive_tests, positive



* Given that a user needs to invoke "Edit Short Answer Type Question"



Edit a question using an valid creatorId
----------------------------------------
* And the user set the request authentication configurations as follows
     |Configuration Property Name       |Configuration Property Value   |
     |----------------------------------|-------------------------------|
     |isAccessTokenIncluded             |True                           |
     |isAccessTokenRetrievedFromTextFile|True                           |
     |accessTokenString                 |N/A                            |
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |41                                                       |
     |#kind                           |SHORT_ANSWER                                             |
     |#learningObjectives             |objective1                                               |
     |#imageUrl                       |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |TEXT                                                     |
     |#questionPrompt                 |Who is Osanda Deshan?                                    |
     |#promptType                     |TEXT                                                     |
     |#timeout                        |120                                                      |
     |#rationale                      |rationale                                                |
     |#boxId                          |5                                                        |
     |#correctAttempts                |1                                                        |
     |#inCorrectAttempts              |0                                                        |
     |#lastAswered                    |2018-01-01T12:00:00+01:00                                |
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
     |Id             |5a095d1b5ed274e204b9554b |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.question.prompt                         |Who is Osanda Deshan?                                    |
     |$.question.media                          |TEXT                                                     |
     |$.question.promptType                     |TEXT                                                     |
     |$.kind                                    |SHORT_ANSWER                                             |
     |$.answers[0].value                        |Osanda Deshan                                            |