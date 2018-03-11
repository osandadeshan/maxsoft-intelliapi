Edit Short Answer Type Question using Question Service - Positive Test Specification
====================================================================================
Date Created    : 11/15/2017
Version   		: 1.0.0
Owner      		: Osanda Deshan
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.


tags: edit_question, edit_question-positive_tests, positive



* Create a short answer type question
* And save the JSON Path values in the response inside the data stores
    |DataStore Type |Variable Name  |Value To Be Stored     |
    |---------------|---------------|-----------------------|
    |scenario       |questionId     |$.id                   |
* Given that a user needs to invoke "Edit Short Answer Type Question using Question Service"
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



Edit a question using an valid creatorId
----------------------------------------
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
     |#isDeleted                      |true                                                     |
     |#tempQuestionId                 |testId                                                   |
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
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                 |Value                                                    |
     |------------------------------------------|---------------------------------------------------------|
     |$.question.prompt                         |Who is Osanda Deshan?                                    |
     |$.question.media                          |TEXT                                                     |
     |$.question.promptType                     |TEXT                                                     |
     |$.kind                                    |SHORT_ANSWER                                             |
     |$.deleted                                 |true                                                     |
     |$.answers[0].value                        |Osanda Deshan                                            |