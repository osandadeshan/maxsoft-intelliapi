Create All Type Question using Question Service - Negative Test Specification
=============================================================================
Date Created    : 12/08/2017
Version   		: 1.0.0
Owner      		: Osanda Deshan
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.


tags: create_question, create_question_all_type, create_question-negative_tests, negative



* Create a deck
* And save the JSON Path values in the response inside the data stores
    |DataStore Type |Variable Name              |Value To Be Stored     |
    |---------------|---------------------------|-----------------------|
    |scenario       |deckId                     |$.id                   |
* Given that a user needs to invoke "Create All Type Question using Question Service"
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |



Create a question using an empty value for the creatorId
--------------------------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name    |Attribute Value To Be Set                                |
     |--------------------------------|-------------------|---------------|----------------------------|---------------------------------------------------------|
     |#creatorId                      |n                  |               |                            |                                                         |
     |#creatorPlatform                |n                  |               |                            |Web                                                      |
     |#creatoredSource                |n                  |               |                            |App                                                      |
     |#creatoredType                  |n                  |               |                            |Manual                                                   |
     |#deckId                         |y                  |scenario       |deckId                      |                                                         |
     |#kind                           |n                  |               |                            |ALL                                                      |
     |#isDeleted                      |n                  |               |                            |false                                                    |
     |#tempQuestionId                 |n                  |               |                            |testId                                                   |
     |#learningObjectives             |n                  |               |                            |learningObjective1                                       |
     |#imageUrl                       |n                  |               |                            |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |n                  |               |                            |TEXT                                                     |
     |#questionPrompt                 |n                  |               |                            |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |n                  |               |                            |TEXT                                                     |
     |#timeout                        |n                  |               |                            |60                                                       |
     |#rationale                      |n                  |               |                            |rationale                                                |
     |#boxId                          |n                  |               |                            |0                                                        |
     |#correctAttempts                |n                  |               |                            |1                                                        |
     |#inCorrectAttempts              |n                  |               |                            |0                                                        |
     |#lastAswered                    |n                  |               |                            |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |n                  |               |                            |0                                                        |
     |#skips                          |n                  |               |                            |0                                                        |
     |#userId                         |n                  |               |                            |0                                                        |
     |#correctAnswerList              |n                  |               |                            |1,2                                                      |
     |#answer1Id                      |n                  |               |                            |1                                                        |
     |#answer1Value                   |n                  |               |                            |Osanda                                                   |
     |#answer1Type                    |n                  |               |                            |TEXT                                                     |
     |#answer1CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer2Id                      |n                  |               |                            |2                                                        |
     |#answer2Value                   |n                  |               |                            |Gemunu                                                   |
     |#answer2Type                    |n                  |               |                            |TEXT                                                     |
     |#answer2CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer3Id                      |n                  |               |                            |3                                                        |
     |#answer3Value                   |n                  |               |                            |Eranga                                                   |
     |#answer3Type                    |n                  |               |                            |TEXT                                                     |
     |#answer3CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer4Id                      |n                  |               |                            |4                                                        |
     |#answer4Value                   |n                  |               |                            |Heshan                                                   |
     |#answer4Type                    |n                  |               |                            |TEXT                                                     |
     |#answer4CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer5Id                      |n                  |               |                            |5                                                        |
     |#answer5Value                   |n                  |               |                            |Thilina                                                  |
     |#answer5Type                    |n                  |               |                            |TEXT                                                     |
     |#answer5CaseSensitive           |n                  |               |                            |true                                                     |
     |#tags                           |n                  |               |                            |MaxSoft                                                  |
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



Create a question using an invalid creatorPlatform
--------------------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name    |Attribute Value To Be Set                                |
     |--------------------------------|-------------------|---------------|----------------------------|---------------------------------------------------------|
     |#creatorId                      |n                  |               |                            |osanda12                                                 |
     |#creatorPlatform                |n                  |               |                            |We                                                       |
     |#creatoredSource                |n                  |               |                            |App                                                      |
     |#creatoredType                  |n                  |               |                            |Manual                                                   |
     |#deckId                         |y                  |scenario       |deckId                      |                                                         |
     |#kind                           |n                  |               |                            |ALL                                                      |
     |#isDeleted                      |n                  |               |                            |false                                                    |
     |#tempQuestionId                 |n                  |               |                            |testId                                                   |
     |#learningObjectives             |n                  |               |                            |learningObjective1                                       |
     |#imageUrl                       |n                  |               |                            |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |n                  |               |                            |TEXT                                                     |
     |#questionPrompt                 |n                  |               |                            |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |n                  |               |                            |TEXT                                                     |
     |#timeout                        |n                  |               |                            |60                                                       |
     |#rationale                      |n                  |               |                            |rationale                                                |
     |#boxId                          |n                  |               |                            |0                                                        |
     |#correctAttempts                |n                  |               |                            |1                                                        |
     |#inCorrectAttempts              |n                  |               |                            |0                                                        |
     |#lastAswered                    |n                  |               |                            |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |n                  |               |                            |0                                                        |
     |#skips                          |n                  |               |                            |0                                                        |
     |#userId                         |n                  |               |                            |0                                                        |
     |#correctAnswerList              |n                  |               |                            |1,2                                                      |
     |#answer1Id                      |n                  |               |                            |1                                                        |
     |#answer1Value                   |n                  |               |                            |Osanda                                                   |
     |#answer1Type                    |n                  |               |                            |TEXT                                                     |
     |#answer1CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer2Id                      |n                  |               |                            |2                                                        |
     |#answer2Value                   |n                  |               |                            |Gemunu                                                   |
     |#answer2Type                    |n                  |               |                            |TEXT                                                     |
     |#answer2CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer3Id                      |n                  |               |                            |3                                                        |
     |#answer3Value                   |n                  |               |                            |Eranga                                                   |
     |#answer3Type                    |n                  |               |                            |TEXT                                                     |
     |#answer3CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer4Id                      |n                  |               |                            |4                                                        |
     |#answer4Value                   |n                  |               |                            |Heshan                                                   |
     |#answer4Type                    |n                  |               |                            |TEXT                                                     |
     |#answer4CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer5Id                      |n                  |               |                            |5                                                        |
     |#answer5Value                   |n                  |               |                            |Thilina                                                  |
     |#answer5Type                    |n                  |               |                            |TEXT                                                     |
     |#answer5CaseSensitive           |n                  |               |                            |true                                                     |
     |#tags                           |n                  |               |                            |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |error.validation                                         |
     |$.description                             |null                                                     |
     |$.fieldErrors[0].objectName               |                                                         |
     |$.fieldErrors[0].field                    |creatorPlatform                                          |



Create a question using an empty creatorPlatform
------------------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name    |Attribute Value To Be Set                                |
     |--------------------------------|-------------------|---------------|----------------------------|---------------------------------------------------------|
     |#creatorId                      |n                  |               |                            |osanda12                                                 |
     |#creatorPlatform                |n                  |               |                            |                                                         |
     |#creatoredSource                |n                  |               |                            |App                                                      |
     |#creatoredType                  |n                  |               |                            |Manual                                                   |
     |#deckId                         |y                  |scenario       |deckId                      |                                                         |
     |#kind                           |n                  |               |                            |ALL                                                      |
     |#isDeleted                      |n                  |               |                            |false                                                    |
     |#tempQuestionId                 |n                  |               |                            |testId                                                   |
     |#learningObjectives             |n                  |               |                            |learningObjective1                                       |
     |#imageUrl                       |n                  |               |                            |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |n                  |               |                            |TEXT                                                     |
     |#questionPrompt                 |n                  |               |                            |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |n                  |               |                            |TEXT                                                     |
     |#timeout                        |n                  |               |                            |60                                                       |
     |#rationale                      |n                  |               |                            |rationale                                                |
     |#boxId                          |n                  |               |                            |0                                                        |
     |#correctAttempts                |n                  |               |                            |1                                                        |
     |#inCorrectAttempts              |n                  |               |                            |0                                                        |
     |#lastAswered                    |n                  |               |                            |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |n                  |               |                            |0                                                        |
     |#skips                          |n                  |               |                            |0                                                        |
     |#userId                         |n                  |               |                            |0                                                        |
     |#correctAnswerList              |n                  |               |                            |1,2                                                      |
     |#answer1Id                      |n                  |               |                            |1                                                        |
     |#answer1Value                   |n                  |               |                            |Osanda                                                   |
     |#answer1Type                    |n                  |               |                            |TEXT                                                     |
     |#answer1CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer2Id                      |n                  |               |                            |2                                                        |
     |#answer2Value                   |n                  |               |                            |Gemunu                                                   |
     |#answer2Type                    |n                  |               |                            |TEXT                                                     |
     |#answer2CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer3Id                      |n                  |               |                            |3                                                        |
     |#answer3Value                   |n                  |               |                            |Eranga                                                   |
     |#answer3Type                    |n                  |               |                            |TEXT                                                     |
     |#answer3CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer4Id                      |n                  |               |                            |4                                                        |
     |#answer4Value                   |n                  |               |                            |Heshan                                                   |
     |#answer4Type                    |n                  |               |                            |TEXT                                                     |
     |#answer4CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer5Id                      |n                  |               |                            |5                                                        |
     |#answer5Value                   |n                  |               |                            |Thilina                                                  |
     |#answer5Type                    |n                  |               |                            |TEXT                                                     |
     |#answer5CaseSensitive           |n                  |               |                            |true                                                     |
     |#tags                           |n                  |               |                            |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |error.validation                                         |
     |$.description                             |null                                                     |
     |$.fieldErrors[0].objectName               |                                                         |
     |$.fieldErrors[0].field                    |creatorPlatform                                          |



Create a question using an invalid creatoredSource
--------------------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name    |Attribute Value To Be Set                                |
     |--------------------------------|-------------------|---------------|----------------------------|---------------------------------------------------------|
     |#creatorId                      |n                  |               |                            |osanda12                                                 |
     |#creatorPlatform                |n                  |               |                            |Web                                                      |
     |#creatoredSource                |n                  |               |                            |Ap                                                       |
     |#creatoredType                  |n                  |               |                            |Manual                                                   |
     |#deckId                         |y                  |scenario       |deckId                      |                                                         |
     |#kind                           |n                  |               |                            |ALL                                                      |
     |#isDeleted                      |n                  |               |                            |false                                                    |
     |#tempQuestionId                 |n                  |               |                            |testId                                                   |
     |#learningObjectives             |n                  |               |                            |learningObjective1                                       |
     |#imageUrl                       |n                  |               |                            |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |n                  |               |                            |TEXT                                                     |
     |#questionPrompt                 |n                  |               |                            |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |n                  |               |                            |TEXT                                                     |
     |#timeout                        |n                  |               |                            |60                                                       |
     |#rationale                      |n                  |               |                            |rationale                                                |
     |#boxId                          |n                  |               |                            |0                                                        |
     |#correctAttempts                |n                  |               |                            |1                                                        |
     |#inCorrectAttempts              |n                  |               |                            |0                                                        |
     |#lastAswered                    |n                  |               |                            |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |n                  |               |                            |0                                                        |
     |#skips                          |n                  |               |                            |0                                                        |
     |#userId                         |n                  |               |                            |0                                                        |
     |#correctAnswerList              |n                  |               |                            |1,2                                                      |
     |#answer1Id                      |n                  |               |                            |1                                                        |
     |#answer1Value                   |n                  |               |                            |Osanda                                                   |
     |#answer1Type                    |n                  |               |                            |TEXT                                                     |
     |#answer1CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer2Id                      |n                  |               |                            |2                                                        |
     |#answer2Value                   |n                  |               |                            |Gemunu                                                   |
     |#answer2Type                    |n                  |               |                            |TEXT                                                     |
     |#answer2CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer3Id                      |n                  |               |                            |3                                                        |
     |#answer3Value                   |n                  |               |                            |Eranga                                                   |
     |#answer3Type                    |n                  |               |                            |TEXT                                                     |
     |#answer3CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer4Id                      |n                  |               |                            |4                                                        |
     |#answer4Value                   |n                  |               |                            |Heshan                                                   |
     |#answer4Type                    |n                  |               |                            |TEXT                                                     |
     |#answer4CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer5Id                      |n                  |               |                            |5                                                        |
     |#answer5Value                   |n                  |               |                            |Thilina                                                  |
     |#answer5Type                    |n                  |               |                            |TEXT                                                     |
     |#answer5CaseSensitive           |n                  |               |                            |true                                                     |
     |#tags                           |n                  |               |                            |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |error.validation                                         |
     |$.description                             |null                                                     |
     |$.fieldErrors[0].objectName               |                                                         |
     |$.fieldErrors[0].field                    |creatoredSource                                          |



Create a question using an empty creatoredSource
------------------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name    |Attribute Value To Be Set                                |
     |--------------------------------|-------------------|---------------|----------------------------|---------------------------------------------------------|
     |#creatorId                      |n                  |               |                            |osanda12                                                 |
     |#creatorPlatform                |n                  |               |                            |Web                                                      |
     |#creatoredSource                |n                  |               |                            |                                                         |
     |#creatoredType                  |n                  |               |                            |Manual                                                   |
     |#deckId                         |y                  |scenario       |deckId                      |                                                         |
     |#kind                           |n                  |               |                            |ALL                                                      |
     |#isDeleted                      |n                  |               |                            |false                                                    |
     |#tempQuestionId                 |n                  |               |                            |testId                                                   |
     |#learningObjectives             |n                  |               |                            |learningObjective1                                       |
     |#imageUrl                       |n                  |               |                            |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |n                  |               |                            |TEXT                                                     |
     |#questionPrompt                 |n                  |               |                            |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |n                  |               |                            |TEXT                                                     |
     |#timeout                        |n                  |               |                            |60                                                       |
     |#rationale                      |n                  |               |                            |rationale                                                |
     |#boxId                          |n                  |               |                            |0                                                        |
     |#correctAttempts                |n                  |               |                            |1                                                        |
     |#inCorrectAttempts              |n                  |               |                            |0                                                        |
     |#lastAswered                    |n                  |               |                            |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |n                  |               |                            |0                                                        |
     |#skips                          |n                  |               |                            |0                                                        |
     |#userId                         |n                  |               |                            |0                                                        |
     |#correctAnswerList              |n                  |               |                            |1,2                                                      |
     |#answer1Id                      |n                  |               |                            |1                                                        |
     |#answer1Value                   |n                  |               |                            |Osanda                                                   |
     |#answer1Type                    |n                  |               |                            |TEXT                                                     |
     |#answer1CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer2Id                      |n                  |               |                            |2                                                        |
     |#answer2Value                   |n                  |               |                            |Gemunu                                                   |
     |#answer2Type                    |n                  |               |                            |TEXT                                                     |
     |#answer2CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer3Id                      |n                  |               |                            |3                                                        |
     |#answer3Value                   |n                  |               |                            |Eranga                                                   |
     |#answer3Type                    |n                  |               |                            |TEXT                                                     |
     |#answer3CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer4Id                      |n                  |               |                            |4                                                        |
     |#answer4Value                   |n                  |               |                            |Heshan                                                   |
     |#answer4Type                    |n                  |               |                            |TEXT                                                     |
     |#answer4CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer5Id                      |n                  |               |                            |5                                                        |
     |#answer5Value                   |n                  |               |                            |Thilina                                                  |
     |#answer5Type                    |n                  |               |                            |TEXT                                                     |
     |#answer5CaseSensitive           |n                  |               |                            |true                                                     |
     |#tags                           |n                  |               |                            |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |error.validation                                         |
     |$.description                             |null                                                     |
     |$.fieldErrors[0].objectName               |                                                         |
     |$.fieldErrors[0].field                    |creatoredSource                                          |



Create a question using an invalid creatoredType
------------------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name    |Attribute Value To Be Set                                |
     |--------------------------------|-------------------|---------------|----------------------------|---------------------------------------------------------|
     |#creatorId                      |n                  |               |                            |osanda12                                                 |
     |#creatorPlatform                |n                  |               |                            |Web                                                      |
     |#creatoredSource                |n                  |               |                            |App                                                      |
     |#creatoredType                  |n                  |               |                            |Manua                                                    |
     |#deckId                         |y                  |scenario       |deckId                      |                                                         |
     |#kind                           |n                  |               |                            |ALL                                                      |
     |#isDeleted                      |n                  |               |                            |false                                                    |
     |#tempQuestionId                 |n                  |               |                            |testId                                                   |
     |#learningObjectives             |n                  |               |                            |learningObjective1                                       |
     |#imageUrl                       |n                  |               |                            |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |n                  |               |                            |TEXT                                                     |
     |#questionPrompt                 |n                  |               |                            |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |n                  |               |                            |TEXT                                                     |
     |#timeout                        |n                  |               |                            |60                                                       |
     |#rationale                      |n                  |               |                            |rationale                                                |
     |#boxId                          |n                  |               |                            |0                                                        |
     |#correctAttempts                |n                  |               |                            |1                                                        |
     |#inCorrectAttempts              |n                  |               |                            |0                                                        |
     |#lastAswered                    |n                  |               |                            |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |n                  |               |                            |0                                                        |
     |#skips                          |n                  |               |                            |0                                                        |
     |#userId                         |n                  |               |                            |0                                                        |
     |#correctAnswerList              |n                  |               |                            |1,2                                                      |
     |#answer1Id                      |n                  |               |                            |1                                                        |
     |#answer1Value                   |n                  |               |                            |Osanda                                                   |
     |#answer1Type                    |n                  |               |                            |TEXT                                                     |
     |#answer1CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer2Id                      |n                  |               |                            |2                                                        |
     |#answer2Value                   |n                  |               |                            |Gemunu                                                   |
     |#answer2Type                    |n                  |               |                            |TEXT                                                     |
     |#answer2CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer3Id                      |n                  |               |                            |3                                                        |
     |#answer3Value                   |n                  |               |                            |Eranga                                                   |
     |#answer3Type                    |n                  |               |                            |TEXT                                                     |
     |#answer3CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer4Id                      |n                  |               |                            |4                                                        |
     |#answer4Value                   |n                  |               |                            |Heshan                                                   |
     |#answer4Type                    |n                  |               |                            |TEXT                                                     |
     |#answer4CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer5Id                      |n                  |               |                            |5                                                        |
     |#answer5Value                   |n                  |               |                            |Thilina                                                  |
     |#answer5Type                    |n                  |               |                            |TEXT                                                     |
     |#answer5CaseSensitive           |n                  |               |                            |true                                                     |
     |#tags                           |n                  |               |                            |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |error.validation                                         |
     |$.description                             |null                                                     |
     |$.fieldErrors[0].objectName               |                                                         |
     |$.fieldErrors[0].field                    |creatoredType                                            |



Create a question using an empty creatoredType
----------------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name    |Attribute Value To Be Set                                |
     |--------------------------------|-------------------|---------------|----------------------------|---------------------------------------------------------|
     |#creatorId                      |n                  |               |                            |osanda12                                                 |
     |#creatorPlatform                |n                  |               |                            |Web                                                      |
     |#creatoredSource                |n                  |               |                            |App                                                      |
     |#creatoredType                  |n                  |               |                            |                                                         |
     |#deckId                         |y                  |scenario       |deckId                      |                                                         |
     |#kind                           |n                  |               |                            |ALL                                                      |
     |#isDeleted                      |n                  |               |                            |false                                                    |
     |#tempQuestionId                 |n                  |               |                            |testId                                                   |
     |#learningObjectives             |n                  |               |                            |learningObjective1                                       |
     |#imageUrl                       |n                  |               |                            |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |n                  |               |                            |TEXT                                                     |
     |#questionPrompt                 |n                  |               |                            |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |n                  |               |                            |TEXT                                                     |
     |#timeout                        |n                  |               |                            |60                                                       |
     |#rationale                      |n                  |               |                            |rationale                                                |
     |#boxId                          |n                  |               |                            |0                                                        |
     |#correctAttempts                |n                  |               |                            |1                                                        |
     |#inCorrectAttempts              |n                  |               |                            |0                                                        |
     |#lastAswered                    |n                  |               |                            |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |n                  |               |                            |0                                                        |
     |#skips                          |n                  |               |                            |0                                                        |
     |#userId                         |n                  |               |                            |0                                                        |
     |#correctAnswerList              |n                  |               |                            |1,2                                                      |
     |#answer1Id                      |n                  |               |                            |1                                                        |
     |#answer1Value                   |n                  |               |                            |Osanda                                                   |
     |#answer1Type                    |n                  |               |                            |TEXT                                                     |
     |#answer1CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer2Id                      |n                  |               |                            |2                                                        |
     |#answer2Value                   |n                  |               |                            |Gemunu                                                   |
     |#answer2Type                    |n                  |               |                            |TEXT                                                     |
     |#answer2CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer3Id                      |n                  |               |                            |3                                                        |
     |#answer3Value                   |n                  |               |                            |Eranga                                                   |
     |#answer3Type                    |n                  |               |                            |TEXT                                                     |
     |#answer3CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer4Id                      |n                  |               |                            |4                                                        |
     |#answer4Value                   |n                  |               |                            |Heshan                                                   |
     |#answer4Type                    |n                  |               |                            |TEXT                                                     |
     |#answer4CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer5Id                      |n                  |               |                            |5                                                        |
     |#answer5Value                   |n                  |               |                            |Thilina                                                  |
     |#answer5Type                    |n                  |               |                            |TEXT                                                     |
     |#answer5CaseSensitive           |n                  |               |                            |true                                                     |
     |#tags                           |n                  |               |                            |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |error.validation                                         |
     |$.description                             |null                                                     |
     |$.fieldErrors[0].objectName               |                                                         |
     |$.fieldErrors[0].field                    |creatoredType                                            |



Create a question using an invalid deckId type
----------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |osanda                                                   |
     |#kind                           |ALL                                                      |
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
     |#isDeleted                      |false                                                    |
     |#tempQuestionId                 |testId                                                   |
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



Create a question using an empty deckId
---------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set                                |
     |--------------------------------|---------------------------------------------------------|
     |#creatorId                      |osanda12                                                 |
     |#creatorPlatform                |Web                                                      |
     |#creatoredSource                |App                                                      |
     |#creatoredType                  |Manual                                                   |
     |#deckId                         |                                                         |
     |#kind                           |ALL                                                      |
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



Create a question using an invalid kind
---------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name    |Attribute Value To Be Set                                |
     |--------------------------------|-------------------|---------------|----------------------------|---------------------------------------------------------|
     |#creatorId                      |n                  |               |                            |osanda12                                                 |
     |#creatorPlatform                |n                  |               |                            |Web                                                      |
     |#creatoredSource                |n                  |               |                            |App                                                      |
     |#creatoredType                  |n                  |               |                            |Manual                                                   |
     |#deckId                         |y                  |scenario       |deckId                      |                                                         |
     |#kind                           |n                  |               |                            |AL                                                       |
     |#isDeleted                      |n                  |               |                            |false                                                    |
     |#tempQuestionId                 |n                  |               |                            |testId                                                   |
     |#learningObjectives             |n                  |               |                            |learningObjective1                                       |
     |#imageUrl                       |n                  |               |                            |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |n                  |               |                            |TEXT                                                     |
     |#questionPrompt                 |n                  |               |                            |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |n                  |               |                            |TEXT                                                     |
     |#timeout                        |n                  |               |                            |60                                                       |
     |#rationale                      |n                  |               |                            |rationale                                                |
     |#boxId                          |n                  |               |                            |0                                                        |
     |#correctAttempts                |n                  |               |                            |1                                                        |
     |#inCorrectAttempts              |n                  |               |                            |0                                                        |
     |#lastAswered                    |n                  |               |                            |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |n                  |               |                            |0                                                        |
     |#skips                          |n                  |               |                            |0                                                        |
     |#userId                         |n                  |               |                            |0                                                        |
     |#correctAnswerList              |n                  |               |                            |1,2                                                      |
     |#answer1Id                      |n                  |               |                            |1                                                        |
     |#answer1Value                   |n                  |               |                            |Osanda                                                   |
     |#answer1Type                    |n                  |               |                            |TEXT                                                     |
     |#answer1CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer2Id                      |n                  |               |                            |2                                                        |
     |#answer2Value                   |n                  |               |                            |Gemunu                                                   |
     |#answer2Type                    |n                  |               |                            |TEXT                                                     |
     |#answer2CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer3Id                      |n                  |               |                            |3                                                        |
     |#answer3Value                   |n                  |               |                            |Eranga                                                   |
     |#answer3Type                    |n                  |               |                            |TEXT                                                     |
     |#answer3CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer4Id                      |n                  |               |                            |4                                                        |
     |#answer4Value                   |n                  |               |                            |Heshan                                                   |
     |#answer4Type                    |n                  |               |                            |TEXT                                                     |
     |#answer4CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer5Id                      |n                  |               |                            |5                                                        |
     |#answer5Value                   |n                  |               |                            |Thilina                                                  |
     |#answer5Type                    |n                  |               |                            |TEXT                                                     |
     |#answer5CaseSensitive           |n                  |               |                            |true                                                     |
     |#tags                           |n                  |               |                            |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.description                             |null                                                     |
     |$.fieldErrors                             |null                                                     |



