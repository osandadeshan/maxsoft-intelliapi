Edit MCQ Type Question using Question Service - Negative Test Specification
===========================================================================
Date Editd    : 12/08/2017
Version   		: 1.0.0
Owner      		: Osanda Deshan
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.


tags: edit_question, edit_question_mcq_type, edit_question-positive_tests, negative



* Create a MCQ question
* And save the JSON Path values in the response inside the data stores
    |DataStore Type |Variable Name  |Value To Be Stored     |
    |---------------|---------------|-----------------------|
    |scenario       |questionId     |$.id                   |
* Given that a user needs to invoke "Edit MCQ Type Question using Question Service"
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
------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |                                                         |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |51                                                       |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
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
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |51                                                       |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
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
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
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
     |#deckId                         |51                                                       |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
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
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
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
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
     |#learningObjectives             |learningObjective1                                       |
     |#imageUrl                       |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |TEXT                                                     |
     |#questionPrompt                 |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
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
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
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
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
     |#learningObjectives             |learningObjective1                                       |
     |#imageUrl                       |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |TEXT                                                     |
     |#questionPrompt                 |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |TEXT                                                     |
     |#timeout                        |60                                                       |
     |#rationale                      |rationale                                                |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
     |#boxId                          |0                                                        |
     |#correctAttempts                |1                                                        |
     |#inCorrectAttempts              |0                                                        |
     |#lastAswered                    |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |0                                                        |
     |#skips                          |0                                                        |
     |#userId                         |0                                                        |
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
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



Edit a question using an invalid deckId type
----------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
     |#deckId                         |osanda                                                   |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.description                             |null                                                     |
     |$.fieldErrors                             |null                                                     |



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
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
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
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOIC                                           |
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
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
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
     |#deckId                         |51                                                       |
     |#kind                           |                                                         |
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
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
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
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
     |#learningObjectives             |objective1                                               |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
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
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
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
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
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
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
     |#learningObjectives             |objective1                                               |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
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
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
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
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
     |#learningObjectives             |objective1                                               |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
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
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
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
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
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
     |#deckId                         |51                                                       |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
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
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
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
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
     |#learningObjectives             |objective1                                               |
     |#imageUrl                       |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |TEXT                                                     |
     |#questionPrompt                 |Who is the owner of MaxSoft?                             |
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
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
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
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
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
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
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
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
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
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#correctAttempts                |correctAt1                                               |
     |#inCorrectAttempts              |0                                                        |
     |#lastAswered                    |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |0                                                        |
     |#skips                          |0                                                        |
     |#userId                         |0                                                        |
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
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
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#correctAttempts                |-1                                                       |
     |#inCorrectAttempts              |0                                                        |
     |#lastAswered                    |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |0                                                        |
     |#skips                          |0                                                        |
     |#userId                         |0                                                        |
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
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
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#correctAttempts                |@#                                                       |
     |#inCorrectAttempts              |0                                                        |
     |#lastAswered                    |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |0                                                        |
     |#skips                          |0                                                        |
     |#userId                         |0                                                        |
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
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
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#correctAttempts                |                                                         |
     |#inCorrectAttempts              |0                                                        |
     |#lastAswered                    |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |0                                                        |
     |#skips                          |0                                                        |
     |#userId                         |0                                                        |
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
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
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#inCorrectAttempts              |@#$                                                      |
     |#lastAswered                    |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |0                                                        |
     |#skips                          |0                                                        |
     |#userId                         |0                                                        |
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
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
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
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
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
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
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#inCorrectAttempts              |                                                         |
     |#lastAswered                    |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |0                                                        |
     |#skips                          |0                                                        |
     |#userId                         |0                                                        |
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.description                             |null                                                     |
     |$.fieldErrors                             |null                                                     |



