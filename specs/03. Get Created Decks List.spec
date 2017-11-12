Get Created Decks List Specification
====================================
Date Created    : 09/20/2017
Version   		: 1.0.0
Owner      		: Osanda Deshan
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.


tags: get_created_decks_list



* Given that a user needs to invoke "Get all Decks"



Get created decks list using a valid userId and valid filter
------------------------------------------------------------
* And the user set the request authentication configurations as follows
     |Configuration Property Name       |Configuration Property Value   |
     |----------------------------------|-------------------------------|
     |isAccessTokenIncluded             |True                           |
     |isAccessTokenRetrievedFromTextFile|True                           |
     |accessTokenString                 |N/A                            |
     |isHeadersInclueded                |True                           |
     |isJsonBodyIncluded                |False                          |
* And the user set the request headers as follows
     |Header Name                     |Header Value             |
     |--------------------------------|-------------------------|
     |X-Platform                      |Android                  |
* And the user set the query parameters as follows
     |Query Parameter|Query Value|
     |---------------|-----------|
     |userId         |osanda12   |
     |filter         |created    |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path             |Value     |
     |----------------------|----------|
     |$.[:1].title          |QE Test3  |
     |$.[:1].subject.name   |SUB 1     |
     |$.[:1].userId         |Osanda    |



Get created decks list using a invalid userId and valid filter
--------------------------------------------------------------
* And the user set the request authentication configurations as follows
     |Configuration Property Name       |Configuration Property Value   |
     |----------------------------------|-------------------------------|
     |isAccessTokenIncluded             |True                           |
     |isAccessTokenRetrievedFromTextFile|True                           |
     |accessTokenString                 |N/A                            |
     |isHeadersInclueded                |True                           |
     |isJsonBodyIncluded                |False                          |
* And the user set the request headers as follows
     |Header Name                     |Header Value             |
     |--------------------------------|-------------------------|
     |X-Platform                      |Android                  |
* And the user set the query parameters as follows
     |Query Parameter|Query Value|
     |---------------|-----------|
     |userId         |roo        |
     |filter         |created    |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path|Expected Result|
     |---------|---------------|
     |$        |[]             |



Get created decks list using a empty userId and valid filter
------------------------------------------------------------
* And the user set the request authentication configurations as follows
     |Configuration Property Name       |Configuration Property Value   |
     |----------------------------------|-------------------------------|
     |isAccessTokenIncluded             |True                           |
     |isAccessTokenRetrievedFromTextFile|True                           |
     |accessTokenString                 |N/A                            |
     |isHeadersInclueded                |True                           |
     |isJsonBodyIncluded                |False                          |
* And the user set the request headers as follows
     |Header Name                     |Header Value             |
     |--------------------------------|-------------------------|
     |X-Platform                      |Android                  |
* And the user set the query parameters as follows
     |Query Parameter|Query Value|
     |---------------|-----------|
     |userId         |           |
     |filter         |created    |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path|Expected Result|
     |---------|---------------|
     |$        |[]             |



Get created decks list without any query parameters
---------------------------------------------------
* And the user set the request authentication configurations as follows
     |Configuration Property Name       |Configuration Property Value   |
     |----------------------------------|-------------------------------|
     |isAccessTokenIncluded             |True                           |
     |isAccessTokenRetrievedFromTextFile|True                           |
     |accessTokenString                 |N/A                            |
     |isHeadersInclueded                |True                           |
     |isJsonBodyIncluded                |False                          |
* And the user set the request headers as follows
     |Header Name                     |Header Value             |
     |--------------------------------|-------------------------|
     |X-Platform                      |Android                  |
* And the user set the query parameters as follows
     |Query Parameter|Query Value|
     |---------------|-----------|
     |               |           |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path  |Expected Result                                                     |
     |-----------|--------------------------------------------------------------------|
     |$.status   |400                                                                 |
     |$.error    |Bad Request                                                         |
     |$.message  |Required String parameter 'userId' is not present                   |
     |$.exception|org.springframework.web.bind.MissingServletRequestParameterException|



Get created decks list without userID query parameter
-----------------------------------------------------
* And the user set the request authentication configurations as follows
     |Configuration Property Name       |Configuration Property Value   |
     |----------------------------------|-------------------------------|
     |isAccessTokenIncluded             |True                           |
     |isAccessTokenRetrievedFromTextFile|True                           |
     |accessTokenString                 |N/A                            |
     |isHeadersInclueded                |True                           |
     |isJsonBodyIncluded                |False                          |
* And the user set the request headers as follows
     |Header Name                     |Header Value             |
     |--------------------------------|-------------------------|
     |X-Platform                      |Android                  |