Create a question using an empty kind
-------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name    |Attribute Value To Be Set                                |
     |--------------------------------|-------------------|---------------|----------------------------|---------------------------------------------------------|
     |#creatorId                      |n                  |               |                            |osanda12                                                 |
     |#creatorPlatform                |n                  |               |                            |Web                                                      |
     |#creatoredSource                |n                  |               |                            |App                                                      |
     |#creatoredType                  |n                  |               |                            |Manual                                                   |
     |#deckId                         |y                  |scenario       |deckId                      |                                                         |
     |#kind                           |n                  |               |                            |                                                         |
     |#isDeleted                      |n                  |               |                            |false                                                    |
     |#tempQuestionId                 |n                  |               |                            |testId                                                   |
     |#learningObjectives             |n                  |               |                            |learningObjective1                                       |
     |#imageUrl                       |n                  |               |                            |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |n                  |               |                            |TEXT                                                     |
     |#questionPrompt                 |n                  |               |                            |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |n                  |               |                            |TEXT                                                     |
     |#timeout                        |n                  |               |                            |60                                                       |
     |#rationale                      |n                  |               |                            |rationale                                                |
     |#boxId                          |n                  |               |                            |0                                                        |
     |#correctAttempts                |n                  |               |                            |1                                                        |
     |#inCorrectAttempts              |n                  |               |                            |0                                                        |
     |#lastAswered                    |n                  |               |                            |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |n                  |               |                            |0                                                        |
     |#skips                          |n                  |               |                            |0                                                        |
     |#userId                         |n                  |               |                            |0                                                        |
     |#correctAnswerList              |n                  |               |                            |1,2                                                      |
     |#answer1Id                      |n                  |               |                            |1                                                        |
     |#answer1Value                   |n                  |               |                            |Osanda                                                   |
     |#answer1Type                    |n                  |               |                            |TEXT                                                     |
     |#answer1CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer2Id                      |n                  |               |                            |2                                                        |
     |#answer2Value                   |n                  |               |                            |Gemunu                                                   |
     |#answer2Type                    |n                  |               |                            |TEXT                                                     |
     |#answer2CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer3Id                      |n                  |               |                            |3                                                        |
     |#answer3Value                   |n                  |               |                            |Eranga                                                   |
     |#answer3Type                    |n                  |               |                            |TEXT                                                     |
     |#answer3CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer4Id                      |n                  |               |                            |4                                                        |
     |#answer4Value                   |n                  |               |                            |Heshan                                                   |
     |#answer4Type                    |n                  |               |                            |TEXT                                                     |
     |#answer4CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer5Id                      |n                  |               |                            |5                                                        |
     |#answer5Value                   |n                  |               |                            |Thilina                                                  |
     |#answer5Type                    |n                  |               |                            |TEXT                                                     |
     |#answer5CaseSensitive           |n                  |               |                            |true                                                     |
     |#tags                           |n                  |               |                            |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.description                             |null                                                     |
     |$.fieldErrors                             |null                                                     |



Create a question using an invalid media
----------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name    |Attribute Value To Be Set                                |
     |--------------------------------|-------------------|---------------|----------------------------|---------------------------------------------------------|
     |#creatorId                      |n                  |               |                            |osanda12                                                 |
     |#creatorPlatform                |n                  |               |                            |Web                                                      |
     |#creatoredSource                |n                  |               |                            |App                                                      |
     |#creatoredType                  |n                  |               |                            |Manual                                                   |
     |#deckId                         |y                  |scenario       |deckId                      |                                                         |
     |#kind                           |n                  |               |                            |ALL                                                      |
     |#isDeleted                      |n                  |               |                            |false                                                    |
     |#tempQuestionId                 |n                  |               |                            |testId                                                   |
     |#learningObjectives             |n                  |               |                            |learningObjective1                                       |
     |#imageUrl                       |n                  |               |                            |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |n                  |               |                            |TEX                                                      |
     |#questionPrompt                 |n                  |               |                            |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |n                  |               |                            |TEXT                                                     |
     |#timeout                        |n                  |               |                            |60                                                       |
     |#rationale                      |n                  |               |                            |rationale                                                |
     |#boxId                          |n                  |               |                            |0                                                        |
     |#correctAttempts                |n                  |               |                            |1                                                        |
     |#inCorrectAttempts              |n                  |               |                            |0                                                        |
     |#lastAswered                    |n                  |               |                            |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |n                  |               |                            |0                                                        |
     |#skips                          |n                  |               |                            |0                                                        |
     |#userId                         |n                  |               |                            |0                                                        |
     |#correctAnswerList              |n                  |               |                            |1,2                                                      |
     |#answer1Id                      |n                  |               |                            |1                                                        |
     |#answer1Value                   |n                  |               |                            |Osanda                                                   |
     |#answer1Type                    |n                  |               |                            |TEXT                                                     |
     |#answer1CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer2Id                      |n                  |               |                            |2                                                        |
     |#answer2Value                   |n                  |               |                            |Gemunu                                                   |
     |#answer2Type                    |n                  |               |                            |TEXT                                                     |
     |#answer2CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer3Id                      |n                  |               |                            |3                                                        |
     |#answer3Value                   |n                  |               |                            |Eranga                                                   |
     |#answer3Type                    |n                  |               |                            |TEXT                                                     |
     |#answer3CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer4Id                      |n                  |               |                            |4                                                        |
     |#answer4Value                   |n                  |               |                            |Heshan                                                   |
     |#answer4Type                    |n                  |               |                            |TEXT                                                     |
     |#answer4CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer5Id                      |n                  |               |                            |5                                                        |
     |#answer5Value                   |n                  |               |                            |Thilina                                                  |
     |#answer5Type                    |n                  |               |                            |TEXT                                                     |
     |#answer5CaseSensitive           |n                  |               |                            |true                                                     |
     |#tags                           |n                  |               |                            |MaxSoft                                                  |
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



Create a question using an empty media
--------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name    |Attribute Value To Be Set                                |
     |--------------------------------|-------------------|---------------|----------------------------|---------------------------------------------------------|
     |#creatorId                      |n                  |               |                            |osanda12                                                 |
     |#creatorPlatform                |n                  |               |                            |Web                                                      |
     |#creatoredSource                |n                  |               |                            |App                                                      |
     |#creatoredType                  |n                  |               |                            |Manual                                                   |
     |#deckId                         |y                  |scenario       |deckId                      |                                                         |
     |#kind                           |n                  |               |                            |ALL                                                      |
     |#isDeleted                      |n                  |               |                            |false                                                    |
     |#tempQuestionId                 |n                  |               |                            |testId                                                   |
     |#learningObjectives             |n                  |               |                            |learningObjective1                                       |
     |#imageUrl                       |n                  |               |                            |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |n                  |               |                            |                                                         |
     |#questionPrompt                 |n                  |               |                            |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |n                  |               |                            |TEXT                                                     |
     |#timeout                        |n                  |               |                            |60                                                       |
     |#rationale                      |n                  |               |                            |rationale                                                |
     |#boxId                          |n                  |               |                            |0                                                        |
     |#correctAttempts                |n                  |               |                            |1                                                        |
     |#inCorrectAttempts              |n                  |               |                            |0                                                        |
     |#lastAswered                    |n                  |               |                            |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |n                  |               |                            |0                                                        |
     |#skips                          |n                  |               |                            |0                                                        |
     |#userId                         |n                  |               |                            |0                                                        |
     |#correctAnswerList              |n                  |               |                            |1,2                                                      |
     |#answer1Id                      |n                  |               |                            |1                                                        |
     |#answer1Value                   |n                  |               |                            |Osanda                                                   |
     |#answer1Type                    |n                  |               |                            |TEXT                                                     |
     |#answer1CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer2Id                      |n                  |               |                            |2                                                        |
     |#answer2Value                   |n                  |               |                            |Gemunu                                                   |
     |#answer2Type                    |n                  |               |                            |TEXT                                                     |
     |#answer2CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer3Id                      |n                  |               |                            |3                                                        |
     |#answer3Value                   |n                  |               |                            |Eranga                                                   |
     |#answer3Type                    |n                  |               |                            |TEXT                                                     |
     |#answer3CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer4Id                      |n                  |               |                            |4                                                        |
     |#answer4Value                   |n                  |               |                            |Heshan                                                   |
     |#answer4Type                    |n                  |               |                            |TEXT                                                     |
     |#answer4CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer5Id                      |n                  |               |                            |5                                                        |
     |#answer5Value                   |n                  |               |                            |Thilina                                                  |
     |#answer5Type                    |n                  |               |                            |TEXT                                                     |
     |#answer5CaseSensitive           |n                  |               |                            |true                                                     |
     |#tags                           |n                  |               |                            |MaxSoft                                                  |
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



Create a question using an empty questionPrompt
-----------------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name    |Attribute Value To Be Set                                |
     |--------------------------------|-------------------|---------------|----------------------------|---------------------------------------------------------|
     |#creatorId                      |n                  |               |                            |osanda12                                                 |
     |#creatorPlatform                |n                  |               |                            |Web                                                      |
     |#creatoredSource                |n                  |               |                            |App                                                      |
     |#creatoredType                  |n                  |               |                            |Manual                                                   |
     |#deckId                         |y                  |scenario       |deckId                      |                                                         |
     |#kind                           |n                  |               |                            |ALL                                                      |
     |#isDeleted                      |n                  |               |                            |false                                                    |
     |#tempQuestionId                 |n                  |               |                            |testId                                                   |
     |#learningObjectives             |n                  |               |                            |learningObjective1                                       |
     |#imageUrl                       |n                  |               |                            |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |n                  |               |                            |TEXT                                                     |
     |#questionPrompt                 |n                  |               |                            |                                                         |
     |#promptType                     |n                  |               |                            |TEXT                                                     |
     |#timeout                        |n                  |               |                            |60                                                       |
     |#rationale                      |n                  |               |                            |rationale                                                |
     |#boxId                          |n                  |               |                            |0                                                        |
     |#correctAttempts                |n                  |               |                            |1                                                        |
     |#inCorrectAttempts              |n                  |               |                            |0                                                        |
     |#lastAswered                    |n                  |               |                            |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |n                  |               |                            |0                                                        |
     |#skips                          |n                  |               |                            |0                                                        |
     |#userId                         |n                  |               |                            |0                                                        |
     |#correctAnswerList              |n                  |               |                            |1,2                                                      |
     |#answer1Id                      |n                  |               |                            |1                                                        |
     |#answer1Value                   |n                  |               |                            |Osanda                                                   |
     |#answer1Type                    |n                  |               |                            |TEXT                                                     |
     |#answer1CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer2Id                      |n                  |               |                            |2                                                        |
     |#answer2Value                   |n                  |               |                            |Gemunu                                                   |
     |#answer2Type                    |n                  |               |                            |TEXT                                                     |
     |#answer2CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer3Id                      |n                  |               |                            |3                                                        |
     |#answer3Value                   |n                  |               |                            |Eranga                                                   |
     |#answer3Type                    |n                  |               |                            |TEXT                                                     |
     |#answer3CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer4Id                      |n                  |               |                            |4                                                        |
     |#answer4Value                   |n                  |               |                            |Heshan                                                   |
     |#answer4Type                    |n                  |               |                            |TEXT                                                     |
     |#answer4CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer5Id                      |n                  |               |                            |5                                                        |
     |#answer5Value                   |n                  |               |                            |Thilina                                                  |
     |#answer5Type                    |n                  |               |                            |TEXT                                                     |
     |#answer5CaseSensitive           |n                  |               |                            |true                                                     |
     |#tags                           |n                  |               |                            |MaxSoft                                                  |
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



Create a question using an invalid promptType
---------------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name    |Attribute Value To Be Set                                |
     |--------------------------------|-------------------|---------------|----------------------------|---------------------------------------------------------|
     |#creatorId                      |n                  |               |                            |osanda12                                                 |
     |#creatorPlatform                |n                  |               |                            |Web                                                      |
     |#creatoredSource                |n                  |               |                            |App                                                      |
     |#creatoredType                  |n                  |               |                            |Manual                                                   |
     |#deckId                         |y                  |scenario       |deckId                      |                                                         |
     |#kind                           |n                  |               |                            |ALL                                                      |
     |#isDeleted                      |n                  |               |                            |false                                                    |
     |#tempQuestionId                 |n                  |               |                            |testId                                                   |
     |#learningObjectives             |n                  |               |                            |learningObjective1                                       |
     |#imageUrl                       |n                  |               |                            |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |n                  |               |                            |TEXT                                                     |
     |#questionPrompt                 |n                  |               |                            |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |n                  |               |                            |TEX                                                      |
     |#timeout                        |n                  |               |                            |60                                                       |
     |#rationale                      |n                  |               |                            |rationale                                                |
     |#boxId                          |n                  |               |                            |0                                                        |
     |#correctAttempts                |n                  |               |                            |1                                                        |
     |#inCorrectAttempts              |n                  |               |                            |0                                                        |
     |#lastAswered                    |n                  |               |                            |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |n                  |               |                            |0                                                        |
     |#skips                          |n                  |               |                            |0                                                        |
     |#userId                         |n                  |               |                            |0                                                        |
     |#correctAnswerList              |n                  |               |                            |1,2                                                      |
     |#answer1Id                      |n                  |               |                            |1                                                        |
     |#answer1Value                   |n                  |               |                            |Osanda                                                   |
     |#answer1Type                    |n                  |               |                            |TEXT                                                     |
     |#answer1CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer2Id                      |n                  |               |                            |2                                                        |
     |#answer2Value                   |n                  |               |                            |Gemunu                                                   |
     |#answer2Type                    |n                  |               |                            |TEXT                                                     |
     |#answer2CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer3Id                      |n                  |               |                            |3                                                        |
     |#answer3Value                   |n                  |               |                            |Eranga                                                   |
     |#answer3Type                    |n                  |               |                            |TEXT                                                     |
     |#answer3CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer4Id                      |n                  |               |                            |4                                                        |
     |#answer4Value                   |n                  |               |                            |Heshan                                                   |
     |#answer4Type                    |n                  |               |                            |TEXT                                                     |
     |#answer4CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer5Id                      |n                  |               |                            |5                                                        |
     |#answer5Value                   |n                  |               |                            |Thilina                                                  |
     |#answer5Type                    |n                  |               |                            |TEXT                                                     |
     |#answer5CaseSensitive           |n                  |               |                            |true                                                     |
     |#tags                           |n                  |               |                            |MaxSoft                                                  |
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



Create a question using an empty promptType
-------------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name    |Attribute Value To Be Set                                |
     |--------------------------------|-------------------|---------------|----------------------------|---------------------------------------------------------|
     |#creatorId                      |n                  |               |                            |osanda12                                                 |
     |#creatorPlatform                |n                  |               |                            |Web                                                      |
     |#creatoredSource                |n                  |               |                            |App                                                      |
     |#creatoredType                  |n                  |               |                            |Manual                                                   |
     |#deckId                         |y                  |scenario       |deckId                      |                                                         |
     |#kind                           |n                  |               |                            |ALL                                                      |
     |#isDeleted                      |n                  |               |                            |false                                                    |
     |#tempQuestionId                 |n                  |               |                            |testId                                                   |
     |#learningObjectives             |n                  |               |                            |learningObjective1                                       |
     |#imageUrl                       |n                  |               |                            |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |n                  |               |                            |TEXT                                                     |
     |#questionPrompt                 |n                  |               |                            |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |n                  |               |                            |                                                         |
     |#timeout                        |n                  |               |                            |60                                                       |
     |#rationale                      |n                  |               |                            |rationale                                                |
     |#boxId                          |n                  |               |                            |0                                                        |
     |#correctAttempts                |n                  |               |                            |1                                                        |
     |#inCorrectAttempts              |n                  |               |                            |0                                                        |
     |#lastAswered                    |n                  |               |                            |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |n                  |               |                            |0                                                        |
     |#skips                          |n                  |               |                            |0                                                        |
     |#userId                         |n                  |               |                            |0                                                        |
     |#correctAnswerList              |n                  |               |                            |1,2                                                      |
     |#answer1Id                      |n                  |               |                            |1                                                        |
     |#answer1Value                   |n                  |               |                            |Osanda                                                   |
     |#answer1Type                    |n                  |               |                            |TEXT                                                     |
     |#answer1CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer2Id                      |n                  |               |                            |2                                                        |
     |#answer2Value                   |n                  |               |                            |Gemunu                                                   |
     |#answer2Type                    |n                  |               |                            |TEXT                                                     |
     |#answer2CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer3Id                      |n                  |               |                            |3                                                        |
     |#answer3Value                   |n                  |               |                            |Eranga                                                   |
     |#answer3Type                    |n                  |               |                            |TEXT                                                     |
     |#answer3CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer4Id                      |n                  |               |                            |4                                                        |
     |#answer4Value                   |n                  |               |                            |Heshan                                                   |
     |#answer4Type                    |n                  |               |                            |TEXT                                                     |
     |#answer4CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer5Id                      |n                  |               |                            |5                                                        |
     |#answer5Value                   |n                  |               |                            |Thilina                                                  |
     |#answer5Type                    |n                  |               |                            |TEXT                                                     |
     |#answer5CaseSensitive           |n                  |               |                            |true                                                     |
     |#tags                           |n                  |               |                            |MaxSoft                                                  |
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



Create a question using a string as the timeout
-----------------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name    |Attribute Value To Be Set                                |
     |--------------------------------|-------------------|---------------|----------------------------|---------------------------------------------------------|
     |#creatorId                      |n                  |               |                            |osanda12                                                 |
     |#creatorPlatform                |n                  |               |                            |Web                                                      |
     |#creatoredSource                |n                  |               |                            |App                                                      |
     |#creatoredType                  |n                  |               |                            |Manual                                                   |
     |#deckId                         |y                  |scenario       |deckId                      |                                                         |
     |#kind                           |n                  |               |                            |ALL                                                      |
     |#isDeleted                      |n                  |               |                            |false                                                    |
     |#tempQuestionId                 |n                  |               |                            |testId                                                   |
     |#learningObjectives             |n                  |               |                            |learningObjective1                                       |
     |#imageUrl                       |n                  |               |                            |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |n                  |               |                            |TEXT                                                     |
     |#questionPrompt                 |n                  |               |                            |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |n                  |               |                            |TEXT                                                     |
     |#timeout                        |n                  |               |                            |a0                                                       |
     |#rationale                      |n                  |               |                            |rationale                                                |
     |#boxId                          |n                  |               |                            |0                                                        |
     |#correctAttempts                |n                  |               |                            |1                                                        |
     |#inCorrectAttempts              |n                  |               |                            |0                                                        |
     |#lastAswered                    |n                  |               |                            |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |n                  |               |                            |0                                                        |
     |#skips                          |n                  |               |                            |0                                                        |
     |#userId                         |n                  |               |                            |0                                                        |
     |#correctAnswerList              |n                  |               |                            |1,2                                                      |
     |#answer1Id                      |n                  |               |                            |1                                                        |
     |#answer1Value                   |n                  |               |                            |Osanda                                                   |
     |#answer1Type                    |n                  |               |                            |TEXT                                                     |
     |#answer1CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer2Id                      |n                  |               |                            |2                                                        |
     |#answer2Value                   |n                  |               |                            |Gemunu                                                   |
     |#answer2Type                    |n                  |               |                            |TEXT                                                     |
     |#answer2CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer3Id                      |n                  |               |                            |3                                                        |
     |#answer3Value                   |n                  |               |                            |Eranga                                                   |
     |#answer3Type                    |n                  |               |                            |TEXT                                                     |
     |#answer3CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer4Id                      |n                  |               |                            |4                                                        |
     |#answer4Value                   |n                  |               |                            |Heshan                                                   |
     |#answer4Type                    |n                  |               |                            |TEXT                                                     |
     |#answer4CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer5Id                      |n                  |               |                            |5                                                        |
     |#answer5Value                   |n                  |               |                            |Thilina                                                  |
     |#answer5Type                    |n                  |               |                            |TEXT                                                     |
     |#answer5CaseSensitive           |n                  |               |                            |true                                                     |
     |#tags                           |n                  |               |                            |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.description                             |null                                                     |
     |$.fieldErrors                             |null                                                     |



Create a question using an negative value as the timeout
--------------------------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name    |Attribute Value To Be Set                                |
     |--------------------------------|-------------------|---------------|----------------------------|---------------------------------------------------------|
     |#creatorId                      |n                  |               |                            |osanda12                                                 |
     |#creatorPlatform                |n                  |               |                            |Web                                                      |
     |#creatoredSource                |n                  |               |                            |App                                                      |
     |#creatoredType                  |n                  |               |                            |Manual                                                   |
     |#deckId                         |y                  |scenario       |deckId                      |                                                         |
     |#kind                           |n                  |               |                            |ALL                                                      |
     |#isDeleted                      |n                  |               |                            |false                                                    |
     |#tempQuestionId                 |n                  |               |                            |testId                                                   |
     |#learningObjectives             |n                  |               |                            |learningObjective1                                       |
     |#imageUrl                       |n                  |               |                            |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |n                  |               |                            |TEXT                                                     |
     |#questionPrompt                 |n                  |               |                            |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |n                  |               |                            |TEXT                                                     |
     |#timeout                        |n                  |               |                            |-60                                                      |
     |#rationale                      |n                  |               |                            |rationale                                                |
     |#boxId                          |n                  |               |                            |0                                                        |
     |#correctAttempts                |n                  |               |                            |1                                                        |
     |#inCorrectAttempts              |n                  |               |                            |0                                                        |
     |#lastAswered                    |n                  |               |                            |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |n                  |               |                            |0                                                        |
     |#skips                          |n                  |               |                            |0                                                        |
     |#userId                         |n                  |               |                            |0                                                        |
     |#correctAnswerList              |n                  |               |                            |1,2                                                      |
     |#answer1Id                      |n                  |               |                            |1                                                        |
     |#answer1Value                   |n                  |               |                            |Osanda                                                   |
     |#answer1Type                    |n                  |               |                            |TEXT                                                     |
     |#answer1CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer2Id                      |n                  |               |                            |2                                                        |
     |#answer2Value                   |n                  |               |                            |Gemunu                                                   |
     |#answer2Type                    |n                  |               |                            |TEXT                                                     |
     |#answer2CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer3Id                      |n                  |               |                            |3                                                        |
     |#answer3Value                   |n                  |               |                            |Eranga                                                   |
     |#answer3Type                    |n                  |               |                            |TEXT                                                     |
     |#answer3CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer4Id                      |n                  |               |                            |4                                                        |
     |#answer4Value                   |n                  |               |                            |Heshan                                                   |
     |#answer4Type                    |n                  |               |                            |TEXT                                                     |
     |#answer4CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer5Id                      |n                  |               |                            |5                                                        |
     |#answer5Value                   |n                  |               |                            |Thilina                                                  |
     |#answer5Type                    |n                  |               |                            |TEXT                                                     |
     |#answer5CaseSensitive           |n                  |               |                            |true                                                     |
     |#tags                           |n                  |               |                            |MaxSoft                                                  |
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



