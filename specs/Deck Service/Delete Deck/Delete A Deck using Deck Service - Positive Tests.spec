Delete A Deck using Deck Service - Positive Test Specification
==============================================================
Date Created    : 01/09/2018
Version   		: 1.0.0
Owner      		: Osanda Deshan
Description  	: This specification covers delete a deck scenarios from the aggregation service


tags: deck_service, deck_management, delete_a_deck


* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |



Delete a Deck using a valid deckId
----------------------------------
* Create a deck
* And save the JSON Path values in the response inside the data stores
    |DataStore Type |Variable Name  |Value To Be Stored     |
    |---------------|---------------|-----------------------|
    |spec           |deckId         |$.id                   |
* Given that a user needs to invoke "Delete a Deck using Deck Service"
* And the user set the path parameters using data stores as follows
    |Path Name      |Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value     |
    |---------------|-------------------|---------------|------------------------|---------------|
    |deckId         |y                  |spec           |deckId                  |N/A            |
* When the user invokes the API
* Then the status code for the request is "200"