Edit a question using a positive integer value as the lastAswered
-------------------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
     |#learningObjectives             |objective1                                               |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
     |#imageUrl                       |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL|
     |#media                          |TEXT                                                     |
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
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
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
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#inCorrectAttempts              |0                                                        |
     |#lastAswered                    |1.2                                                      |
     |#questionId                     |0                                                        |
     |#skips                          |0                                                        |
     |#userId                         |0                                                        |
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
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
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#inCorrectAttempts              |0                                                        |
     |#lastAswered                    |abc                                                      |
     |#questionId                     |0                                                        |
     |#skips                          |0                                                        |
     |#userId                         |0                                                        |
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
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
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
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
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
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
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
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
     |#deckId                         |51                                                       |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#questionId                     |a                                                        |
     |#skips                          |0                                                        |
     |#userId                         |0                                                        |
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
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
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#questionId                     |@#                                                       |
     |#skips                          |0                                                        |
     |#userId                         |0                                                        |
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
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
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#questionId                     |                                                         |
     |#skips                          |0                                                        |
     |#userId                         |0                                                        |
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
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
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
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
----------------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#skips                          |@#$                                                      |
     |#userId                         |0                                                        |
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
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
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#inCorrectAttempts              |0                                                        |
     |#lastAswered                    |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |0                                                        |
     |#skips                          |ab                                                       |
     |#userId                         |0                                                        |
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
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
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#skips                          |                                                         |
     |#userId                         |0                                                        |
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
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
     |#deckId                         |51                                                       |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
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
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#inCorrectAttempts              |0                                                        |
     |#lastAswered                    |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |0                                                        |
     |#skips                          |0                                                        |
     |#userId                         |ab                                                       |
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
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
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#inCorrectAttempts              |0                                                        |
     |#lastAswered                    |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |0                                                        |
     |#skips                          |0                                                        |
     |#userId                         |!@#                                                      |
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
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
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#inCorrectAttempts              |0                                                        |
     |#lastAswered                    |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |0                                                        |
     |#skips                          |0                                                        |
     |#userId                         |                                                         |
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.description                             |null                                                     |
     |$.fieldErrors                             |null                                                     |



Edit a question using a string value as the correctAnswerList
---------------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#userId                         |1                                                        |
     |#correctAnswerList              |correctAnswerList                                        |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.description                             |null                                                     |
     |$.fieldErrors                             |null                                                     |



Edit a question using a special character as the correctAnswerList
--------------------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#userId                         |1                                                        |
     |#correctAnswerList              |@                                                        |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.description                             |null                                                     |
     |$.fieldErrors                             |null                                                     |



Edit a question using an empty value as the correctAnswerList
---------------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#userId                         |1                                                        |
     |#correctAnswerList              |                                                         |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |error.validation                                         |
     |$.description                             |null                                                     |
     |$.fieldErrors[0].objectName               |                                                         |
     |$.fieldErrors[0].field                    |correctAnswers                                           |
     |$.fieldErrors[0].message                  |'correctAnswers' should be present                       |



Edit a question using an empty string as the correctAnswerList
----------------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#inCorrectAttempts              |0                                                        |
     |#lastAswered                    |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |0                                                        |
     |#skips                          |0                                                        |
     |#userId                         |1                                                        |
     |#correctAnswerList              |""                                                       |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |error.validation                                         |
     |$.description                             |null                                                     |
     |$.fieldErrors[0].objectName               |                                                         |
     |$.fieldErrors[0].field                    |correctAnswers                                           |
     |$.fieldErrors[0].message                  |correctAnswers' Cannot contain null values               |



Edit a question using null value as the correctAnswerList
-----------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#inCorrectAttempts              |0                                                        |
     |#lastAswered                    |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |0                                                        |
     |#skips                          |0                                                        |
     |#userId                         |1                                                        |
     |#correctAnswerList              |null                                                     |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |error.validation                                         |
     |$.description                             |null                                                     |
     |$.fieldErrors[0].objectName               |                                                         |
     |$.fieldErrors[0].field                    |correctAnswers                                           |
     |$.fieldErrors[0].message                  |correctAnswers' Cannot contain null values               |



Edit a question using a string value as the answer1Id
-------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#inCorrectAttempts              |0                                                        |
     |#lastAswered                    |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |0                                                        |
     |#skips                          |0                                                        |
     |#userId                         |0                                                        |
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |"id"                                                     |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |answers: Invalid value 'id'                              |
     |$.description                             |null                                                     |
     |$.fieldErrors                             |null                                                     |



Edit a question using a special character as the answer1Id
------------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#inCorrectAttempts              |0                                                        |
     |#lastAswered                    |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |0                                                        |
     |#skips                          |0                                                        |
     |#userId                         |0                                                        |
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |"@"                                                      |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |answers: Invalid value '@'                               |
     |$.description                             |null                                                     |
     |$.fieldErrors                             |null                                                     |



