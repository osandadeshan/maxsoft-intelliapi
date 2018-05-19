Create Short Answer Type Question using Aggregation Service - Positive Test Specification
=========================================================================================
Date Created    : 11/06/2017
Version   		: 1.0.0
Owner      		: Osanda Deshan
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.


tags: create_question, create_question_short_answer_type, create_question-positive_tests, positive



* Create a deck
* And save the JSON Path values in the response inside the data stores
    |DataStore Type |Variable Name              |Value To Be Stored     |
    |---------------|---------------------------|-----------------------|
    |scenario       |deckId                     |$.id                   |
* Given that a user needs to invoke "Create Short Answer Type Question using Aggregation Service"
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |



Create a question using a decimal value as the boxId
----------------------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name    |Attribute Value To Be Set                                |
     |--------------------------------|-------------------|---------------|----------------------------|---------------------------------------------------------|
     |#creatorId                      |n                  |               |                            |osanda12                                                 |
     |#creatorPlatform                |n                  |               |                            |Web                                                      |
     |#creatoredSource                |n                  |               |                            |App                                                      |
     |#creatoredType                  |n                  |               |                            |Manual                                                   |
     |#deckId                         |y                  |scenario       |deckId                      |                                                         |
     |#isDeleted                      |n                  |               |                            |false                                                    |
     |#tempQuestionId                 |n                  |               |                            |testId                                                   |
     |#kind                           |n                  |               |                            |SHORT_ANSWER                                             |
     |#learningObjectives             |n                  |               |                            |objective1                                               |
     |#imageUrl                       |n                  |               |                            |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |n                  |               |                            |TEXT                                                     |
     |#questionPrompt                 |n                  |               |                            |Who is the owner of MaxSoft?                             |
     |#promptType                     |n                  |               |                            |TEXT                                                     |
     |#timeout                        |n                  |               |                            |120                                                      |
     |#rationale                      |n                  |               |                            |rationale                                                |
     |#boxId                          |n                  |               |                            |5.5                                                      |
     |#correctAttempts                |n                  |               |                            |1                                                        |
     |#inCorrectAttempts              |n                  |               |                            |0                                                        |
     |#lastAswered                    |n                  |               |                            |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |n                  |               |                            |0                                                        |
     |#skips                          |n                  |               |                            |0                                                        |
     |#userId                         |n                  |               |                            |0                                                        |
     |#correctAnswerId                |n                  |               |                            |1                                                        |
     |#correctAnswerValue             |n                  |               |                            |Osanda Deshan                                            |
     |#iscorrectAnswerCaseSensitive   |n                  |               |                            |false                                                    |
     |#correctAnswerType              |n                  |               |                            |TEXT                                                     |
     |#tags                           |n                  |               |                            |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "201"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.stats.boxId                             |5                                                        |



Create a question using a decimal value as the userId
-----------------------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name    |Attribute Value To Be Set                                |
     |--------------------------------|-------------------|---------------|----------------------------|---------------------------------------------------------|
     |#creatorId                      |n                  |               |                            |osanda12                                                 |
     |#creatorPlatform                |n                  |               |                            |Web                                                      |
     |#creatoredSource                |n                  |               |                            |App                                                      |
     |#creatoredType                  |n                  |               |                            |Manual                                                   |
     |#deckId                         |y                  |scenario       |deckId                      |                                                         |
     |#isDeleted                      |n                  |               |                            |false                                                    |
     |#tempQuestionId                 |n                  |               |                            |testId                                                   |
     |#kind                           |n                  |               |                            |SHORT_ANSWER                                             |
     |#learningObjectives             |n                  |               |                            |objective1                                               |
     |#imageUrl                       |n                  |               |                            |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |n                  |               |                            |TEXT                                                     |
     |#questionPrompt                 |n                  |               |                            |Who is the owner of MaxSoft?                             |
     |#promptType                     |n                  |               |                            |TEXT                                                     |
     |#timeout                        |n                  |               |                            |120                                                      |
     |#rationale                      |n                  |               |                            |rationale                                                |
     |#boxId                          |n                  |               |                            |5                                                        |
     |#correctAttempts                |n                  |               |                            |1                                                        |
     |#inCorrectAttempts              |n                  |               |                            |0                                                        |
     |#lastAswered                    |n                  |               |                            |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |n                  |               |                            |0                                                        |
     |#skips                          |n                  |               |                            |0                                                        |
     |#userId                         |n                  |               |                            |2.5                                                      |
     |#correctAnswerId                |n                  |               |                            |1                                                        |
     |#correctAnswerValue             |n                  |               |                            |Osanda Deshan                                            |
     |#iscorrectAnswerCaseSensitive   |n                  |               |                            |false                                                    |
     |#correctAnswerType              |n                  |               |                            |TEXT                                                     |
     |#tags                           |n                  |               |                            |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "201"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.stats.userId                            |2                                                        |



