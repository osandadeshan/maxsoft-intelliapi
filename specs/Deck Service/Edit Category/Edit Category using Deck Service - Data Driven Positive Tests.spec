Edit A Category using Deck Service - Data Driven Positive Tests Specification
=============================================================================
Date Created    : 01/16/2018
Version         : 1.0.0
Owner      	    : Osanda Deshan
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.


tags: edit_category, edit_category-positive_tests, positive


table: /resources/data_driven_test_csv/edit_category/edit_a_category_using_deck_service.csv



* Create a category
* And save the JSON Path values in the response inside the data stores
    |DataStore Type |Variable Name  |Value To Be Stored     |
    |---------------|---------------|-----------------------|
    |spec           |categoryId     |$.id                   |
* Given that a user needs to invoke <api>
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |
* And the user set the path parameters using data stores as follows
    |Path Name      |Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value     |
    |---------------|-------------------|---------------|------------------------|---------------|
    |categoryId     |y                  |spec           |categoryId              |N/A            |



Edit a Category using valid payload
-----------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set               |
     |--------------------------------|----------------------------------------|
     |#name                           |<name>                                  |
     |#description                    |<description>                           |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                         |Value                                   |
     |--------------------------------------------------|----------------------------------------|
     |$.name                                            |<name>                                  |
     |$.description                                     |<description>                           |