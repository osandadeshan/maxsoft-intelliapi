# Get All Questions In A Deck using Aggregation Service Specification
Date Created    : 11/06/2017
Version   		: 1.0.0
Owner      		: Osanda Deshan
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.


tags: get_all_questions_in_a_deck, ci_ready



## Get all questions of a deck
* Create a my deck with all types of 9 questions
* Given that a user needs to invoke "Get all Questions using Aggregation Service"
* And the user set the request authentication configurations as follows 

   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |Yes                |
   |Do you need to retrieve the access token from the text file?      |Yes                |
   |Provide the access token if you need to authorize the API manually|N/A                |
* And the user set the query parameters using data stores as follows 

   |Query Name|Is Data Store Used?|Data Store Type|Data Store Variable Name|Query Value|
   |----------|-------------------|---------------|------------------------|-----------|
   |deckId    |y                  |spec           |myDeckIdWith9Questions  |N/A        |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following 

   |JSON Path                            |Value                                       |
   |-------------------------------------|--------------------------------------------|
   |$.questions.[-1:].question.prompt    |Who is the owner of MaxSoft? _ _ _ _ _ _ _ _|
   |$.questions.[-1:].question.media     |TEXT                                        |
   |$.questions.[-1:].question.promptType|TEXT                                        |
   |$.questions.[-1:].creatoredSource    |App                                         |
   |$.questions.[-1:].answers.[0].type   |TEXT                                        |