* And the user set the query parameters as follows
     |Query Parameter|Query Value|
     |---------------|-----------|
     |filter         |created    |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path  |Expected Result                                                     |
     |-----------|--------------------------------------------------------------------|
     |$.status   |400                                                                 |
     |$.error    |Bad Request                                                         |
     |$.message  |Required String parameter 'userId' is not present                   |
     |$.exception|org.springframework.web.bind.MissingServletRequestParameterException|



Get created decks list without filter query parameter
-----------------------------------------------------
* And the user set the request authentication configurations as follows
     |Configuration Property Name       |Configuration Property Value   |
     |----------------------------------|-------------------------------|
     |isAccessTokenIncluded             |True                           |
     |isAccessTokenRetrievedFromTextFile|True                           |
     |accessTokenString                 |N/A                            |
     |isHeadersInclueded                |True                           |
     |isJsonBodyIncluded                |False                          |
* And the user set the request headers as follows
     |Header Name                     |Header Value             |
     |--------------------------------|-------------------------|
     |X-Platform                      |Android                  |
* And the user set the query parameters as follows
     |Query Parameter|Query Value|
     |---------------|-----------|
     |userId         |osanda12   |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path  |Expected Result                                                     |
     |-----------|--------------------------------------------------------------------|
     |$.status   |400                                                                 |
     |$.error    |Bad Request                                                         |
     |$.message  |Required String parameter 'filter' is not present                   |
     |$.exception|org.springframework.web.bind.MissingServletRequestParameterException|



Get created decks list with invalid query parameters
----------------------------------------------------
* And the user set the request authentication configurations as follows
     |Configuration Property Name       |Configuration Property Value   |
     |----------------------------------|-------------------------------|
     |isAccessTokenIncluded             |True                           |
     |isAccessTokenRetrievedFromTextFile|True                           |
     |accessTokenString                 |N/A                            |
     |isHeadersInclueded                |True                           |
     |isJsonBodyIncluded                |False                          |
* And the user set the request headers as follows
     |Header Name                     |Header Value             |
     |--------------------------------|-------------------------|
     |X-Platform                      |Android                  |
* And the user set the query parameters as follows
     |Query Parameter|Query Value|
     |---------------|-----------|
     |userId         |osanda12   |
     |filte          |created    |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path  |Expected Result                                                     |
     |-----------|--------------------------------------------------------------------|
     |$.status   |400                                                                 |
     |$.error    |Bad Request                                                         |
     |$.message  |Required String parameter 'filter' is not present                   |
     |$.exception|org.springframework.web.bind.MissingServletRequestParameterException|



Get created decks list using a valid userId and valid filter without access token
---------------------------------------------------------------------------------
* And the user set the request authentication configurations as follows
     |Configuration Property Name       |Configuration Property Value   |
     |----------------------------------|-------------------------------|
     |isAccessTokenIncluded             |False                          |
     |isAccessTokenRetrievedFromTextFile|False                          |
     |accessTokenString                 |N/A                            |
     |isHeadersInclueded                |True                           |
     |isJsonBodyIncluded                |False                          |
* And the user set the request headers as follows
     |Header Name                     |Header Value             |
     |--------------------------------|-------------------------|
     |X-Platform                      |Android                  |
* And the user set the query parameters as follows
     |Query Parameter|Query Value|
     |---------------|-----------|
     |userId         |osanda12   |
     |filter         |created    |
* When the user invokes the API
* Then the status code for the request is "401"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path|Expected Result|
     |---------|---------------|
     |$.status |401            |
     |$.error  |Unauthorized   |
     |$.message|Invalid token  |



Get created decks list using a valid userId and valid filter with empty access token
------------------------------------------------------------------------------------
* And the user set the request authentication configurations as follows
     |Configuration Property Name       |Configuration Property Value   |
     |----------------------------------|-------------------------------|
     |isAccessTokenIncluded             |True                           |
     |isAccessTokenRetrievedFromTextFile|False                          |
     |accessTokenString                 |                               |
     |isHeadersInclueded                |True                           |
     |isJsonBodyIncluded                |False                          |
* And the user set the request headers as follows
     |Header Name                     |Header Value             |
     |--------------------------------|-------------------------|
     |X-Platform                      |Android                  |
* And the user set the query parameters as follows
     |Query Parameter|Query Value|
     |---------------|-----------|
     |userId         |osanda12   |
     |filter         |created    |
* When the user invokes the API
* Then the status code for the request is "401"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path|Expected Result|
     |---------|---------------|
     |$.status |401            |
     |$.error  |Unauthorized   |
     |$.message|Invalid token  |


