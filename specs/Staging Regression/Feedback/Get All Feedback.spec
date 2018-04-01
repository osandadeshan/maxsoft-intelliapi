Get All Feedback Specification
==============================
Date Created    : 03/04/2018
Version         : 1.0.0
Owner      	    : Osanda Deshan
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.


tags: feedback, get_feedback, ci_ready



* Given that a user needs to invoke "Get All Feedback"
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |



Get all feedback using valid payload
------------------------------------
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Existence in the response should be equal to the following
     |JSON Path                          |isExists?                               |
     |-----------------------------------|----------------------------------------|
     |$[-1:]._id                         |true                                    |
     |$[-1:].comment                     |true                                    |
     |$[-1:].username                    |true                                    |
     |$[-1:].rating                      |true                                    |
     |$[-1:].appId                       |true                                    |
     |$[-1:].email                       |true                                    |
     |$[-1:].appName                     |true                                    |
     |$[-1:].dateTime                    |true                                    |