Create a question using a string value as the boxId
---------------------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name    |Attribute Value To Be Set                                |
     |--------------------------------|-------------------|---------------|----------------------------|---------------------------------------------------------|
     |#creatorId                      |n                  |               |                            |osanda12                                                 |
     |#creatorPlatform                |n                  |               |                            |Web                                                      |
     |#creatoredSource                |n                  |               |                            |App                                                      |
     |#creatoredType                  |n                  |               |                            |Manual                                                   |
     |#deckId                         |y                  |scenario       |deckId                      |                                                         |
     |#kind                           |n                  |               |                            |ALL                                                      |
     |#isDeleted                      |n                  |               |                            |false                                                    |
     |#tempQuestionId                 |n                  |               |                            |testId                                                   |
     |#learningObjectives             |n                  |               |                            |learningObjective1                                       |
     |#imageUrl                       |n                  |               |                            |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |n                  |               |                            |TEXT                                                     |
     |#questionPrompt                 |n                  |               |                            |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |n                  |               |                            |TEXT                                                     |
     |#timeout                        |n                  |               |                            |60                                                       |
     |#rationale                      |n                  |               |                            |rationale                                                |
     |#boxId                          |n                  |               |                            |a                                                        |
     |#correctAttempts                |n                  |               |                            |1                                                        |
     |#inCorrectAttempts              |n                  |               |                            |0                                                        |
     |#lastAswered                    |n                  |               |                            |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |n                  |               |                            |0                                                        |
     |#skips                          |n                  |               |                            |0                                                        |
     |#userId                         |n                  |               |                            |0                                                        |
     |#correctAnswerList              |n                  |               |                            |1,2                                                      |
     |#answer1Id                      |n                  |               |                            |1                                                        |
     |#answer1Value                   |n                  |               |                            |Osanda                                                   |
     |#answer1Type                    |n                  |               |                            |TEXT                                                     |
     |#answer1CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer2Id                      |n                  |               |                            |2                                                        |
     |#answer2Value                   |n                  |               |                            |Gemunu                                                   |
     |#answer2Type                    |n                  |               |                            |TEXT                                                     |
     |#answer2CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer3Id                      |n                  |               |                            |3                                                        |
     |#answer3Value                   |n                  |               |                            |Eranga                                                   |
     |#answer3Type                    |n                  |               |                            |TEXT                                                     |
     |#answer3CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer4Id                      |n                  |               |                            |4                                                        |
     |#answer4Value                   |n                  |               |                            |Heshan                                                   |
     |#answer4Type                    |n                  |               |                            |TEXT                                                     |
     |#answer4CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer5Id                      |n                  |               |                            |5                                                        |
     |#answer5Value                   |n                  |               |                            |Thilina                                                  |
     |#answer5Type                    |n                  |               |                            |TEXT                                                     |
     |#answer5CaseSensitive           |n                  |               |                            |true                                                     |
     |#tags                           |n                  |               |                            |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.description                             |null                                                     |
     |$.fieldErrors                             |null                                                     |



Create a question using a negative integer value as the boxId
-------------------------------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name    |Attribute Value To Be Set                                |
     |--------------------------------|-------------------|---------------|----------------------------|---------------------------------------------------------|
     |#creatorId                      |n                  |               |                            |osanda12                                                 |
     |#creatorPlatform                |n                  |               |                            |Web                                                      |
     |#creatoredSource                |n                  |               |                            |App                                                      |
     |#creatoredType                  |n                  |               |                            |Manual                                                   |
     |#deckId                         |y                  |scenario       |deckId                      |                                                         |
     |#kind                           |n                  |               |                            |ALL                                                      |
     |#isDeleted                      |n                  |               |                            |false                                                    |
     |#tempQuestionId                 |n                  |               |                            |testId                                                   |
     |#learningObjectives             |n                  |               |                            |learningObjective1                                       |
     |#imageUrl                       |n                  |               |                            |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |n                  |               |                            |TEXT                                                     |
     |#questionPrompt                 |n                  |               |                            |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |n                  |               |                            |TEXT                                                     |
     |#timeout                        |n                  |               |                            |60                                                       |
     |#rationale                      |n                  |               |                            |rationale                                                |
     |#boxId                          |n                  |               |                            |-2                                                       |
     |#correctAttempts                |n                  |               |                            |1                                                        |
     |#inCorrectAttempts              |n                  |               |                            |0                                                        |
     |#lastAswered                    |n                  |               |                            |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |n                  |               |                            |0                                                        |
     |#skips                          |n                  |               |                            |0                                                        |
     |#userId                         |n                  |               |                            |0                                                        |
     |#correctAnswerList              |n                  |               |                            |1,2                                                      |
     |#answer1Id                      |n                  |               |                            |1                                                        |
     |#answer1Value                   |n                  |               |                            |Osanda                                                   |
     |#answer1Type                    |n                  |               |                            |TEXT                                                     |
     |#answer1CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer2Id                      |n                  |               |                            |2                                                        |
     |#answer2Value                   |n                  |               |                            |Gemunu                                                   |
     |#answer2Type                    |n                  |               |                            |TEXT                                                     |
     |#answer2CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer3Id                      |n                  |               |                            |3                                                        |
     |#answer3Value                   |n                  |               |                            |Eranga                                                   |
     |#answer3Type                    |n                  |               |                            |TEXT                                                     |
     |#answer3CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer4Id                      |n                  |               |                            |4                                                        |
     |#answer4Value                   |n                  |               |                            |Heshan                                                   |
     |#answer4Type                    |n                  |               |                            |TEXT                                                     |
     |#answer4CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer5Id                      |n                  |               |                            |5                                                        |
     |#answer5Value                   |n                  |               |                            |Thilina                                                  |
     |#answer5Type                    |n                  |               |                            |TEXT                                                     |
     |#answer5CaseSensitive           |n                  |               |                            |true                                                     |
     |#tags                           |n                  |               |                            |MaxSoft                                                  |
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



Create a question using an empty value as the boxId
---------------------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name    |Attribute Value To Be Set                                |
     |--------------------------------|-------------------|---------------|----------------------------|---------------------------------------------------------|
     |#creatorId                      |n                  |               |                            |osanda12                                                 |
     |#creatorPlatform                |n                  |               |                            |Web                                                      |
     |#creatoredSource                |n                  |               |                            |App                                                      |
     |#creatoredType                  |n                  |               |                            |Manual                                                   |
     |#deckId                         |y                  |scenario       |deckId                      |                                                         |
     |#kind                           |n                  |               |                            |ALL                                                      |
     |#isDeleted                      |n                  |               |                            |false                                                    |
     |#tempQuestionId                 |n                  |               |                            |testId                                                   |
     |#learningObjectives             |n                  |               |                            |learningObjective1                                       |
     |#imageUrl                       |n                  |               |                            |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |n                  |               |                            |TEXT                                                     |
     |#questionPrompt                 |n                  |               |                            |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |n                  |               |                            |TEXT                                                     |
     |#timeout                        |n                  |               |                            |60                                                       |
     |#rationale                      |n                  |               |                            |rationale                                                |
     |#boxId                          |n                  |               |                            |                                                         |
     |#correctAttempts                |n                  |               |                            |1                                                        |
     |#inCorrectAttempts              |n                  |               |                            |0                                                        |
     |#lastAswered                    |n                  |               |                            |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |n                  |               |                            |0                                                        |
     |#skips                          |n                  |               |                            |0                                                        |
     |#userId                         |n                  |               |                            |0                                                        |
     |#correctAnswerList              |n                  |               |                            |1,2                                                      |
     |#answer1Id                      |n                  |               |                            |1                                                        |
     |#answer1Value                   |n                  |               |                            |Osanda                                                   |
     |#answer1Type                    |n                  |               |                            |TEXT                                                     |
     |#answer1CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer2Id                      |n                  |               |                            |2                                                        |
     |#answer2Value                   |n                  |               |                            |Gemunu                                                   |
     |#answer2Type                    |n                  |               |                            |TEXT                                                     |
     |#answer2CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer3Id                      |n                  |               |                            |3                                                        |
     |#answer3Value                   |n                  |               |                            |Eranga                                                   |
     |#answer3Type                    |n                  |               |                            |TEXT                                                     |
     |#answer3CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer4Id                      |n                  |               |                            |4                                                        |
     |#answer4Value                   |n                  |               |                            |Heshan                                                   |
     |#answer4Type                    |n                  |               |                            |TEXT                                                     |
     |#answer4CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer5Id                      |n                  |               |                            |5                                                        |
     |#answer5Value                   |n                  |               |                            |Thilina                                                  |
     |#answer5Type                    |n                  |               |                            |TEXT                                                     |
     |#answer5CaseSensitive           |n                  |               |                            |true                                                     |
     |#tags                           |n                  |               |                            |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.description                             |null                                                     |
     |$.fieldErrors                             |null                                                     |



Create a question using a string value as the correctAttempts
-------------------------------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name    |Attribute Value To Be Set                                |
     |--------------------------------|-------------------|---------------|----------------------------|---------------------------------------------------------|
     |#creatorId                      |n                  |               |                            |osanda12                                                 |
     |#creatorPlatform                |n                  |               |                            |Web                                                      |
     |#creatoredSource                |n                  |               |                            |App                                                      |
     |#creatoredType                  |n                  |               |                            |Manual                                                   |
     |#deckId                         |y                  |scenario       |deckId                      |                                                         |
     |#kind                           |n                  |               |                            |ALL                                                      |
     |#isDeleted                      |n                  |               |                            |false                                                    |
     |#tempQuestionId                 |n                  |               |                            |testId                                                   |
     |#learningObjectives             |n                  |               |                            |learningObjective1                                       |
     |#imageUrl                       |n                  |               |                            |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |n                  |               |                            |TEXT                                                     |
     |#questionPrompt                 |n                  |               |                            |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |n                  |               |                            |TEXT                                                     |
     |#timeout                        |n                  |               |                            |60                                                       |
     |#rationale                      |n                  |               |                            |rationale                                                |
     |#boxId                          |n                  |               |                            |0                                                        |
     |#correctAttempts                |n                  |               |                            |a                                                        |
     |#inCorrectAttempts              |n                  |               |                            |0                                                        |
     |#lastAswered                    |n                  |               |                            |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |n                  |               |                            |0                                                        |
     |#skips                          |n                  |               |                            |0                                                        |
     |#userId                         |n                  |               |                            |0                                                        |
     |#correctAnswerList              |n                  |               |                            |1,2                                                      |
     |#answer1Id                      |n                  |               |                            |1                                                        |
     |#answer1Value                   |n                  |               |                            |Osanda                                                   |
     |#answer1Type                    |n                  |               |                            |TEXT                                                     |
     |#answer1CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer2Id                      |n                  |               |                            |2                                                        |
     |#answer2Value                   |n                  |               |                            |Gemunu                                                   |
     |#answer2Type                    |n                  |               |                            |TEXT                                                     |
     |#answer2CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer3Id                      |n                  |               |                            |3                                                        |
     |#answer3Value                   |n                  |               |                            |Eranga                                                   |
     |#answer3Type                    |n                  |               |                            |TEXT                                                     |
     |#answer3CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer4Id                      |n                  |               |                            |4                                                        |
     |#answer4Value                   |n                  |               |                            |Heshan                                                   |
     |#answer4Type                    |n                  |               |                            |TEXT                                                     |
     |#answer4CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer5Id                      |n                  |               |                            |5                                                        |
     |#answer5Value                   |n                  |               |                            |Thilina                                                  |
     |#answer5Type                    |n                  |               |                            |TEXT                                                     |
     |#answer5CaseSensitive           |n                  |               |                            |true                                                     |
     |#tags                           |n                  |               |                            |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.description                             |null                                                     |
     |$.fieldErrors                             |null                                                     |



Create a question using a negative integer value as the correctAttempts
-----------------------------------------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name    |Attribute Value To Be Set                                |
     |--------------------------------|-------------------|---------------|----------------------------|---------------------------------------------------------|
     |#creatorId                      |n                  |               |                            |osanda12                                                 |
     |#creatorPlatform                |n                  |               |                            |Web                                                      |
     |#creatoredSource                |n                  |               |                            |App                                                      |
     |#creatoredType                  |n                  |               |                            |Manual                                                   |
     |#deckId                         |y                  |scenario       |deckId                      |                                                         |
     |#kind                           |n                  |               |                            |ALL                                                      |
     |#isDeleted                      |n                  |               |                            |false                                                    |
     |#tempQuestionId                 |n                  |               |                            |testId                                                   |
     |#learningObjectives             |n                  |               |                            |learningObjective1                                       |
     |#imageUrl                       |n                  |               |                            |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |n                  |               |                            |TEXT                                                     |
     |#questionPrompt                 |n                  |               |                            |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |n                  |               |                            |TEXT                                                     |
     |#timeout                        |n                  |               |                            |60                                                       |
     |#rationale                      |n                  |               |                            |rationale                                                |
     |#boxId                          |n                  |               |                            |0                                                        |
     |#correctAttempts                |n                  |               |                            |-1                                                       |
     |#inCorrectAttempts              |n                  |               |                            |0                                                        |
     |#lastAswered                    |n                  |               |                            |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |n                  |               |                            |0                                                        |
     |#skips                          |n                  |               |                            |0                                                        |
     |#userId                         |n                  |               |                            |0                                                        |
     |#correctAnswerList              |n                  |               |                            |1,2                                                      |
     |#answer1Id                      |n                  |               |                            |1                                                        |
     |#answer1Value                   |n                  |               |                            |Osanda                                                   |
     |#answer1Type                    |n                  |               |                            |TEXT                                                     |
     |#answer1CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer2Id                      |n                  |               |                            |2                                                        |
     |#answer2Value                   |n                  |               |                            |Gemunu                                                   |
     |#answer2Type                    |n                  |               |                            |TEXT                                                     |
     |#answer2CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer3Id                      |n                  |               |                            |3                                                        |
     |#answer3Value                   |n                  |               |                            |Eranga                                                   |
     |#answer3Type                    |n                  |               |                            |TEXT                                                     |
     |#answer3CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer4Id                      |n                  |               |                            |4                                                        |
     |#answer4Value                   |n                  |               |                            |Heshan                                                   |
     |#answer4Type                    |n                  |               |                            |TEXT                                                     |
     |#answer4CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer5Id                      |n                  |               |                            |5                                                        |
     |#answer5Value                   |n                  |               |                            |Thilina                                                  |
     |#answer5Type                    |n                  |               |                            |TEXT                                                     |
     |#answer5CaseSensitive           |n                  |               |                            |true                                                     |
     |#tags                           |n                  |               |                            |MaxSoft                                                  |
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



Create a question using a special characters value as the correctAttempts
-------------------------------------------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name    |Attribute Value To Be Set                                |
     |--------------------------------|-------------------|---------------|----------------------------|---------------------------------------------------------|
     |#creatorId                      |n                  |               |                            |osanda12                                                 |
     |#creatorPlatform                |n                  |               |                            |Web                                                      |
     |#creatoredSource                |n                  |               |                            |App                                                      |
     |#creatoredType                  |n                  |               |                            |Manual                                                   |
     |#deckId                         |y                  |scenario       |deckId                      |                                                         |
     |#kind                           |n                  |               |                            |ALL                                                      |
     |#isDeleted                      |n                  |               |                            |false                                                    |
     |#tempQuestionId                 |n                  |               |                            |testId                                                   |
     |#learningObjectives             |n                  |               |                            |learningObjective1                                       |
     |#imageUrl                       |n                  |               |                            |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |n                  |               |                            |TEXT                                                     |
     |#questionPrompt                 |n                  |               |                            |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |n                  |               |                            |TEXT                                                     |
     |#timeout                        |n                  |               |                            |60                                                       |
     |#rationale                      |n                  |               |                            |rationale                                                |
     |#boxId                          |n                  |               |                            |0                                                        |
     |#correctAttempts                |n                  |               |                            |@                                                        |
     |#inCorrectAttempts              |n                  |               |                            |0                                                        |
     |#lastAswered                    |n                  |               |                            |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |n                  |               |                            |0                                                        |
     |#skips                          |n                  |               |                            |0                                                        |
     |#userId                         |n                  |               |                            |0                                                        |
     |#correctAnswerList              |n                  |               |                            |1,2                                                      |
     |#answer1Id                      |n                  |               |                            |1                                                        |
     |#answer1Value                   |n                  |               |                            |Osanda                                                   |
     |#answer1Type                    |n                  |               |                            |TEXT                                                     |
     |#answer1CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer2Id                      |n                  |               |                            |2                                                        |
     |#answer2Value                   |n                  |               |                            |Gemunu                                                   |
     |#answer2Type                    |n                  |               |                            |TEXT                                                     |
     |#answer2CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer3Id                      |n                  |               |                            |3                                                        |
     |#answer3Value                   |n                  |               |                            |Eranga                                                   |
     |#answer3Type                    |n                  |               |                            |TEXT                                                     |
     |#answer3CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer4Id                      |n                  |               |                            |4                                                        |
     |#answer4Value                   |n                  |               |                            |Heshan                                                   |
     |#answer4Type                    |n                  |               |                            |TEXT                                                     |
     |#answer4CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer5Id                      |n                  |               |                            |5                                                        |
     |#answer5Value                   |n                  |               |                            |Thilina                                                  |
     |#answer5Type                    |n                  |               |                            |TEXT                                                     |
     |#answer5CaseSensitive           |n                  |               |                            |true                                                     |
     |#tags                           |n                  |               |                            |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.description                             |null                                                     |
     |$.fieldErrors                             |null                                                     |



Create a question using an empty value as the correctAttempts
-------------------------------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name    |Attribute Value To Be Set                                |
     |--------------------------------|-------------------|---------------|----------------------------|---------------------------------------------------------|
     |#creatorId                      |n                  |               |                            |osanda12                                                 |
     |#creatorPlatform                |n                  |               |                            |Web                                                      |
     |#creatoredSource                |n                  |               |                            |App                                                      |
     |#creatoredType                  |n                  |               |                            |Manual                                                   |
     |#deckId                         |y                  |scenario       |deckId                      |                                                         |
     |#kind                           |n                  |               |                            |ALL                                                      |
     |#isDeleted                      |n                  |               |                            |false                                                    |
     |#tempQuestionId                 |n                  |               |                            |testId                                                   |
     |#learningObjectives             |n                  |               |                            |learningObjective1                                       |
     |#imageUrl                       |n                  |               |                            |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |n                  |               |                            |TEXT                                                     |
     |#questionPrompt                 |n                  |               |                            |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |n                  |               |                            |TEXT                                                     |
     |#timeout                        |n                  |               |                            |60                                                       |
     |#rationale                      |n                  |               |                            |rationale                                                |
     |#boxId                          |n                  |               |                            |0                                                        |
     |#correctAttempts                |n                  |               |                            |                                                         |
     |#inCorrectAttempts              |n                  |               |                            |0                                                        |
     |#lastAswered                    |n                  |               |                            |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |n                  |               |                            |0                                                        |
     |#skips                          |n                  |               |                            |0                                                        |
     |#userId                         |n                  |               |                            |0                                                        |
     |#correctAnswerList              |n                  |               |                            |1,2                                                      |
     |#answer1Id                      |n                  |               |                            |1                                                        |
     |#answer1Value                   |n                  |               |                            |Osanda                                                   |
     |#answer1Type                    |n                  |               |                            |TEXT                                                     |
     |#answer1CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer2Id                      |n                  |               |                            |2                                                        |
     |#answer2Value                   |n                  |               |                            |Gemunu                                                   |
     |#answer2Type                    |n                  |               |                            |TEXT                                                     |
     |#answer2CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer3Id                      |n                  |               |                            |3                                                        |
     |#answer3Value                   |n                  |               |                            |Eranga                                                   |
     |#answer3Type                    |n                  |               |                            |TEXT                                                     |
     |#answer3CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer4Id                      |n                  |               |                            |4                                                        |
     |#answer4Value                   |n                  |               |                            |Heshan                                                   |
     |#answer4Type                    |n                  |               |                            |TEXT                                                     |
     |#answer4CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer5Id                      |n                  |               |                            |5                                                        |
     |#answer5Value                   |n                  |               |                            |Thilina                                                  |
     |#answer5Type                    |n                  |               |                            |TEXT                                                     |
     |#answer5CaseSensitive           |n                  |               |                            |true                                                     |
     |#tags                           |n                  |               |                            |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.description                             |null                                                     |
     |$.fieldErrors                             |null                                                     |



Create a question using a special characters value as the inCorrectAttempts
---------------------------------------------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name    |Attribute Value To Be Set                                |
     |--------------------------------|-------------------|---------------|----------------------------|---------------------------------------------------------|
     |#creatorId                      |n                  |               |                            |osanda12                                                 |
     |#creatorPlatform                |n                  |               |                            |Web                                                      |
     |#creatoredSource                |n                  |               |                            |App                                                      |
     |#creatoredType                  |n                  |               |                            |Manual                                                   |
     |#deckId                         |y                  |scenario       |deckId                      |                                                         |
     |#kind                           |n                  |               |                            |ALL                                                      |
     |#isDeleted                      |n                  |               |                            |false                                                    |
     |#tempQuestionId                 |n                  |               |                            |testId                                                   |
     |#learningObjectives             |n                  |               |                            |learningObjective1                                       |
     |#imageUrl                       |n                  |               |                            |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |n                  |               |                            |TEXT                                                     |
     |#questionPrompt                 |n                  |               |                            |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |n                  |               |                            |TEXT                                                     |
     |#timeout                        |n                  |               |                            |60                                                       |
     |#rationale                      |n                  |               |                            |rationale                                                |
     |#boxId                          |n                  |               |                            |0                                                        |
     |#correctAttempts                |n                  |               |                            |1                                                        |
     |#inCorrectAttempts              |n                  |               |                            |@                                                        |
     |#lastAswered                    |n                  |               |                            |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |n                  |               |                            |0                                                        |
     |#skips                          |n                  |               |                            |0                                                        |
     |#userId                         |n                  |               |                            |0                                                        |
     |#correctAnswerList              |n                  |               |                            |1,2                                                      |
     |#answer1Id                      |n                  |               |                            |1                                                        |
     |#answer1Value                   |n                  |               |                            |Osanda                                                   |
     |#answer1Type                    |n                  |               |                            |TEXT                                                     |
     |#answer1CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer2Id                      |n                  |               |                            |2                                                        |
     |#answer2Value                   |n                  |               |                            |Gemunu                                                   |
     |#answer2Type                    |n                  |               |                            |TEXT                                                     |
     |#answer2CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer3Id                      |n                  |               |                            |3                                                        |
     |#answer3Value                   |n                  |               |                            |Eranga                                                   |
     |#answer3Type                    |n                  |               |                            |TEXT                                                     |
     |#answer3CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer4Id                      |n                  |               |                            |4                                                        |
     |#answer4Value                   |n                  |               |                            |Heshan                                                   |
     |#answer4Type                    |n                  |               |                            |TEXT                                                     |
     |#answer4CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer5Id                      |n                  |               |                            |5                                                        |
     |#answer5Value                   |n                  |               |                            |Thilina                                                  |
     |#answer5Type                    |n                  |               |                            |TEXT                                                     |
     |#answer5CaseSensitive           |n                  |               |                            |true                                                     |
     |#tags                           |n                  |               |                            |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.description                             |null                                                     |
     |$.fieldErrors                             |null                                                     |



Create a question using a string value as the inCorrectAttempts
---------------------------------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name    |Attribute Value To Be Set                                |
     |--------------------------------|-------------------|---------------|----------------------------|---------------------------------------------------------|
     |#creatorId                      |n                  |               |                            |osanda12                                                 |
     |#creatorPlatform                |n                  |               |                            |Web                                                      |
     |#creatoredSource                |n                  |               |                            |App                                                      |
     |#creatoredType                  |n                  |               |                            |Manual                                                   |
     |#deckId                         |y                  |scenario       |deckId                      |                                                         |
     |#kind                           |n                  |               |                            |ALL                                                      |
     |#isDeleted                      |n                  |               |                            |false                                                    |
     |#tempQuestionId                 |n                  |               |                            |testId                                                   |
     |#learningObjectives             |n                  |               |                            |learningObjective1                                       |
     |#imageUrl                       |n                  |               |                            |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |n                  |               |                            |TEXT                                                     |
     |#questionPrompt                 |n                  |               |                            |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |n                  |               |                            |TEXT                                                     |
     |#timeout                        |n                  |               |                            |60                                                       |
     |#rationale                      |n                  |               |                            |rationale                                                |
     |#boxId                          |n                  |               |                            |0                                                        |
     |#correctAttempts                |n                  |               |                            |1                                                        |
     |#inCorrectAttempts              |n                  |               |                            |a                                                        |
     |#lastAswered                    |n                  |               |                            |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |n                  |               |                            |0                                                        |
     |#skips                          |n                  |               |                            |0                                                        |
     |#userId                         |n                  |               |                            |0                                                        |
     |#correctAnswerList              |n                  |               |                            |1,2                                                      |
     |#answer1Id                      |n                  |               |                            |1                                                        |
     |#answer1Value                   |n                  |               |                            |Osanda                                                   |
     |#answer1Type                    |n                  |               |                            |TEXT                                                     |
     |#answer1CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer2Id                      |n                  |               |                            |2                                                        |
     |#answer2Value                   |n                  |               |                            |Gemunu                                                   |
     |#answer2Type                    |n                  |               |                            |TEXT                                                     |
     |#answer2CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer3Id                      |n                  |               |                            |3                                                        |
     |#answer3Value                   |n                  |               |                            |Eranga                                                   |
     |#answer3Type                    |n                  |               |                            |TEXT                                                     |
     |#answer3CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer4Id                      |n                  |               |                            |4                                                        |
     |#answer4Value                   |n                  |               |                            |Heshan                                                   |
     |#answer4Type                    |n                  |               |                            |TEXT                                                     |
     |#answer4CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer5Id                      |n                  |               |                            |5                                                        |
     |#answer5Value                   |n                  |               |                            |Thilina                                                  |
     |#answer5Type                    |n                  |               |                            |TEXT                                                     |
     |#answer5CaseSensitive           |n                  |               |                            |true                                                     |
     |#tags                           |n                  |               |                            |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.description                             |null                                                     |
     |$.fieldErrors                             |null                                                     |



