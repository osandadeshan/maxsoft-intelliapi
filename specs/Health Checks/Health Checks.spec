Health Checks Specification
===========================
Date Created    : 02/08/2018
Version   		: 1.0.0
Owner      		: Osanda Deshan
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.


tags: health_checks



Invoke PI Service Health Check
------------------------------
tags: pi_service, health_checks

* Given that a user needs to invoke "PI Service Health"
* When the user invokes the API
* Then the status code for the request is "200"



Invoke Document Service Health Check
------------------------------------
tags: document_service, health_checks

* Given that a user needs to invoke "Document Service Health"
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path               |Expected Result                         |
     |------------------------|----------------------------------------|
     |$.name                  |Document Service API                    |
     |$.health                |null                                    |
     |$._links.self.href      |https://documentservice-qa.stg-prsn.com |



Invoke Smart Card Creation Health Check
---------------------------------------
tags: smart_card_service, health_checks

* Given that a user needs to invoke "Smart Card Creation Health"
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path               |Expected Result                         |
     |------------------------|----------------------------------------|
     |$.status                |Ok                                      |