Edit a question using a negative integer value as the answer1Id
-----------------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#inCorrectAttempts              |0                                                        |
     |#lastAswered                    |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |0                                                        |
     |#skips                          |0                                                        |
     |#userId                         |0                                                        |
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |-1                                                       |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |error.validation                                         |
     |$.description                             |null                                                     |
     |$.fieldErrors[0].objectName               |                                                         |
     |$.fieldErrors[0].field                    |answers[0].id                                            |
     |$.fieldErrors[0].message                  |Answers id should be a positive integer.                 |



Edit a question using an empty value as the answer1Id
-------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#inCorrectAttempts              |0                                                        |
     |#lastAswered                    |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |0                                                        |
     |#skips                          |0                                                        |
     |#userId                         |0                                                        |
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |""                                                       |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |error.validation                                         |
     |$.description                             |null                                                     |
     |$.fieldErrors[0].objectName               |                                                         |
     |$.fieldErrors[0].field                    |answers[0].id                                            |
     |$.fieldErrors[0].message                  |Answers id should be a positive integer.                 |



Edit a question using null value as the answer1Id
---------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#userId                         |0                                                        |
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |null                                                     |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |error.validation                                         |
     |$.description                             |null                                                     |
     |$.fieldErrors[0].objectName               |                                                         |
     |$.fieldErrors[0].field                    |answers[0].id                                            |
     |$.fieldErrors[0].message                  |Answers id should be a positive integer.                 |



Edit a question using empty value as the answer1Value
-------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#userId                         |0                                                        |
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |                                                         |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |error.validation                                         |
     |$.description                             |null                                                     |
     |$.fieldErrors[0].objectName               |                                                         |
     |$.fieldErrors[0].field                    |answers[0].value                                         |
     |$.fieldErrors[0].message                  |'value' Cannot be null or empty                          |



Edit a question using null value as the answer1Value
------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#inCorrectAttempts              |0                                                        |
     |#lastAswered                    |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |0                                                        |
     |#skips                          |0                                                        |
     |#userId                         |0                                                        |
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |"null"                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |error.validation                                         |
     |$.description                             |null                                                     |
     |$.fieldErrors[0].objectName               |                                                         |
     |$.fieldErrors[0].field                    |answers[0].value                                         |
     |$.fieldErrors[0].message                  |'value' Cannot be null or empty                          |


Edit a question using empty value as the answer1Type
------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#userId                         |0                                                        |
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |                                                         |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |error.validation                                         |
     |$.description                             |null                                                     |
     |$.fieldErrors[0].objectName               |                                                         |
     |$.fieldErrors[0].field                    |answers[0].type                                          |
     |$.fieldErrors[0].message                  |must match \"TEXT\|HTML\|IMAGE\|VIDEO\|AUDIO\            |


Edit a question using null as the answer1Type
-----------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |51                                                       |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1	                                                    |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |"null"                                                   |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |error.validation                                         |
     |$.description                             |null                                                     |
     |$.fieldErrors[0].objectName               |                                                         |
     |$.fieldErrors[0].field                    |answers[0].type                                          |
     |$.fieldErrors[0].message                  |must match \"TEXT\|HTML\|IMAGE\|VIDEO\|AUDIO\            |


Edit a question using String as the answer1Type
-------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#userId                         |0                                                        |
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1	                                                    |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEX                                                      |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |error.validation                                         |
     |$.description                             |null                                                     |
     |$.fieldErrors[0].objectName               |                                                         |
     |$.fieldErrors[0].field                    |answers[0].type                                          |
     |$.fieldErrors[0].message                  |must match \"TEXT\|HTML\|IMAGE\|VIDEO\|AUDIO\            |


Edit a question using numbers as the answer1Type
--------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |51                                                       |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1	                                                    |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |1                                                        |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |error.validation                                         |
     |$.description                             |null                                                     |
     |$.fieldErrors[0].objectName               |                                                         |
     |$.fieldErrors[0].field                    |answers[0].type                                          |
     |$.fieldErrors[0].message                  |must match \"TEXT\|HTML\|IMAGE\|VIDEO\|AUDIO\            |