Create a question using a negative integer value as the inCorrectAttempts
-------------------------------------------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name    |Attribute Value To Be Set                                |
     |--------------------------------|-------------------|---------------|----------------------------|---------------------------------------------------------|
     |#creatorId                      |n                  |               |                            |osanda12                                                 |
     |#creatorPlatform                |n                  |               |                            |Web                                                      |
     |#creatoredSource                |n                  |               |                            |App                                                      |
     |#creatoredType                  |n                  |               |                            |Manual                                                   |
     |#deckId                         |y                  |scenario       |deckId                      |                                                         |
     |#kind                           |n                  |               |                            |ALL                                                      |
     |#isDeleted                      |n                  |               |                            |false                                                    |
     |#tempQuestionId                 |n                  |               |                            |testId                                                   |
     |#learningObjectives             |n                  |               |                            |learningObjective1                                       |
     |#imageUrl                       |n                  |               |                            |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |n                  |               |                            |TEXT                                                     |
     |#questionPrompt                 |n                  |               |                            |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |n                  |               |                            |TEXT                                                     |
     |#timeout                        |n                  |               |                            |60                                                       |
     |#rationale                      |n                  |               |                            |rationale                                                |
     |#boxId                          |n                  |               |                            |0                                                        |
     |#correctAttempts                |n                  |               |                            |1                                                        |
     |#inCorrectAttempts              |n                  |               |                            |-2                                                       |
     |#lastAswered                    |n                  |               |                            |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |n                  |               |                            |0                                                        |
     |#skips                          |n                  |               |                            |0                                                        |
     |#userId                         |n                  |               |                            |0                                                        |
     |#correctAnswerList              |n                  |               |                            |1,2                                                      |
     |#answer1Id                      |n                  |               |                            |1                                                        |
     |#answer1Value                   |n                  |               |                            |Osanda                                                   |
     |#answer1Type                    |n                  |               |                            |TEXT                                                     |
     |#answer1CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer2Id                      |n                  |               |                            |2                                                        |
     |#answer2Value                   |n                  |               |                            |Gemunu                                                   |
     |#answer2Type                    |n                  |               |                            |TEXT                                                     |
     |#answer2CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer3Id                      |n                  |               |                            |3                                                        |
     |#answer3Value                   |n                  |               |                            |Eranga                                                   |
     |#answer3Type                    |n                  |               |                            |TEXT                                                     |
     |#answer3CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer4Id                      |n                  |               |                            |4                                                        |
     |#answer4Value                   |n                  |               |                            |Heshan                                                   |
     |#answer4Type                    |n                  |               |                            |TEXT                                                     |
     |#answer4CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer5Id                      |n                  |               |                            |5                                                        |
     |#answer5Value                   |n                  |               |                            |Thilina                                                  |
     |#answer5Type                    |n                  |               |                            |TEXT                                                     |
     |#answer5CaseSensitive           |n                  |               |                            |true                                                     |
     |#tags                           |n                  |               |                            |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.description                             |null                                                     |
     |$.fieldErrors[0].message                  |'skips' should be zero or positive integer.              |



Create a question using an empty value as the inCorrectAttempts
---------------------------------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name    |Attribute Value To Be Set                                |
     |--------------------------------|-------------------|---------------|----------------------------|---------------------------------------------------------|
     |#creatorId                      |n                  |               |                            |osanda12                                                 |
     |#creatorPlatform                |n                  |               |                            |Web                                                      |
     |#creatoredSource                |n                  |               |                            |App                                                      |
     |#creatoredType                  |n                  |               |                            |Manual                                                   |
     |#deckId                         |y                  |scenario       |deckId                      |                                                         |
     |#kind                           |n                  |               |                            |ALL                                                      |
     |#isDeleted                      |n                  |               |                            |false                                                    |
     |#tempQuestionId                 |n                  |               |                            |testId                                                   |
     |#learningObjectives             |n                  |               |                            |learningObjective1                                       |
     |#imageUrl                       |n                  |               |                            |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |n                  |               |                            |TEXT                                                     |
     |#questionPrompt                 |n                  |               |                            |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |n                  |               |                            |TEXT                                                     |
     |#timeout                        |n                  |               |                            |60                                                       |
     |#rationale                      |n                  |               |                            |rationale                                                |
     |#boxId                          |n                  |               |                            |0                                                        |
     |#correctAttempts                |n                  |               |                            |1                                                        |
     |#inCorrectAttempts              |n                  |               |                            |                                                         |
     |#lastAswered                    |n                  |               |                            |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |n                  |               |                            |0                                                        |
     |#skips                          |n                  |               |                            |0                                                        |
     |#userId                         |n                  |               |                            |0                                                        |
     |#correctAnswerList              |n                  |               |                            |1,2                                                      |
     |#answer1Id                      |n                  |               |                            |1                                                        |
     |#answer1Value                   |n                  |               |                            |Osanda                                                   |
     |#answer1Type                    |n                  |               |                            |TEXT                                                     |
     |#answer1CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer2Id                      |n                  |               |                            |2                                                        |
     |#answer2Value                   |n                  |               |                            |Gemunu                                                   |
     |#answer2Type                    |n                  |               |                            |TEXT                                                     |
     |#answer2CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer3Id                      |n                  |               |                            |3                                                        |
     |#answer3Value                   |n                  |               |                            |Eranga                                                   |
     |#answer3Type                    |n                  |               |                            |TEXT                                                     |
     |#answer3CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer4Id                      |n                  |               |                            |4                                                        |
     |#answer4Value                   |n                  |               |                            |Heshan                                                   |
     |#answer4Type                    |n                  |               |                            |TEXT                                                     |
     |#answer4CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer5Id                      |n                  |               |                            |5                                                        |
     |#answer5Value                   |n                  |               |                            |Thilina                                                  |
     |#answer5Type                    |n                  |               |                            |TEXT                                                     |
     |#answer5CaseSensitive           |n                  |               |                            |true                                                     |
     |#tags                           |n                  |               |                            |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.description                             |null                                                     |
     |$.fieldErrors                             |null                                                     |



Create a question using a negative integer value as the questionId
------------------------------------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name    |Attribute Value To Be Set                                |
     |--------------------------------|-------------------|---------------|----------------------------|---------------------------------------------------------|
     |#creatorId                      |n                  |               |                            |osanda12                                                 |
     |#creatorPlatform                |n                  |               |                            |Web                                                      |
     |#creatoredSource                |n                  |               |                            |App                                                      |
     |#creatoredType                  |n                  |               |                            |Manual                                                   |
     |#deckId                         |y                  |scenario       |deckId                      |                                                         |
     |#kind                           |n                  |               |                            |ALL                                                      |
     |#isDeleted                      |n                  |               |                            |false                                                    |
     |#tempQuestionId                 |n                  |               |                            |testId                                                   |
     |#learningObjectives             |n                  |               |                            |learningObjective1                                       |
     |#imageUrl                       |n                  |               |                            |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |n                  |               |                            |TEXT                                                     |
     |#questionPrompt                 |n                  |               |                            |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |n                  |               |                            |TEXT                                                     |
     |#timeout                        |n                  |               |                            |60                                                       |
     |#rationale                      |n                  |               |                            |rationale                                                |
     |#boxId                          |n                  |               |                            |0                                                        |
     |#correctAttempts                |n                  |               |                            |1                                                        |
     |#inCorrectAttempts              |n                  |               |                            |0                                                        |
     |#lastAswered                    |n                  |               |                            |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |n                  |               |                            |-1                                                       |
     |#skips                          |n                  |               |                            |0                                                        |
     |#userId                         |n                  |               |                            |0                                                        |
     |#correctAnswerList              |n                  |               |                            |1,2                                                      |
     |#answer1Id                      |n                  |               |                            |1                                                        |
     |#answer1Value                   |n                  |               |                            |Osanda                                                   |
     |#answer1Type                    |n                  |               |                            |TEXT                                                     |
     |#answer1CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer2Id                      |n                  |               |                            |2                                                        |
     |#answer2Value                   |n                  |               |                            |Gemunu                                                   |
     |#answer2Type                    |n                  |               |                            |TEXT                                                     |
     |#answer2CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer3Id                      |n                  |               |                            |3                                                        |
     |#answer3Value                   |n                  |               |                            |Eranga                                                   |
     |#answer3Type                    |n                  |               |                            |TEXT                                                     |
     |#answer3CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer4Id                      |n                  |               |                            |4                                                        |
     |#answer4Value                   |n                  |               |                            |Heshan                                                   |
     |#answer4Type                    |n                  |               |                            |TEXT                                                     |
     |#answer4CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer5Id                      |n                  |               |                            |5                                                        |
     |#answer5Value                   |n                  |               |                            |Thilina                                                  |
     |#answer5Type                    |n                  |               |                            |TEXT                                                     |
     |#answer5CaseSensitive           |n                  |               |                            |true                                                     |
     |#tags                           |n                  |               |                            |MaxSoft                                                  |
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



Create a question using a string value as the questionId
--------------------------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name    |Attribute Value To Be Set                                |
     |--------------------------------|-------------------|---------------|----------------------------|---------------------------------------------------------|
     |#creatorId                      |n                  |               |                            |osanda12                                                 |
     |#creatorPlatform                |n                  |               |                            |Web                                                      |
     |#creatoredSource                |n                  |               |                            |App                                                      |
     |#creatoredType                  |n                  |               |                            |Manual                                                   |
     |#deckId                         |y                  |scenario       |deckId                      |                                                         |
     |#kind                           |n                  |               |                            |ALL                                                      |
     |#isDeleted                      |n                  |               |                            |false                                                    |
     |#tempQuestionId                 |n                  |               |                            |testId                                                   |
     |#learningObjectives             |n                  |               |                            |learningObjective1                                       |
     |#imageUrl                       |n                  |               |                            |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |n                  |               |                            |TEXT                                                     |
     |#questionPrompt                 |n                  |               |                            |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |n                  |               |                            |TEXT                                                     |
     |#timeout                        |n                  |               |                            |60                                                       |
     |#rationale                      |n                  |               |                            |rationale                                                |
     |#boxId                          |n                  |               |                            |0                                                        |
     |#correctAttempts                |n                  |               |                            |1                                                        |
     |#inCorrectAttempts              |n                  |               |                            |0                                                        |
     |#lastAswered                    |n                  |               |                            |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |n                  |               |                            |0                                                        |
     |#skips                          |n                  |               |                            |a                                                        |
     |#userId                         |n                  |               |                            |0                                                        |
     |#correctAnswerList              |n                  |               |                            |1,2                                                      |
     |#answer1Id                      |n                  |               |                            |1                                                        |
     |#answer1Value                   |n                  |               |                            |Osanda                                                   |
     |#answer1Type                    |n                  |               |                            |TEXT                                                     |
     |#answer1CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer2Id                      |n                  |               |                            |2                                                        |
     |#answer2Value                   |n                  |               |                            |Gemunu                                                   |
     |#answer2Type                    |n                  |               |                            |TEXT                                                     |
     |#answer2CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer3Id                      |n                  |               |                            |3                                                        |
     |#answer3Value                   |n                  |               |                            |Eranga                                                   |
     |#answer3Type                    |n                  |               |                            |TEXT                                                     |
     |#answer3CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer4Id                      |n                  |               |                            |4                                                        |
     |#answer4Value                   |n                  |               |                            |Heshan                                                   |
     |#answer4Type                    |n                  |               |                            |TEXT                                                     |
     |#answer4CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer5Id                      |n                  |               |                            |5                                                        |
     |#answer5Value                   |n                  |               |                            |Thilina                                                  |
     |#answer5Type                    |n                  |               |                            |TEXT                                                     |
     |#answer5CaseSensitive           |n                  |               |                            |true                                                     |
     |#tags                           |n                  |               |                            |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.description                             |null                                                     |
     |$.fieldErrors                             |null                                                     |



Create a question using a special characters value as the questionId
--------------------------------------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name    |Attribute Value To Be Set                                |
     |--------------------------------|-------------------|---------------|----------------------------|---------------------------------------------------------|
     |#creatorId                      |n                  |               |                            |osanda12                                                 |
     |#creatorPlatform                |n                  |               |                            |Web                                                      |
     |#creatoredSource                |n                  |               |                            |App                                                      |
     |#creatoredType                  |n                  |               |                            |Manual                                                   |
     |#deckId                         |y                  |scenario       |deckId                      |                                                         |
     |#kind                           |n                  |               |                            |ALL                                                      |
     |#isDeleted                      |n                  |               |                            |false                                                    |
     |#tempQuestionId                 |n                  |               |                            |testId                                                   |
     |#learningObjectives             |n                  |               |                            |learningObjective1                                       |
     |#imageUrl                       |n                  |               |                            |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |n                  |               |                            |TEXT                                                     |
     |#questionPrompt                 |n                  |               |                            |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |n                  |               |                            |TEXT                                                     |
     |#timeout                        |n                  |               |                            |60                                                       |
     |#rationale                      |n                  |               |                            |rationale                                                |
     |#boxId                          |n                  |               |                            |0                                                        |
     |#correctAttempts                |n                  |               |                            |1                                                        |
     |#inCorrectAttempts              |n                  |               |                            |0                                                        |
     |#lastAswered                    |n                  |               |                            |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |n                  |               |                            |0                                                        |
     |#skips                          |n                  |               |                            |@                                                        |
     |#userId                         |n                  |               |                            |0                                                        |
     |#correctAnswerList              |n                  |               |                            |1,2                                                      |
     |#answer1Id                      |n                  |               |                            |1                                                        |
     |#answer1Value                   |n                  |               |                            |Osanda                                                   |
     |#answer1Type                    |n                  |               |                            |TEXT                                                     |
     |#answer1CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer2Id                      |n                  |               |                            |2                                                        |
     |#answer2Value                   |n                  |               |                            |Gemunu                                                   |
     |#answer2Type                    |n                  |               |                            |TEXT                                                     |
     |#answer2CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer3Id                      |n                  |               |                            |3                                                        |
     |#answer3Value                   |n                  |               |                            |Eranga                                                   |
     |#answer3Type                    |n                  |               |                            |TEXT                                                     |
     |#answer3CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer4Id                      |n                  |               |                            |4                                                        |
     |#answer4Value                   |n                  |               |                            |Heshan                                                   |
     |#answer4Type                    |n                  |               |                            |TEXT                                                     |
     |#answer4CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer5Id                      |n                  |               |                            |5                                                        |
     |#answer5Value                   |n                  |               |                            |Thilina                                                  |
     |#answer5Type                    |n                  |               |                            |TEXT                                                     |
     |#answer5CaseSensitive           |n                  |               |                            |true                                                     |
     |#tags                           |n                  |               |                            |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.description                             |null                                                     |
     |$.fieldErrors                             |null                                                     |



Create a question using an empty value as the questionId
--------------------------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name    |Attribute Value To Be Set                                |
     |--------------------------------|-------------------|---------------|----------------------------|---------------------------------------------------------|
     |#creatorId                      |n                  |               |                            |osanda12                                                 |
     |#creatorPlatform                |n                  |               |                            |Web                                                      |
     |#creatoredSource                |n                  |               |                            |App                                                      |
     |#creatoredType                  |n                  |               |                            |Manual                                                   |
     |#deckId                         |y                  |scenario       |deckId                      |                                                         |
     |#kind                           |n                  |               |                            |ALL                                                      |
     |#isDeleted                      |n                  |               |                            |false                                                    |
     |#tempQuestionId                 |n                  |               |                            |testId                                                   |
     |#learningObjectives             |n                  |               |                            |learningObjective1                                       |
     |#imageUrl                       |n                  |               |                            |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |n                  |               |                            |TEXT                                                     |
     |#questionPrompt                 |n                  |               |                            |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |n                  |               |                            |TEXT                                                     |
     |#timeout                        |n                  |               |                            |60                                                       |
     |#rationale                      |n                  |               |                            |rationale                                                |
     |#boxId                          |n                  |               |                            |0                                                        |
     |#correctAttempts                |n                  |               |                            |1                                                        |
     |#inCorrectAttempts              |n                  |               |                            |0                                                        |
     |#lastAswered                    |n                  |               |                            |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |n                  |               |                            |                                                         |
     |#skips                          |n                  |               |                            |0                                                        |
     |#userId                         |n                  |               |                            |0                                                        |
     |#correctAnswerList              |n                  |               |                            |1,2                                                      |
     |#answer1Id                      |n                  |               |                            |1                                                        |
     |#answer1Value                   |n                  |               |                            |Osanda                                                   |
     |#answer1Type                    |n                  |               |                            |TEXT                                                     |
     |#answer1CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer2Id                      |n                  |               |                            |2                                                        |
     |#answer2Value                   |n                  |               |                            |Gemunu                                                   |
     |#answer2Type                    |n                  |               |                            |TEXT                                                     |
     |#answer2CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer3Id                      |n                  |               |                            |3                                                        |
     |#answer3Value                   |n                  |               |                            |Eranga                                                   |
     |#answer3Type                    |n                  |               |                            |TEXT                                                     |
     |#answer3CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer4Id                      |n                  |               |                            |4                                                        |
     |#answer4Value                   |n                  |               |                            |Heshan                                                   |
     |#answer4Type                    |n                  |               |                            |TEXT                                                     |
     |#answer4CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer5Id                      |n                  |               |                            |5                                                        |
     |#answer5Value                   |n                  |               |                            |Thilina                                                  |
     |#answer5Type                    |n                  |               |                            |TEXT                                                     |
     |#answer5CaseSensitive           |n                  |               |                            |true                                                     |
     |#tags                           |n                  |               |                            |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.description                             |null                                                     |
     |$.fieldErrors                             |null                                                     |



Create a question using a negative integer value as the skips
-------------------------------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name    |Attribute Value To Be Set                                |
     |--------------------------------|-------------------|---------------|----------------------------|---------------------------------------------------------|
     |#creatorId                      |n                  |               |                            |osanda12                                                 |
     |#creatorPlatform                |n                  |               |                            |Web                                                      |
     |#creatoredSource                |n                  |               |                            |App                                                      |
     |#creatoredType                  |n                  |               |                            |Manual                                                   |
     |#deckId                         |y                  |scenario       |deckId                      |                                                         |
     |#kind                           |n                  |               |                            |ALL                                                      |
     |#isDeleted                      |n                  |               |                            |false                                                    |
     |#tempQuestionId                 |n                  |               |                            |testId                                                   |
     |#learningObjectives             |n                  |               |                            |learningObjective1                                       |
     |#imageUrl                       |n                  |               |                            |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |n                  |               |                            |TEXT                                                     |
     |#questionPrompt                 |n                  |               |                            |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |n                  |               |                            |TEXT                                                     |
     |#timeout                        |n                  |               |                            |60                                                       |
     |#rationale                      |n                  |               |                            |rationale                                                |
     |#boxId                          |n                  |               |                            |0                                                        |
     |#correctAttempts                |n                  |               |                            |1                                                        |
     |#inCorrectAttempts              |n                  |               |                            |0                                                        |
     |#lastAswered                    |n                  |               |                            |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |n                  |               |                            |0                                                        |
     |#skips                          |n                  |               |                            |-2                                                        |
     |#userId                         |n                  |               |                            |0                                                        |
     |#correctAnswerList              |n                  |               |                            |1,2                                                      |
     |#answer1Id                      |n                  |               |                            |1                                                        |
     |#answer1Value                   |n                  |               |                            |Osanda                                                   |
     |#answer1Type                    |n                  |               |                            |TEXT                                                     |
     |#answer1CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer2Id                      |n                  |               |                            |2                                                        |
     |#answer2Value                   |n                  |               |                            |Gemunu                                                   |
     |#answer2Type                    |n                  |               |                            |TEXT                                                     |
     |#answer2CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer3Id                      |n                  |               |                            |3                                                        |
     |#answer3Value                   |n                  |               |                            |Eranga                                                   |
     |#answer3Type                    |n                  |               |                            |TEXT                                                     |
     |#answer3CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer4Id                      |n                  |               |                            |4                                                        |
     |#answer4Value                   |n                  |               |                            |Heshan                                                   |
     |#answer4Type                    |n                  |               |                            |TEXT                                                     |
     |#answer4CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer5Id                      |n                  |               |                            |5                                                        |
     |#answer5Value                   |n                  |               |                            |Thilina                                                  |
     |#answer5Type                    |n                  |               |                            |TEXT                                                     |
     |#answer5CaseSensitive           |n                  |               |                            |true                                                     |
     |#tags                           |n                  |               |                            |MaxSoft                                                  |
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



Create a question using a special characters value as the skips
---------------------------------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name    |Attribute Value To Be Set                                |
     |--------------------------------|-------------------|---------------|----------------------------|---------------------------------------------------------|
     |#creatorId                      |n                  |               |                            |osanda12                                                 |
     |#creatorPlatform                |n                  |               |                            |Web                                                      |
     |#creatoredSource                |n                  |               |                            |App                                                      |
     |#creatoredType                  |n                  |               |                            |Manual                                                   |
     |#deckId                         |y                  |scenario       |deckId                      |                                                         |
     |#kind                           |n                  |               |                            |ALL                                                      |
     |#isDeleted                      |n                  |               |                            |false                                                    |
     |#tempQuestionId                 |n                  |               |                            |testId                                                   |
     |#learningObjectives             |n                  |               |                            |learningObjective1                                       |
     |#imageUrl                       |n                  |               |                            |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |n                  |               |                            |TEXT                                                     |
     |#questionPrompt                 |n                  |               |                            |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |n                  |               |                            |TEXT                                                     |
     |#timeout                        |n                  |               |                            |60                                                       |
     |#rationale                      |n                  |               |                            |rationale                                                |
     |#boxId                          |n                  |               |                            |0                                                        |
     |#correctAttempts                |n                  |               |                            |1                                                        |
     |#inCorrectAttempts              |n                  |               |                            |0                                                        |
     |#lastAswered                    |n                  |               |                            |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |n                  |               |                            |0                                                        |
     |#skips                          |n                  |               |                            |@                                                        |
     |#userId                         |n                  |               |                            |0                                                        |
     |#correctAnswerList              |n                  |               |                            |1,2                                                      |
     |#answer1Id                      |n                  |               |                            |1                                                        |
     |#answer1Value                   |n                  |               |                            |Osanda                                                   |
     |#answer1Type                    |n                  |               |                            |TEXT                                                     |
     |#answer1CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer2Id                      |n                  |               |                            |2                                                        |
     |#answer2Value                   |n                  |               |                            |Gemunu                                                   |
     |#answer2Type                    |n                  |               |                            |TEXT                                                     |
     |#answer2CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer3Id                      |n                  |               |                            |3                                                        |
     |#answer3Value                   |n                  |               |                            |Eranga                                                   |
     |#answer3Type                    |n                  |               |                            |TEXT                                                     |
     |#answer3CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer4Id                      |n                  |               |                            |4                                                        |
     |#answer4Value                   |n                  |               |                            |Heshan                                                   |
     |#answer4Type                    |n                  |               |                            |TEXT                                                     |
     |#answer4CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer5Id                      |n                  |               |                            |5                                                        |
     |#answer5Value                   |n                  |               |                            |Thilina                                                  |
     |#answer5Type                    |n                  |               |                            |TEXT                                                     |
     |#answer5CaseSensitive           |n                  |               |                            |true                                                     |
     |#tags                           |n                  |               |                            |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.description                             |null                                                     |
     |$.fieldErrors                             |null                                                     |



