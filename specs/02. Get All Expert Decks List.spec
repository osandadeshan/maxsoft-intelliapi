Get All Expert Decks List Specification
=======================================
Date Created    : 09/20/2017
Version   		: 1.0.0
Owner      		: Osanda Deshan
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.


tags: get_all_expert_decks_list



* Given that a user needs to invoke "Get all Decks"



Get all decks list using the valid X-Platform (X-Platform = "Authoring")
------------------------------------------------------------------------
* And the user set the request authentication configurations as follows
     |Configuration Property Name       |Configuration Property Value   |
     |----------------------------------|-------------------------------|
     |isAccessTokenIncluded             |True                           |
     |isAccessTokenRetrievedFromTextFile|True                           |
     |accessTokenString                 |N/A                            |
* And the user set the request headers as follows
     |Header Name                     |Header Value             |
     |--------------------------------|-------------------------|
     |X-Platform                      |Authoring                |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                |Value                                 |
     |-------------------------|--------------------------------------|
     |$.[-1:].title            |Software Test Automation using Gauge  |
     |$.[-1:].description      |Test Automation                       |
     |$.[-1:].subject.name     |Test Automation                       |
     |$.[-1:].book.bookAuthor  |Gemunu                                |
     |$.[-1:].userId           |osanda12                              |



Get all decks list using the valid X-Platform (X-Platform = "Android")
----------------------------------------------------------------------
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
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                |Value                                 |
     |-------------------------|--------------------------------------|
     |$.status                 |400                                   |
     |$.error                  |Bad Request                           |
     |$.message                |X-Platform id is not valid            |



Get all decks list using the valid X-Platform (X-Platform = "iOS")
------------------------------------------------------------------
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
     |X-Platform                      |iOS                      |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                |Value                                 |
     |-------------------------|--------------------------------------|
     |$.status                 |400                                   |
     |$.error                  |Bad Request                           |
     |$.message                |X-Platform id is not valid            |



Get all decks list using the valid X-Platform (X-Platform = "Web")
------------------------------------------------------------------
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
     |X-Platform                      |Web                      |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                |Value                                 |
     |-------------------------|--------------------------------------|
     |$.status                 |400                                   |
     |$.error                  |Bad Request                           |
     |$.message                |X-Platform id is not valid            |

