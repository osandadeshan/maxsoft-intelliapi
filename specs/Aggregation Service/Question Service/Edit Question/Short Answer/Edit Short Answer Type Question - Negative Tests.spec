Edit Short Answer Type Question using Aggregation Service - Negative Test Specification
=======================================================================================
Date Editd    : 11/13/2017
Version   		: 1.0.0
Owner      		: Osanda Deshan
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.


tags: edit_question, edit_question_short_answer_type, edit_question-positive_tests, negative



* Create a short answer type question
* And save the JSON Path values in the response inside the data stores
    |DataStore Type |Variable Name  |Value To Be Stored     |
    |---------------|---------------|-----------------------|
    |scenario       |questionId     |$.id                   |
* Given that a user needs to invoke "Edit Short Answer Type Question using Aggregation Service"
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



Edit a question using an empty value for the creatorId
--------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |                                                         |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |5a603af62e02d86561172dac                                 |
     |#kind                           |SHORT_ANSWER                                             |
     |#learningObjectives             |learningObjective1                                       |
     |#imageUrl                       |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |TEXT                                                     |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
     |#questionPrompt                 |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |TEXT                                                     |
     |#timeout                        |60                                                       |
     |#rationale                      |rationale                                                |
     |#boxId                          |0                                                        |
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
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |error.validation                                         |
     |$.description                             |null                                                     |
     |$.fieldErrors[0].objectName               |                                                         |
     |$.fieldErrors[0].field                    |creatorId                                                |
     |$.fieldErrors[0].message                  |'creatorId' Cannot be null or empty                      |



Edit a question using an invalid creatorPlatform
--------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |We                                                       |
     |#creatoredSource                |App                                                      |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |5a603af62e02d86561172dac                                 |
     |#kind                           |SHORT_ANSWER                                             |
     |#learningObjectives             |learningObjective1                                       |
     |#imageUrl                       |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |TEXT                                                     |
     |#questionPrompt                 |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |TEXT                                                     |
     |#timeout                        |60                                                       |
     |#rationale                      |rationale                                                |
     |#boxId                          |0                                                        |
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
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |error.validation                                         |
     |$.description                             |null                                                     |
     |$.fieldErrors[0].objectName               |                                                         |
     |$.fieldErrors[0].field                    |creatorPlatform                                          |



Edit a question using an empty creatorPlatform
------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |                                                         |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |5a603af62e02d86561172dac                                 |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
     |#kind                           |SHORT_ANSWER                                             |
     |#learningObjectives             |learningObjective1                                       |
     |#imageUrl                       |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |TEXT                                                     |
     |#questionPrompt                 |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |TEXT                                                     |
     |#timeout                        |60                                                       |
     |#rationale                      |rationale                                                |
     |#boxId                          |0                                                        |
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
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |error.validation                                         |
     |$.description                             |null                                                     |
     |$.fieldErrors[0].objectName               |                                                         |
     |$.fieldErrors[0].field                    |creatorPlatform                                          |



Edit a question using an invalid creatoredSource
--------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |Ap                                                       |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |5a603af62e02d86561172dac                                 |
     |#kind                           |SHORT_ANSWER                                             |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
     |#learningObjectives             |learningObjective1                                       |
     |#imageUrl                       |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |TEXT                                                     |
     |#questionPrompt                 |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |TEXT                                                     |
     |#timeout                        |60                                                       |
     |#rationale                      |rationale                                                |
     |#boxId                          |0                                                        |
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
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |error.validation                                         |
     |$.description                             |null                                                     |
     |$.fieldErrors[0].objectName               |                                                         |
     |$.fieldErrors[0].field                    |creatoredSource                                          |



Edit a question using an empty creatoredSource
------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |                                                         |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |5a603af62e02d86561172dac                                 |
     |#kind                           |SHORT_ANSWER                                             |
     |#learningObjectives             |learningObjective1                                       |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
     |#imageUrl                       |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |TEXT                                                     |
     |#questionPrompt                 |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |TEXT                                                     |
     |#timeout                        |60                                                       |
     |#rationale                      |rationale                                                |
     |#boxId                          |0                                                        |
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
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |error.validation                                         |
     |$.description                             |null                                                     |
     |$.fieldErrors[0].objectName               |                                                         |
     |$.fieldErrors[0].field                    |creatoredSource                                          |