Create a question using a string value as the skips
---------------------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name    |Attribute Value To Be Set                                |
     |--------------------------------|-------------------|---------------|----------------------------|---------------------------------------------------------|
     |#creatorId                      |n                  |               |                            |osanda12                                                 |
     |#creatorPlatform                |n                  |               |                            |Web                                                      |
     |#creatoredSource                |n                  |               |                            |App                                                      |
     |#creatoredType                  |n                  |               |                            |Manual                                                   |
     |#deckId                         |y                  |scenario       |deckId                      |                                                         |
     |#kind                           |n                  |               |                            |ALL                                                      |
     |#isDeleted                      |n                  |               |                            |false                                                    |
     |#tempQuestionId                 |n                  |               |                            |testId                                                   |
     |#learningObjectives             |n                  |               |                            |learningObjective1                                       |
     |#imageUrl                       |n                  |               |                            |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |n                  |               |                            |TEXT                                                     |
     |#questionPrompt                 |n                  |               |                            |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |n                  |               |                            |TEXT                                                     |
     |#timeout                        |n                  |               |                            |60                                                       |
     |#rationale                      |n                  |               |                            |rationale                                                |
     |#boxId                          |n                  |               |                            |0                                                        |
     |#correctAttempts                |n                  |               |                            |1                                                        |
     |#inCorrectAttempts              |n                  |               |                            |0                                                        |
     |#lastAswered                    |n                  |               |                            |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |n                  |               |                            |0                                                        |
     |#skips                          |n                  |               |                            |a                                                        |
     |#userId                         |n                  |               |                            |0                                                        |
     |#correctAnswerList              |n                  |               |                            |1,2                                                      |
     |#answer1Id                      |n                  |               |                            |1                                                        |
     |#answer1Value                   |n                  |               |                            |Osanda                                                   |
     |#answer1Type                    |n                  |               |                            |TEXT                                                     |
     |#answer1CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer2Id                      |n                  |               |                            |2                                                        |
     |#answer2Value                   |n                  |               |                            |Gemunu                                                   |
     |#answer2Type                    |n                  |               |                            |TEXT                                                     |
     |#answer2CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer3Id                      |n                  |               |                            |3                                                        |
     |#answer3Value                   |n                  |               |                            |Eranga                                                   |
     |#answer3Type                    |n                  |               |                            |TEXT                                                     |
     |#answer3CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer4Id                      |n                  |               |                            |4                                                        |
     |#answer4Value                   |n                  |               |                            |Heshan                                                   |
     |#answer4Type                    |n                  |               |                            |TEXT                                                     |
     |#answer4CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer5Id                      |n                  |               |                            |5                                                        |
     |#answer5Value                   |n                  |               |                            |Thilina                                                  |
     |#answer5Type                    |n                  |               |                            |TEXT                                                     |
     |#answer5CaseSensitive           |n                  |               |                            |true                                                     |
     |#tags                           |n                  |               |                            |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.description                             |null                                                     |
     |$.fieldErrors                             |null                                                     |



Create a question using an empty value as the skips
---------------------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name    |Attribute Value To Be Set                                |
     |--------------------------------|-------------------|---------------|----------------------------|---------------------------------------------------------|
     |#creatorId                      |n                  |               |                            |osanda12                                                 |
     |#creatorPlatform                |n                  |               |                            |Web                                                      |
     |#creatoredSource                |n                  |               |                            |App                                                      |
     |#creatoredType                  |n                  |               |                            |Manual                                                   |
     |#deckId                         |y                  |scenario       |deckId                      |                                                         |
     |#kind                           |n                  |               |                            |ALL                                                      |
     |#isDeleted                      |n                  |               |                            |false                                                    |
     |#tempQuestionId                 |n                  |               |                            |testId                                                   |
     |#learningObjectives             |n                  |               |                            |learningObjective1                                       |
     |#imageUrl                       |n                  |               |                            |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |n                  |               |                            |TEXT                                                     |
     |#questionPrompt                 |n                  |               |                            |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |n                  |               |                            |TEXT                                                     |
     |#timeout                        |n                  |               |                            |60                                                       |
     |#rationale                      |n                  |               |                            |rationale                                                |
     |#boxId                          |n                  |               |                            |0                                                        |
     |#correctAttempts                |n                  |               |                            |1                                                        |
     |#inCorrectAttempts              |n                  |               |                            |0                                                        |
     |#lastAswered                    |n                  |               |                            |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |n                  |               |                            |0                                                        |
     |#skips                          |n                  |               |                            |                                                         |
     |#userId                         |n                  |               |                            |0                                                        |
     |#correctAnswerList              |n                  |               |                            |1,2                                                      |
     |#answer1Id                      |n                  |               |                            |1                                                        |
     |#answer1Value                   |n                  |               |                            |Osanda                                                   |
     |#answer1Type                    |n                  |               |                            |TEXT                                                     |
     |#answer1CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer2Id                      |n                  |               |                            |2                                                        |
     |#answer2Value                   |n                  |               |                            |Gemunu                                                   |
     |#answer2Type                    |n                  |               |                            |TEXT                                                     |
     |#answer2CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer3Id                      |n                  |               |                            |3                                                        |
     |#answer3Value                   |n                  |               |                            |Eranga                                                   |
     |#answer3Type                    |n                  |               |                            |TEXT                                                     |
     |#answer3CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer4Id                      |n                  |               |                            |4                                                        |
     |#answer4Value                   |n                  |               |                            |Heshan                                                   |
     |#answer4Type                    |n                  |               |                            |TEXT                                                     |
     |#answer4CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer5Id                      |n                  |               |                            |5                                                        |
     |#answer5Value                   |n                  |               |                            |Thilina                                                  |
     |#answer5Type                    |n                  |               |                            |TEXT                                                     |
     |#answer5CaseSensitive           |n                  |               |                            |true                                                     |
     |#tags                           |n                  |               |                            |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.description                             |null                                                     |
     |$.fieldErrors                             |null                                                     |



Create a question using a negative integer value as the userId
--------------------------------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name    |Attribute Value To Be Set                                |
     |--------------------------------|-------------------|---------------|----------------------------|---------------------------------------------------------|
     |#creatorId                      |n                  |               |                            |osanda12                                                 |
     |#creatorPlatform                |n                  |               |                            |Web                                                      |
     |#creatoredSource                |n                  |               |                            |App                                                      |
     |#creatoredType                  |n                  |               |                            |Manual                                                   |
     |#deckId                         |y                  |scenario       |deckId                      |                                                         |
     |#kind                           |n                  |               |                            |ALL                                                      |
     |#isDeleted                      |n                  |               |                            |false                                                    |
     |#tempQuestionId                 |n                  |               |                            |testId                                                   |
     |#learningObjectives             |n                  |               |                            |learningObjective1                                       |
     |#imageUrl                       |n                  |               |                            |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |n                  |               |                            |TEXT                                                     |
     |#questionPrompt                 |n                  |               |                            |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |n                  |               |                            |TEXT                                                     |
     |#timeout                        |n                  |               |                            |60                                                       |
     |#rationale                      |n                  |               |                            |rationale                                                |
     |#boxId                          |n                  |               |                            |0                                                        |
     |#correctAttempts                |n                  |               |                            |1                                                        |
     |#inCorrectAttempts              |n                  |               |                            |0                                                        |
     |#lastAswered                    |n                  |               |                            |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |n                  |               |                            |0                                                        |
     |#skips                          |n                  |               |                            |0                                                        |
     |#userId                         |n                  |               |                            |-2                                                       |
     |#correctAnswerList              |n                  |               |                            |1,2                                                      |
     |#answer1Id                      |n                  |               |                            |1                                                        |
     |#answer1Value                   |n                  |               |                            |Osanda                                                   |
     |#answer1Type                    |n                  |               |                            |TEXT                                                     |
     |#answer1CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer2Id                      |n                  |               |                            |2                                                        |
     |#answer2Value                   |n                  |               |                            |Gemunu                                                   |
     |#answer2Type                    |n                  |               |                            |TEXT                                                     |
     |#answer2CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer3Id                      |n                  |               |                            |3                                                        |
     |#answer3Value                   |n                  |               |                            |Eranga                                                   |
     |#answer3Type                    |n                  |               |                            |TEXT                                                     |
     |#answer3CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer4Id                      |n                  |               |                            |4                                                        |
     |#answer4Value                   |n                  |               |                            |Heshan                                                   |
     |#answer4Type                    |n                  |               |                            |TEXT                                                     |
     |#answer4CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer5Id                      |n                  |               |                            |5                                                        |
     |#answer5Value                   |n                  |               |                            |Thilina                                                  |
     |#answer5Type                    |n                  |               |                            |TEXT                                                     |
     |#answer5CaseSensitive           |n                  |               |                            |true                                                     |
     |#tags                           |n                  |               |                            |MaxSoft                                                  |
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



Create a question using a string value as the userId
----------------------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name    |Attribute Value To Be Set                                |
     |--------------------------------|-------------------|---------------|----------------------------|---------------------------------------------------------|
     |#creatorId                      |n                  |               |                            |osanda12                                                 |
     |#creatorPlatform                |n                  |               |                            |Web                                                      |
     |#creatoredSource                |n                  |               |                            |App                                                      |
     |#creatoredType                  |n                  |               |                            |Manual                                                   |
     |#deckId                         |y                  |scenario       |deckId                      |                                                         |
     |#kind                           |n                  |               |                            |ALL                                                      |
     |#isDeleted                      |n                  |               |                            |false                                                    |
     |#tempQuestionId                 |n                  |               |                            |testId                                                   |
     |#learningObjectives             |n                  |               |                            |learningObjective1                                       |
     |#imageUrl                       |n                  |               |                            |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |n                  |               |                            |TEXT                                                     |
     |#questionPrompt                 |n                  |               |                            |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |n                  |               |                            |TEXT                                                     |
     |#timeout                        |n                  |               |                            |60                                                       |
     |#rationale                      |n                  |               |                            |rationale                                                |
     |#boxId                          |n                  |               |                            |0                                                        |
     |#correctAttempts                |n                  |               |                            |1                                                        |
     |#inCorrectAttempts              |n                  |               |                            |0                                                        |
     |#lastAswered                    |n                  |               |                            |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |n                  |               |                            |0                                                        |
     |#skips                          |n                  |               |                            |0                                                        |
     |#userId                         |n                  |               |                            |abc                                                      |
     |#correctAnswerList              |n                  |               |                            |1,2                                                      |
     |#answer1Id                      |n                  |               |                            |1                                                        |
     |#answer1Value                   |n                  |               |                            |Osanda                                                   |
     |#answer1Type                    |n                  |               |                            |TEXT                                                     |
     |#answer1CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer2Id                      |n                  |               |                            |2                                                        |
     |#answer2Value                   |n                  |               |                            |Gemunu                                                   |
     |#answer2Type                    |n                  |               |                            |TEXT                                                     |
     |#answer2CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer3Id                      |n                  |               |                            |3                                                        |
     |#answer3Value                   |n                  |               |                            |Eranga                                                   |
     |#answer3Type                    |n                  |               |                            |TEXT                                                     |
     |#answer3CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer4Id                      |n                  |               |                            |4                                                        |
     |#answer4Value                   |n                  |               |                            |Heshan                                                   |
     |#answer4Type                    |n                  |               |                            |TEXT                                                     |
     |#answer4CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer5Id                      |n                  |               |                            |5                                                        |
     |#answer5Value                   |n                  |               |                            |Thilina                                                  |
     |#answer5Type                    |n                  |               |                            |TEXT                                                     |
     |#answer5CaseSensitive           |n                  |               |                            |true                                                     |
     |#tags                           |n                  |               |                            |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.description                             |null                                                     |
     |$.fieldErrors                             |null                                                     |



Create a question using a special character as the userId
---------------------------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name    |Attribute Value To Be Set                                |
     |--------------------------------|-------------------|---------------|----------------------------|---------------------------------------------------------|
     |#creatorId                      |n                  |               |                            |osanda12                                                 |
     |#creatorPlatform                |n                  |               |                            |Web                                                      |
     |#creatoredSource                |n                  |               |                            |App                                                      |
     |#creatoredType                  |n                  |               |                            |Manual                                                   |
     |#deckId                         |y                  |scenario       |deckId                      |                                                         |
     |#kind                           |n                  |               |                            |ALL                                                      |
     |#isDeleted                      |n                  |               |                            |false                                                    |
     |#tempQuestionId                 |n                  |               |                            |testId                                                   |
     |#learningObjectives             |n                  |               |                            |learningObjective1                                       |
     |#imageUrl                       |n                  |               |                            |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |n                  |               |                            |TEXT                                                     |
     |#questionPrompt                 |n                  |               |                            |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |n                  |               |                            |TEXT                                                     |
     |#timeout                        |n                  |               |                            |60                                                       |
     |#rationale                      |n                  |               |                            |rationale                                                |
     |#boxId                          |n                  |               |                            |0                                                        |
     |#correctAttempts                |n                  |               |                            |1                                                        |
     |#inCorrectAttempts              |n                  |               |                            |0                                                        |
     |#lastAswered                    |n                  |               |                            |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |n                  |               |                            |0                                                        |
     |#skips                          |n                  |               |                            |0                                                        |
     |#userId                         |n                  |               |                            |@                                                        |
     |#correctAnswerList              |n                  |               |                            |1,2                                                      |
     |#answer1Id                      |n                  |               |                            |1                                                        |
     |#answer1Value                   |n                  |               |                            |Osanda                                                   |
     |#answer1Type                    |n                  |               |                            |TEXT                                                     |
     |#answer1CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer2Id                      |n                  |               |                            |2                                                        |
     |#answer2Value                   |n                  |               |                            |Gemunu                                                   |
     |#answer2Type                    |n                  |               |                            |TEXT                                                     |
     |#answer2CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer3Id                      |n                  |               |                            |3                                                        |
     |#answer3Value                   |n                  |               |                            |Eranga                                                   |
     |#answer3Type                    |n                  |               |                            |TEXT                                                     |
     |#answer3CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer4Id                      |n                  |               |                            |4                                                        |
     |#answer4Value                   |n                  |               |                            |Heshan                                                   |
     |#answer4Type                    |n                  |               |                            |TEXT                                                     |
     |#answer4CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer5Id                      |n                  |               |                            |5                                                        |
     |#answer5Value                   |n                  |               |                            |Thilina                                                  |
     |#answer5Type                    |n                  |               |                            |TEXT                                                     |
     |#answer5CaseSensitive           |n                  |               |                            |true                                                     |
     |#tags                           |n                  |               |                            |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.description                             |null                                                     |
     |$.fieldErrors                             |null                                                     |



Create a question using an empty value as the userId
----------------------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name    |Attribute Value To Be Set                                |
     |--------------------------------|-------------------|---------------|----------------------------|---------------------------------------------------------|
     |#creatorId                      |n                  |               |                            |osanda12                                                 |
     |#creatorPlatform                |n                  |               |                            |Web                                                      |
     |#creatoredSource                |n                  |               |                            |App                                                      |
     |#creatoredType                  |n                  |               |                            |Manual                                                   |
     |#deckId                         |y                  |scenario       |deckId                      |                                                         |
     |#kind                           |n                  |               |                            |ALL                                                      |
     |#isDeleted                      |n                  |               |                            |false                                                    |
     |#tempQuestionId                 |n                  |               |                            |testId                                                   |
     |#learningObjectives             |n                  |               |                            |learningObjective1                                       |
     |#imageUrl                       |n                  |               |                            |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |n                  |               |                            |TEXT                                                     |
     |#questionPrompt                 |n                  |               |                            |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |n                  |               |                            |TEXT                                                     |
     |#timeout                        |n                  |               |                            |60                                                       |
     |#rationale                      |n                  |               |                            |rationale                                                |
     |#boxId                          |n                  |               |                            |0                                                        |
     |#correctAttempts                |n                  |               |                            |1                                                        |
     |#inCorrectAttempts              |n                  |               |                            |0                                                        |
     |#lastAswered                    |n                  |               |                            |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |n                  |               |                            |0                                                        |
     |#skips                          |n                  |               |                            |0                                                        |
     |#userId                         |n                  |               |                            |                                                         |
     |#correctAnswerList              |n                  |               |                            |1,2                                                      |
     |#answer1Id                      |n                  |               |                            |1                                                        |
     |#answer1Value                   |n                  |               |                            |Osanda                                                   |
     |#answer1Type                    |n                  |               |                            |TEXT                                                     |
     |#answer1CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer2Id                      |n                  |               |                            |2                                                        |
     |#answer2Value                   |n                  |               |                            |Gemunu                                                   |
     |#answer2Type                    |n                  |               |                            |TEXT                                                     |
     |#answer2CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer3Id                      |n                  |               |                            |3                                                        |
     |#answer3Value                   |n                  |               |                            |Eranga                                                   |
     |#answer3Type                    |n                  |               |                            |TEXT                                                     |
     |#answer3CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer4Id                      |n                  |               |                            |4                                                        |
     |#answer4Value                   |n                  |               |                            |Heshan                                                   |
     |#answer4Type                    |n                  |               |                            |TEXT                                                     |
     |#answer4CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer5Id                      |n                  |               |                            |5                                                        |
     |#answer5Value                   |n                  |               |                            |Thilina                                                  |
     |#answer5Type                    |n                  |               |                            |TEXT                                                     |
     |#answer5CaseSensitive           |n                  |               |                            |true                                                     |
     |#tags                           |n                  |               |                            |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.description                             |null                                                     |
     |$.fieldErrors                             |null                                                     |



Create a question using a string value as the correctAnswerList
---------------------------------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name    |Attribute Value To Be Set                                |
     |--------------------------------|-------------------|---------------|----------------------------|---------------------------------------------------------|
     |#creatorId                      |n                  |               |                            |osanda12                                                 |
     |#creatorPlatform                |n                  |               |                            |Web                                                      |
     |#creatoredSource                |n                  |               |                            |App                                                      |
     |#creatoredType                  |n                  |               |                            |Manual                                                   |
     |#deckId                         |y                  |scenario       |deckId                      |                                                         |
     |#kind                           |n                  |               |                            |ALL                                                      |
     |#isDeleted                      |n                  |               |                            |false                                                    |
     |#tempQuestionId                 |n                  |               |                            |testId                                                   |
     |#learningObjectives             |n                  |               |                            |learningObjective1                                       |
     |#imageUrl                       |n                  |               |                            |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |n                  |               |                            |TEXT                                                     |
     |#questionPrompt                 |n                  |               |                            |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |n                  |               |                            |TEXT                                                     |
     |#timeout                        |n                  |               |                            |60                                                       |
     |#rationale                      |n                  |               |                            |rationale                                                |
     |#boxId                          |n                  |               |                            |0                                                        |
     |#correctAttempts                |n                  |               |                            |1                                                        |
     |#inCorrectAttempts              |n                  |               |                            |0                                                        |
     |#lastAswered                    |n                  |               |                            |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |n                  |               |                            |0                                                        |
     |#skips                          |n                  |               |                            |0                                                        |
     |#userId                         |n                  |               |                            |0                                                        |
     |#correctAnswerList              |n                  |               |                            |abc                                                      |
     |#answer1Id                      |n                  |               |                            |1                                                        |
     |#answer1Value                   |n                  |               |                            |Osanda                                                   |
     |#answer1Type                    |n                  |               |                            |TEXT                                                     |
     |#answer1CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer2Id                      |n                  |               |                            |2                                                        |
     |#answer2Value                   |n                  |               |                            |Gemunu                                                   |
     |#answer2Type                    |n                  |               |                            |TEXT                                                     |
     |#answer2CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer3Id                      |n                  |               |                            |3                                                        |
     |#answer3Value                   |n                  |               |                            |Eranga                                                   |
     |#answer3Type                    |n                  |               |                            |TEXT                                                     |
     |#answer3CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer4Id                      |n                  |               |                            |4                                                        |
     |#answer4Value                   |n                  |               |                            |Heshan                                                   |
     |#answer4Type                    |n                  |               |                            |TEXT                                                     |
     |#answer4CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer5Id                      |n                  |               |                            |5                                                        |
     |#answer5Value                   |n                  |               |                            |Thilina                                                  |
     |#answer5Type                    |n                  |               |                            |TEXT                                                     |
     |#answer5CaseSensitive           |n                  |               |                            |true                                                     |
     |#tags                           |n                  |               |                            |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.description                             |null                                                     |
     |$.fieldErrors                             |null                                                     |



Create a question using a special character as the correctAnswerList
--------------------------------------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name    |Attribute Value To Be Set                                |
     |--------------------------------|-------------------|---------------|----------------------------|---------------------------------------------------------|
     |#creatorId                      |n                  |               |                            |osanda12                                                 |
     |#creatorPlatform                |n                  |               |                            |Web                                                      |
     |#creatoredSource                |n                  |               |                            |App                                                      |
     |#creatoredType                  |n                  |               |                            |Manual                                                   |
     |#deckId                         |y                  |scenario       |deckId                      |                                                         |
     |#kind                           |n                  |               |                            |ALL                                                      |
     |#isDeleted                      |n                  |               |                            |false                                                    |
     |#tempQuestionId                 |n                  |               |                            |testId                                                   |
     |#learningObjectives             |n                  |               |                            |learningObjective1                                       |
     |#imageUrl                       |n                  |               |                            |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |n                  |               |                            |TEXT                                                     |
     |#questionPrompt                 |n                  |               |                            |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |n                  |               |                            |TEXT                                                     |
     |#timeout                        |n                  |               |                            |60                                                       |
     |#rationale                      |n                  |               |                            |rationale                                                |
     |#boxId                          |n                  |               |                            |0                                                        |
     |#correctAttempts                |n                  |               |                            |1                                                        |
     |#inCorrectAttempts              |n                  |               |                            |0                                                        |
     |#lastAswered                    |n                  |               |                            |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |n                  |               |                            |0                                                        |
     |#skips                          |n                  |               |                            |0                                                        |
     |#userId                         |n                  |               |                            |0                                                        |
     |#correctAnswerList              |n                  |               |                            |@                                                        |
     |#answer1Id                      |n                  |               |                            |1                                                        |
     |#answer1Value                   |n                  |               |                            |Osanda                                                   |
     |#answer1Type                    |n                  |               |                            |TEXT                                                     |
     |#answer1CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer2Id                      |n                  |               |                            |2                                                        |
     |#answer2Value                   |n                  |               |                            |Gemunu                                                   |
     |#answer2Type                    |n                  |               |                            |TEXT                                                     |
     |#answer2CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer3Id                      |n                  |               |                            |3                                                        |
     |#answer3Value                   |n                  |               |                            |Eranga                                                   |
     |#answer3Type                    |n                  |               |                            |TEXT                                                     |
     |#answer3CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer4Id                      |n                  |               |                            |4                                                        |
     |#answer4Value                   |n                  |               |                            |Heshan                                                   |
     |#answer4Type                    |n                  |               |                            |TEXT                                                     |
     |#answer4CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer5Id                      |n                  |               |                            |5                                                        |
     |#answer5Value                   |n                  |               |                            |Thilina                                                  |
     |#answer5Type                    |n                  |               |                            |TEXT                                                     |
     |#answer5CaseSensitive           |n                  |               |                            |true                                                     |
     |#tags                           |n                  |               |                            |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.description                             |null                                                     |
     |$.fieldErrors                             |null                                                     |



Create a question using an empty value as the correctAnswerList
---------------------------------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name    |Attribute Value To Be Set                                |
     |--------------------------------|-------------------|---------------|----------------------------|---------------------------------------------------------|
     |#creatorId                      |n                  |               |                            |osanda12                                                 |
     |#creatorPlatform                |n                  |               |                            |Web                                                      |
     |#creatoredSource                |n                  |               |                            |App                                                      |
     |#creatoredType                  |n                  |               |                            |Manual                                                   |
     |#deckId                         |y                  |scenario       |deckId                      |                                                         |
     |#kind                           |n                  |               |                            |ALL                                                      |
     |#isDeleted                      |n                  |               |                            |false                                                    |
     |#tempQuestionId                 |n                  |               |                            |testId                                                   |
     |#learningObjectives             |n                  |               |                            |learningObjective1                                       |
     |#imageUrl                       |n                  |               |                            |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |n                  |               |                            |TEXT                                                     |
     |#questionPrompt                 |n                  |               |                            |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |n                  |               |                            |TEXT                                                     |
     |#timeout                        |n                  |               |                            |60                                                       |
     |#rationale                      |n                  |               |                            |rationale                                                |
     |#boxId                          |n                  |               |                            |0                                                        |
     |#correctAttempts                |n                  |               |                            |1                                                        |
     |#inCorrectAttempts              |n                  |               |                            |0                                                        |
     |#lastAswered                    |n                  |               |                            |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |n                  |               |                            |0                                                        |
     |#skips                          |n                  |               |                            |0                                                        |
     |#userId                         |n                  |               |                            |0                                                        |
     |#correctAnswerList              |n                  |               |                            |                                                         |
     |#answer1Id                      |n                  |               |                            |1                                                        |
     |#answer1Value                   |n                  |               |                            |Osanda                                                   |
     |#answer1Type                    |n                  |               |                            |TEXT                                                     |
     |#answer1CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer2Id                      |n                  |               |                            |2                                                        |
     |#answer2Value                   |n                  |               |                            |Gemunu                                                   |
     |#answer2Type                    |n                  |               |                            |TEXT                                                     |
     |#answer2CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer3Id                      |n                  |               |                            |3                                                        |
     |#answer3Value                   |n                  |               |                            |Eranga                                                   |
     |#answer3Type                    |n                  |               |                            |TEXT                                                     |
     |#answer3CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer4Id                      |n                  |               |                            |4                                                        |
     |#answer4Value                   |n                  |               |                            |Heshan                                                   |
     |#answer4Type                    |n                  |               |                            |TEXT                                                     |
     |#answer4CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer5Id                      |n                  |               |                            |5                                                        |
     |#answer5Value                   |n                  |               |                            |Thilina                                                  |
     |#answer5Type                    |n                  |               |                            |TEXT                                                     |
     |#answer5CaseSensitive           |n                  |               |                            |true                                                     |
     |#tags                           |n                  |               |                            |MaxSoft                                                  |
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



