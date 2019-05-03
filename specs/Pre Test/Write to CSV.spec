# Write to CSV Specification

Project Name : MaxSoft-IntelliAPI
Developer    : Osanda Deshan
Version      : 1.0.0
Date         : 6/7/2018
Time         : 9:30 PM
Description  : This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.



## Get all questions of a deck using a valid deckId

* Add 4 questions into a deck by deckId saved in "Spec" type data store named "deckIdWith4Questions"

* Given that a user needs to invoke "Get All Questions Of Deck"
* And the user set the query parameters using data stores as follows 

   |Query Parameter|Is Data Store Used?|Data Store Type|Data Store Variable Name|Query Value|
   |---------------|-------------------|---------------|------------------------|-----------|
   |deckId         |y                  |Spec           |deckIdWith4Questions    |           |
* And the user set the request authentication configurations as follows 

   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |Yes                |
   |Do you need to retrieve the access token from the text file?      |Yes                |
   |Provide the access token if you need to authorize the API manually|N/A                |
* When the user invokes the API
* Then the status code for the request is "200"
* And save the JSON Array values of the response into CSV files 

   |JSON Path        |Header Name|CSV File Path                 |
   |-----------------|-----------|------------------------------|
   |$.questions[*].id|questionId |/resources/csv/questionIds.csv|

* Delete deck by deckId saved in "Spec" type data store named "deckIdWith4Questions"