Edit a question using an invalid creatoredType
------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manua                                                    |
     |#deckId                         |5a603af62e02d86561172dac                                 |
     |#kind                           |SHORT_ANSWER                                             |
     |#learningObjectives             |learningObjective1                                       |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
     |#imageUrl                       |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |TEXT                                                     |
     |#questionPrompt                 |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |TEXT                                                     |
     |#timeout                        |60                                                       |
     |#rationale                      |rationale                                                |
     |#boxId                          |0                                                        |
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
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |error.validation                                         |
     |$.description                             |null                                                     |
     |$.fieldErrors[0].objectName               |                                                         |
     |$.fieldErrors[0].field                    |creatoredType                                            |



Edit a question using an empty creatoredType
----------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manua                                                    |
     |#deckId                         |5a603af62e02d86561172dac                                 |
     |#kind                           |SHORT_ANSWER                                             |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
     |#learningObjectives             |learningObjective1                                       |
     |#imageUrl                       |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |TEXT                                                     |
     |#questionPrompt                 |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |TEXT                                                     |
     |#timeout                        |60                                                       |
     |#rationale                      |rationale                                                |
     |#boxId                          |0                                                        |
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
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |error.validation                                         |
     |$.description                             |null                                                     |
     |$.fieldErrors[0].objectName               |                                                         |
     |$.fieldErrors[0].field                    |creatoredType                                            |



Edit a question using an empty deckId
---------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |                                                         |
     |#kind                           |SHORT_ANSWER                                             |
     |#learningObjectives             |learningObjective1                                       |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
     |#imageUrl                       |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |TEXT                                                     |
     |#questionPrompt                 |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |TEXT                                                     |
     |#timeout                        |60                                                       |
     |#rationale                      |rationale                                                |
     |#boxId                          |0                                                        |
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
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.description                             |null                                                     |
     |$.fieldErrors                             |null                                                     |



Edit a question using a null deckId
-------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |"null"                                                   |
     |#kind                           |SHORT_ANSWER                                             |
     |#learningObjectives             |learningObjective1                                       |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
     |#imageUrl                       |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |TEXT                                                     |
     |#questionPrompt                 |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |TEXT                                                     |
     |#timeout                        |60                                                       |
     |#rationale                      |rationale                                                |
     |#boxId                          |0                                                        |
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
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.description                             |null                                                     |
     |$.fieldErrors                             |null                                                     |



Edit a question using an integer deckId
-----------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |"#deckId"                       |2                                                        |
     |#kind                           |SHORT_ANSWER                                             |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
     |#learningObjectives             |learningObjective1                                       |
     |#imageUrl                       |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |TEXT                                                     |
     |#questionPrompt                 |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |TEXT                                                     |
     |#timeout                        |60                                                       |
     |#rationale                      |rationale                                                |
     |#boxId                          |0                                                        |
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
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.description                             |null                                                     |
     |$.fieldErrors                             |null                                                     |



Edit a question using an invalid kind
---------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |5a603af62e02d86561172dac                                 |
     |#kind                           |SHORT_ANSWE                                              |
     |#learningObjectives             |learningObjective1                                       |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
     |#imageUrl                       |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |TEXT                                                     |
     |#questionPrompt                 |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |TEXT                                                     |
     |#timeout                        |60                                                       |
     |#rationale                      |rationale                                                |
     |#boxId                          |0                                                        |
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
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.description                             |null                                                     |
     |$.fieldErrors                             |null                                                     |



Edit a question using an empty kind
-------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |5a603af62e02d86561172dac                                 |
     |#kind                           |                                                         |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
     |#learningObjectives             |learningObjective1                                       |
     |#imageUrl                       |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |TEXT                                                     |
     |#questionPrompt                 |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |TEXT                                                     |
     |#timeout                        |60                                                       |
     |#rationale                      |rationale                                                |
     |#boxId                          |0                                                        |
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
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.description                             |null                                                     |
     |$.fieldErrors                             |null                                                     |



Edit a question using an invalid media
----------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |5a603af62e02d86561172dac                                 |
     |#kind                           |SHORT_ANSWER                                             |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
     |#learningObjectives             |objective1                                               |
     |#imageUrl                       |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |TEX                                                      |
     |#questionPrompt                 |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |TEXT                                                     |
     |#timeout                        |60                                                       |
     |#rationale                      |rationale                                                |
     |#boxId                          |0                                                        |
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
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |error.validation                                         |
     |$.description                             |null                                                     |
     |$.fieldErrors[0].objectName               |                                                         |
     |$.fieldErrors[0].field                    |question.media                                           |
     |$.fieldErrors[0].message                  |must match \"TEXT\|HTML\|IMAGE\|VIDEO\|AUDIO             |