Create a question using an empty string as the correctAnswerList
----------------------------------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name    |Attribute Value To Be Set                                |
     |--------------------------------|-------------------|---------------|----------------------------|---------------------------------------------------------|
     |#creatorId                      |n                  |               |                            |osanda12                                                 |
     |#creatorPlatform                |n                  |               |                            |Web                                                      |
     |#creatoredSource                |n                  |               |                            |App                                                      |
     |#creatoredType                  |n                  |               |                            |Manual                                                   |
     |#deckId                         |y                  |scenario       |deckId                      |                                                         |
     |#kind                           |n                  |               |                            |ALL                                                      |
     |#isDeleted                      |n                  |               |                            |false                                                    |
     |#tempQuestionId                 |n                  |               |                            |testId                                                   |
     |#learningObjectives             |n                  |               |                            |learningObjective1                                       |
     |#imageUrl                       |n                  |               |                            |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |n                  |               |                            |TEXT                                                     |
     |#questionPrompt                 |n                  |               |                            |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |n                  |               |                            |TEXT                                                     |
     |#timeout                        |n                  |               |                            |60                                                       |
     |#rationale                      |n                  |               |                            |rationale                                                |
     |#boxId                          |n                  |               |                            |0                                                        |
     |#correctAttempts                |n                  |               |                            |1                                                        |
     |#inCorrectAttempts              |n                  |               |                            |0                                                        |
     |#lastAswered                    |n                  |               |                            |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |n                  |               |                            |0                                                        |
     |#skips                          |n                  |               |                            |0                                                        |
     |#userId                         |n                  |               |                            |0                                                        |
     |#correctAnswerList              |n                  |               |                            |""                                                       |
     |#answer1Id                      |n                  |               |                            |1                                                        |
     |#answer1Value                   |n                  |               |                            |Osanda                                                   |
     |#answer1Type                    |n                  |               |                            |TEXT                                                     |
     |#answer1CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer2Id                      |n                  |               |                            |2                                                        |
     |#answer2Value                   |n                  |               |                            |Gemunu                                                   |
     |#answer2Type                    |n                  |               |                            |TEXT                                                     |
     |#answer2CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer3Id                      |n                  |               |                            |3                                                        |
     |#answer3Value                   |n                  |               |                            |Eranga                                                   |
     |#answer3Type                    |n                  |               |                            |TEXT                                                     |
     |#answer3CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer4Id                      |n                  |               |                            |4                                                        |
     |#answer4Value                   |n                  |               |                            |Heshan                                                   |
     |#answer4Type                    |n                  |               |                            |TEXT                                                     |
     |#answer4CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer5Id                      |n                  |               |                            |5                                                        |
     |#answer5Value                   |n                  |               |                            |Thilina                                                  |
     |#answer5Type                    |n                  |               |                            |TEXT                                                     |
     |#answer5CaseSensitive           |n                  |               |                            |true                                                     |
     |#tags                           |n                  |               |                            |MaxSoft                                                  |
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



Create a question using null value as the correctAnswerList
-----------------------------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name    |Attribute Value To Be Set                                |
     |--------------------------------|-------------------|---------------|----------------------------|---------------------------------------------------------|
     |#creatorId                      |n                  |               |                            |osanda12                                                 |
     |#creatorPlatform                |n                  |               |                            |Web                                                      |
     |#creatoredSource                |n                  |               |                            |App                                                      |
     |#creatoredType                  |n                  |               |                            |Manual                                                   |
     |#deckId                         |y                  |scenario       |deckId                      |                                                         |
     |#kind                           |n                  |               |                            |ALL                                                      |
     |#isDeleted                      |n                  |               |                            |false                                                    |
     |#tempQuestionId                 |n                  |               |                            |testId                                                   |
     |#learningObjectives             |n                  |               |                            |learningObjective1                                       |
     |#imageUrl                       |n                  |               |                            |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |n                  |               |                            |TEXT                                                     |
     |#questionPrompt                 |n                  |               |                            |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |n                  |               |                            |TEXT                                                     |
     |#timeout                        |n                  |               |                            |60                                                       |
     |#rationale                      |n                  |               |                            |rationale                                                |
     |#boxId                          |n                  |               |                            |0                                                        |
     |#correctAttempts                |n                  |               |                            |1                                                        |
     |#inCorrectAttempts              |n                  |               |                            |0                                                        |
     |#lastAswered                    |n                  |               |                            |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |n                  |               |                            |0                                                        |
     |#skips                          |n                  |               |                            |0                                                        |
     |#userId                         |n                  |               |                            |0                                                        |
     |#correctAnswerList              |n                  |               |                            |null                                                     |
     |#answer1Id                      |n                  |               |                            |1                                                        |
     |#answer1Value                   |n                  |               |                            |Osanda                                                   |
     |#answer1Type                    |n                  |               |                            |TEXT                                                     |
     |#answer1CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer2Id                      |n                  |               |                            |2                                                        |
     |#answer2Value                   |n                  |               |                            |Gemunu                                                   |
     |#answer2Type                    |n                  |               |                            |TEXT                                                     |
     |#answer2CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer3Id                      |n                  |               |                            |3                                                        |
     |#answer3Value                   |n                  |               |                            |Eranga                                                   |
     |#answer3Type                    |n                  |               |                            |TEXT                                                     |
     |#answer3CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer4Id                      |n                  |               |                            |4                                                        |
     |#answer4Value                   |n                  |               |                            |Heshan                                                   |
     |#answer4Type                    |n                  |               |                            |TEXT                                                     |
     |#answer4CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer5Id                      |n                  |               |                            |5                                                        |
     |#answer5Value                   |n                  |               |                            |Thilina                                                  |
     |#answer5Type                    |n                  |               |                            |TEXT                                                     |
     |#answer5CaseSensitive           |n                  |               |                            |true                                                     |
     |#tags                           |n                  |               |                            |MaxSoft                                                  |
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



Create a question using a string value as the answer1Id
-------------------------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name    |Attribute Value To Be Set                                |
     |--------------------------------|-------------------|---------------|----------------------------|---------------------------------------------------------|
     |#creatorId                      |n                  |               |                            |osanda12                                                 |
     |#creatorPlatform                |n                  |               |                            |Web                                                      |
     |#creatoredSource                |n                  |               |                            |App                                                      |
     |#creatoredType                  |n                  |               |                            |Manual                                                   |
     |#deckId                         |y                  |scenario       |deckId                      |                                                         |
     |#kind                           |n                  |               |                            |ALL                                                      |
     |#isDeleted                      |n                  |               |                            |false                                                    |
     |#tempQuestionId                 |n                  |               |                            |testId                                                   |
     |#learningObjectives             |n                  |               |                            |learningObjective1                                       |
     |#imageUrl                       |n                  |               |                            |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |n                  |               |                            |TEXT                                                     |
     |#questionPrompt                 |n                  |               |                            |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |n                  |               |                            |TEXT                                                     |
     |#timeout                        |n                  |               |                            |60                                                       |
     |#rationale                      |n                  |               |                            |rationale                                                |
     |#boxId                          |n                  |               |                            |0                                                        |
     |#correctAttempts                |n                  |               |                            |1                                                        |
     |#inCorrectAttempts              |n                  |               |                            |0                                                        |
     |#lastAswered                    |n                  |               |                            |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |n                  |               |                            |0                                                        |
     |#skips                          |n                  |               |                            |0                                                        |
     |#userId                         |n                  |               |                            |0                                                        |
     |#correctAnswerList              |n                  |               |                            |1,2                                                      |
     |#answer1Id                      |n                  |               |                            |"a"                                                      |
     |#answer1Value                   |n                  |               |                            |Osanda                                                   |
     |#answer1Type                    |n                  |               |                            |TEXT                                                     |
     |#answer1CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer2Id                      |n                  |               |                            |2                                                        |
     |#answer2Value                   |n                  |               |                            |Gemunu                                                   |
     |#answer2Type                    |n                  |               |                            |TEXT                                                     |
     |#answer2CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer3Id                      |n                  |               |                            |3                                                        |
     |#answer3Value                   |n                  |               |                            |Eranga                                                   |
     |#answer3Type                    |n                  |               |                            |TEXT                                                     |
     |#answer3CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer4Id                      |n                  |               |                            |4                                                        |
     |#answer4Value                   |n                  |               |                            |Heshan                                                   |
     |#answer4Type                    |n                  |               |                            |TEXT                                                     |
     |#answer4CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer5Id                      |n                  |               |                            |5                                                        |
     |#answer5Value                   |n                  |               |                            |Thilina                                                  |
     |#answer5Type                    |n                  |               |                            |TEXT                                                     |
     |#answer5CaseSensitive           |n                  |               |                            |true                                                     |
     |#tags                           |n                  |               |                            |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |answers: Invalid value 'a'                               |
     |$.description                             |null                                                     |
     |$.fieldErrors                             |null                                                     |



Create a question using a special character as the answer1Id
------------------------------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name    |Attribute Value To Be Set                                |
     |--------------------------------|-------------------|---------------|----------------------------|---------------------------------------------------------|
     |#creatorId                      |n                  |               |                            |osanda12                                                 |
     |#creatorPlatform                |n                  |               |                            |Web                                                      |
     |#creatoredSource                |n                  |               |                            |App                                                      |
     |#creatoredType                  |n                  |               |                            |Manual                                                   |
     |#deckId                         |y                  |scenario       |deckId                      |                                                         |
     |#kind                           |n                  |               |                            |ALL                                                      |
     |#isDeleted                      |n                  |               |                            |false                                                    |
     |#tempQuestionId                 |n                  |               |                            |testId                                                   |
     |#learningObjectives             |n                  |               |                            |learningObjective1                                       |
     |#imageUrl                       |n                  |               |                            |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |n                  |               |                            |TEXT                                                     |
     |#questionPrompt                 |n                  |               |                            |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |n                  |               |                            |TEXT                                                     |
     |#timeout                        |n                  |               |                            |60                                                       |
     |#rationale                      |n                  |               |                            |rationale                                                |
     |#boxId                          |n                  |               |                            |0                                                        |
     |#correctAttempts                |n                  |               |                            |1                                                        |
     |#inCorrectAttempts              |n                  |               |                            |0                                                        |
     |#lastAswered                    |n                  |               |                            |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |n                  |               |                            |0                                                        |
     |#skips                          |n                  |               |                            |0                                                        |
     |#userId                         |n                  |               |                            |0                                                        |
     |#correctAnswerList              |n                  |               |                            |1,2                                                      |
     |#answer1Id                      |n                  |               |                            |"@"                                                      |
     |#answer1Value                   |n                  |               |                            |Osanda                                                   |
     |#answer1Type                    |n                  |               |                            |TEXT                                                     |
     |#answer1CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer2Id                      |n                  |               |                            |2                                                        |
     |#answer2Value                   |n                  |               |                            |Gemunu                                                   |
     |#answer2Type                    |n                  |               |                            |TEXT                                                     |
     |#answer2CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer3Id                      |n                  |               |                            |3                                                        |
     |#answer3Value                   |n                  |               |                            |Eranga                                                   |
     |#answer3Type                    |n                  |               |                            |TEXT                                                     |
     |#answer3CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer4Id                      |n                  |               |                            |4                                                        |
     |#answer4Value                   |n                  |               |                            |Heshan                                                   |
     |#answer4Type                    |n                  |               |                            |TEXT                                                     |
     |#answer4CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer5Id                      |n                  |               |                            |5                                                        |
     |#answer5Value                   |n                  |               |                            |Thilina                                                  |
     |#answer5Type                    |n                  |               |                            |TEXT                                                     |
     |#answer5CaseSensitive           |n                  |               |                            |true                                                     |
     |#tags                           |n                  |               |                            |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |answers: Invalid value '@'                               |
     |$.description                             |null                                                     |
     |$.fieldErrors                             |null                                                     |



Create a question using a negative integer value as the answer1Id
-----------------------------------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name    |Attribute Value To Be Set                                |
     |--------------------------------|-------------------|---------------|----------------------------|---------------------------------------------------------|
     |#creatorId                      |n                  |               |                            |osanda12                                                 |
     |#creatorPlatform                |n                  |               |                            |Web                                                      |
     |#creatoredSource                |n                  |               |                            |App                                                      |
     |#creatoredType                  |n                  |               |                            |Manual                                                   |
     |#deckId                         |y                  |scenario       |deckId                      |                                                         |
     |#kind                           |n                  |               |                            |ALL                                                      |
     |#isDeleted                      |n                  |               |                            |false                                                    |
     |#tempQuestionId                 |n                  |               |                            |testId                                                   |
     |#learningObjectives             |n                  |               |                            |learningObjective1                                       |
     |#imageUrl                       |n                  |               |                            |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |n                  |               |                            |TEXT                                                     |
     |#questionPrompt                 |n                  |               |                            |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |n                  |               |                            |TEXT                                                     |
     |#timeout                        |n                  |               |                            |60                                                       |
     |#rationale                      |n                  |               |                            |rationale                                                |
     |#boxId                          |n                  |               |                            |0                                                        |
     |#correctAttempts                |n                  |               |                            |1                                                        |
     |#inCorrectAttempts              |n                  |               |                            |0                                                        |
     |#lastAswered                    |n                  |               |                            |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |n                  |               |                            |0                                                        |
     |#skips                          |n                  |               |                            |0                                                        |
     |#userId                         |n                  |               |                            |0                                                        |
     |#correctAnswerList              |n                  |               |                            |1,2                                                      |
     |#answer1Id                      |n                  |               |                            |-1                                                       |
     |#answer1Value                   |n                  |               |                            |Osanda                                                   |
     |#answer1Type                    |n                  |               |                            |TEXT                                                     |
     |#answer1CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer2Id                      |n                  |               |                            |2                                                        |
     |#answer2Value                   |n                  |               |                            |Gemunu                                                   |
     |#answer2Type                    |n                  |               |                            |TEXT                                                     |
     |#answer2CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer3Id                      |n                  |               |                            |3                                                        |
     |#answer3Value                   |n                  |               |                            |Eranga                                                   |
     |#answer3Type                    |n                  |               |                            |TEXT                                                     |
     |#answer3CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer4Id                      |n                  |               |                            |4                                                        |
     |#answer4Value                   |n                  |               |                            |Heshan                                                   |
     |#answer4Type                    |n                  |               |                            |TEXT                                                     |
     |#answer4CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer5Id                      |n                  |               |                            |5                                                        |
     |#answer5Value                   |n                  |               |                            |Thilina                                                  |
     |#answer5Type                    |n                  |               |                            |TEXT                                                     |
     |#answer5CaseSensitive           |n                  |               |                            |true                                                     |
     |#tags                           |n                  |               |                            |MaxSoft                                                  |
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



Create a question using an empty value as the answer1Id
-------------------------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name    |Attribute Value To Be Set                                |
     |--------------------------------|-------------------|---------------|----------------------------|---------------------------------------------------------|
     |#creatorId                      |n                  |               |                            |osanda12                                                 |
     |#creatorPlatform                |n                  |               |                            |Web                                                      |
     |#creatoredSource                |n                  |               |                            |App                                                      |
     |#creatoredType                  |n                  |               |                            |Manual                                                   |
     |#deckId                         |y                  |scenario       |deckId                      |                                                         |
     |#kind                           |n                  |               |                            |ALL                                                      |
     |#isDeleted                      |n                  |               |                            |false                                                    |
     |#tempQuestionId                 |n                  |               |                            |testId                                                   |
     |#learningObjectives             |n                  |               |                            |learningObjective1                                       |
     |#imageUrl                       |n                  |               |                            |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |n                  |               |                            |TEXT                                                     |
     |#questionPrompt                 |n                  |               |                            |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |n                  |               |                            |TEXT                                                     |
     |#timeout                        |n                  |               |                            |60                                                       |
     |#rationale                      |n                  |               |                            |rationale                                                |
     |#boxId                          |n                  |               |                            |0                                                        |
     |#correctAttempts                |n                  |               |                            |1                                                        |
     |#inCorrectAttempts              |n                  |               |                            |0                                                        |
     |#lastAswered                    |n                  |               |                            |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |n                  |               |                            |0                                                        |
     |#skips                          |n                  |               |                            |0                                                        |
     |#userId                         |n                  |               |                            |0                                                        |
     |#correctAnswerList              |n                  |               |                            |1,2                                                      |
     |#answer1Id                      |n                  |               |                            |""                                                       |
     |#answer1Value                   |n                  |               |                            |Osanda                                                   |
     |#answer1Type                    |n                  |               |                            |TEXT                                                     |
     |#answer1CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer2Id                      |n                  |               |                            |2                                                        |
     |#answer2Value                   |n                  |               |                            |Gemunu                                                   |
     |#answer2Type                    |n                  |               |                            |TEXT                                                     |
     |#answer2CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer3Id                      |n                  |               |                            |3                                                        |
     |#answer3Value                   |n                  |               |                            |Eranga                                                   |
     |#answer3Type                    |n                  |               |                            |TEXT                                                     |
     |#answer3CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer4Id                      |n                  |               |                            |4                                                        |
     |#answer4Value                   |n                  |               |                            |Heshan                                                   |
     |#answer4Type                    |n                  |               |                            |TEXT                                                     |
     |#answer4CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer5Id                      |n                  |               |                            |5                                                        |
     |#answer5Value                   |n                  |               |                            |Thilina                                                  |
     |#answer5Type                    |n                  |               |                            |TEXT                                                     |
     |#answer5CaseSensitive           |n                  |               |                            |true                                                     |
     |#tags                           |n                  |               |                            |MaxSoft                                                  |
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



Create a question using null value as the answer1Id
---------------------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name    |Attribute Value To Be Set                                |
     |--------------------------------|-------------------|---------------|----------------------------|---------------------------------------------------------|
     |#creatorId                      |n                  |               |                            |osanda12                                                 |
     |#creatorPlatform                |n                  |               |                            |Web                                                      |
     |#creatoredSource                |n                  |               |                            |App                                                      |
     |#creatoredType                  |n                  |               |                            |Manual                                                   |
     |#deckId                         |y                  |scenario       |deckId                      |                                                         |
     |#kind                           |n                  |               |                            |ALL                                                      |
     |#isDeleted                      |n                  |               |                            |false                                                    |
     |#tempQuestionId                 |n                  |               |                            |testId                                                   |
     |#learningObjectives             |n                  |               |                            |learningObjective1                                       |
     |#imageUrl                       |n                  |               |                            |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |n                  |               |                            |TEXT                                                     |
     |#questionPrompt                 |n                  |               |                            |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |n                  |               |                            |TEXT                                                     |
     |#timeout                        |n                  |               |                            |60                                                       |
     |#rationale                      |n                  |               |                            |rationale                                                |
     |#boxId                          |n                  |               |                            |0                                                        |
     |#correctAttempts                |n                  |               |                            |1                                                        |
     |#inCorrectAttempts              |n                  |               |                            |0                                                        |
     |#lastAswered                    |n                  |               |                            |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |n                  |               |                            |0                                                        |
     |#skips                          |n                  |               |                            |0                                                        |
     |#userId                         |n                  |               |                            |0                                                        |
     |#correctAnswerList              |n                  |               |                            |1,2                                                      |
     |#answer1Id                      |n                  |               |                            |null                                                     |
     |#answer1Value                   |n                  |               |                            |Osanda                                                   |
     |#answer1Type                    |n                  |               |                            |TEXT                                                     |
     |#answer1CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer2Id                      |n                  |               |                            |2                                                        |
     |#answer2Value                   |n                  |               |                            |Gemunu                                                   |
     |#answer2Type                    |n                  |               |                            |TEXT                                                     |
     |#answer2CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer3Id                      |n                  |               |                            |3                                                        |
     |#answer3Value                   |n                  |               |                            |Eranga                                                   |
     |#answer3Type                    |n                  |               |                            |TEXT                                                     |
     |#answer3CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer4Id                      |n                  |               |                            |4                                                        |
     |#answer4Value                   |n                  |               |                            |Heshan                                                   |
     |#answer4Type                    |n                  |               |                            |TEXT                                                     |
     |#answer4CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer5Id                      |n                  |               |                            |5                                                        |
     |#answer5Value                   |n                  |               |                            |Thilina                                                  |
     |#answer5Type                    |n                  |               |                            |TEXT                                                     |
     |#answer5CaseSensitive           |n                  |               |                            |true                                                     |
     |#tags                           |n                  |               |                            |MaxSoft                                                  |
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



Create a question using empty value as the answer1Value
-------------------------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name    |Attribute Value To Be Set                                |
     |--------------------------------|-------------------|---------------|----------------------------|---------------------------------------------------------|
     |#creatorId                      |n                  |               |                            |osanda12                                                 |
     |#creatorPlatform                |n                  |               |                            |Web                                                      |
     |#creatoredSource                |n                  |               |                            |App                                                      |
     |#creatoredType                  |n                  |               |                            |Manual                                                   |
     |#deckId                         |y                  |scenario       |deckId                      |                                                         |
     |#kind                           |n                  |               |                            |ALL                                                      |
     |#isDeleted                      |n                  |               |                            |false                                                    |
     |#tempQuestionId                 |n                  |               |                            |testId                                                   |
     |#learningObjectives             |n                  |               |                            |learningObjective1                                       |
     |#imageUrl                       |n                  |               |                            |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |n                  |               |                            |TEXT                                                     |
     |#questionPrompt                 |n                  |               |                            |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |n                  |               |                            |TEXT                                                     |
     |#timeout                        |n                  |               |                            |60                                                       |
     |#rationale                      |n                  |               |                            |rationale                                                |
     |#boxId                          |n                  |               |                            |0                                                        |
     |#correctAttempts                |n                  |               |                            |1                                                        |
     |#inCorrectAttempts              |n                  |               |                            |0                                                        |
     |#lastAswered                    |n                  |               |                            |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |n                  |               |                            |0                                                        |
     |#skips                          |n                  |               |                            |0                                                        |
     |#userId                         |n                  |               |                            |0                                                        |
     |#correctAnswerList              |n                  |               |                            |1,2                                                      |
     |#answer1Id                      |n                  |               |                            |1                                                        |
     |#answer1Value                   |n                  |               |                            |                                                         |
     |#answer1Type                    |n                  |               |                            |TEXT                                                     |
     |#answer1CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer2Id                      |n                  |               |                            |2                                                        |
     |#answer2Value                   |n                  |               |                            |Gemunu                                                   |
     |#answer2Type                    |n                  |               |                            |TEXT                                                     |
     |#answer2CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer3Id                      |n                  |               |                            |3                                                        |
     |#answer3Value                   |n                  |               |                            |Eranga                                                   |
     |#answer3Type                    |n                  |               |                            |TEXT                                                     |
     |#answer3CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer4Id                      |n                  |               |                            |4                                                        |
     |#answer4Value                   |n                  |               |                            |Heshan                                                   |
     |#answer4Type                    |n                  |               |                            |TEXT                                                     |
     |#answer4CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer5Id                      |n                  |               |                            |5                                                        |
     |#answer5Value                   |n                  |               |                            |Thilina                                                  |
     |#answer5Type                    |n                  |               |                            |TEXT                                                     |
     |#answer5CaseSensitive           |n                  |               |                            |true                                                     |
     |#tags                           |n                  |               |                            |MaxSoft                                                  |
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