Create a question using a decimal value as the questionId
---------------------------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name    |Attribute Value To Be Set                                |
     |--------------------------------|-------------------|---------------|----------------------------|---------------------------------------------------------|
     |#creatorId                      |n                  |               |                            |osanda12                                                 |
     |#creatorPlatform                |n                  |               |                            |Web                                                      |
     |#creatoredSource                |n                  |               |                            |App                                                      |
     |#creatoredType                  |n                  |               |                            |Manual                                                   |
     |#deckId                         |y                  |scenario       |deckId                      |                                                         |
     |#isDeleted                      |n                  |               |                            |false                                                    |
     |#tempQuestionId                 |n                  |               |                            |testId                                                   |
     |#kind                           |n                  |               |                            |SHORT_ANSWER                                             |
     |#learningObjectives             |n                  |               |                            |objective1                                               |
     |#imageUrl                       |n                  |               |                            |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |n                  |               |                            |TEXT                                                     |
     |#questionPrompt                 |n                  |               |                            |Who is the owner of MaxSoft?                             |
     |#promptType                     |n                  |               |                            |TEXT                                                     |
     |#timeout                        |n                  |               |                            |120                                                      |
     |#rationale                      |n                  |               |                            |rationale                                                |
     |#boxId                          |n                  |               |                            |5                                                        |
     |#correctAttempts                |n                  |               |                            |1                                                        |
     |#inCorrectAttempts              |n                  |               |                            |0                                                        |
     |#lastAswered                    |n                  |               |                            |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |n                  |               |                            |1.2                                                      |
     |#skips                          |n                  |               |                            |0                                                        |
     |#userId                         |n                  |               |                            |0                                                        |
     |#correctAnswerId                |n                  |               |                            |1                                                        |
     |#correctAnswerValue             |n                  |               |                            |Osanda Deshan                                            |
     |#iscorrectAnswerCaseSensitive   |n                  |               |                            |false                                                    |
     |#correctAnswerType              |n                  |               |                            |TEXT                                                     |
     |#tags                           |n                  |               |                            |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "201"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.stats.questionId                        |1                                                        |



Create a question using an empty value as the lastAswered
---------------------------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name    |Attribute Value To Be Set                                |
     |--------------------------------|-------------------|---------------|----------------------------|---------------------------------------------------------|
     |#creatorId                      |n                  |               |                            |osanda12                                                 |
     |#creatorPlatform                |n                  |               |                            |Web                                                      |
     |#creatoredSource                |n                  |               |                            |App                                                      |
     |#creatoredType                  |n                  |               |                            |Manual                                                   |
     |#deckId                         |y                  |scenario       |deckId                      |                                                         |
     |#isDeleted                      |n                  |               |                            |false                                                    |
     |#tempQuestionId                 |n                  |               |                            |testId                                                   |
     |#kind                           |n                  |               |                            |SHORT_ANSWER                                             |
     |#learningObjectives             |n                  |               |                            |objective1                                               |
     |#imageUrl                       |n                  |               |                            |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |n                  |               |                            |TEXT                                                     |
     |#questionPrompt                 |n                  |               |                            |Who is the owner of MaxSoft?                             |
     |#promptType                     |n                  |               |                            |TEXT                                                     |
     |#timeout                        |n                  |               |                            |120                                                      |
     |#rationale                      |n                  |               |                            |rationale                                                |
     |#boxId                          |n                  |               |                            |5                                                        |
     |#correctAttempts                |n                  |               |                            |1                                                        |
     |#inCorrectAttempts              |n                  |               |                            |0                                                        |
     |#lastAswered                    |n                  |               |                            |                                                         |
     |#questionId                     |n                  |               |                            |2                                                        |
     |#skips                          |n                  |               |                            |0                                                        |
     |#userId                         |n                  |               |                            |0                                                        |
     |#correctAnswerId                |n                  |               |                            |1                                                        |
     |#correctAnswerValue             |n                  |               |                            |Osanda Deshan                                            |
     |#iscorrectAnswerCaseSensitive   |n                  |               |                            |false                                                    |
     |#correctAnswerType              |n                  |               |                            |TEXT                                                     |
     |#tags                           |n                  |               |                            |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "201"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.stats.lastAswered                       |null                                                     |



