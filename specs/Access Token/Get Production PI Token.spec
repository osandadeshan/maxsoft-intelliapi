Get Production PI Token Specification
=====================================
Date Created    : 02/28/2018
Version   		: 1.0.0
Owner      		: Osanda Deshan
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.


tags: get_pi_token


* Given that a user needs to invoke "Get Production PI Token"
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |



Invoke PI API in Production Environment using valid username and password and save the access token inside the text file
------------------------------------------------------------------------------------------------------------------------
tags: get_pi_token, production

* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set          |
     |--------------------------------|-----------------------------------|
     |#username                       |smartflashcards_system             |
     |#password                       |DKLIYvBBt3RJ1juHKi1gsR6PSJWlN54t   |
* When the user invokes the API
* Then the status code for the request is "201"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path     |Expected Result|
     |--------------|---------------|
     |$.status      |success        |
* And save the access token in the response which is located inside the JSON Path of "$.data"