Create a question using null value as the answer1Value
------------------------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name    |Attribute Value To Be Set                                |
     |--------------------------------|-------------------|---------------|----------------------------|---------------------------------------------------------|
     |#creatorId                      |n                  |               |                            |osanda12                                                 |
     |#creatorPlatform                |n                  |               |                            |Web                                                      |
     |#creatoredSource                |n                  |               |                            |App                                                      |
     |#creatoredType                  |n                  |               |                            |Manual                                                   |
     |#deckId                         |y                  |scenario       |deckId                      |                                                         |
     |#kind                           |n                  |               |                            |ALL                                                      |
     |#isDeleted                      |n                  |               |                            |false                                                    |
     |#tempQuestionId                 |n                  |               |                            |testId                                                   |
     |#learningObjectives             |n                  |               |                            |learningObjective1                                       |
     |#imageUrl                       |n                  |               |                            |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |n                  |               |                            |TEXT                                                     |
     |#questionPrompt                 |n                  |               |                            |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |n                  |               |                            |TEXT                                                     |
     |#timeout                        |n                  |               |                            |60                                                       |
     |#rationale                      |n                  |               |                            |rationale                                                |
     |#boxId                          |n                  |               |                            |0                                                        |
     |#correctAttempts                |n                  |               |                            |1                                                        |
     |#inCorrectAttempts              |n                  |               |                            |0                                                        |
     |#lastAswered                    |n                  |               |                            |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |n                  |               |                            |0                                                        |
     |#skips                          |n                  |               |                            |0                                                        |
     |#userId                         |n                  |               |                            |0                                                        |
     |#correctAnswerList              |n                  |               |                            |1,2                                                      |
     |#answer1Id                      |n                  |               |                            |1                                                        |
     |#answer1Value                   |n                  |               |                            |"null"                                                   |
     |#answer1Type                    |n                  |               |                            |TEXT                                                     |
     |#answer1CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer2Id                      |n                  |               |                            |2                                                        |
     |#answer2Value                   |n                  |               |                            |Gemunu                                                   |
     |#answer2Type                    |n                  |               |                            |TEXT                                                     |
     |#answer2CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer3Id                      |n                  |               |                            |3                                                        |
     |#answer3Value                   |n                  |               |                            |Eranga                                                   |
     |#answer3Type                    |n                  |               |                            |TEXT                                                     |
     |#answer3CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer4Id                      |n                  |               |                            |4                                                        |
     |#answer4Value                   |n                  |               |                            |Heshan                                                   |
     |#answer4Type                    |n                  |               |                            |TEXT                                                     |
     |#answer4CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer5Id                      |n                  |               |                            |5                                                        |
     |#answer5Value                   |n                  |               |                            |Thilina                                                  |
     |#answer5Type                    |n                  |               |                            |TEXT                                                     |
     |#answer5CaseSensitive           |n                  |               |                            |true                                                     |
     |#tags                           |n                  |               |                            |MaxSoft                                                  |
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


Create a question using empty value as the answer1Type
------------------------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name    |Attribute Value To Be Set                                |
     |--------------------------------|-------------------|---------------|----------------------------|---------------------------------------------------------|
     |#creatorId                      |n                  |               |                            |osanda12                                                 |
     |#creatorPlatform                |n                  |               |                            |Web                                                      |
     |#creatoredSource                |n                  |               |                            |App                                                      |
     |#creatoredType                  |n                  |               |                            |Manual                                                   |
     |#deckId                         |y                  |scenario       |deckId                      |                                                         |
     |#kind                           |n                  |               |                            |ALL                                                      |
     |#isDeleted                      |n                  |               |                            |false                                                    |
     |#tempQuestionId                 |n                  |               |                            |testId                                                   |
     |#learningObjectives             |n                  |               |                            |learningObjective1                                       |
     |#imageUrl                       |n                  |               |                            |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |n                  |               |                            |TEXT                                                     |
     |#questionPrompt                 |n                  |               |                            |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |n                  |               |                            |TEXT                                                     |
     |#timeout                        |n                  |               |                            |60                                                       |
     |#rationale                      |n                  |               |                            |rationale                                                |
     |#boxId                          |n                  |               |                            |0                                                        |
     |#correctAttempts                |n                  |               |                            |1                                                        |
     |#inCorrectAttempts              |n                  |               |                            |0                                                        |
     |#lastAswered                    |n                  |               |                            |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |n                  |               |                            |0                                                        |
     |#skips                          |n                  |               |                            |0                                                        |
     |#userId                         |n                  |               |                            |0                                                        |
     |#correctAnswerList              |n                  |               |                            |1,2                                                      |
     |#answer1Id                      |n                  |               |                            |1                                                        |
     |#answer1Value                   |n                  |               |                            |Osanda                                                   |
     |#answer1Type                    |n                  |               |                            |                                                         |
     |#answer1CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer2Id                      |n                  |               |                            |2                                                        |
     |#answer2Value                   |n                  |               |                            |Gemunu                                                   |
     |#answer2Type                    |n                  |               |                            |TEXT                                                     |
     |#answer2CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer3Id                      |n                  |               |                            |3                                                        |
     |#answer3Value                   |n                  |               |                            |Eranga                                                   |
     |#answer3Type                    |n                  |               |                            |TEXT                                                     |
     |#answer3CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer4Id                      |n                  |               |                            |4                                                        |
     |#answer4Value                   |n                  |               |                            |Heshan                                                   |
     |#answer4Type                    |n                  |               |                            |TEXT                                                     |
     |#answer4CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer5Id                      |n                  |               |                            |5                                                        |
     |#answer5Value                   |n                  |               |                            |Thilina                                                  |
     |#answer5Type                    |n                  |               |                            |TEXT                                                     |
     |#answer5CaseSensitive           |n                  |               |                            |true                                                     |
     |#tags                           |n                  |               |                            |MaxSoft                                                  |
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


Create a question using null as the answer1Type
-----------------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name    |Attribute Value To Be Set                                |
     |--------------------------------|-------------------|---------------|----------------------------|---------------------------------------------------------|
     |#creatorId                      |n                  |               |                            |osanda12                                                 |
     |#creatorPlatform                |n                  |               |                            |Web                                                      |
     |#creatoredSource                |n                  |               |                            |App                                                      |
     |#creatoredType                  |n                  |               |                            |Manual                                                   |
     |#deckId                         |y                  |scenario       |deckId                      |                                                         |
     |#kind                           |n                  |               |                            |ALL                                                      |
     |#isDeleted                      |n                  |               |                            |false                                                    |
     |#tempQuestionId                 |n                  |               |                            |testId                                                   |
     |#learningObjectives             |n                  |               |                            |learningObjective1                                       |
     |#imageUrl                       |n                  |               |                            |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |n                  |               |                            |TEXT                                                     |
     |#questionPrompt                 |n                  |               |                            |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |n                  |               |                            |TEXT                                                     |
     |#timeout                        |n                  |               |                            |60                                                       |
     |#rationale                      |n                  |               |                            |rationale                                                |
     |#boxId                          |n                  |               |                            |0                                                        |
     |#correctAttempts                |n                  |               |                            |1                                                        |
     |#inCorrectAttempts              |n                  |               |                            |0                                                        |
     |#lastAswered                    |n                  |               |                            |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |n                  |               |                            |0                                                        |
     |#skips                          |n                  |               |                            |0                                                        |
     |#userId                         |n                  |               |                            |0                                                        |
     |#correctAnswerList              |n                  |               |                            |1,2                                                      |
     |#answer1Id                      |n                  |               |                            |1                                                        |
     |#answer1Value                   |n                  |               |                            |Osanda                                                   |
     |#answer1Type                    |n                  |               |                            |"null"                                                   |
     |#answer1CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer2Id                      |n                  |               |                            |2                                                        |
     |#answer2Value                   |n                  |               |                            |Gemunu                                                   |
     |#answer2Type                    |n                  |               |                            |TEXT                                                     |
     |#answer2CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer3Id                      |n                  |               |                            |3                                                        |
     |#answer3Value                   |n                  |               |                            |Eranga                                                   |
     |#answer3Type                    |n                  |               |                            |TEXT                                                     |
     |#answer3CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer4Id                      |n                  |               |                            |4                                                        |
     |#answer4Value                   |n                  |               |                            |Heshan                                                   |
     |#answer4Type                    |n                  |               |                            |TEXT                                                     |
     |#answer4CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer5Id                      |n                  |               |                            |5                                                        |
     |#answer5Value                   |n                  |               |                            |Thilina                                                  |
     |#answer5Type                    |n                  |               |                            |TEXT                                                     |
     |#answer5CaseSensitive           |n                  |               |                            |true                                                     |
     |#tags                           |n                  |               |                            |MaxSoft                                                  |
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


Create a question using String as the answer1Type
-------------------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name    |Attribute Value To Be Set                                |
     |--------------------------------|-------------------|---------------|----------------------------|---------------------------------------------------------|
     |#creatorId                      |n                  |               |                            |osanda12                                                 |
     |#creatorPlatform                |n                  |               |                            |Web                                                      |
     |#creatoredSource                |n                  |               |                            |App                                                      |
     |#creatoredType                  |n                  |               |                            |Manual                                                   |
     |#deckId                         |y                  |scenario       |deckId                      |                                                         |
     |#kind                           |n                  |               |                            |ALL                                                      |
     |#isDeleted                      |n                  |               |                            |false                                                    |
     |#tempQuestionId                 |n                  |               |                            |testId                                                   |
     |#learningObjectives             |n                  |               |                            |learningObjective1                                       |
     |#imageUrl                       |n                  |               |                            |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |n                  |               |                            |TEXT                                                     |
     |#questionPrompt                 |n                  |               |                            |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |n                  |               |                            |TEXT                                                     |
     |#timeout                        |n                  |               |                            |60                                                       |
     |#rationale                      |n                  |               |                            |rationale                                                |
     |#boxId                          |n                  |               |                            |0                                                        |
     |#correctAttempts                |n                  |               |                            |1                                                        |
     |#inCorrectAttempts              |n                  |               |                            |0                                                        |
     |#lastAswered                    |n                  |               |                            |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |n                  |               |                            |0                                                        |
     |#skips                          |n                  |               |                            |0                                                        |
     |#userId                         |n                  |               |                            |0                                                        |
     |#correctAnswerList              |n                  |               |                            |1,2                                                      |
     |#answer1Id                      |n                  |               |                            |1                                                        |
     |#answer1Value                   |n                  |               |                            |Osanda                                                   |
     |#answer1Type                    |n                  |               |                            |TEX                                                      |
     |#answer1CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer2Id                      |n                  |               |                            |2                                                        |
     |#answer2Value                   |n                  |               |                            |Gemunu                                                   |
     |#answer2Type                    |n                  |               |                            |TEXT                                                     |
     |#answer2CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer3Id                      |n                  |               |                            |3                                                        |
     |#answer3Value                   |n                  |               |                            |Eranga                                                   |
     |#answer3Type                    |n                  |               |                            |TEXT                                                     |
     |#answer3CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer4Id                      |n                  |               |                            |4                                                        |
     |#answer4Value                   |n                  |               |                            |Heshan                                                   |
     |#answer4Type                    |n                  |               |                            |TEXT                                                     |
     |#answer4CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer5Id                      |n                  |               |                            |5                                                        |
     |#answer5Value                   |n                  |               |                            |Thilina                                                  |
     |#answer5Type                    |n                  |               |                            |TEXT                                                     |
     |#answer5CaseSensitive           |n                  |               |                            |true                                                     |
     |#tags                           |n                  |               |                            |MaxSoft                                                  |
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


Create a question using numbers as the answer1Type
--------------------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name    |Attribute Value To Be Set                                |
     |--------------------------------|-------------------|---------------|----------------------------|---------------------------------------------------------|
     |#creatorId                      |n                  |               |                            |osanda12                                                 |
     |#creatorPlatform                |n                  |               |                            |Web                                                      |
     |#creatoredSource                |n                  |               |                            |App                                                      |
     |#creatoredType                  |n                  |               |                            |Manual                                                   |
     |#deckId                         |y                  |scenario       |deckId                      |                                                         |
     |#kind                           |n                  |               |                            |ALL                                                      |
     |#isDeleted                      |n                  |               |                            |false                                                    |
     |#tempQuestionId                 |n                  |               |                            |testId                                                   |
     |#learningObjectives             |n                  |               |                            |learningObjective1                                       |
     |#imageUrl                       |n                  |               |                            |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |n                  |               |                            |TEXT                                                     |
     |#questionPrompt                 |n                  |               |                            |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |n                  |               |                            |TEXT                                                     |
     |#timeout                        |n                  |               |                            |60                                                       |
     |#rationale                      |n                  |               |                            |rationale                                                |
     |#boxId                          |n                  |               |                            |0                                                        |
     |#correctAttempts                |n                  |               |                            |1                                                        |
     |#inCorrectAttempts              |n                  |               |                            |0                                                        |
     |#lastAswered                    |n                  |               |                            |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |n                  |               |                            |0                                                        |
     |#skips                          |n                  |               |                            |0                                                        |
     |#userId                         |n                  |               |                            |0                                                        |
     |#correctAnswerList              |n                  |               |                            |1,2                                                      |
     |#answer1Id                      |n                  |               |                            |1                                                        |
     |#answer1Value                   |n                  |               |                            |Osanda                                                   |
     |#answer1Type                    |n                  |               |                            |1                                                        |
     |#answer1CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer2Id                      |n                  |               |                            |2                                                        |
     |#answer2Value                   |n                  |               |                            |Gemunu                                                   |
     |#answer2Type                    |n                  |               |                            |TEXT                                                     |
     |#answer2CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer3Id                      |n                  |               |                            |3                                                        |
     |#answer3Value                   |n                  |               |                            |Eranga                                                   |
     |#answer3Type                    |n                  |               |                            |TEXT                                                     |
     |#answer3CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer4Id                      |n                  |               |                            |4                                                        |
     |#answer4Value                   |n                  |               |                            |Heshan                                                   |
     |#answer4Type                    |n                  |               |                            |TEXT                                                     |
     |#answer4CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer5Id                      |n                  |               |                            |5                                                        |
     |#answer5Value                   |n                  |               |                            |Thilina                                                  |
     |#answer5Type                    |n                  |               |                            |TEXT                                                     |
     |#answer5CaseSensitive           |n                  |               |                            |true                                                     |
     |#tags                           |n                  |               |                            |MaxSoft                                                  |
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



Create a question using a string value as the answer2Id
-------------------------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name    |Attribute Value To Be Set                                |
     |--------------------------------|-------------------|---------------|----------------------------|---------------------------------------------------------|
     |#creatorId                      |n                  |               |                            |osanda12                                                 |
     |#creatorPlatform                |n                  |               |                            |Web                                                      |
     |#creatoredSource                |n                  |               |                            |App                                                      |
     |#creatoredType                  |n                  |               |                            |Manual                                                   |
     |#deckId                         |y                  |scenario       |deckId                      |                                                         |
     |#kind                           |n                  |               |                            |ALL                                                      |
     |#isDeleted                      |n                  |               |                            |false                                                    |
     |#tempQuestionId                 |n                  |               |                            |testId                                                   |
     |#learningObjectives             |n                  |               |                            |learningObjective1                                       |
     |#imageUrl                       |n                  |               |                            |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |n                  |               |                            |TEXT                                                     |
     |#questionPrompt                 |n                  |               |                            |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |n                  |               |                            |TEXT                                                     |
     |#timeout                        |n                  |               |                            |60                                                       |
     |#rationale                      |n                  |               |                            |rationale                                                |
     |#boxId                          |n                  |               |                            |0                                                        |
     |#correctAttempts                |n                  |               |                            |1                                                        |
     |#inCorrectAttempts              |n                  |               |                            |0                                                        |
     |#lastAswered                    |n                  |               |                            |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |n                  |               |                            |0                                                        |
     |#skips                          |n                  |               |                            |0                                                        |
     |#userId                         |n                  |               |                            |0                                                        |
     |#correctAnswerList              |n                  |               |                            |1,2                                                      |
     |#answer2Id                      |n                  |               |                            |"a"                                                      |
     |#answer2Value                   |n                  |               |                            |Osanda                                                   |
     |#answer2Type                    |n                  |               |                            |TEXT                                                     |
     |#answer2CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer1Id                      |n                  |               |                            |1                                                        |
     |#answer1Value                   |n                  |               |                            |Gemunu                                                   |
     |#answer1Type                    |n                  |               |                            |TEXT                                                     |
     |#answer1CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer3Id                      |n                  |               |                            |3                                                        |
     |#answer3Value                   |n                  |               |                            |Eranga                                                   |
     |#answer3Type                    |n                  |               |                            |TEXT                                                     |
     |#answer3CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer4Id                      |n                  |               |                            |4                                                        |
     |#answer4Value                   |n                  |               |                            |Heshan                                                   |
     |#answer4Type                    |n                  |               |                            |TEXT                                                     |
     |#answer4CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer5Id                      |n                  |               |                            |5                                                        |
     |#answer5Value                   |n                  |               |                            |Thilina                                                  |
     |#answer5Type                    |n                  |               |                            |TEXT                                                     |
     |#answer5CaseSensitive           |n                  |               |                            |true                                                     |
     |#tags                           |n                  |               |                            |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |answers: Invalid value 'a'                               |
     |$.description                             |null                                                     |
     |$.fieldErrors                             |null                                                     |



Create a question using a special character as the answer2Id
------------------------------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name    |Attribute Value To Be Set                                |
     |--------------------------------|-------------------|---------------|----------------------------|---------------------------------------------------------|
     |#creatorId                      |n                  |               |                            |osanda12                                                 |
     |#creatorPlatform                |n                  |               |                            |Web                                                      |
     |#creatoredSource                |n                  |               |                            |App                                                      |
     |#creatoredType                  |n                  |               |                            |Manual                                                   |
     |#deckId                         |y                  |scenario       |deckId                      |                                                         |
     |#kind                           |n                  |               |                            |ALL                                                      |
     |#isDeleted                      |n                  |               |                            |false                                                    |
     |#tempQuestionId                 |n                  |               |                            |testId                                                   |
     |#learningObjectives             |n                  |               |                            |learningObjective1                                       |
     |#imageUrl                       |n                  |               |                            |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |n                  |               |                            |TEXT                                                     |
     |#questionPrompt                 |n                  |               |                            |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |n                  |               |                            |TEXT                                                     |
     |#timeout                        |n                  |               |                            |60                                                       |
     |#rationale                      |n                  |               |                            |rationale                                                |
     |#boxId                          |n                  |               |                            |0                                                        |
     |#correctAttempts                |n                  |               |                            |1                                                        |
     |#inCorrectAttempts              |n                  |               |                            |0                                                        |
     |#lastAswered                    |n                  |               |                            |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |n                  |               |                            |0                                                        |
     |#skips                          |n                  |               |                            |0                                                        |
     |#userId                         |n                  |               |                            |0                                                        |
     |#correctAnswerList              |n                  |               |                            |1,2                                                      |
     |#answer2Id                      |n                  |               |                            |"@"                                                      |
     |#answer2Value                   |n                  |               |                            |Osanda                                                   |
     |#answer2Type                    |n                  |               |                            |TEXT                                                     |
     |#answer2CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer1Id                      |n                  |               |                            |1                                                        |
     |#answer1Value                   |n                  |               |                            |Gemunu                                                   |
     |#answer1Type                    |n                  |               |                            |TEXT                                                     |
     |#answer1CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer3Id                      |n                  |               |                            |3                                                        |
     |#answer3Value                   |n                  |               |                            |Eranga                                                   |
     |#answer3Type                    |n                  |               |                            |TEXT                                                     |
     |#answer3CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer4Id                      |n                  |               |                            |4                                                        |
     |#answer4Value                   |n                  |               |                            |Heshan                                                   |
     |#answer4Type                    |n                  |               |                            |TEXT                                                     |
     |#answer4CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer5Id                      |n                  |               |                            |5                                                        |
     |#answer5Value                   |n                  |               |                            |Thilina                                                  |
     |#answer5Type                    |n                  |               |                            |TEXT                                                     |
     |#answer5CaseSensitive           |n                  |               |                            |true                                                     |
     |#tags                           |n                  |               |                            |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.message                                 |answers: Invalid value '@'                               |
     |$.description                             |null                                                     |
     |$.fieldErrors                             |null                                                     |



Create a question using a negative integer value as the answer2Id
-----------------------------------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name    |Attribute Value To Be Set                                |
     |--------------------------------|-------------------|---------------|----------------------------|---------------------------------------------------------|
     |#creatorId                      |n                  |               |                            |osanda12                                                 |
     |#creatorPlatform                |n                  |               |                            |Web                                                      |
     |#creatoredSource                |n                  |               |                            |App                                                      |
     |#creatoredType                  |n                  |               |                            |Manual                                                   |
     |#deckId                         |y                  |scenario       |deckId                      |                                                         |
     |#kind                           |n                  |               |                            |ALL                                                      |
     |#isDeleted                      |n                  |               |                            |false                                                    |
     |#tempQuestionId                 |n                  |               |                            |testId                                                   |
     |#learningObjectives             |n                  |               |                            |learningObjective1                                       |
     |#imageUrl                       |n                  |               |                            |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |n                  |               |                            |TEXT                                                     |
     |#questionPrompt                 |n                  |               |                            |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |n                  |               |                            |TEXT                                                     |
     |#timeout                        |n                  |               |                            |60                                                       |
     |#rationale                      |n                  |               |                            |rationale                                                |
     |#boxId                          |n                  |               |                            |0                                                        |
     |#correctAttempts                |n                  |               |                            |1                                                        |
     |#inCorrectAttempts              |n                  |               |                            |0                                                        |
     |#lastAswered                    |n                  |               |                            |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |n                  |               |                            |0                                                        |
     |#skips                          |n                  |               |                            |0                                                        |
     |#userId                         |n                  |               |                            |0                                                        |
     |#correctAnswerList              |n                  |               |                            |1,2                                                      |
     |#answer2Id                      |n                  |               |                            |-1                                                       |
     |#answer2Value                   |n                  |               |                            |Osanda                                                   |
     |#answer2Type                    |n                  |               |                            |TEXT                                                     |
     |#answer2CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer1Id                      |n                  |               |                            |1                                                        |
     |#answer1Value                   |n                  |               |                            |Gemunu                                                   |
     |#answer1Type                    |n                  |               |                            |TEXT                                                     |
     |#answer1CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer3Id                      |n                  |               |                            |3                                                        |
     |#answer3Value                   |n                  |               |                            |Eranga                                                   |
     |#answer3Type                    |n                  |               |                            |TEXT                                                     |
     |#answer3CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer4Id                      |n                  |               |                            |4                                                        |
     |#answer4Value                   |n                  |               |                            |Heshan                                                   |
     |#answer4Type                    |n                  |               |                            |TEXT                                                     |
     |#answer4CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer5Id                      |n                  |               |                            |5                                                        |
     |#answer5Value                   |n                  |               |                            |Thilina                                                  |
     |#answer5Type                    |n                  |               |                            |TEXT                                                     |
     |#answer5CaseSensitive           |n                  |               |                            |true                                                     |
     |#tags                           |n                  |               |                            |MaxSoft                                                  |
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



Create a question using an empty value as the answer2Id
-------------------------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name    |Attribute Value To Be Set                                |
     |--------------------------------|-------------------|---------------|----------------------------|---------------------------------------------------------|
     |#creatorId                      |n                  |               |                            |osanda12                                                 |
     |#creatorPlatform                |n                  |               |                            |Web                                                      |
     |#creatoredSource                |n                  |               |                            |App                                                      |
     |#creatoredType                  |n                  |               |                            |Manual                                                   |
     |#deckId                         |y                  |scenario       |deckId                      |                                                         |
     |#kind                           |n                  |               |                            |ALL                                                      |
     |#isDeleted                      |n                  |               |                            |false                                                    |
     |#tempQuestionId                 |n                  |               |                            |testId                                                   |
     |#learningObjectives             |n                  |               |                            |learningObjective1                                       |
     |#imageUrl                       |n                  |               |                            |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |n                  |               |                            |TEXT                                                     |
     |#questionPrompt                 |n                  |               |                            |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |n                  |               |                            |TEXT                                                     |
     |#timeout                        |n                  |               |                            |60                                                       |
     |#rationale                      |n                  |               |                            |rationale                                                |
     |#boxId                          |n                  |               |                            |0                                                        |
     |#correctAttempts                |n                  |               |                            |1                                                        |
     |#inCorrectAttempts              |n                  |               |                            |0                                                        |
     |#lastAswered                    |n                  |               |                            |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |n                  |               |                            |0                                                        |
     |#skips                          |n                  |               |                            |0                                                        |
     |#userId                         |n                  |               |                            |0                                                        |
     |#correctAnswerList              |n                  |               |                            |1,2                                                      |
     |#answer2Id                      |n                  |               |                            |""                                                       |
     |#answer2Value                   |n                  |               |                            |Osanda                                                   |
     |#answer2Type                    |n                  |               |                            |TEXT                                                     |
     |#answer2CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer1Id                      |n                  |               |                            |1                                                        |
     |#answer1Value                   |n                  |               |                            |Gemunu                                                   |
     |#answer1Type                    |n                  |               |                            |TEXT                                                     |
     |#answer1CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer3Id                      |n                  |               |                            |3                                                        |
     |#answer3Value                   |n                  |               |                            |Eranga                                                   |
     |#answer3Type                    |n                  |               |                            |TEXT                                                     |
     |#answer3CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer4Id                      |n                  |               |                            |4                                                        |
     |#answer4Value                   |n                  |               |                            |Heshan                                                   |
     |#answer4Type                    |n                  |               |                            |TEXT                                                     |
     |#answer4CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer5Id                      |n                  |               |                            |5                                                        |
     |#answer5Value                   |n                  |               |                            |Thilina                                                  |
     |#answer5Type                    |n                  |               |                            |TEXT                                                     |
     |#answer5CaseSensitive           |n                  |               |                            |true                                                     |
     |#tags                           |n                  |               |                            |MaxSoft                                                  |
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