Edit a question using a string value as the answer2Id
-------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#userId                         |0                                                        |
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |"id"                                                     |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |answers: Invalid value 'id'                              |
     |$.description                             |null                                                     |
     |$.fieldErrors                             |null                                                     |



Edit a question using a special character as the answer2Id
------------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#inCorrectAttempts              |0                                                        |
     |#lastAswered                    |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |0                                                        |
     |#skips                          |0                                                        |
     |#userId                         |0                                                        |
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |"@"                                                      |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |answers: Invalid value '@'                               |
     |$.description                             |null                                                     |
     |$.fieldErrors                             |null                                                     |



Edit a question using a negative integer value as the answer2Id
-----------------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#inCorrectAttempts              |0                                                        |
     |#lastAswered                    |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |0                                                        |
     |#skips                          |0                                                        |
     |#userId                         |0                                                        |
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |-2                                                       |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |error.validation                                         |
     |$.description                             |null                                                     |
     |$.fieldErrors[0].objectName               |                                                         |
     |$.fieldErrors[0].field                    |answers[1].id                                            |
     |$.fieldErrors[0].message                  |Answers id should be a positive integer.                 |



Edit a question using an empty value as the answer2Id
-------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#inCorrectAttempts              |0                                                        |
     |#lastAswered                    |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |0                                                        |
     |#skips                          |0                                                        |
     |#userId                         |0                                                        |
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |""                                                       |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |error.validation                                         |
     |$.description                             |null                                                     |
     |$.fieldErrors[0].objectName               |                                                         |
     |$.fieldErrors[0].field                    |answers[1].id                                            |
     |$.fieldErrors[0].message                  |Answers id should be a positive integer.                 |



Edit a question using null value as the answer2Id
---------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#inCorrectAttempts              |0                                                        |
     |#lastAswered                    |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |0                                                        |
     |#skips                          |0                                                        |
     |#userId                         |0                                                        |
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |null                                                     |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |error.validation                                         |
     |$.description                             |null                                                     |
     |$.fieldErrors[0].objectName               |                                                         |
     |$.fieldErrors[0].field                    |answers[1].id                                            |
     |$.fieldErrors[0].message                  |Answers id should be a positive integer.                 |



Edit a question using empty value as the answer2Value
-------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#inCorrectAttempts              |0                                                        |
     |#lastAswered                    |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |0                                                        |
     |#skips                          |0                                                        |
     |#userId                         |0                                                        |
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |answer1                                                  |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |                                                         |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |error.validation                                         |
     |$.description                             |null                                                     |
     |$.fieldErrors[0].objectName               |                                                         |
     |$.fieldErrors[0].field                    |answers[1].value                                         |
     |$.fieldErrors[0].message                  |'value' Cannot be null or empty                          |



Edit a question using null value as the answer2Value
------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#inCorrectAttempts              |0                                                        |
     |#lastAswered                    |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |0                                                        |
     |#skips                          |0                                                        |
     |#userId                         |0                                                        |
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |answer1                                                  |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |"null"                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |error.validation                                         |
     |$.description                             |null                                                     |
     |$.fieldErrors[0].objectName               |                                                         |
     |$.fieldErrors[0].field                    |answers[1].value                                         |
     |$.fieldErrors[0].message                  |'value' Cannot be null or empty                          |


Edit a question using empty value as the answer2Type
------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |51                                                       |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |                                                         |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |error.validation                                         |
     |$.description                             |null                                                     |
     |$.fieldErrors[0].objectName               |                                                         |
     |$.fieldErrors[0].field                    |answers[1].type                                          |
     |$.fieldErrors[0].message                  |must match \"TEXT\|HTML\|IMAGE\|VIDEO\|AUDIO\            |


Edit a question using null as the answer2Type
-----------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#userId                         |0                                                        |
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1	                                                    |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |"null"                                                   |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |error.validation                                         |
     |$.description                             |null                                                     |
     |$.fieldErrors[0].objectName               |                                                         |
     |$.fieldErrors[0].field                    |answers[1].type                                          |
     |$.fieldErrors[0].message                  |must match \"TEXT\|HTML\|IMAGE\|VIDEO\|AUDIO\            |


