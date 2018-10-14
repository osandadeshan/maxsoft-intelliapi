# Delete a Question using Aggregation Service Specification
Date Created    : 11/14/2017
Version   		: 1.0.0
Owner      		: Osanda Deshan
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.


tags: delete_a_question, ci_ready



## Delete the only question using valid question id (short answer type)
* Create a short answer type question
* And save the JSON Path values in the response inside the data stores 

   |DataStore Type|Variable Name|Value To Be Stored|
   |--------------|-------------|------------------|
   |scenario      |questionId   |$.id              |
* Given that a user needs to invoke "Delete a Question using Aggregation Service"
* And the user set the request authentication configurations as follows 

   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |Yes                |
   |Do you need to retrieve the access token from the text file?      |Yes                |
   |Provide the access token if you need to authorize the API manually|N/A                |
* And the user set the path parameters using data stores as follows 

   |Path Name |Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value|
   |----------|-------------------|---------------|------------------------|----------|
   |questionId|y                  |scenario       |questionId              |N/A       |
* When the user invokes the API
* Then the status code for the request is "204"

## Delete the only question using valid question id (MCQ type)
* Create a MCQ question using Aggregation Service
* And save the JSON Path values in the response inside the data stores 

   |DataStore Type|Variable Name|Value To Be Stored|
   |--------------|-------------|------------------|
   |scenario      |questionId   |$.id              |
* Given that a user needs to invoke "Delete a Question using Aggregation Service"
* And the user set the request authentication configurations as follows 

   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |Yes                |
   |Do you need to retrieve the access token from the text file?      |Yes                |
   |Provide the access token if you need to authorize the API manually|N/A                |
* And the user set the path parameters using data stores as follows 

   |Path Name |Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value|
   |----------|-------------------|---------------|------------------------|----------|
   |questionId|y                  |scenario       |questionId              |N/A       |
* When the user invokes the API
* Then the status code for the request is "204"

## Delete the only question using valid question id (ALL type)
* Create an All type question using Aggregation Service
* And save the JSON Path values in the response inside the data stores 

   |DataStore Type|Variable Name|Value To Be Stored|
   |--------------|-------------|------------------|
   |scenario      |questionId   |$.id              |
* Given that a user needs to invoke "Delete a Question using Aggregation Service"
* And the user set the request authentication configurations as follows 

   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |Yes                |
   |Do you need to retrieve the access token from the text file?      |Yes                |
   |Provide the access token if you need to authorize the API manually|N/A                |
* And the user set the path parameters using data stores as follows 

   |Path Name |Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value|
   |----------|-------------------|---------------|------------------------|----------|
   |questionId|y                  |scenario       |questionId              |N/A       |
* When the user invokes the API
* Then the status code for the request is "204"

## Delete the second question using valid question id (short answer type)
* Create a my deck with all types of 9 questions
* Given that a user needs to invoke "Delete a Question using Aggregation Service"
* And the user set the request authentication configurations as follows 

   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |Yes                |
   |Do you need to retrieve the access token from the text file?      |Yes                |
   |Provide the access token if you need to authorize the API manually|N/A                |
* And the user set the path parameters using data stores as follows 

   |Path Name |Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value|
   |----------|-------------------|---------------|------------------------|----------|
   |questionId|y                  |scenario       |cardId2                 |N/A       |
* When the user invokes the API
* Then the status code for the request is "204"

## Delete the second last question using valid question id (MCQ type)
* Create a deck with 4 MCQ questions
* Given that a user needs to invoke "Delete a Question using Aggregation Service"
* And the user set the request authentication configurations as follows 

   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |Yes                |
   |Do you need to retrieve the access token from the text file?      |Yes                |
   |Provide the access token if you need to authorize the API manually|N/A                |
* And the user set the path parameters using data stores as follows 

   |Path Name |Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value|
   |----------|-------------------|---------------|------------------------|----------|
   |questionId|y                  |spec           |mcqCardId2              |N/A       |
* When the user invokes the API
* Then the status code for the request is "204"

## Delete the fifth question using valid question id (ALL type)
* Create a my deck with all types of 9 questions
* Given that a user needs to invoke "Delete a Question using Aggregation Service"
* And the user set the request authentication configurations as follows 

   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |Yes                |
   |Do you need to retrieve the access token from the text file?      |Yes                |
   |Provide the access token if you need to authorize the API manually|N/A                |
* And the user set the path parameters using data stores as follows 

   |Path Name |Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value|
   |----------|-------------------|---------------|------------------------|----------|
   |questionId|y                  |scenario       |cardId5                 |N/A       |
* When the user invokes the API
* Then the status code for the request is "204"
