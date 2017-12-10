Create Short Answer Type Question - Positive Test Specification
===============================================================
Date Created    : 11/06/2017
Version   		: 1.0.0
Owner      		: Osanda Deshan
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.


tags: create_question, create_question_short_answer_type, create_question-positive_tests, positive



* Given that a user needs to invoke "Create Short Answer Type Question"



Create a question using a decimal value as the boxId
----------------------------------------------------
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
     |#deckId                         |51                                                       |
     |#kind                           |SHORT_ANSWER                                             |
     |#learningObjectives             |objective1                                               |
     |#imageUrl                       |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |TEXT                                                     |
     |#questionPrompt                 |Who is the owner of MaxSoft?                             |
     |#promptType                     |TEXT                                                     |
     |#timeout                        |120                                                      |
     |#rationale                      |rationale                                                |
     |#boxId                          |5.5                                                      |
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
* When the user invokes the API
* Then the status code for the request is "201"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.stats.boxId                             |5                                                        |



Create a question using a decimal value as the userId
-----------------------------------------------------
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
     |#deckId                         |51                                                       |
     |#kind                           |SHORT_ANSWER                                             |
     |#learningObjectives             |objective1                                               |
     |#imageUrl                       |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |TEXT                                                     |
     |#questionPrompt                 |Who is the owner of MaxSoft?                             |
     |#promptType                     |TEXT                                                     |
     |#timeout                        |120                                                      |
     |#rationale                      |rationale                                                |
     |#boxId                          |1                                                        |
     |#correctAttempts                |1                                                        |
     |#inCorrectAttempts              |0                                                        |
     |#lastAswered                    |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |0                                                        |
     |#skips                          |0                                                        |
     |#userId                         |2.5                                                      |
     |#correctAnswerId                |1                                                        |
     |#correctAnswerValue             |Osanda Deshan                                            |
     |#iscorrectAnswerCaseSensitive   |false                                                    |
     |#correctAnswerType              |TEXT                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "201"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.stats.userId                            |2                                                        |



Create a question using a decimal value as the questionId
---------------------------------------------------------
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
     |#deckId                         |51                                                       |
     |#kind                           |SHORT_ANSWER                                             |
     |#learningObjectives             |objective1                                               |
     |#imageUrl                       |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |TEXT                                                     |
     |#questionPrompt                 |Who is the owner of MaxSoft?                             |
     |#promptType                     |TEXT                                                     |
     |#timeout                        |120                                                      |
     |#rationale                      |rationale                                                |
     |#boxId                          |1                                                        |
     |#correctAttempts                |1                                                        |
     |#inCorrectAttempts              |0                                                        |
     |#lastAswered                    |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |1.2                                                      |
     |#skips                          |0                                                        |
     |#userId                         |0                                                        |
     |#correctAnswerId                |1                                                        |
     |#correctAnswerValue             |Osanda Deshan                                            |
     |#iscorrectAnswerCaseSensitive   |false                                                    |
     |#correctAnswerType              |TEXT                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "201"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.stats.questionId                        |1                                                        |



Create a question using an empty value as the lastAswered
---------------------------------------------------------
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
     |#deckId                         |51                                                       |
     |#kind                           |SHORT_ANSWER                                             |
     |#learningObjectives             |objective1                                               |
     |#imageUrl                       |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |TEXT                                                     |
     |#questionPrompt                 |Who is the owner of MaxSoft?                             |
     |#promptType                     |TEXT                                                     |
     |#timeout                        |120                                                      |
     |#rationale                      |rationale                                                |
     |#boxId                          |1                                                        |
     |#correctAttempts                |1                                                        |
     |#inCorrectAttempts              |0                                                        |
     |#lastAswered                    |                                                         |
     |#questionId                     |0                                                        |
     |#skips                          |0                                                        |
     |#userId                         |0                                                        |
     |#correctAnswerId                |1                                                        |
     |#correctAnswerValue             |Osanda Deshan                                            |
     |#iscorrectAnswerCaseSensitive   |false                                                    |
     |#correctAnswerType              |TEXT                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "201"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.stats.lastAswered                       |null                                                     |