Edit a question using String as the answer2Type
-------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#inCorrectAttempts              |0                                                        |
     |#lastAswered                    |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |0                                                        |
     |#skips                          |0                                                        |
     |#userId                         |0                                                        |
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1	                                                    |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEX                                                      |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |error.validation                                         |
     |$.description                             |null                                                     |
     |$.fieldErrors[0].objectName               |                                                         |
     |$.fieldErrors[0].field                    |answers[1].type                                          |
     |$.fieldErrors[0].message                  |must match \"TEXT\|HTML\|IMAGE\|VIDEO\|AUDIO\            |


Edit a question using numbers as the answer2Type
--------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#userId                         |0                                                        |
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1	                                                    |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |1                                                        |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |error.validation                                         |
     |$.description                             |null                                                     |
     |$.fieldErrors[0].objectName               |                                                         |
     |$.fieldErrors[0].field                    |answers[1].type                                          |
     |$.fieldErrors[0].message                  |must match \"TEXT\|HTML\|IMAGE\|VIDEO\|AUDIO\            |



Edit a question using a string value as the answer3Id
-------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#inCorrectAttempts              |0                                                        |
     |#lastAswered                    |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |0                                                        |
     |#skips                          |0                                                        |
     |#userId                         |0                                                        |
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |"id"                                                     |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |answers: Invalid value 'id'                              |
     |$.description                             |null                                                     |
     |$.fieldErrors                             |null                                                     |



Edit a question using a special character as the answer3Id
------------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#inCorrectAttempts              |0                                                        |
     |#lastAswered                    |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |0                                                        |
     |#skips                          |0                                                        |
     |#userId                         |0                                                        |
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |"@"                                                      |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |answers: Invalid value '@'                               |
     |$.description                             |null                                                     |
     |$.fieldErrors                             |null                                                     |



Edit a question using a negative integer value as the answer3Id
-----------------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |51                                                       |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |-3                                                       |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |error.validation                                         |
     |$.description                             |null                                                     |
     |$.fieldErrors[0].objectName               |                                                         |
     |$.fieldErrors[0].field                    |answers[2].id                                            |
     |$.fieldErrors[0].message                  |Answers id should be a positive integer.                 |



Edit a question using an empty value as the answer3Id
-------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#userId                         |0                                                        |
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |""                                                       |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |error.validation                                         |
     |$.description                             |null                                                     |
     |$.fieldErrors[0].objectName               |                                                         |
     |$.fieldErrors[0].field                    |answers[2].id                                            |
     |$.fieldErrors[0].message                  |Answers id should be a positive integer.                 |



Edit a question using null value as the answer3Id
---------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#inCorrectAttempts              |0                                                        |
     |#lastAswered                    |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |0                                                        |
     |#skips                          |0                                                        |
     |#userId                         |0                                                        |
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |null                                                     |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |error.validation                                         |
     |$.description                             |null                                                     |
     |$.fieldErrors[0].objectName               |                                                         |
     |$.fieldErrors[0].field                    |answers[2].id                                            |
     |$.fieldErrors[0].message                  |Answers id should be a positive integer.                 |



Edit a question using empty value as the answer3Value
-------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#inCorrectAttempts              |0                                                        |
     |#lastAswered                    |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |0                                                        |
     |#skips                          |0                                                        |
     |#userId                         |0                                                        |
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |answer1                                                  |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |answer2                                                  |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |                                                         |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |error.validation                                         |
     |$.description                             |null                                                     |
     |$.fieldErrors[0].objectName               |                                                         |
     |$.fieldErrors[0].field                    |answers[2].value                                         |
     |$.fieldErrors[0].message                  |'value' Cannot be null or empty                          |



Edit a question using null value as the answer3Value
------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#inCorrectAttempts              |0                                                        |
     |#lastAswered                    |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |0                                                        |
     |#skips                          |0                                                        |
     |#userId                         |0                                                        |
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |answer1                                                  |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |answer2                                                  |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |"null"                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |error.validation                                         |
     |$.description                             |null                                                     |
     |$.fieldErrors[0].objectName               |                                                         |
     |$.fieldErrors[0].field                    |answers[2].value                                         |
     |$.fieldErrors[0].message                  |'value' Cannot be null or empty                          |


Edit a question using empty value as the answer3Type
------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#userId                         |0                                                        |
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |                                                         |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |error.validation                                         |
     |$.description                             |null                                                     |
     |$.fieldErrors[0].objectName               |                                                         |
     |$.fieldErrors[0].field                    |answers[2].type                                          |
     |$.fieldErrors[0].message                  |must match \"TEXT\|HTML\|IMAGE\|VIDEO\|AUDIO\            |


