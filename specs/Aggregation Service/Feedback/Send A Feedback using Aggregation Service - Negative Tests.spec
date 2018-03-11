Send A Feedback using Aggregation Service - Negative Tests Specification
========================================================================
Date Created    : 03/04/2018
Version         : 1.0.0
Owner      	    : Osanda Deshan
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.


tags: feedback, send_feedback-negative_tests, negative



* Given that a user needs to invoke "Send A Feedback using Aggregation Service"
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |



Send a feedback using comment as empty
--------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set               |
     |--------------------------------|----------------------------------------|
     |#comment                        |                                        |
     |#username                       |Osanda                                  |
     |#rating                         |Awesome                                 |
     |#appId                          |sfc_mvp                                 |
     |#email                          |osanda@maxsoftlk.com                    |
     |#appName                        |sfc_mvp_ios                             |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                          |Value                                   |
     |-----------------------------------|----------------------------------------|
     |$.code                             |400                                     |
     |$.description                      |comment: may not be empty               |
	 


Send a feedback using username as empty
---------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set               |
     |--------------------------------|----------------------------------------|
     |#comment                        |no comments                             |
     |#username                       |                                  	   |
     |#rating                         |Awesome                                 |
     |#appId                          |sfc_mvp                                 |
     |#email                          |osanda@maxsoftlk.com                    |
     |#appName                        |sfc_mvp_ios                             |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                          |Value                                   |
     |-----------------------------------|----------------------------------------|
     |$.code                             |400                                     |
     |$.description                      |username: may not be empty              |

	 
	 
Send a feedback using rating as empty
-------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set               |
     |--------------------------------|----------------------------------------|
     |#comment                        |no comments                             |
     |#username                       |Osanda                                  |
     |#rating                         |                                        |
     |#appId                          |sfc_mvp                                 |
     |#email                          |osanda@maxsoftlk.com                    |
     |#appName                        |sfc_mvp_ios                             |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                          |Value                                   |
     |-----------------------------------|----------------------------------------|
     |$.code                             |400                                     |
     |$.description                      |rating: may not be empty                |



Send a feedback using appId as empty
------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set               |
     |--------------------------------|----------------------------------------|
     |#comment                        |no comments                             |
     |#username                       |Osanda                                  |
     |#rating                         |Awesome                                 |
     |#appId                          |                                        |
     |#email                          |osanda@maxsoftlk.com                    |
     |#appName                        |sfc_mvp_ios                             |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                          |Value                                   |
     |-----------------------------------|----------------------------------------|
     |$.code                             |400                                     |
     |$.description                      |appId: may not be empty                 |



Send a feedback using comment as null
-------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set               |
     |--------------------------------|----------------------------------------|
     |#comment                        |"null"                                  |
     |#username                       |Osanda                                  |
     |#rating                         |Awesome                                 |
     |#appId                          |sfc_mvp                                 |
     |#email                          |osanda@maxsoftlk.com                    |
     |#appName                        |sfc_mvp_ios                             |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                          |Value                                   |
     |-----------------------------------|----------------------------------------|
     |$.code                             |400                                     |
     |$.description                      |comment: may not be empty               |
	 


Send a feedback using username as null
--------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set               |
     |--------------------------------|----------------------------------------|
     |#comment                        |no comments                             |
     |#username                       |"null"                                  |
     |#rating                         |Awesome                                 |
     |#appId                          |sfc_mvp                                 |
     |#email                          |osanda@maxsoftlk.com                    |
     |#appName                        |sfc_mvp_ios                             |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                          |Value                                   |
     |-----------------------------------|----------------------------------------|
     |$.code                             |400                                     |
     |$.description                      |username: may not be empty              |

	 
	 
Send a feedback using rating as null
------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set               |
     |--------------------------------|----------------------------------------|
     |#comment                        |no comments                             |
     |#username                       |Osanda                                  |
     |#rating                         |"null"                                  |
     |#appId                          |sfc_mvp                                 |
     |#email                          |osanda@maxsoftlk.com                    |
     |#appName                        |sfc_mvp_ios                             |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                          |Value                                   |
     |-----------------------------------|----------------------------------------|
     |$.code                             |400                                     |
     |$.description                      |rating: may not be empty                |



Send a feedback using appId as null
-----------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set               |
     |--------------------------------|----------------------------------------|
     |#comment                        |no comments                             |
     |#username                       |Osanda                                  |
     |#rating                         |Awesome                                 |
     |#appId                          |"null"                                  |
     |#email                          |osanda@maxsoftlk.com                    |
     |#appName                        |sfc_mvp_ios                             |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                          |Value                                   |
     |-----------------------------------|----------------------------------------|
     |$.code                             |400                                     |
     |$.description                      |appId: may not be empty                 |