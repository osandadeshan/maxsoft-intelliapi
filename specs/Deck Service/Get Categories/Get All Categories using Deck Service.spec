Get All Categories using Deck Service Specification
===================================================
Date Created    : 01/12/2018
Version   		: 1.0.0
Owner      		: Yasith Edirisooriya
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.


tags: get_all_categories



Get all categories using a valid categoryId
-------------------------------------------
* Create a category
* And save the JSON Path values in the response inside the data stores
     |DataStore Type |Variable Name  |Value To Be Stored     |
     |---------------|---------------|-----------------------|
     |scenario       |categoryId     |$.id                   |
* Given that a user needs to invoke "Get All Categories in Deck Service"
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the values inside the data stores
    |JSON Path      |Is Data Store Used?|Data Store Type|Data Store Variable Name|Expected Value |
    |---------------|-------------------|---------------|------------------------|---------------|
    |$[-1:].id      |y                  |scenario       |categoryId              |N/A            |

* And the JSON Path Assertions for the response should be equal to the values inside the data stores
     |JSON Path             |Is Data Store Used?|Data Store Type|Data Store Variable Name|Value                     |
     |----------------------|-------------------|---------------|------------------------|--------------------------|
     |$[-1:].id             |y                  |scenario       |categoryId              |                          |
     |$[-1:].name           |n                  |               |                        |Science                   |
     |$[-1:].description    |n                  |               |                        |Always learning           |