Edit a question using null as the answer3Type
-----------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#userId                         |0                                                        |
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1	                                                    |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |"null"                                                   |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |error.validation                                         |
     |$.description                             |null                                                     |
     |$.fieldErrors[0].objectName               |                                                         |
     |$.fieldErrors[0].field                    |answers[2].type                                          |
     |$.fieldErrors[0].message                  |must match \"TEXT\|HTML\|IMAGE\|VIDEO\|AUDIO\            |


Edit a question using String as the answer3Type
-------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#userId                         |0                                                        |
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1	                                                    |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEX                                                      |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |error.validation                                         |
     |$.description                             |null                                                     |
     |$.fieldErrors[0].objectName               |                                                         |
     |$.fieldErrors[0].field                    |answers[2].type                                          |
     |$.fieldErrors[0].message                  |must match \"TEXT\|HTML\|IMAGE\|VIDEO\|AUDIO\            |


Edit a question using numbers as the answer3Type
--------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |51                                                       |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1	                                                    |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |3                                                        |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |error.validation                                         |
     |$.description                             |null                                                     |
     |$.fieldErrors[0].objectName               |                                                         |
     |$.fieldErrors[0].field                    |answers[2].type                                          |
     |$.fieldErrors[0].message                  |must match \"TEXT\|HTML\|IMAGE\|VIDEO\|AUDIO\            |



Edit a question using a string value as the answer4Id
-------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#userId                         |0                                                        |
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |"id"                                                     |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |answers: Invalid value 'id'                              |
     |$.description                             |null                                                     |
     |$.fieldErrors                             |null                                                     |



Edit a question using a special character as the answer4Id
------------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#inCorrectAttempts              |0                                                        |
     |#lastAswered                    |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |0                                                        |
     |#skips                          |0                                                        |
     |#userId                         |0                                                        |
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |"@"                                                      |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |answers: Invalid value '@'                               |
     |$.description                             |null                                                     |
     |$.fieldErrors                             |null                                                     |



Edit a question using a negative integer value as the answer4Id
-----------------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#inCorrectAttempts              |0                                                        |
     |#lastAswered                    |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |0                                                        |
     |#skips                          |0                                                        |
     |#userId                         |0                                                        |
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |-4                                                       |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |error.validation                                         |
     |$.description                             |null                                                     |
     |$.fieldErrors[0].objectName               |                                                         |
     |$.fieldErrors[0].field                    |answers[3].id                                            |
     |$.fieldErrors[0].message                  |Answers id should be a positive integer.                 |



Edit a question using an empty value as the answer4Id
-------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#inCorrectAttempts              |0                                                        |
     |#lastAswered                    |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |0                                                        |
     |#skips                          |0                                                        |
     |#userId                         |0                                                        |
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |""                                                       |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |error.validation                                         |
     |$.description                             |null                                                     |
     |$.fieldErrors[0].objectName               |                                                         |
     |$.fieldErrors[0].field                    |answers[3].id                                            |
     |$.fieldErrors[0].message                  |Answers id should be a positive integer.                 |



Edit a question using null value as the answer4Id
---------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#userId                         |0                                                        |
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |null                                                     |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |error.validation                                         |
     |$.description                             |null                                                     |
     |$.fieldErrors[0].objectName               |                                                         |
     |$.fieldErrors[0].field                    |answers[3].id                                            |
     |$.fieldErrors[0].message                  |Answers id should be a positive integer.                 |



Edit a question using empty value as the answer4Value
-------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#inCorrectAttempts              |0                                                        |
     |#lastAswered                    |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |0                                                        |
     |#skips                          |0                                                        |
     |#userId                         |0                                                        |
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |answer1                                                  |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |answer2                                                  |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |answer3                                                  |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |                                                         |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |error.validation                                         |
     |$.description                             |null                                                     |
     |$.fieldErrors[0].objectName               |                                                         |
     |$.fieldErrors[0].field                    |answers[3].value                                         |
     |$.fieldErrors[0].message                  |'value' Cannot be null or empty                          |