Edit a question using an empty media
--------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |5a603af62e02d86561172dac                                 |
     |#kind                           |SHORT_ANSWER                                             |
     |#learningObjectives             |objective1                                               |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
     |#imageUrl                       |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |                                                         |
     |#questionPrompt                 |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |TEXT                                                     |
     |#timeout                        |60                                                       |
     |#rationale                      |rationale                                                |
     |#boxId                          |0                                                        |
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
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |error.validation                                         |
     |$.description                             |null                                                     |
     |$.fieldErrors[0].objectName               |                                                         |
     |$.fieldErrors[0].field                    |question.media                                           |
     |$.fieldErrors[0].message                  |must match \"TEXT\|HTML\|IMAGE\|VIDEO\|AUDIO             |



Edit a question using an empty questionPrompt
-----------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |5a603af62e02d86561172dac                                 |
     |#kind                           |SHORT_ANSWER                                             |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
     |#learningObjectives             |objective1                                               |
     |#imageUrl                       |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |TEXT                                                     |
     |#questionPrompt                 |                                                         |
     |#promptType                     |TEXT                                                     |
     |#timeout                        |60                                                       |
     |#rationale                      |rationale                                                |
     |#boxId                          |0                                                        |
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
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |error.validation                                         |
     |$.description                             |null                                                     |
     |$.fieldErrors[0].objectName               |                                                         |
     |$.fieldErrors[0].field                    |question.prompt                                          |
     |$.fieldErrors[0].message                  |'prompt' Cannot be null or empty                         |



Edit a question using an invalid promptType
---------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |5a603af62e02d86561172dac                                 |
     |#kind                           |SHORT_ANSWER                                             |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
     |#learningObjectives             |objective1                                               |
     |#imageUrl                       |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |TEXT                                                     |
     |#questionPrompt                 |Who is the owner of MaxSoft?                             |
     |#promptType                     |TEX                                                      |
     |#timeout                        |60                                                       |
     |#rationale                      |rationale                                                |
     |#boxId                          |0                                                        |
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
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |error.validation                                         |
     |$.description                             |null                                                     |
     |$.fieldErrors[0].objectName               |                                                         |
     |$.fieldErrors[0].field                    |question.promptType                                      |
     |$.fieldErrors[0].message                  |must match \"HTML\|TEXT\|IMAGE                           |



Edit a question using an empty promptType
-------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |5a603af62e02d86561172dac                                 |
     |#kind                           |SHORT_ANSWER                                             |
     |#learningObjectives             |objective1                                               |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
     |#imageUrl                       |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |TEXT                                                     |
     |#questionPrompt                 |Who is the owner of MaxSoft?                             |
     |#promptType                     |                                                         |
     |#timeout                        |60                                                       |
     |#rationale                      |rationale                                                |
     |#boxId                          |0                                                        |
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
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
	 |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |error.validation                                         |
     |$.description                             |null                                                     |
     |$.fieldErrors[0].objectName               |                                                         |
     |$.fieldErrors[0].field                    |question.promptType                                      |
     |$.fieldErrors[0].message                  |must match \"HTML\|TEXT\|IMAGE                           |



Edit a question using a string as the timeout
-----------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |5a603af62e02d86561172dac                                 |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
     |#kind                           |SHORT_ANSWER                                             |
     |#learningObjectives             |objective1                                               |
     |#imageUrl                       |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |TEXT                                                     |
     |#questionPrompt                 |Who is the owner of MaxSoft?                             |
     |#promptType                     |TEXT                                                     |
     |#timeout                        |a0                                                       |
     |#rationale                      |rationale                                                |
     |#boxId                          |0                                                        |
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
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.description                             |null                                                     |
     |$.fieldErrors                             |null                                                     |



Edit a question using an negative value as the timeout
--------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |5a603af62e02d86561172dac                                 |
     |#kind                           |SHORT_ANSWER                                             |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
     |#learningObjectives             |objective1                                               |
     |#imageUrl                       |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |TEXT                                                     |
     |#questionPrompt                 |Who is the owner of MaxSoft?                             |
     |#promptType                     |TEXT                                                     |
     |#timeout                        |-20                                                      |
     |#rationale                      |rationale                                                |
     |#boxId                          |0                                                        |
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
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |error.validation                                         |
     |$.description                             |null                                                     |
     |$.fieldErrors[0].objectName               |                                                         |
     |$.fieldErrors[0].field                    |question.timeout                                         |
     |$.fieldErrors[0].message                  |'timeout' should be zero or positive integer.            |