Create a question using a decimal value as the inCorrectAttempts
----------------------------------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name    |Attribute Value To Be Set                                |
     |--------------------------------|-------------------|---------------|----------------------------|---------------------------------------------------------|
     |#creatorId                      |n                  |               |                            |osanda12                                                 |
     |#creatorPlatform                |n                  |               |                            |Web                                                      |
     |#creatoredSource                |n                  |               |                            |App                                                      |
     |#creatoredType                  |n                  |               |                            |Manual                                                   |
     |#deckId                         |y                  |scenario       |deckId                      |                                                         |
     |#isDeleted                      |n                  |               |                            |false                                                    |
     |#tempQuestionId                 |n                  |               |                            |testId                                                   |
     |#kind                           |n                  |               |                            |SHORT_ANSWER                                             |
     |#learningObjectives             |n                  |               |                            |objective1                                               |
     |#imageUrl                       |n                  |               |                            |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |n                  |               |                            |TEXT                                                     |
     |#questionPrompt                 |n                  |               |                            |Who is the owner of MaxSoft?                             |
     |#promptType                     |n                  |               |                            |TEXT                                                     |
     |#timeout                        |n                  |               |                            |120                                                      |
     |#rationale                      |n                  |               |                            |rationale                                                |
     |#boxId                          |n                  |               |                            |5                                                        |
     |#correctAttempts                |n                  |               |                            |1                                                        |
     |#inCorrectAttempts              |n                  |               |                            |2.5                                                      |
     |#lastAswered                    |n                  |               |                            |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |n                  |               |                            |0                                                        |
     |#skips                          |n                  |               |                            |0                                                        |
     |#userId                         |n                  |               |                            |0                                                        |
     |#correctAnswerId                |n                  |               |                            |1                                                        |
     |#correctAnswerValue             |n                  |               |                            |Osanda Deshan                                            |
     |#iscorrectAnswerCaseSensitive   |n                  |               |                            |false                                                    |
     |#correctAnswerType              |n                  |               |                            |TEXT                                                     |
     |#tags                           |n                  |               |                            |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "201"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.stats.inCorrectAttempts                 |2                                                        |



Create a question using a decimal value as the correctAttempts
--------------------------------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name    |Attribute Value To Be Set                                |
     |--------------------------------|-------------------|---------------|----------------------------|---------------------------------------------------------|
     |#creatorId                      |n                  |               |                            |osanda12                                                 |
     |#creatorPlatform                |n                  |               |                            |Web                                                      |
     |#creatoredSource                |n                  |               |                            |App                                                      |
     |#creatoredType                  |n                  |               |                            |Manual                                                   |
     |#deckId                         |y                  |scenario       |deckId                      |                                                         |
     |#isDeleted                      |n                  |               |                            |false                                                    |
     |#tempQuestionId                 |n                  |               |                            |testId                                                   |
     |#kind                           |n                  |               |                            |SHORT_ANSWER                                             |
     |#learningObjectives             |n                  |               |                            |objective1                                               |
     |#imageUrl                       |n                  |               |                            |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |n                  |               |                            |TEXT                                                     |
     |#questionPrompt                 |n                  |               |                            |Who is the owner of MaxSoft?                             |
     |#promptType                     |n                  |               |                            |TEXT                                                     |
     |#timeout                        |n                  |               |                            |120                                                      |
     |#rationale                      |n                  |               |                            |rationale                                                |
     |#boxId                          |n                  |               |                            |5                                                        |
     |#correctAttempts                |n                  |               |                            |1.1                                                      |
     |#inCorrectAttempts              |n                  |               |                            |0                                                        |
     |#lastAswered                    |n                  |               |                            |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |n                  |               |                            |0                                                        |
     |#skips                          |n                  |               |                            |0                                                        |
     |#userId                         |n                  |               |                            |0                                                        |
     |#correctAnswerId                |n                  |               |                            |1                                                        |
     |#correctAnswerValue             |n                  |               |                            |Osanda Deshan                                            |
     |#iscorrectAnswerCaseSensitive   |n                  |               |                            |false                                                    |
     |#correctAnswerType              |n                  |               |                            |TEXT                                                     |
     |#tags                           |n                  |               |                            |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "201"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.stats.correctAttempts                   |1                                                        |



