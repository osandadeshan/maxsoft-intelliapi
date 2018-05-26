Create Questions From Text using Aggregation Service - Positive Test Specification
==================================================================================
Date Created    : 05/23/2018
Version   		: 1.0.0
Owner      		: Osanda Deshan
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.


tags: create_questions_from_text, create_questions_from_text-positive_tests, positive, ci_ready



* Create a deck
* And save the JSON Path values in the response inside the data stores
    |DataStore Type |Variable Name  |Value To Be Stored     |
    |---------------|---------------|-----------------------|
    |scenario       |deckId         |$.id                   |
* Given that a user needs to invoke "Create Questions from Text using Aggregation Service"
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |



Create Questions from Text using multiple paragraphs
----------------------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template |Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value                                       |
     |---------------------------------|-------------------|---------------|------------------------|-------------------------------------------------|
     |#deckId                          |y                  |scenario       |deckId                  |N/A                                              |
     |#timeout                         |n                  |               |                        |200                                              |
     |#media                           |n                  |               |                        |TEXT                                             |
     |#imageUrl                        |n                  |               |                        |http://somehost/someimg.jpg                      |
     |#promptType                      |n                  |               |                        |TEXT                                             |
     |#creatorId                       |n                  |               |                        |osanda                                           |
     |#creatorPlatform                 |n                  |               |                        |Mobile                                           |
     |#creatoredSource                 |n                  |               |                        |Clipper                                          |
     |#creatoredType                   |n                  |               |                        |Auto                                             |
     |#title                           |n                  |               |                        |Cards from text                                  |
     |#userId                          |n                  |               |                        |osan                                             |
     |#isExpert                        |n                  |               |                        |false                                            |
     |#questionText                    |n                  |               |                        |<file:/resources/text_files/paragraphs1.txt>     |
* When the user invokes the API
* Then the status code for the request is "201"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                    |Value                                                    |
     |---------------------------------------------|---------------------------------------------------------|
     |$[0].question.media                          |TEXT                                                     |
     |$[0].question.imageUrl                       |http://somehost/someimg.jpg                              |
     |$[0].question.promptType                     |TEXT                                                     |
     |$[0].question.timeout                        |200                                                      |
     |$[0].stats                                   |null                                                     |
     |$[0].kind                                    |SHORT_ANSWER                                             |
     |$[0].learningObjectives[0]                   |Empty                                                    |
     |$[0].rationale                               |Test Rationalae                                          |
     |$[0].creatorId                               |osanda                                                   |
     |$[0].creatoredType                           |Auto                                                     |
     |$[0].creatorPlatform                         |Mobile                                                   |
     |$[0].creatoredSource                         |Clipper                                                  |
     |$[0].correctAnswers                          |null                                                     |