Edit a question using a string value as the boxId
---------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |5a603af62e02d86561172dac                                 |
     |#kind                           |SHORT_ANSWER                                             |
     |#learningObjectives             |objective1                                               |
     |#imageUrl                       |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |TEXT                                                     |
     |#questionPrompt                 |Who is the owner of MaxSoft?                             |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
     |#promptType                     |TEXT                                                     |
     |#timeout                        |120                                                      |
     |#rationale                      |rationale                                                |
     |#boxId                          |boxId                                                    |
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
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.description                             |null                                                     |
     |$.fieldErrors                             |null                                                     |



Edit a question using a negative integer value as the boxId
-------------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |5a603af62e02d86561172dac                                 |
     |#kind                           |SHORT_ANSWER                                             |
     |#learningObjectives             |objective1                                               |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
     |#imageUrl                       |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |TEXT                                                     |
     |#questionPrompt                 |Who is the owner of MaxSoft?                             |
     |#promptType                     |TEXT                                                     |
     |#timeout                        |120                                                      |
     |#rationale                      |rationale                                                |
     |#boxId                          |-1                                                       |
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
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |error.validation                                         |
     |$.description                             |null                                                     |
     |$.fieldErrors[0].objectName               |                                                         |
     |$.fieldErrors[0].field                    |stats.boxId                                              |
     |$.fieldErrors[0].message                  |'boxId' should be zero or positive integer.              |



Edit a question using an empty value as the boxId
---------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
     |#deckId                         |5a603af62e02d86561172dac                                 |
     |#kind                           |SHORT_ANSWER                                             |
     |#learningObjectives             |objective1                                               |
     |#imageUrl                       |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |TEXT                                                     |
     |#questionPrompt                 |Who is the owner of MaxSoft?                             |
     |#promptType                     |TEXT                                                     |
     |#timeout                        |120                                                      |
     |#rationale                      |rationale                                                |
     |#boxId                          |5.5                                                      |
     |#correctAttempts                |                                                         |
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
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.description                             |null                                                     |
     |$.fieldErrors                             |null                                                     |



Edit a question using a string value as the correctAttempts
-------------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |5a603af62e02d86561172dac                                 |
     |#kind                           |SHORT_ANSWER                                             |
     |#learningObjectives             |objective1                                               |
     |#imageUrl                       |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |TEXT                                                     |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
     |#questionPrompt                 |Who is the owner of MaxSoft?                             |
     |#promptType                     |TEXT                                                     |
     |#timeout                        |120                                                      |
     |#rationale                      |rationale                                                |
     |#boxId                          |1                                                        |
     |#correctAttempts                |correctAt1                                               |
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
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.description                             |null                                                     |
     |$.fieldErrors                             |null                                                     |



Edit a question using a negative integer value as the correctAttempts
-----------------------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |5a603af62e02d86561172dac                                 |
     |#kind                           |SHORT_ANSWER                                             |
     |#learningObjectives             |objective1                                               |
     |#imageUrl                       |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |TEXT                                                     |
     |#questionPrompt                 |Who is the owner of MaxSoft?                             |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
     |#promptType                     |TEXT                                                     |
     |#timeout                        |120                                                      |
     |#rationale                      |rationale                                                |
     |#boxId                          |1                                                        |
     |#correctAttempts                |-1                                                       |
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
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |error.validation                                         |
     |$.description                             |null                                                     |
     |$.fieldErrors[0].objectName               |                                                         |
     |$.fieldErrors[0].field                    |stats.correctAttempts                                    |
     |$.fieldErrors[0].message                  |'correctAttempts' should be zero or positive integer.    |



Edit a question using a special characters value as the correctAttempts
-------------------------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |5a603af62e02d86561172dac                                 |
     |#kind                           |SHORT_ANSWER                                             |
     |#learningObjectives             |objective1                                               |
     |#imageUrl                       |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |TEXT                                                     |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
     |#questionPrompt                 |Who is the owner of MaxSoft?                             |
     |#promptType                     |TEXT                                                     |
     |#timeout                        |120                                                      |
     |#rationale                      |rationale                                                |
     |#boxId                          |1                                                        |
     |#correctAttempts                |@#                                                       |
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
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.description                             |null                                                     |
     |$.fieldErrors                             |null                                                     |



