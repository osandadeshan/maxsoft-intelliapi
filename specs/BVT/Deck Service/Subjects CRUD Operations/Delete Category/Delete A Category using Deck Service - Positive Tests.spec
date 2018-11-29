# Delete A Category using Deck Service - Positive Test Specification
Date Created    : 01/16/2018
Version   		: 1.0.0
Owner      		: Osanda Deshan
Description  	: This specification covers delete a deck scenarios from the aggregation service


tags: deck_service, deck_management, delete_a_category


* Given that a user needs to invoke "Delete A Category in Deck Service"
* And the user set the request authentication configurations as follows 

   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |Yes                |
   |Do you need to retrieve the access token from the text file?      |Yes                |
   |Provide the access token if you need to authorize the API manually|N/A                |



## Delete a category using valid category id
* Create a category
* And save the JSON Path values in the response inside the data stores 

   |DataStore Type|Variable Name|Value To Be Stored|
   |--------------|-------------|------------------|
   |spec          |categoryId   |$.id              |
* Given that a user needs to invoke "Delete A Category in Deck Service"
* And the user set the path parameters using data stores as follows 

   |Path Name |Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value|
   |----------|-------------------|---------------|------------------------|----------|
   |categoryId|y                  |spec           |categoryId              |N/A       |
* When the user invokes the API
* Then the status code for the request is "200"

