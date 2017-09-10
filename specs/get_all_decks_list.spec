Get All Decks List Specification
================================
Date Created    : 08/22/2017
Version   		: 1.0.0
Owner      		: Osanda Deshan
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.


tags: get_all_decks_list



Details of testing environment
------------------------------
* Testing environment details



Get all decks list using a valid userId
---------------------------------------
* Given that a user needs to invoke "Get all Decks"
* When the user invokes the API using the following query parameters
     |Query Parameter|Query Value|
     |---------------|-----------|
     |userId         |1          |
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path    |Value                                                  |
     |-------------|-------------------------------------------------------|
     |$[0].id      |182                                                    |
     |$[0].title   |Sociology: Crime, Deviance, and Social Control (Ch. 17)|
     |$[0].isExpert|true                                                   |
     |$[0].userId  |user                                                   |



Get all decks list using an invalid userId
------------------------------------------
* Given that a user needs to invoke "Get all Decks"
* When the user invokes the API using the following query parameters
     |Query Parameter|Query Value|
     |---------------|-----------|
     |userId         |1000       |
* Then the status code for the request is "500"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path    |Value                    |
     |-------------|-------------------------|
     |$.message    |error.internalServerError|
     |$.description|Internal server error    |
     |$.fieldErrors|null                     |



Get all decks list using userId as empty
----------------------------------------
* Given that a user needs to invoke "Get all Decks"
* When the user invokes the API using the following query parameters
     |Query Parameter|Query Value|
     |---------------|-----------|
     |userId         |           |
* Then the status code for the request is "500"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path    |Value                    |
     |-------------|-------------------------|
     |$.message    |error.internalServerError|
     |$.description|Internal server error    |
     |$.fieldErrors|null                     |



Get all decks list using userId as null
---------------------------------------
* Given that a user needs to invoke "Get all Decks"
* When the user invokes the API using the following query parameters
     |Query Parameter|Query Value|
     |---------------|-----------|
     |userId         |null       |
* Then the status code for the request is "500"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path    |Value                    |
     |-------------|-------------------------|
     |$.message    |error.internalServerError|
     |$.description|Internal server error    |
     |$.fieldErrors|null                     |



Get all decks list using an invalid query parameter
---------------------------------------------------
* Given that a user needs to invoke "Get all Decks"
* When the user invokes the API using the following query parameters
     |Query Parameter|Query Value|
     |---------------|-----------|
     |user           |1          |
* Then the status code for the request is "500"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path    |Value                    |
     |-------------|-------------------------|
     |$.message    |error.internalServerError|
     |$.description|Internal server error    |
     |$.fieldErrors|null                     |



Get all decks list using invalid query parameters
-------------------------------------------------
* Given that a user needs to invoke "Get all Decks"
* When the user invokes the API using the following query parameters
     |Query Parameter|Query Value|
     |---------------|-----------|
     |userId         |1          |
     |userIs         |2          |
     |userIa         |3          |
     |userIq         |4          |
* Then the status code for the request is "500"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path    |Value                    |
     |-------------|-------------------------|
     |$.message    |error.internalServerError|
     |$.description|Internal server error    |
     |$.fieldErrors|null                     |



Get all decks list without any query parameters
-----------------------------------------------
* Given that a user needs to invoke "Get all Decks"
* When the user invokes the API using the following query parameters
     |Query Parameter|Query Value|
     |---------------|-----------|
     |               |           |
* Then the status code for the request is "500"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path    |Value                    |
     |-------------|-------------------------|
     |$.message    |error.internalServerError|
     |$.description|Internal server error    |
     |$.fieldErrors|null                     |


