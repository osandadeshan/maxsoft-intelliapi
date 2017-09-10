Get All Medicines Specification (Access Token obtained from the DataStore for the Specification)
================================================================================================
Date Created    : 07/13/2017
Version   		: 1.0.0
Owner      		: Osanda Deshan
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.


tags: get_all_medicines



* Given that a user needs to invoke "Login API"
* When the user invokes the API using the following request <file:/resources/api_requests/login/login.txt>
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path |Expected Result             |
     |----------|----------------------------|
     |$.status  |successful                  |
* And get the attribute value for the attribute of "token" in the response and save it in the data store named "accessToken"



Get All Medicines using a valid token
-------------------------------------
* Given that a user needs to invoke "Get All Medicines"
* When the user invokes the API using the following request "{}" and valid access token which saved in the data store named "accessToken"
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path     |Expected Result|
     |--------------|---------------|
     |$.status      |error          |
     |$.medicineList|null           |
