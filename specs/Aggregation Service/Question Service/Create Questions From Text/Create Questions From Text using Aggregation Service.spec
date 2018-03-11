Create Questions From Text using Aggregation Service Specification
==================================================================
Date Created    : 02/04/2018
Version   		: 1.0.0
Owner      		: Osanda Deshan
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.


tags: create_questions_from_text, create_questions_from_text-positive_tests, positive


table: /resources/data_driven_test_csv/create_questions_from_text/create_questions_from_text-positive_tests.csv



* Create a deck
* And save the JSON Path values in the response inside the data stores
    |DataStore Type |Variable Name  |Value To Be Stored     |
    |---------------|---------------|-----------------------|
    |scenario       |deckId         |$.id                   |
* Given that a user needs to invoke <api>
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |



Create Questions from Text using a valid payload
------------------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template |Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value         |
     |---------------------------------|-------------------|---------------|------------------------|-------------------|
     |#deckId                          |y                  |scenario       |deckId                  |N/A                |
     |#timeout                         |n                  |               |                        |<timeout>          |
     |#media                           |n                  |               |                        |<media>            |
     |#imageUrl                        |n                  |               |                        |<imageUrl>         |
     |#promptType                      |n                  |               |                        |<promptType>       |
     |#creatorId                       |n                  |               |                        |<creatorId>        |
     |#creatorPlatform                 |n                  |               |                        |<creatorPlatform>  |
     |#creatoredSource                 |n                  |               |                        |<creatoredSource>  |
     |#creatoredType                   |n                  |               |                        |<creatoredType>    |
     |#title                           |n                  |               |                        |<title>            |
     |#userId                          |n                  |               |                        |<userId>           |
     |#isExpert                        |n                  |               |                        |<isExpert>         |
     |#questionText                    |n                  |               |                        |<questionText>     |
* When the user invokes the API
* Then the status code for the request is "201"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                    |Value                                                    |
     |---------------------------------------------|---------------------------------------------------------|
     |$[0].question.media                          |<media>                                                  |
     |$[0].question.imageUrl                       |<imageUrl>                                               |
     |$[0].question.promptType                     |<promptType>                                             |
     |$[0].question.timeout                        |<timeout>                                                |
     |$[0].stats                                   |null                                                     |
     |$[0].kind                                    |<kind>                                                   |
     |$[0].learningObjectives[0]                   |Empty                                                    |
     |$[0].rationale                               |Test Rationalae                                          |
     |$[0].creatorId                               |<creatorId>                                              |
     |$[0].creatoredType                           |Auto                                                     |
     |$[0].creatorPlatform                         |<creatorPlatform>                                        |
     |$[0].creatoredSource                         |<creatoredSource>                                        |
     |$[0].correctAnswers                          |null                                                     |