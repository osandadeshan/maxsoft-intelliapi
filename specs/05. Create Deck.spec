Create A Deck Specification
===========================
Date Created    : 08/23/2017
Version   		: 1.0.0
Owner      		: Osanda Deshan
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.


tags: create_deck



* Given that a user needs to invoke "Create Deck"



Details of testing environment
------------------------------
* Get the configuration details of the testing environment



Create a Deck using valid parameters
------------------------------------
* And the user set the request authentication configurations as follows
     |Configuration Property Name       |Configuration Property Value   |
     |----------------------------------|-------------------------------|
     |isAccessTokenIncluded             |True                           |
     |isAccessTokenRetrievedFromTextFile|True                           |
     |accessTokenString                 |N/A                            |
     |isHeadersInclueded                |True                           |
     |isJsonBodyIncluded                |True                           |
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set|
     |--------------------------------|-------------------------|
     |#examDate                       |2017-12-21               |
     |#title                          |QE Test3                 |
     |#userId                         |Osanda                   |
* And the user set the request headers as follows
     |Header Name                     |Header Value             |
     |--------------------------------|-------------------------|
     |X-Platform                      |Authoring                |
* When the user invokes the API
* Then the status code for the request is "201"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path     |Expected Result|
     |--------------|---------------|
     |$.title       |QE Test3       |
     |$.subject.id  |5              |
     |$.subject.name|SUB 1          |
     |$.examDate    |1508544000000  |
     |$.userId      |Osanda         |



Create a Deck using empty exam date
-----------------------------------
* And the user set the request authentication configurations as follows
     |Configuration Property Name       |Configuration Property Value   |
     |----------------------------------|-------------------------------|
     |isAccessTokenIncluded             |True                           |
     |isAccessTokenRetrievedFromTextFile|True                           |
     |accessTokenString                 |N/A                            |
     |isHeadersInclueded                |True                           |
     |isJsonBodyIncluded                |True                           |
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set|
     |--------------------------------|-------------------------|
     |#examDate                       |                         |
     |#subjectId                      |5                        |
     |#title                          |QE Test3                 |
     |#userId                         |Osanda                   |
* And the user set the request headers as follows
     |Header Name                     |Header Value             |
     |--------------------------------|-------------------------|
     |X-Platform                      |Android                  |
* When the user invokes the API
* Then the status code for the request is "201"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path     |Expected Result|
     |--------------|---------------|
     |$.title       |QE Test3       |
     |$.subject.id  |5              |
     |$.subject.name|SUB 1          |
     |$.examDate    |null           |
     |$.userId      |Osanda         |



Create a Deck using null exam date
----------------------------------
* And the user set the request authentication configurations as follows
     |Configuration Property Name       |Configuration Property Value   |
     |----------------------------------|-------------------------------|
     |isAccessTokenIncluded             |True                           |
     |isAccessTokenRetrievedFromTextFile|True                           |
     |accessTokenString                 |N/A                            |
     |isHeadersInclueded                |True                           |
     |isJsonBodyIncluded                |True                           |
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set|
     |--------------------------------|-------------------------|
     |#examDate                       |null                     |
     |#subjectId                      |5                        |
     |#title                          |QE Test3                 |
     |#userId                         |Osanda                   |
* And the user set the request headers as follows
     |Header Name                     |Header Value             |
     |--------------------------------|-------------------------|
     |X-Platform                      |Android                  |
* When the user invokes the API
* Then the status code for the request is "201"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path     |Expected Result|
     |--------------|---------------|
     |$.title       |QE Test3       |
     |$.subject.id  |5              |
     |$.subject.name|SUB 1          |
     |$.examDate    |null           |
     |$.userId      |Osanda         |



Create a Deck using invalid exam date
-------------------------------------
* And the user set the request authentication configurations as follows
     |Configuration Property Name       |Configuration Property Value   |
     |----------------------------------|-------------------------------|
     |isAccessTokenIncluded             |True                           |
     |isAccessTokenRetrievedFromTextFile|True                           |
     |accessTokenString                 |N/A                            |
     |isHeadersInclueded                |True                           |
     |isJsonBodyIncluded                |True                           |
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set|
     |--------------------------------|-------------------------|
     |#examDate                       |this is not a date       |
     |#subjectId                      |5                        |
     |#title                          |QE Test3                 |
     |#userId                         |Osanda                   |
* And the user set the request headers as follows
     |Header Name                     |Header Value             |
     |--------------------------------|-------------------------|
     |X-Platform                      |Android                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path  |Expected Result                                                   |
     |-----------|------------------------------------------------------------------|
     |$.status   |400                                                               |
     |$.error    |Bad Request                                                       |
     |$.exception|org.springframework.http.converter.HttpMessageNotReadableException|
