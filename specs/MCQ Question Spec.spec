MCQ Specification
=================
Created by UNimaOs on 12/8/2017

This is an executable specification file which follows markdown syntax.
Every heading in this file denotes a scenario. Every bulleted point denotes a step.


* Given that a user needs to invoke "Create MCQ Type Question"



Create a question using a string value as the answer1Id
-------------------------------------------------------
* And the user set the request authentication configurations as follows
     |Configuration Property Name       |Configuration Property Value   |
     |----------------------------------|-------------------------------|
     |isAccessTokenIncluded             |True                           |
     |isAccessTokenRetrievedFromTextFile|True                           |
     |accessTokenString                 |N/A                            |
     |isHeadersInclueded                |False                          |
     |isJsonBodyIncluded                |True                           |
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



Create a question using a special character as the answer1Id
------------------------------------------------------------
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



Create a question using a negative integer value as the answer1Id
-----------------------------------------------------------------
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



Create a question using an empty value as the answer1Id
-------------------------------------------------------
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



Create a question using null value as the answer1Id
---------------------------------------------------
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



Create a question using empty value as the answer1Value
-------------------------------------------------------
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
     |$.fieldErrors[0].field                    |answers[0].id                                            |
     |$.fieldErrors[0].message                  |Answers id should be a positive integer.                 |
	 
	 
	 
Create a question using null value as the answer1Value
------------------------------------------------------
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
     |#answer1Value                   |null                                                     |
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
	 
	 
Create a question using empty value as the answer1Type
------------------------------------------------------
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
     |$.fieldErrors[0].field                    |answers[0].id                                            |
     |$.fieldErrors[0].message                  |Answers id should be a positive integer.                 |
	 
	 
Create a question using null as the answer1Type
-----------------------------------------------
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
     |#answer1Type                    |null                                                     |
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
	 
	 
Create a question using String as the answer1Type
-------------------------------------------------
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
     |$.fieldErrors[0].field                    |answers[0].id                                            |
     |$.fieldErrors[0].message                  |Answers id should be a positive integer.                 |
	 
	 
Create a question using numbers as the answer1Type
--------------------------------------------------
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
     |$.fieldErrors[0].field                    |answers[0].id                                            |
     |$.fieldErrors[0].message                  |Answers id should be a positive integer.                 |