Edit a question using null value as the answer4Value
------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#inCorrectAttempts              |0                                                        |
     |#lastAswered                    |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |0                                                        |
     |#skips                          |0                                                        |
     |#userId                         |0                                                        |
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |answer1                                                  |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |answer2                                                  |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |answer3                                                  |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |"null"                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |error.validation                                         |
     |$.description                             |null                                                     |
     |$.fieldErrors[0].objectName               |                                                         |
     |$.fieldErrors[0].field                    |answers[3].value                                         |
     |$.fieldErrors[0].message                  |'value' Cannot be null or empty                          |


Edit a question using empty value as the answer4Type
------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#userId                         |0                                                        |
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |                                                         |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |error.validation                                         |
     |$.description                             |null                                                     |
     |$.fieldErrors[0].objectName               |                                                         |
     |$.fieldErrors[0].field                    |answers[3].type                                          |
     |$.fieldErrors[0].message                  |must match \"TEXT\|HTML\|IMAGE\|VIDEO\|AUDIO\            |


Edit a question using null as the answer4Type
-----------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#inCorrectAttempts              |0                                                        |
     |#lastAswered                    |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |0                                                        |
     |#skips                          |0                                                        |
     |#userId                         |0                                                        |
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1	                                                    |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |"null"                                                   |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |error.validation                                         |
     |$.description                             |null                                                     |
     |$.fieldErrors[0].objectName               |                                                         |
     |$.fieldErrors[0].field                    |answers[3].type                                          |
     |$.fieldErrors[0].message                  |must match \"TEXT\|HTML\|IMAGE\|VIDEO\|AUDIO\            |


Edit a question using String as the answer4Type
-------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#inCorrectAttempts              |0                                                        |
     |#lastAswered                    |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |0                                                        |
     |#skips                          |0                                                        |
     |#userId                         |0                                                        |
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1	                                                    |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEX                                                      |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |error.validation                                         |
     |$.description                             |null                                                     |
     |$.fieldErrors[0].objectName               |                                                         |
     |$.fieldErrors[0].field                    |answers[3].type                                          |
     |$.fieldErrors[0].message                  |must match \"TEXT\|HTML\|IMAGE\|VIDEO\|AUDIO\            |


Edit a question using numbers as the answer4Type
--------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#inCorrectAttempts              |0                                                        |
     |#lastAswered                    |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |0                                                        |
     |#skips                          |0                                                        |
     |#userId                         |0                                                        |
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1	                                                    |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |4                                                        |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |error.validation                                         |
     |$.description                             |null                                                     |
     |$.fieldErrors[0].objectName               |                                                         |
     |$.fieldErrors[0].field                    |answers[3].type                                          |
     |$.fieldErrors[0].message                  |must match \"TEXT\|HTML\|IMAGE\|VIDEO\|AUDIO\            |



Edit a question using a string value as the answer5Id
-------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#inCorrectAttempts              |0                                                        |
     |#lastAswered                    |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |0                                                        |
     |#skips                          |0                                                        |
     |#userId                         |0                                                        |
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |"id"                                                     |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |answers: Invalid value 'id'                              |
     |$.description                             |null                                                     |
     |$.fieldErrors                             |null                                                     |



Edit a question using a special character as the answer5Id
------------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#userId                         |0                                                        |
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |"@"                                                      |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |answers: Invalid value '@'                               |
     |$.description                             |null                                                     |
     |$.fieldErrors                             |null                                                     |



Edit a question using a negative integer value as the answer5Id
-----------------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |51                                                       |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |-5                                                       |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |error.validation                                         |
     |$.description                             |null                                                     |
     |$.fieldErrors[0].objectName               |                                                         |
     |$.fieldErrors[0].field                    |answers[4].id                                            |
     |$.fieldErrors[0].message                  |Answers id should be a positive integer.                 |



Edit a question using an empty value as the answer5Id
-------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |51                                                       |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |""                                                       |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |error.validation                                         |
     |$.description                             |null                                                     |
     |$.fieldErrors[0].objectName               |                                                         |
     |$.fieldErrors[0].field                    |answers[4].id                                            |
     |$.fieldErrors[0].message                  |Answers id should be a positive integer.                 |



Edit a question using null value as the answer5Id
---------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |51                                                       |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |null                                                     |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |error.validation                                         |
     |$.description                             |null                                                     |
     |$.fieldErrors[0].objectName               |                                                         |
     |$.fieldErrors[0].field                    |answers[4].id                                            |
     |$.fieldErrors[0].message                  |Answers id should be a positive integer.                 |



