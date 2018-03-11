Get A Category using Deck Service Specification
===============================================
Date Created    : 01/12/2018
Version   		: 1.0.0
Owner      		: Yasith Edirisooriya
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.


tags: get_a_category



Get a category using a valid categoryId
---------------------------------------
* Create a category
* And save the JSON Path values in the response inside the data stores
    |DataStore Type |Variable Name  |Value To Be Stored     |
    |---------------|---------------|-----------------------|
    |scenario       |categoryId     |$.id                   |
* Given that a user needs to invoke "Get A Category in Deck Service"
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |
* And the user set the path parameters using data stores as follows
    |Path Name      |Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value     |
    |---------------|-------------------|---------------|------------------------|---------------|
    |categoryId     |y                  |scenario       |categoryId              |N/A            |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the values inside the data stores
     |JSON Path             |Is Data Store Used?|Data Store Type|Data Store Variable Name|Value                     |
     |----------------------|-------------------|---------------|------------------------|--------------------------|
     |$.id                  |y                  |scenario       |categoryId              |                          |
     |$.name                |n                  |               |                        |Science                   |
     |$.description         |n                  |               |                        |Always learning           |



Get a category using an invalid categoryId
------------------------------------------
* Given that a user needs to invoke "Get A Category in Deck Service"
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |
* And the user set the path parameters as follows
     |Path Parameter |Path Value                |
     |---------------|--------------------------|
     |categoryId     |5a58465d2b77102e0312548c  |
* When the user invokes the API
* Then the status code for the request is "404"



Get a category using null value as the categoryId
-------------------------------------------------
* Given that a user needs to invoke "Get A Category in Deck Service"
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |
* And the user set the path parameters as follows
     |Path Parameter |Path Value                |
     |---------------|--------------------------|
     |categoryId     |null                      |
* When the user invokes the API
* Then the status code for the request is "404"