Create a question using a decimal value as the inCorrectAttempts
----------------------------------------------------------------
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
     |#deckId                         |51                                                       |
     |#kind                           |SHORT_ANSWER                                             |
     |#learningObjectives             |objective1                                               |
     |#imageUrl                       |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |TEXT                                                     |
     |#questionPrompt                 |Who is the owner of MaxSoft?                             |
     |#promptType                     |TEXT                                                     |
     |#timeout                        |120                                                      |
     |#rationale                      |rationale                                                |
     |#boxId                          |1                                                        |
     |#correctAttempts                |1                                                        |
     |#inCorrectAttempts              |2.5                                                      |
     |#lastAswered                    |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |0                                                        |
     |#skips                          |0                                                        |
     |#userId                         |0                                                        |
     |#correctAnswerId                |1                                                        |
     |#correctAnswerValue             |Osanda Deshan                                            |
     |#iscorrectAnswerCaseSensitive   |false                                                    |
     |#correctAnswerType              |TEXT                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "201"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.stats.inCorrectAttempts                 |2                                                        |



Create a question using a decimal value as the correctAttempts
--------------------------------------------------------------
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
     |#deckId                         |51                                                       |
     |#kind                           |SHORT_ANSWER                                             |
     |#learningObjectives             |objective1                                               |
     |#imageUrl                       |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |TEXT                                                     |
     |#questionPrompt                 |Who is the owner of MaxSoft?                             |
     |#promptType                     |TEXT                                                     |
     |#timeout                        |120                                                      |
     |#rationale                      |rationale                                                |
     |#boxId                          |1                                                        |
     |#correctAttempts                |1.1                                                      |
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
* When the user invokes the API
* Then the status code for the request is "201"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.stats.correctAttempts                   |1                                                        |



Create a question using a decimal value as the skips
----------------------------------------------------
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
     |#deckId                         |51                                                       |
     |#kind                           |SHORT_ANSWER                                             |
     |#learningObjectives             |objective1                                               |
     |#imageUrl                       |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |TEXT                                                     |
     |#questionPrompt                 |Who is the owner of MaxSoft?                             |
     |#promptType                     |TEXT                                                     |
     |#timeout                        |120                                                      |
     |#rationale                      |rationale                                                |
     |#boxId                          |1                                                        |
     |#correctAttempts                |1                                                        |
     |#inCorrectAttempts              |0                                                        |
     |#lastAswered                    |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |0                                                        |
     |#skips                          |2.1                                                      |
     |#userId                         |0                                                        |
     |#correctAnswerId                |1                                                        |
     |#correctAnswerValue             |Osanda Deshan                                            |
     |#iscorrectAnswerCaseSensitive   |false                                                    |
     |#correctAnswerType              |TEXT                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "201"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.stats.skips                             |2                                                        |



Create a question using a positive integer value as the iscorrectAnswerCaseSensitive
------------------------------------------------------------------------------------
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
     |#deckId                         |51                                                       |
     |#kind                           |SHORT_ANSWER                                             |
     |#learningObjectives             |objective1                                               |
     |#imageUrl                       |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |TEXT                                                     |
     |#questionPrompt                 |Who is the owner of MaxSoft?                             |
     |#promptType                     |TEXT                                                     |
     |#timeout                        |120                                                      |
     |#rationale                      |rationale                                                |
     |#boxId                          |1                                                        |
     |#correctAttempts                |1                                                        |
     |#inCorrectAttempts              |0                                                        |
     |#lastAswered                    |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |0                                                        |
     |#skips                          |0                                                        |
     |#userId                         |0                                                        |
     |#correctAnswerId                |1                                                        |
     |#correctAnswerValue             |Osanda Deshan                                            |
     |#iscorrectAnswerCaseSensitive   |123                                                      |
     |#correctAnswerType              |TEXT                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "201"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.answers[0].caseSensitive                |true                                                     |



Create a question using negative integer value as the iscorrectAnswerCaseSensitive
----------------------------------------------------------------------------------
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
     |#deckId                         |51                                                       |
     |#kind                           |SHORT_ANSWER                                             |
     |#learningObjectives             |objective1                                               |
     |#imageUrl                       |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |TEXT                                                     |
     |#questionPrompt                 |Who is the owner of MaxSoft?                             |
     |#promptType                     |TEXT                                                     |
     |#timeout                        |120                                                      |
     |#rationale                      |rationale                                                |
     |#boxId                          |1                                                        |
     |#correctAttempts                |1                                                        |
     |#inCorrectAttempts              |0                                                        |
     |#lastAswered                    |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |0                                                        |
     |#skips                          |0                                                        |
     |#userId                         |0                                                        |
     |#correctAnswerId                |1                                                        |
     |#correctAnswerValue             |Osanda Deshan                                            |
     |#iscorrectAnswerCaseSensitive   |-1                                                       |
     |#correctAnswerType              |TEXT                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "201"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.answers[0].caseSensitive                |true                                                     |