Edit a question using an empty value as the correctAttempts
-------------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |5a603af62e02d86561172dac                                 |
     |#kind                           |SHORT_ANSWER                                             |
     |#learningObjectives             |objective1                                               |
     |#imageUrl                       |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |TEXT                                                     |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
     |#questionPrompt                 |Who is the owner of MaxSoft?                             |
     |#promptType                     |TEXT                                                     |
     |#timeout                        |120                                                      |
     |#rationale                      |rationale                                                |
     |#boxId                          |1                                                        |
     |#correctAttempts                |                                                         |
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
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.description                             |null                                                     |
     |$.fieldErrors                             |null                                                     |



Edit a question using a special characters value as the inCorrectAttempts
---------------------------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |5a603af62e02d86561172dac                                 |
     |#kind                           |SHORT_ANSWER                                             |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
     |#learningObjectives             |objective1                                               |
     |#imageUrl                       |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |TEXT                                                     |
     |#questionPrompt                 |Who is the owner of MaxSoft?                             |
     |#promptType                     |TEXT                                                     |
     |#timeout                        |120                                                      |
     |#rationale                      |rationale                                                |
     |#boxId                          |1                                                        |
     |#correctAttempts                |1                                                        |
     |#inCorrectAttempts              |@#$                                                      |
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
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.description                             |null                                                     |
     |$.fieldErrors                             |null                                                     |



Edit a question using a string value as the inCorrectAttempts
---------------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |5a603af62e02d86561172dac                                 |
     |#kind                           |SHORT_ANSWER                                             |
     |#learningObjectives             |objective1                                               |
     |#imageUrl                       |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |TEXT                                                     |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
     |#questionPrompt                 |Who is the owner of MaxSoft?                             |
     |#promptType                     |TEXT                                                     |
     |#timeout                        |120                                                      |
     |#rationale                      |rationale                                                |
     |#boxId                          |1                                                        |
     |#correctAttempts                |1                                                        |
     |#inCorrectAttempts              |a                                                        |
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
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.description                             |null                                                     |
     |$.fieldErrors                             |null                                                     |



Edit a question using a negative integer value as the inCorrectAttempts
-------------------------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |5a603af62e02d86561172dac                                 |
     |#kind                           |SHORT_ANSWER                                             |
     |#learningObjectives             |objective1                                               |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
     |#imageUrl                       |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |TEXT                                                     |
     |#questionPrompt                 |Who is the owner of MaxSoft?                             |
     |#promptType                     |TEXT                                                     |
     |#timeout                        |120                                                      |
     |#rationale                      |rationale                                                |
     |#boxId                          |1                                                        |
     |#correctAttempts                |1                                                        |
     |#inCorrectAttempts              |a                                                        |
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
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.description                             |null                                                     |
     |$.fieldErrors                             |null                                                     |



Edit a question using an empty value as the inCorrectAttempts
---------------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |5a603af62e02d86561172dac                                 |
     |#kind                           |SHORT_ANSWER                                             |
     |#learningObjectives             |objective1                                               |
     |#imageUrl                       |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |TEXT                                                     |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
     |#questionPrompt                 |Who is the owner of MaxSoft?                             |
     |#promptType                     |TEXT                                                     |
     |#timeout                        |120                                                      |
     |#rationale                      |rationale                                                |
     |#boxId                          |1                                                        |
     |#correctAttempts                |1                                                        |
     |#inCorrectAttempts              |                                                         |
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
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.description                             |null                                                     |
     |$.fieldErrors                             |null                                                     |



Edit a question using a integer value as the lastAswered
----------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |5a603af62e02d86561172dac                                 |
     |#kind                           |SHORT_ANSWER                                             |
     |#learningObjectives             |objective1                                               |
     |#imageUrl                       |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |TEXT                                                     |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
     |#questionPrompt                 |Who is the owner of MaxSoft?                             |
     |#promptType                     |TEXT                                                     |
     |#timeout                        |120                                                      |
     |#rationale                      |rationale                                                |
     |#boxId                          |1                                                        |
     |#correctAttempts                |1                                                        |
     |#inCorrectAttempts              |0                                                        |
     |#lastAswered                    |123                                                      |
     |#questionId                     |0                                                        |
     |#skips                          |0                                                        |
     |#userId                         |0                                                        |
     |#correctAnswerId                |1                                                        |
     |#correctAnswerValue             |Osanda Deshan                                            |
     |#iscorrectAnswerCaseSensitive   |false                                                    |
     |#correctAnswerType              |TEXT                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.stats.lastAswered                       |123                                                      |



