Login Specification
===================
Date Created    : 07/13/2017
Version   		: 1.0.0
Owner      		: Osanda Deshan
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.


tags: login



Login Scenario
--------------
* Given that a user needs to invoke "Login API"
* When the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set|
     |--------------------------------|-------------------------|
     |#username                       |aansar@gmail.com         |
     |#password                       |ayesha@123               |
* When the user invokes the API using the above request payload
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path |Expected Result             |
     |----------|----------------------------|
     |$.status  |successful                  |