Edit a question using empty value as the answer5Value
-------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |51                                                       |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |answer1                                                  |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |answer2                                                  |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |answer3                                                  |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |answer4                                                  |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |                                                         |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |error.validation                                         |
     |$.description                             |null                                                     |
     |$.fieldErrors[0].objectName               |                                                         |
     |$.fieldErrors[0].field                    |answers[4].value                                         |
     |$.fieldErrors[0].message                  |'value' Cannot be null or empty                          |



Edit a question using null value as the answer5Value
------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |51                                                       |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |answer1                                                  |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |answer2                                                  |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |answer3                                                  |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |"null"                                                   |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |error.validation                                         |
     |$.description                             |null                                                     |
     |$.fieldErrors[0].objectName               |                                                         |
     |$.fieldErrors[0].field                    |answers[4].value                                         |
     |$.fieldErrors[0].message                  |'value' Cannot be null or empty                          |


Edit a question using empty value as the answer5Type
------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |51                                                       |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |                                                         |
     |#answer5CaseSensitive           |true                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |error.validation                                         |
     |$.description                             |null                                                     |
     |$.fieldErrors[0].objectName               |                                                         |
     |$.fieldErrors[0].field                    |answers[4].type                                          |
     |$.fieldErrors[0].message                  |must match \"TEXT\|HTML\|IMAGE\|VIDEO\|AUDIO\            |


Edit a question using null as the answer5Type
-----------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |51                                                       |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1	                                                    |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |"null"                                                   |
     |#answer5CaseSensitive           |true                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |error.validation                                         |
     |$.description                             |null                                                     |
     |$.fieldErrors[0].objectName               |                                                         |
     |$.fieldErrors[0].field                    |answers[4].type                                          |
     |$.fieldErrors[0].message                  |must match \"TEXT\|HTML\|IMAGE\|VIDEO\|AUDIO\            |


Edit a question using String as the answer5Type
-------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |51                                                       |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1	                                                    |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEX                                                      |
     |#answer5CaseSensitive           |true                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |error.validation                                         |
     |$.description                             |null                                                     |
     |$.fieldErrors[0].objectName               |                                                         |
     |$.fieldErrors[0].field                    |answers[4].type                                          |
     |$.fieldErrors[0].message                  |must match \"TEXT\|HTML\|IMAGE\|VIDEO\|AUDIO\            |


Edit a question using numbers as the answer5Type
--------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |51                                                       |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#userId                         |0                                                        |
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1	                                                    |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |5                                                        |
     |#answer5CaseSensitive           |true                                                     |
     |#tags                           |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |error.validation                                         |
     |$.description                             |null                                                     |
     |$.fieldErrors[0].objectName               |                                                         |
     |$.fieldErrors[0].field                    |answers[4].type                                          |
     |$.fieldErrors[0].message                  |must match \"TEXT\|HTML\|IMAGE\|VIDEO\|AUDIO\            |



Edit a question using an invalid imageUrl
-------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |51                                                       |
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
     |#kind                           |MULTIPLE_CHOICE                                          |
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
     |#correctAnswerList              |1,2                                                      |
     |#answer1Id                      |1                                                        |
     |#answer1Value                   |Osanda                                                   |
     |#answer1Type                    |TEXT                                                     |
     |#answer1CaseSensitive           |true                                                     |
     |#answer2Id                      |2                                                        |
     |#answer2Value                   |Gemunu                                                   |
     |#answer2Type                    |TEXT                                                     |
     |#answer2CaseSensitive           |true                                                     |
     |#answer3Id                      |3                                                        |
     |#answer3Value                   |Eranga                                                   |
     |#answer3Type                    |TEXT                                                     |
     |#answer3CaseSensitive           |false                                                    |
     |#answer4Id                      |4                                                        |
     |#answer4Value                   |Heshan                                                   |
     |#answer4Type                    |TEXT                                                     |
     |#answer4CaseSensitive           |false                                                    |
     |#answer5Id                      |5                                                        |
     |#answer5Value                   |Thilina                                                  |
     |#answer5Type                    |TEXT                                                     |
     |#answer5CaseSensitive           |true                                                     |
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