Edit a question using a decimal value as the lastAswered
----------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |5a603af62e02d86561172dac                                 |
     |#kind                           |SHORT_ANSWER                                             |
     |#learningObjectives             |objective1                                               |
     |#imageUrl                       |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |TEXT                                                     |
     |#questionPrompt                 |Who is the owner of MaxSoft?                             |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
     |#promptType                     |TEXT                                                     |
     |#timeout                        |120                                                      |
     |#rationale                      |rationale                                                |
     |#boxId                          |1                                                        |
     |#correctAttempts                |1                                                        |
     |#inCorrectAttempts              |0                                                        |
     |#lastAswered                    |1.2                                                      |
     |#questionId                     |0                                                        |
     |#skips                          |0                                                        |
     |#userId                         |0                                                        |
     |#correctAnswerId                |1                                                        |
     |#correctAnswerValue             |Osanda Deshan                                            |
     |#iscorrectAnswerCaseSensitive   |false                                                    |
     |#correctAnswerType              |TEXT                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |stats: Invalid value '1.2'                               |
     |$.description                             |null                                                     |
     |$.fieldErrors                             |null                                                     |



Edit a question using a string value as the lastAnswered
----------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |5a603af62e02d86561172dac                                 |
     |#kind                           |SHORT_ANSWER                                             |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
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
     |#lastAswered                    |abc                                                      |
     |#questionId                     |0                                                        |
     |#skips                          |0                                                        |
     |#userId                         |0                                                        |
     |#correctAnswerId                |1                                                        |
     |#correctAnswerValue             |Osanda Deshan                                            |
     |#iscorrectAnswerCaseSensitive   |false                                                    |
     |#correctAnswerType              |TEXT                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |stats: Invalid value 'abc'                               |
     |$.description                             |null                                                     |
     |$.fieldErrors                             |null                                                     |



Edit a question using a negative integer value as the lastAswered
-------------------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |5a603af62e02d86561172dac                                 |
     |#kind                           |SHORT_ANSWER                                             |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
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
     |#lastAswered                    |-1                                                       |
     |#questionId                     |0                                                        |
     |#skips                          |0                                                        |
     |#userId                         |0                                                        |
     |#correctAnswerId                |1                                                        |
     |#correctAnswerValue             |Osanda Deshan                                            |
     |#iscorrectAnswerCaseSensitive   |false                                                    |
     |#correctAnswerType              |TEXT                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.stats.lastAswered                       |-1                                                       |



Edit a question using a special character value as the lastAswered
--------------------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |5a603af62e02d86561172dac                                 |
     |#kind                           |SHORT_ANSWER                                             |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
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
     |#lastAswered                    |@#                                                       |
     |#questionId                     |0                                                        |
     |#skips                          |0                                                        |
     |#userId                         |0                                                        |
     |#correctAnswerId                |1                                                        |
     |#correctAnswerValue             |Osanda Deshan                                            |
     |#iscorrectAnswerCaseSensitive   |false                                                    |
     |#correctAnswerType              |TEXT                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |stats: Invalid value '@#'                                |
     |$.description                             |null                                                     |
     |$.fieldErrors                             |null                                                     |



Edit a question using a negative integer value as the questionId
------------------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |5a603af62e02d86561172dac                                 |
     |#kind                           |SHORT_ANSWER                                             |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
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
     |#questionId                     |-1                                                       |
     |#skips                          |0                                                        |
     |#userId                         |0                                                        |
     |#correctAnswerId                |1                                                        |
     |#correctAnswerValue             |Osanda Deshan                                            |
     |#iscorrectAnswerCaseSensitive   |false                                                    |
     |#correctAnswerType              |TEXT                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |error.validation                                         |
     |$.description                             |null                                                     |
     |$.fieldErrors[0].objectName               |                                                         |
     |$.fieldErrors[0].field                    |stats.questionId                                         |
     |$.fieldErrors[0].message                  |'questionId' should be zero or positive integer.         |



Edit a question using a string value as the questionId
--------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |5a603af62e02d86561172dac                                 |
     |#kind                           |SHORT_ANSWER                                             |
     |#learningObjectives             |objective1                                               |
     |#imageUrl                       |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |TEXT                                                     |
     |#questionPrompt                 |Who is the owner of MaxSoft?                             |
     |#promptType                     |TEXT                                                     |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
     |#timeout                        |120                                                      |
     |#rationale                      |rationale                                                |
     |#boxId                          |1                                                        |
     |#correctAttempts                |1                                                        |
     |#inCorrectAttempts              |0                                                        |
     |#lastAswered                    |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |a                                                        |
     |#skips                          |0                                                        |
     |#userId                         |0                                                        |
     |#correctAnswerId                |1                                                        |
     |#correctAnswerValue             |Osanda Deshan                                            |
     |#iscorrectAnswerCaseSensitive   |false                                                    |
     |#correctAnswerType              |TEXT                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.description                             |null                                                     |
     |$.fieldErrors                             |null                                                     |