Create a question using a decimal value as the skips
----------------------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name    |Attribute Value To Be Set                                |
     |--------------------------------|-------------------|---------------|----------------------------|---------------------------------------------------------|
     |#creatorId                      |n                  |               |                            |osanda12                                                 |
     |#creatorPlatform                |n                  |               |                            |Web                                                      |
     |#creatoredSource                |n                  |               |                            |App                                                      |
     |#creatoredType                  |n                  |               |                            |Manual                                                   |
     |#deckId                         |y                  |scenario       |deckId                      |                                                         |
     |#isDeleted                      |n                  |               |                            |false                                                    |
     |#tempQuestionId                 |n                  |               |                            |testId                                                   |
     |#kind                           |n                  |               |                            |SHORT_ANSWER                                             |
     |#learningObjectives             |n                  |               |                            |objective1                                               |
     |#imageUrl                       |n                  |               |                            |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |n                  |               |                            |TEXT                                                     |
     |#questionPrompt                 |n                  |               |                            |Who is the owner of MaxSoft?                             |
     |#promptType                     |n                  |               |                            |TEXT                                                     |
     |#timeout                        |n                  |               |                            |120                                                      |
     |#rationale                      |n                  |               |                            |rationale                                                |
     |#boxId                          |n                  |               |                            |5                                                        |
     |#correctAttempts                |n                  |               |                            |1                                                        |
     |#inCorrectAttempts              |n                  |               |                            |0                                                        |
     |#lastAswered                    |n                  |               |                            |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |n                  |               |                            |0                                                        |
     |#skips                          |n                  |               |                            |2.2                                                      |
     |#userId                         |n                  |               |                            |0                                                        |
     |#correctAnswerId                |n                  |               |                            |1                                                        |
     |#correctAnswerValue             |n                  |               |                            |Osanda Deshan                                            |
     |#iscorrectAnswerCaseSensitive   |n                  |               |                            |false                                                    |
     |#correctAnswerType              |n                  |               |                            |TEXT                                                     |
     |#tags                           |n                  |               |                            |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "201"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.stats.skips                             |2                                                        |



Create a question using an empty learningObjective
--------------------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name    |Attribute Value To Be Set                                |
     |--------------------------------|-------------------|---------------|----------------------------|---------------------------------------------------------|
     |#creatorId                      |n                  |               |                            |osanda12                                                 |
     |#creatorPlatform                |n                  |               |                            |Web                                                      |
     |#creatoredSource                |n                  |               |                            |App                                                      |
     |#creatoredType                  |n                  |               |                            |Manual                                                   |
     |#deckId                         |y                  |scenario       |deckId                      |                                                         |
     |#isDeleted                      |n                  |               |                            |false                                                    |
     |#tempQuestionId                 |n                  |               |                            |testId                                                   |
     |#kind                           |n                  |               |                            |SHORT_ANSWER                                             |
     |#learningObjectives             |n                  |               |                            |                                                         |
     |#imageUrl                       |n                  |               |                            |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |n                  |               |                            |TEXT                                                     |
     |#questionPrompt                 |n                  |               |                            |Who is the owner of MaxSoft?                             |
     |#promptType                     |n                  |               |                            |TEXT                                                     |
     |#timeout                        |n                  |               |                            |120                                                      |
     |#rationale                      |n                  |               |                            |rationale                                                |
     |#boxId                          |n                  |               |                            |5                                                        |
     |#correctAttempts                |n                  |               |                            |1                                                        |
     |#inCorrectAttempts              |n                  |               |                            |0                                                        |
     |#lastAswered                    |n                  |               |                            |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |n                  |               |                            |0                                                        |
     |#skips                          |n                  |               |                            |0                                                        |
     |#userId                         |n                  |               |                            |0                                                        |
     |#correctAnswerId                |n                  |               |                            |1                                                        |
     |#correctAnswerValue             |n                  |               |                            |Osanda Deshan                                            |
     |#iscorrectAnswerCaseSensitive   |n                  |               |                            |false                                                    |
     |#correctAnswerType              |n                  |               |                            |TEXT                                                     |
     |#tags                           |n                  |               |                            |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "201"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.learningObjectives[0]                   |                                                         |



