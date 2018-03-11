Get A Feedback Specification
============================
Date Created    : 03/04/2018
Version         : 1.0.0
Owner      	    : Osanda Deshan
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.


tags: feedback, get_a_feedback



Get a feedback using valid payload
----------------------------------
* Send a feedback
* Given that a user needs to invoke "Get All Feedback"
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                          |JSON Path Value                         |
     |-----------------------------------|----------------------------------------|
     |$[-1:].comment                     |This is a good app for learning         |
     |$[-1:].username                    |Osanda                                  |
     |$[-1:].rating                      |Awesome                                 |
     |$[-1:].appId                       |sfc_mvp                                 |
     |$[-1:].email                       |osanda@maxsoftlk.com                    |
     |$[-1:].appName                     |sfc_mvp_ios                             |