Edit a question using a special characters value as the questionId
--------------------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |5a603af62e02d86561172dac                                 |
     |#kind                           |SHORT_ANSWER                                             |
     |#learningObjectives             |objective1                                               |
     |#imageUrl                       |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |TEXT                                                     |
     |#questionPrompt                 |Who is the owner of MaxSoft?                             |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
     |#promptType                     |TEXT                                                     |
     |#timeout                        |120                                                      |
     |#rationale                      |rationale                                                |
     |#boxId                          |1                                                        |
     |#correctAttempts                |1                                                        |
     |#inCorrectAttempts              |0                                                        |
     |#lastAswered                    |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |@#                                                       |
     |#skips                          |0                                                        |
     |#userId                         |0                                                        |
     |#correctAnswerId                |1                                                        |
     |#correctAnswerValue             |Osanda Deshan                                            |
     |#iscorrectAnswerCaseSensitive   |false                                                    |
     |#correctAnswerType              |TEXT                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.description                             |null                                                     |
     |$.fieldErrors                             |null                                                     |



Edit a question using an empty value as the questionId
--------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |5a603af62e02d86561172dac                                 |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
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
     |#questionId                     |                                                         |
     |#skips                          |0                                                        |
     |#userId                         |0                                                        |
     |#correctAnswerId                |1                                                        |
     |#correctAnswerValue             |Osanda Deshan                                            |
     |#iscorrectAnswerCaseSensitive   |false                                                    |
     |#correctAnswerType              |TEXT                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.description                             |null                                                     |
     |$.fieldErrors                             |null                                                     |



Edit a question using a negative integer value as the skips
-------------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |5a603af62e02d86561172dac                                 |
     |#kind                           |SHORT_ANSWER                                             |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
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
     |#skips                          |-1                                                       |
     |#userId                         |0                                                        |
     |#correctAnswerId                |1                                                        |
     |#correctAnswerValue             |Osanda Deshan                                            |
     |#iscorrectAnswerCaseSensitive   |false                                                    |
     |#correctAnswerType              |TEXT                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |error.validation                                         |
     |$.description                             |null                                                     |
     |$.fieldErrors[0].objectName               |                                                         |
     |$.fieldErrors[0].field                    |stats.skips                                              |
     |$.fieldErrors[0].message                  |'skips' should be zero or positive integer.              |



Edit a question using a special characters value as the skips
---------------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |5a603af62e02d86561172dac                                 |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
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
     |#skips                          |@#$                                                      |
     |#userId                         |0                                                        |
     |#correctAnswerId                |1                                                        |
     |#correctAnswerValue             |Osanda Deshan                                            |
     |#iscorrectAnswerCaseSensitive   |false                                                    |
     |#correctAnswerType              |TEXT                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.description                             |null                                                     |
     |$.fieldErrors                             |null                                                     |



Edit a question using a string value as the skips
---------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |5a603af62e02d86561172dac                                 |
     |#kind                           |SHORT_ANSWER                                             |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
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
     |#skips                          |ab                                                       |
     |#userId                         |0                                                        |
     |#correctAnswerId                |1                                                        |
     |#correctAnswerValue             |Osanda Deshan                                            |
     |#iscorrectAnswerCaseSensitive   |false                                                    |
     |#correctAnswerType              |TEXT                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.description                             |null                                                     |
     |$.fieldErrors                             |null                                                     |



Edit a question using an empty value as the skips
---------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |5a603af62e02d86561172dac                                 |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
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
     |#skips                          |                                                         |
     |#userId                         |0                                                        |
     |#correctAnswerId                |1                                                        |
     |#correctAnswerValue             |Osanda Deshan                                            |
     |#iscorrectAnswerCaseSensitive   |false                                                    |
     |#correctAnswerType              |TEXT                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.description                             |null                                                     |
     |$.fieldErrors                             |null                                                     |



