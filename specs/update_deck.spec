Update A Deck Specification
===========================
Date Created    : 08/23/2017
Version   		: 1.0.0
Owner      		: Osanda Deshan
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.


tags: update_deck



* Given that a user needs to invoke "Update Deck"



Details of testing environment
------------------------------
* Testing environment details



Update a Deck using valid parameters
------------------------------------
* When the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set|
     |--------------------------------|-------------------------|
     |#examDate                       |2017-09-21 15:13:51      |
     |#id                             |1421                     |
     |#isExpert                       |false                    |
     |#title                          |QE Update Test           |
     |#userId                         |Osanda                   |
* When the user invokes the API using the valid access token
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path |Expected Result             |
     |----------|----------------------------|
     |$.title   |QE Update Test              |
     |$.isExpert|false                       |
     |$.examDate|2017-09-21T15:13:51.000+0000|
     |$.userId  |Osanda                      |



Update a Deck using empty exam date
-----------------------------------
* When the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set|
     |--------------------------------|-------------------------|
     |#examDate                       |                         |
     |#id                             |1420                     |
     |#isExpert                       |false                    |
     |#title                          |QE Test                  |
     |#userId                         |Osanda                   |
* When the user invokes the API using the valid access token
* Then the status code for the request is "500"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path    |Expected Result          |
     |-------------|-------------------------|
     |$.message    |error.internalServerError|
     |$.description|Internal server error    |
     |$.fieldErrors|null                     |



Update a Deck using null exam date
----------------------------------
* When the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set|
     |--------------------------------|-------------------------|
     |#examDate                       |null                     |
     |#id                             |1419                     |
     |#isExpert                       |false                    |
     |#title                          |QE Test                  |
     |#userId                         |Osanda                   |
* When the user invokes the API using the valid access token
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                  |Expected Result |
     |---------------------------|----------------|
     |$.message                  |error.validation|
     |$.description              |null            |
     |$.fieldErrors[0].objectName|updateDeckDTO   |
     |$.fieldErrors[0].field     |examDate        |
     |$.fieldErrors[0].message   |NotNull         |



Create a Deck using invalid exam date
-------------------------------------
* When the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set|
     |--------------------------------|-------------------------|
     |#examDate                       |nullable                 |
     |#id                             |1418                     |
     |#isExpert                       |false                    |
     |#title                          |QE Test                  |
     |#userId                         |Osanda                   |
* When the user invokes the API using the valid access token
* Then the status code for the request is "500"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path    |Expected Result          |
     |-------------|-------------------------|
     |$.message    |error.internalServerError|
     |$.description|Internal server error    |
     |$.fieldErrors|null                     |
