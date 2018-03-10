Form Data Example Specification
===============================
Date Created    : 03/10/2018
Version   		: 1.0.0
Owner      		: Osanda Deshan
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.



Upload a file using form-data
-----------------------------
* Given that a user needs to invoke "Local File Upload using Aggregation Service"
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |No                             |
     |Do you need to retrieve the access token from the text file?      |N/A                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |
* And the user set the form-data request attributes as follows
     |Form Data Attribute Name        |Form Data Attribute Value      |
     |--------------------------------|-------------------------------|
     |file                            |smartflashcards_system         |
     |creatorId                       |Instructor1                    |
     |creatorPlatform                 |Web                            |
     |creatoredSource                 |File                           |
     |creatoredType                   |Auto                           |
     |deckId                          |5a605b472e02d86561172dad       |
     |examDate                        |                               |
     |isExpert                        |false                          |
     |title                           |Testing local file upload      |
     |userId                          |osan                           |
* When the user invokes the API
* Then the status code for the request is "201"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path     |Expected Result|
     |--------------|---------------|
     |$.status      |success        |