Create a question using null value as the answer2Id
---------------------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name    |Attribute Value To Be Set                                |
     |--------------------------------|-------------------|---------------|----------------------------|---------------------------------------------------------|
     |#creatorId                      |n                  |               |                            |osanda12                                                 |
     |#creatorPlatform                |n                  |               |                            |Web                                                      |
     |#creatoredSource                |n                  |               |                            |App                                                      |
     |#creatoredType                  |n                  |               |                            |Manual                                                   |
     |#deckId                         |y                  |scenario       |deckId                      |                                                         |
     |#kind                           |n                  |               |                            |ALL                                                      |
     |#isDeleted                      |n                  |               |                            |false                                                    |
     |#tempQuestionId                 |n                  |               |                            |testId                                                   |
     |#learningObjectives             |n                  |               |                            |learningObjective1                                       |
     |#imageUrl                       |n                  |               |                            |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |n                  |               |                            |TEXT                                                     |
     |#questionPrompt                 |n                  |               |                            |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |n                  |               |                            |TEXT                                                     |
     |#timeout                        |n                  |               |                            |60                                                       |
     |#rationale                      |n                  |               |                            |rationale                                                |
     |#boxId                          |n                  |               |                            |0                                                        |
     |#correctAttempts                |n                  |               |                            |1                                                        |
     |#inCorrectAttempts              |n                  |               |                            |0                                                        |
     |#lastAswered                    |n                  |               |                            |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |n                  |               |                            |0                                                        |
     |#skips                          |n                  |               |                            |0                                                        |
     |#userId                         |n                  |               |                            |0                                                        |
     |#correctAnswerList              |n                  |               |                            |1,2                                                      |
     |#answer2Id                      |n                  |               |                            |null                                                     |
     |#answer2Value                   |n                  |               |                            |Osanda                                                   |
     |#answer2Type                    |n                  |               |                            |TEXT                                                     |
     |#answer2CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer1Id                      |n                  |               |                            |1                                                        |
     |#answer1Value                   |n                  |               |                            |Gemunu                                                   |
     |#answer1Type                    |n                  |               |                            |TEXT                                                     |
     |#answer1CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer3Id                      |n                  |               |                            |3                                                        |
     |#answer3Value                   |n                  |               |                            |Eranga                                                   |
     |#answer3Type                    |n                  |               |                            |TEXT                                                     |
     |#answer3CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer4Id                      |n                  |               |                            |4                                                        |
     |#answer4Value                   |n                  |               |                            |Heshan                                                   |
     |#answer4Type                    |n                  |               |                            |TEXT                                                     |
     |#answer4CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer5Id                      |n                  |               |                            |5                                                        |
     |#answer5Value                   |n                  |               |                            |Thilina                                                  |
     |#answer5Type                    |n                  |               |                            |TEXT                                                     |
     |#answer5CaseSensitive           |n                  |               |                            |true                                                     |
     |#tags                           |n                  |               |                            |MaxSoft                                                  |
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



Create a question using empty value as the answer2Value
-------------------------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name    |Attribute Value To Be Set                                |
     |--------------------------------|-------------------|---------------|----------------------------|---------------------------------------------------------|
     |#creatorId                      |n                  |               |                            |osanda12                                                 |
     |#creatorPlatform                |n                  |               |                            |Web                                                      |
     |#creatoredSource                |n                  |               |                            |App                                                      |
     |#creatoredType                  |n                  |               |                            |Manual                                                   |
     |#deckId                         |y                  |scenario       |deckId                      |                                                         |
     |#kind                           |n                  |               |                            |ALL                                                      |
     |#isDeleted                      |n                  |               |                            |false                                                    |
     |#tempQuestionId                 |n                  |               |                            |testId                                                   |
     |#learningObjectives             |n                  |               |                            |learningObjective1                                       |
     |#imageUrl                       |n                  |               |                            |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |n                  |               |                            |TEXT                                                     |
     |#questionPrompt                 |n                  |               |                            |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |n                  |               |                            |TEXT                                                     |
     |#timeout                        |n                  |               |                            |60                                                       |
     |#rationale                      |n                  |               |                            |rationale                                                |
     |#boxId                          |n                  |               |                            |0                                                        |
     |#correctAttempts                |n                  |               |                            |1                                                        |
     |#inCorrectAttempts              |n                  |               |                            |0                                                        |
     |#lastAswered                    |n                  |               |                            |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |n                  |               |                            |0                                                        |
     |#skips                          |n                  |               |                            |0                                                        |
     |#userId                         |n                  |               |                            |0                                                        |
     |#correctAnswerList              |n                  |               |                            |1,2                                                      |
     |#answer2Id                      |n                  |               |                            |2                                                        |
     |#answer2Value                   |n                  |               |                            |                                                         |
     |#answer2Type                    |n                  |               |                            |TEXT                                                     |
     |#answer2CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer1Id                      |n                  |               |                            |1                                                        |
     |#answer1Value                   |n                  |               |                            |Gemunu                                                   |
     |#answer1Type                    |n                  |               |                            |TEXT                                                     |
     |#answer1CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer3Id                      |n                  |               |                            |3                                                        |
     |#answer3Value                   |n                  |               |                            |Eranga                                                   |
     |#answer3Type                    |n                  |               |                            |TEXT                                                     |
     |#answer3CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer4Id                      |n                  |               |                            |4                                                        |
     |#answer4Value                   |n                  |               |                            |Heshan                                                   |
     |#answer4Type                    |n                  |               |                            |TEXT                                                     |
     |#answer4CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer5Id                      |n                  |               |                            |5                                                        |
     |#answer5Value                   |n                  |               |                            |Thilina                                                  |
     |#answer5Type                    |n                  |               |                            |TEXT                                                     |
     |#answer5CaseSensitive           |n                  |               |                            |true                                                     |
     |#tags                           |n                  |               |                            |MaxSoft                                                  |
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



Create a question using null value as the answer2Value
------------------------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name    |Attribute Value To Be Set                                |
     |--------------------------------|-------------------|---------------|----------------------------|---------------------------------------------------------|
     |#creatorId                      |n                  |               |                            |osanda12                                                 |
     |#creatorPlatform                |n                  |               |                            |Web                                                      |
     |#creatoredSource                |n                  |               |                            |App                                                      |
     |#creatoredType                  |n                  |               |                            |Manual                                                   |
     |#deckId                         |y                  |scenario       |deckId                      |                                                         |
     |#kind                           |n                  |               |                            |ALL                                                      |
     |#isDeleted                      |n                  |               |                            |false                                                    |
     |#tempQuestionId                 |n                  |               |                            |testId                                                   |
     |#learningObjectives             |n                  |               |                            |learningObjective1                                       |
     |#imageUrl                       |n                  |               |                            |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |n                  |               |                            |TEXT                                                     |
     |#questionPrompt                 |n                  |               |                            |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |n                  |               |                            |TEXT                                                     |
     |#timeout                        |n                  |               |                            |60                                                       |
     |#rationale                      |n                  |               |                            |rationale                                                |
     |#boxId                          |n                  |               |                            |0                                                        |
     |#correctAttempts                |n                  |               |                            |1                                                        |
     |#inCorrectAttempts              |n                  |               |                            |0                                                        |
     |#lastAswered                    |n                  |               |                            |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |n                  |               |                            |0                                                        |
     |#skips                          |n                  |               |                            |0                                                        |
     |#userId                         |n                  |               |                            |0                                                        |
     |#correctAnswerList              |n                  |               |                            |1,2                                                      |
     |#answer2Id                      |n                  |               |                            |2                                                        |
     |#answer2Value                   |n                  |               |                            |"null"                                                   |
     |#answer2Type                    |n                  |               |                            |TEXT                                                     |
     |#answer2CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer1Id                      |n                  |               |                            |1                                                        |
     |#answer1Value                   |n                  |               |                            |Gemunu                                                   |
     |#answer1Type                    |n                  |               |                            |TEXT                                                     |
     |#answer1CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer3Id                      |n                  |               |                            |3                                                        |
     |#answer3Value                   |n                  |               |                            |Eranga                                                   |
     |#answer3Type                    |n                  |               |                            |TEXT                                                     |
     |#answer3CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer4Id                      |n                  |               |                            |4                                                        |
     |#answer4Value                   |n                  |               |                            |Heshan                                                   |
     |#answer4Type                    |n                  |               |                            |TEXT                                                     |
     |#answer4CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer5Id                      |n                  |               |                            |5                                                        |
     |#answer5Value                   |n                  |               |                            |Thilina                                                  |
     |#answer5Type                    |n                  |               |                            |TEXT                                                     |
     |#answer5CaseSensitive           |n                  |               |                            |true                                                     |
     |#tags                           |n                  |               |                            |MaxSoft                                                  |
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


Create a question using empty value as the answer2Type
------------------------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name    |Attribute Value To Be Set                                |
     |--------------------------------|-------------------|---------------|----------------------------|---------------------------------------------------------|
     |#creatorId                      |n                  |               |                            |osanda12                                                 |
     |#creatorPlatform                |n                  |               |                            |Web                                                      |
     |#creatoredSource                |n                  |               |                            |App                                                      |
     |#creatoredType                  |n                  |               |                            |Manual                                                   |
     |#deckId                         |y                  |scenario       |deckId                      |                                                         |
     |#kind                           |n                  |               |                            |ALL                                                      |
     |#isDeleted                      |n                  |               |                            |false                                                    |
     |#tempQuestionId                 |n                  |               |                            |testId                                                   |
     |#learningObjectives             |n                  |               |                            |learningObjective1                                       |
     |#imageUrl                       |n                  |               |                            |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |n                  |               |                            |TEXT                                                     |
     |#questionPrompt                 |n                  |               |                            |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |n                  |               |                            |TEXT                                                     |
     |#timeout                        |n                  |               |                            |60                                                       |
     |#rationale                      |n                  |               |                            |rationale                                                |
     |#boxId                          |n                  |               |                            |0                                                        |
     |#correctAttempts                |n                  |               |                            |1                                                        |
     |#inCorrectAttempts              |n                  |               |                            |0                                                        |
     |#lastAswered                    |n                  |               |                            |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |n                  |               |                            |0                                                        |
     |#skips                          |n                  |               |                            |0                                                        |
     |#userId                         |n                  |               |                            |0                                                        |
     |#correctAnswerList              |n                  |               |                            |1,2                                                      |
     |#answer2Id                      |n                  |               |                            |2                                                        |
     |#answer2Value                   |n                  |               |                            |Osanda                                                   |
     |#answer2Type                    |n                  |               |                            |                                                         |
     |#answer2CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer1Id                      |n                  |               |                            |1                                                        |
     |#answer1Value                   |n                  |               |                            |Gemunu                                                   |
     |#answer1Type                    |n                  |               |                            |TEXT                                                     |
     |#answer1CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer3Id                      |n                  |               |                            |3                                                        |
     |#answer3Value                   |n                  |               |                            |Eranga                                                   |
     |#answer3Type                    |n                  |               |                            |TEXT                                                     |
     |#answer3CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer4Id                      |n                  |               |                            |4                                                        |
     |#answer4Value                   |n                  |               |                            |Heshan                                                   |
     |#answer4Type                    |n                  |               |                            |TEXT                                                     |
     |#answer4CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer5Id                      |n                  |               |                            |5                                                        |
     |#answer5Value                   |n                  |               |                            |Thilina                                                  |
     |#answer5Type                    |n                  |               |                            |TEXT                                                     |
     |#answer5CaseSensitive           |n                  |               |                            |true                                                     |
     |#tags                           |n                  |               |                            |MaxSoft                                                  |
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


Create a question using null as the answer2Type
-----------------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name    |Attribute Value To Be Set                                |
     |--------------------------------|-------------------|---------------|----------------------------|---------------------------------------------------------|
     |#creatorId                      |n                  |               |                            |osanda12                                                 |
     |#creatorPlatform                |n                  |               |                            |Web                                                      |
     |#creatoredSource                |n                  |               |                            |App                                                      |
     |#creatoredType                  |n                  |               |                            |Manual                                                   |
     |#deckId                         |y                  |scenario       |deckId                      |                                                         |
     |#kind                           |n                  |               |                            |ALL                                                      |
     |#isDeleted                      |n                  |               |                            |false                                                    |
     |#tempQuestionId                 |n                  |               |                            |testId                                                   |
     |#learningObjectives             |n                  |               |                            |learningObjective1                                       |
     |#imageUrl                       |n                  |               |                            |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |n                  |               |                            |TEXT                                                     |
     |#questionPrompt                 |n                  |               |                            |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |n                  |               |                            |TEXT                                                     |
     |#timeout                        |n                  |               |                            |60                                                       |
     |#rationale                      |n                  |               |                            |rationale                                                |
     |#boxId                          |n                  |               |                            |0                                                        |
     |#correctAttempts                |n                  |               |                            |1                                                        |
     |#inCorrectAttempts              |n                  |               |                            |0                                                        |
     |#lastAswered                    |n                  |               |                            |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |n                  |               |                            |0                                                        |
     |#skips                          |n                  |               |                            |0                                                        |
     |#userId                         |n                  |               |                            |0                                                        |
     |#correctAnswerList              |n                  |               |                            |1,2                                                      |
     |#answer2Id                      |n                  |               |                            |2                                                        |
     |#answer2Value                   |n                  |               |                            |Osanda                                                   |
     |#answer2Type                    |n                  |               |                            |"null"                                                   |
     |#answer2CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer1Id                      |n                  |               |                            |1                                                        |
     |#answer1Value                   |n                  |               |                            |Gemunu                                                   |
     |#answer1Type                    |n                  |               |                            |TEXT                                                     |
     |#answer1CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer3Id                      |n                  |               |                            |3                                                        |
     |#answer3Value                   |n                  |               |                            |Eranga                                                   |
     |#answer3Type                    |n                  |               |                            |TEXT                                                     |
     |#answer3CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer4Id                      |n                  |               |                            |4                                                        |
     |#answer4Value                   |n                  |               |                            |Heshan                                                   |
     |#answer4Type                    |n                  |               |                            |TEXT                                                     |
     |#answer4CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer5Id                      |n                  |               |                            |5                                                        |
     |#answer5Value                   |n                  |               |                            |Thilina                                                  |
     |#answer5Type                    |n                  |               |                            |TEXT                                                     |
     |#answer5CaseSensitive           |n                  |               |                            |true                                                     |
     |#tags                           |n                  |               |                            |MaxSoft                                                  |
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


Create a question using String as the answer2Type
-------------------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name    |Attribute Value To Be Set                                |
     |--------------------------------|-------------------|---------------|----------------------------|---------------------------------------------------------|
     |#creatorId                      |n                  |               |                            |osanda12                                                 |
     |#creatorPlatform                |n                  |               |                            |Web                                                      |
     |#creatoredSource                |n                  |               |                            |App                                                      |
     |#creatoredType                  |n                  |               |                            |Manual                                                   |
     |#deckId                         |y                  |scenario       |deckId                      |                                                         |
     |#kind                           |n                  |               |                            |ALL                                                      |
     |#isDeleted                      |n                  |               |                            |false                                                    |
     |#tempQuestionId                 |n                  |               |                            |testId                                                   |
     |#learningObjectives             |n                  |               |                            |learningObjective1                                       |
     |#imageUrl                       |n                  |               |                            |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |n                  |               |                            |TEXT                                                     |
     |#questionPrompt                 |n                  |               |                            |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |n                  |               |                            |TEXT                                                     |
     |#timeout                        |n                  |               |                            |60                                                       |
     |#rationale                      |n                  |               |                            |rationale                                                |
     |#boxId                          |n                  |               |                            |0                                                        |
     |#correctAttempts                |n                  |               |                            |1                                                        |
     |#inCorrectAttempts              |n                  |               |                            |0                                                        |
     |#lastAswered                    |n                  |               |                            |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |n                  |               |                            |0                                                        |
     |#skips                          |n                  |               |                            |0                                                        |
     |#userId                         |n                  |               |                            |0                                                        |
     |#correctAnswerList              |n                  |               |                            |1,2                                                      |
     |#answer2Id                      |n                  |               |                            |2                                                        |
     |#answer2Value                   |n                  |               |                            |Osanda                                                   |
     |#answer2Type                    |n                  |               |                            |TEX                                                      |
     |#answer2CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer1Id                      |n                  |               |                            |1                                                        |
     |#answer1Value                   |n                  |               |                            |Gemunu                                                   |
     |#answer1Type                    |n                  |               |                            |TEXT                                                     |
     |#answer1CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer3Id                      |n                  |               |                            |3                                                        |
     |#answer3Value                   |n                  |               |                            |Eranga                                                   |
     |#answer3Type                    |n                  |               |                            |TEXT                                                     |
     |#answer3CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer4Id                      |n                  |               |                            |4                                                        |
     |#answer4Value                   |n                  |               |                            |Heshan                                                   |
     |#answer4Type                    |n                  |               |                            |TEXT                                                     |
     |#answer4CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer5Id                      |n                  |               |                            |5                                                        |
     |#answer5Value                   |n                  |               |                            |Thilina                                                  |
     |#answer5Type                    |n                  |               |                            |TEXT                                                     |
     |#answer5CaseSensitive           |n                  |               |                            |true                                                     |
     |#tags                           |n                  |               |                            |MaxSoft                                                  |
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


Create a question using numbers as the answer2Type
--------------------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name    |Attribute Value To Be Set                                |
     |--------------------------------|-------------------|---------------|----------------------------|---------------------------------------------------------|
     |#creatorId                      |n                  |               |                            |osanda12                                                 |
     |#creatorPlatform                |n                  |               |                            |Web                                                      |
     |#creatoredSource                |n                  |               |                            |App                                                      |
     |#creatoredType                  |n                  |               |                            |Manual                                                   |
     |#deckId                         |y                  |scenario       |deckId                      |                                                         |
     |#kind                           |n                  |               |                            |ALL                                                      |
     |#isDeleted                      |n                  |               |                            |false                                                    |
     |#tempQuestionId                 |n                  |               |                            |testId                                                   |
     |#learningObjectives             |n                  |               |                            |learningObjective1                                       |
     |#imageUrl                       |n                  |               |                            |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |n                  |               |                            |TEXT                                                     |
     |#questionPrompt                 |n                  |               |                            |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |n                  |               |                            |TEXT                                                     |
     |#timeout                        |n                  |               |                            |60                                                       |
     |#rationale                      |n                  |               |                            |rationale                                                |
     |#boxId                          |n                  |               |                            |0                                                        |
     |#correctAttempts                |n                  |               |                            |1                                                        |
     |#inCorrectAttempts              |n                  |               |                            |0                                                        |
     |#lastAswered                    |n                  |               |                            |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |n                  |               |                            |0                                                        |
     |#skips                          |n                  |               |                            |0                                                        |
     |#userId                         |n                  |               |                            |0                                                        |
     |#correctAnswerList              |n                  |               |                            |1,2                                                      |
     |#answer2Id                      |n                  |               |                            |2                                                        |
     |#answer2Value                   |n                  |               |                            |Osanda                                                   |
     |#answer2Type                    |n                  |               |                            |3                                                        |
     |#answer2CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer1Id                      |n                  |               |                            |1                                                        |
     |#answer1Value                   |n                  |               |                            |Gemunu                                                   |
     |#answer1Type                    |n                  |               |                            |TEXT                                                     |
     |#answer1CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer3Id                      |n                  |               |                            |3                                                        |
     |#answer3Value                   |n                  |               |                            |Eranga                                                   |
     |#answer3Type                    |n                  |               |                            |TEXT                                                     |
     |#answer3CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer4Id                      |n                  |               |                            |4                                                        |
     |#answer4Value                   |n                  |               |                            |Heshan                                                   |
     |#answer4Type                    |n                  |               |                            |TEXT                                                     |
     |#answer4CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer5Id                      |n                  |               |                            |5                                                        |
     |#answer5Value                   |n                  |               |                            |Thilina                                                  |
     |#answer5Type                    |n                  |               |                            |TEXT                                                     |
     |#answer5CaseSensitive           |n                  |               |                            |true                                                     |
     |#tags                           |n                  |               |                            |MaxSoft                                                  |
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



Create a question using an invalid imageUrl
-------------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name    |Attribute Value To Be Set                                |
     |--------------------------------|-------------------|---------------|----------------------------|---------------------------------------------------------|
     |#creatorId                      |n                  |               |                            |osanda12                                                 |
     |#creatorPlatform                |n                  |               |                            |Web                                                      |
     |#creatoredSource                |n                  |               |                            |App                                                      |
     |#creatoredType                  |n                  |               |                            |Manual                                                   |
     |#deckId                         |y                  |scenario       |deckId                      |                                                         |
     |#kind                           |n                  |               |                            |ALL                                                      |
     |#isDeleted                      |n                  |               |                            |false                                                    |
     |#tempQuestionId                 |n                  |               |                            |testId                                                   |
     |#learningObjectives             |n                  |               |                            |learningObjective1                                       |
     |#imageUrl                       |n                  |               |                            |35d5b71d1a8a54dd58/download/public?format=ORIGINAL       |
     |#media                          |n                  |               |                            |TEXT                                                     |
     |#questionPrompt                 |n                  |               |                            |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _             |
     |#promptType                     |n                  |               |                            |TEXT                                                     |
     |#timeout                        |n                  |               |                            |60                                                       |
     |#rationale                      |n                  |               |                            |rationale                                                |
     |#boxId                          |n                  |               |                            |0                                                        |
     |#correctAttempts                |n                  |               |                            |1                                                        |
     |#inCorrectAttempts              |n                  |               |                            |0                                                        |
     |#lastAswered                    |n                  |               |                            |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |n                  |               |                            |0                                                        |
     |#skips                          |n                  |               |                            |0                                                        |
     |#userId                         |n                  |               |                            |0                                                        |
     |#correctAnswerList              |n                  |               |                            |1,2                                                      |
     |#answer2Id                      |n                  |               |                            |2                                                        |
     |#answer2Value                   |n                  |               |                            |Osanda                                                   |
     |#answer2Type                    |n                  |               |                            |TEXT                                                     |
     |#answer2CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer1Id                      |n                  |               |                            |1                                                        |
     |#answer1Value                   |n                  |               |                            |Gemunu                                                   |
     |#answer1Type                    |n                  |               |                            |TEXT                                                     |
     |#answer1CaseSensitive           |n                  |               |                            |true                                                     |
     |#answer3Id                      |n                  |               |                            |3                                                        |
     |#answer3Value                   |n                  |               |                            |Eranga                                                   |
     |#answer3Type                    |n                  |               |                            |TEXT                                                     |
     |#answer3CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer4Id                      |n                  |               |                            |4                                                        |
     |#answer4Value                   |n                  |               |                            |Heshan                                                   |
     |#answer4Type                    |n                  |               |                            |TEXT                                                     |
     |#answer4CaseSensitive           |n                  |               |                            |false                                                    |
     |#answer5Id                      |n                  |               |                            |5                                                        |
     |#answer5Value                   |n                  |               |                            |Thilina                                                  |
     |#answer5Type                    |n                  |               |                            |TEXT                                                     |
     |#answer5CaseSensitive           |n                  |               |                            |true                                                     |
     |#tags                           |n                  |               |                            |MaxSoft                                                  |
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