Create a question using a positive integer value as the iscorrectAnswerCaseSensitive
------------------------------------------------------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name    |Attribute Value To Be Set                                |
     |--------------------------------|-------------------|---------------|----------------------------|---------------------------------------------------------|
     |#creatorId                      |n                  |               |                            |osanda12                                                 |
     |#creatorPlatform                |n                  |               |                            |Web                                                      |
     |#creatoredSource                |n                  |               |                            |App                                                      |
     |#creatoredType                  |n                  |               |                            |Manual                                                   |
     |#deckId                         |y                  |scenario       |deckId                      |                                                         |
     |#isDeleted                      |n                  |               |                            |false                                                    |
     |#tempQuestionId                 |n                  |               |                            |testId                                                   |
     |#kind                           |n                  |               |                            |SHORT_ANSWER                                             |
     |#learningObjectives             |n                  |               |                            |objective1                                               |
     |#imageUrl                       |n                  |               |                            |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |n                  |               |                            |TEXT                                                     |
     |#questionPrompt                 |n                  |               |                            |Who is the owner of MaxSoft?                             |
     |#promptType                     |n                  |               |                            |TEXT                                                     |
     |#timeout                        |n                  |               |                            |120                                                      |
     |#rationale                      |n                  |               |                            |rationale                                                |
     |#boxId                          |n                  |               |                            |5                                                        |
     |#correctAttempts                |n                  |               |                            |1                                                        |
     |#inCorrectAttempts              |n                  |               |                            |0                                                        |
     |#lastAswered                    |n                  |               |                            |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |n                  |               |                            |0                                                        |
     |#skips                          |n                  |               |                            |0                                                        |
     |#userId                         |n                  |               |                            |0                                                        |
     |#correctAnswerId                |n                  |               |                            |1                                                        |
     |#correctAnswerValue             |n                  |               |                            |Osanda Deshan                                            |
     |#iscorrectAnswerCaseSensitive   |n                  |               |                            |12344                                                    |
     |#correctAnswerType              |n                  |               |                            |TEXT                                                     |
     |#tags                           |n                  |               |                            |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "201"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.answers[0].caseSensitive                |true                                                     |



Create a question using negative integer value as the iscorrectAnswerCaseSensitive
----------------------------------------------------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name    |Attribute Value To Be Set                                |
     |--------------------------------|-------------------|---------------|----------------------------|---------------------------------------------------------|
     |#creatorId                      |n                  |               |                            |osanda12                                                 |
     |#creatorPlatform                |n                  |               |                            |Web                                                      |
     |#creatoredSource                |n                  |               |                            |App                                                      |
     |#creatoredType                  |n                  |               |                            |Manual                                                   |
     |#deckId                         |y                  |scenario       |deckId                      |                                                         |
     |#isDeleted                      |n                  |               |                            |false                                                    |
     |#tempQuestionId                 |n                  |               |                            |testId                                                   |
     |#kind                           |n                  |               |                            |SHORT_ANSWER                                             |
     |#learningObjectives             |n                  |               |                            |objective1                                               |
     |#imageUrl                       |n                  |               |                            |https://documentservice-qa.stg-prsn.com/api/v1/documents/5a155f35d5b71d1a8a54dd58/download/public?format=ORIGINAL                                    |
     |#media                          |n                  |               |                            |TEXT                                                     |
     |#questionPrompt                 |n                  |               |                            |Who is the owner of MaxSoft?                             |
     |#promptType                     |n                  |               |                            |TEXT                                                     |
     |#timeout                        |n                  |               |                            |120                                                      |
     |#rationale                      |n                  |               |                            |rationale                                                |
     |#boxId                          |n                  |               |                            |5                                                        |
     |#correctAttempts                |n                  |               |                            |1                                                        |
     |#inCorrectAttempts              |n                  |               |                            |0                                                        |
     |#lastAswered                    |n                  |               |                            |2018-01-01T12:00:00+01:00                                |
     |#questionId                     |n                  |               |                            |0                                                        |
     |#skips                          |n                  |               |                            |0                                                        |
     |#userId                         |n                  |               |                            |0                                                        |
     |#correctAnswerId                |n                  |               |                            |1                                                        |
     |#correctAnswerValue             |n                  |               |                            |Osanda Deshan                                            |
     |#iscorrectAnswerCaseSensitive   |n                  |               |                            |-1233                                                    |
     |#correctAnswerType              |n                  |               |                            |TEXT                                                     |
     |#tags                           |n                  |               |                            |MaxSoft                                                  |
* When the user invokes the API
* Then the status code for the request is "201"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.answers[0].caseSensitive                |true                                                     |
