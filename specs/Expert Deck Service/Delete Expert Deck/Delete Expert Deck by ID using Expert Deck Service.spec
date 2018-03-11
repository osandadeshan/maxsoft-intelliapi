Delete Expert Deck by ID using Expert Deck Service Specification
================================================================
Date Created    : 01/20/2017
Version   		: 1.0.0
Owner      		: Kinkini Gamage
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.


tags: delete_expert_deck


* Create an expert deck
* And save the JSON Path values in the response inside the data stores
    |DataStore Type |Variable Name  |Value To Be Stored     |
    |---------------|---------------|-----------------------|
    |scenario       |expertDeckId   |$.id                   |
* Given that a user needs to invoke "Delete Expert Deck by ID using Expert Deck Service"
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |
* And the user set the path parameters using data stores as follows
    |Path Name      |Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value     |
    |---------------|-------------------|---------------|------------------------|---------------|
    |expertDeckId   |y                  |scenario       |expertDeckId            |N/A            |



Delete an expert deck using existing expertDeckId
-------------------------------------------------
tags: delete_expert_deck, positive

* When the user invokes the API
* Then the status code for the request is "200"



Delete an expert deck using already deleted expertDeckId
--------------------------------------------------------
tags: delete_expert_deck, negative

* And the user set the path parameters as follows
     |Path Parameter Name|Path Parameter Value     |
     |-------------------|-------------------------|
     |Id                 |5a62e5b415620613dc8abc5d |
* When the user invokes the API
* Then the status code for the request is "404"



Delete an expert deck using already invalid expertDeckId
--------------------------------------------------------
tags: delete_expert_deck, negative

* And the user set the path parameters as follows
     |Path Parameter Name|Path Parameter Value     |
     |-------------------|-------------------------|
     |Id                 |abc                      |
* When the user invokes the API
* Then the status code for the request is "404"



