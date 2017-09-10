Get All Medicines Specification (Access Token obtained from the text file)
==========================================================================
Date Created    : 07/13/2017
Version   		: 1.0.0
Owner      		: Osanda Deshan
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.


tags: get_all_medicines



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
* And save the access token which is the attribute value of "token" in the response



Details of testing environment
------------------------------
* Testing environment details



Get All Medicines using a valid token
-------------------------------------
* Given that a user needs to invoke "Get All Medicines"
* When the user invokes the API using the following request "{}" and valid access token
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path     |Expected Result|
     |--------------|---------------|
     |$.status      |error          |
     |$.medicineList|null           |