Edit a question using a negative integer value as the userId
--------------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
     |#deckId                         |5a603af62e02d86561172dac                                 |
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
     |#userId                         |-1                                                       |
     |#correctAnswerId                |1                                                        |
     |#correctAnswerValue             |Osanda Deshan                                            |
     |#iscorrectAnswerCaseSensitive   |false                                                    |
     |#correctAnswerType              |TEXT                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |error.validation                                         |
     |$.description                             |null                                                     |
     |$.fieldErrors[0].objectName               |                                                         |
     |$.fieldErrors[0].field                    |stats.userId                                             |
     |$.fieldErrors[0].message                  |'userId' should be zero or positive integer.             |



Edit a question using a string value as the userId
----------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |5a603af62e02d86561172dac                                 |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
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
     |#userId                         |ab                                                       |
     |#correctAnswerId                |1                                                        |
     |#correctAnswerValue             |Osanda Deshan                                            |
     |#iscorrectAnswerCaseSensitive   |false                                                    |
     |#correctAnswerType              |TEXT                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.description                             |null                                                     |
     |$.fieldErrors                             |null                                                     |


Edit a question using a special character as the userId
---------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |5a603af62e02d86561172dac                                 |
     |#kind                           |SHORT_ANSWER                                             |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
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
     |#userId                         |!@#                                                      |
     |#correctAnswerId                |1                                                        |
     |#correctAnswerValue             |Osanda Deshan                                            |
     |#iscorrectAnswerCaseSensitive   |false                                                    |
     |#correctAnswerType              |TEXT                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.description                             |null                                                     |
     |$.fieldErrors                             |null                                                     |



Edit a question using an empty value as the userId
----------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |5a603af62e02d86561172dac                                 |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
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
     |#userId                         |                                                         |
     |#correctAnswerId                |1                                                        |
     |#correctAnswerValue             |Osanda Deshan                                            |
     |#iscorrectAnswerCaseSensitive   |false                                                    |
     |#correctAnswerType              |TEXT                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.description                             |null                                                     |
     |$.fieldErrors                             |null                                                     |



Edit a question using an empty value as the correctAnswer
-----------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |5a603af62e02d86561172dac                                 |
     |#kind                           |SHORT_ANSWER                                             |
     |#learningObjectives             |objective1                                               |
     |#imageUrl                       |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |TEXT                                                     |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
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
     |#correctAnswerValue             |                                                         |
     |#iscorrectAnswerCaseSensitive   |false                                                    |
     |#correctAnswerType              |TEXT                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |error.validation                                         |
     |$.description                             |null                                                     |
     |$.fieldErrors[0].objectName               |                                                         |
     |$.fieldErrors[0].field                    |answers[].value                                          |
     |$.fieldErrors[0].message                  |'value' Cannot be null or empty                          |



Edit a question using a string value as the iscorrectAnswerCaseSensitive
--------------------------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |5a603af62e02d86561172dac                                 |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
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
     |#iscorrectAnswerCaseSensitive   |abc                                                      |
     |#correctAnswerType              |TEXT                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                                                                                                        |
     |------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
     |$.message                                 |Unrecognized token 'abc': was expecting ('true', 'false' or 'null')\n at [Source: java.io.PushbackInputStream@51bf4b27; line: 31, column: 32]|
     |$.description                             |null                                                                                                                                         |
     |$.fieldErrors                             |null                                                                                                                                         |



Edit a question using special characters as the iscorrectAnswerCaseSensitive
------------------------------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |5a603af62e02d86561172dac                                 |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
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
     |#iscorrectAnswerCaseSensitive   |!                                                        |
     |#correctAnswerType              |TEXT                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                                                                                                                                                            |
     |------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
     |$.message                                 |Unexpected character ('!' (code 33)): expected a valid value (number, String, array, object, 'true', 'false' or 'null')\n at [Source: java.io.PushbackInputStream@36b6c47f; line: 31, column: 29]|
     |$.description                             |null                                                                                                                                                                                             |
     |$.fieldErrors                             |null                                                                                                                                                                                             |



Edit a question using an invalid imageUrl
-------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |5a603af62e02d86561172dac                                 |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
     |#kind                           |SHORT_ANSWER                                             |
     |#learningObjectives             |objective1                                               |
     |#imageUrl                       |www.maxsoft/image                                        |
     |#media                          |TEXT                                                     |
     |#questionPrompt                 |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |TEXT                                                     |
     |#timeout                        |60                                                       |
     |#rationale                      |rationale                                                |
     |#boxId                          |0                                                        |
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
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |error.validation                                         |
     |$.description                             |null                                                     |
     |$.fieldErrors[0].objectName               |                                                         |
     |$.fieldErrors[0].field                    |question.imageUrl                                        |
     |$.fieldErrors[0].message                  |must be a valid URL                                      |