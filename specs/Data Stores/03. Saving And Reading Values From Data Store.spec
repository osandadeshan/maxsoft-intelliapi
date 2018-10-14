# Saving And Reading Values From Data Store Specification
Date Created    : 01/07/2018
Version   		: 1.0.0
Owner      		: Osanda Deshan
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.



## Get configurations of the testing environment
* Configurations of the testing environment

## Saving values to Data Store
* And the user save the values inside data stores as follows 

   |DataStore Type|Variable Name|Value To Be Stored |
   |--------------|-------------|-------------------|
   |Scenario      |variable1    |Osanda Deshan      |
   |Specification |variable2    |Osanda Nimalarathna|
   |Scenario      |variable3    |Software Automation|



## Reading values from Data Store
* And the user read the values from data stores as follows 

   |DataStore Type|Variable Name|
   |--------------|-------------|
   |Scenario      |variable1    |
   |Specification |variable2    |
   |Scenario      |variable3    |



## Invoke PI API in Staging Environment using valid username and password using payload text file

tags: get_pi_token, staging

* Given that a user needs to invoke "Get Staging PI Token"
* And the user set the request authentication configurations as follows 

   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |No                 |
   |Do you need to retrieve the access token from the text file?      |N/A                |
   |Provide the access token if you need to authorize the API manually|N/A                |
* And the user set the request payload as follows <file:/resources/payloads/login.txt>
* When the user invokes the API
* Then the status code for the request is "201"
* And the JSON Path Assertions for the response should be equal to the following 

   |JSON Path|Expected Result|
   |---------|---------------|
   |$.status |success        |
* And the JSON Path Existence in the response should be equal to the following 

   |JSON Path|isExists|
   |---------|--------|
   |$.status |true    |
   |$.osa    |false   |
* And save the access token in the response which is located inside the JSON Path of "$.data"
* And save the JSON Path values in the response inside the data stores 

   |DataStore Type|Variable Name|Value To Be Stored|
   |--------------|-------------|------------------|
   |Scenario      |variable4    |$.status          |
   |Specification |variable5    |$.data            |
* And the user read the values from data stores as follows 

   |DataStore Type|Variable Name|
   |--------------|-------------|
   |Scenario      |variable4    |
   |Specification |variable5    |



## Invoke PI API in Staging Environment using valid username and password and save the access token inside the text file

tags: get_pi_token, staging

* Given that a user needs to invoke "Get Staging PI Token"
* And the user save the values inside data stores as follows 

   |DataStore Type|Variable Name|Value To Be Stored |
   |--------------|-------------|-------------------|
   |Scenario      |username     |osanda12           |
   |Specification |variable6    |Osanda Nimalarathna|
   |Scenario      |variable7    |Software Automation|
* And the user set the request headers using data stores as follows 

   |Header Name|Is Data Store Used?|Data Store Type|Data Store Variable Name|Header Value|
   |-----------|-------------------|---------------|------------------------|------------|
   |header1    |y                  |spec           |variable6               |N/A         |
* And the user set the request attributes using data stores as follows 

   |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name|Attribute Value To Be Set|
   |--------------------------------|-------------------|---------------|------------------------|-------------------------|
   |#username                       |y                  |scenario       |username                |N/A                      |
   |#password                       |n                  |N/A            |N/A                     |Password1                |
* When the user invokes the API
* Then the status code for the request is "201"
* And save the JSON Path values in the response inside the data stores 

   |DataStore Type|Variable Name|Value To Be Stored|
   |--------------|-------------|------------------|
   |Scenario      |status       |$.status          |
* And the JSON Path values of the response should contains the following 

   |JSON Path|isContains|
   |---------|----------|
   |$.status |success   |
* And the JSON Path values of the response should contains the values inside the data stores 

   |JSON Path|Is Data Store Used?|Data Store Type|Data Store Variable Name|Expected Value|
   |---------|-------------------|---------------|------------------------|--------------|
   |$.status |y                  |scenario       |status                  |N/A           |
* And the JSON Path values of the response should not contains the following 

   |JSON Path|notContains|
   |---------|-----------|
   |$.status |fail       |
* And the JSON Path values of the response should not contains the values inside the data stores 

   |JSON Path|Is Data Store Used?|Data Store Type|Data Store Variable Name|Expected Value|
   |---------|-------------------|---------------|------------------------|--------------|
   |$.status |y                  |scenario       |variable7               |N/A           |
* And the JSON Path Assertions for the response should be equal to the following 

   |JSON Path|Expected Result|
   |---------|---------------|
   |$.status |success        |
* And the JSON Path Assertions for the response should not be equal to the following 

   |JSON Path|Expected Result|
   |---------|---------------|
   |$.status |fail           |
* And the JSON Path Assertions for the response should be equal to the values inside the data stores 

   |JSON Path|Is Data Store Used?|Data Store Type|Data Store Variable Name|Expected Value|
   |---------|-------------------|---------------|------------------------|--------------|
   |$.status |y                  |scenario       |status                  |N/A           |
   |$.status |n                  |N/A            |N/A                     |success       |
* And the JSON Path Assertions for the response should not be equal to the values inside the data stores 

   |JSON Path|Is Data Store Used?|Data Store Type|Data Store Variable Name|Expected Value|
   |---------|-------------------|---------------|------------------------|--------------|
   |$.status |n                  |N/A            |N/A                     |fail          |
* And save the access token in the response which is located inside the JSON Path of "$.data"
* And the JSON Path Existence in the response should be equal to the following 

   |JSON Path|isExists|
   |---------|--------|
   |$.status |true    |
   |$.osa    |false   |
* And the user set the query parameters using data stores as follows 

   |Query Name|Is Data Store Used?|Data Store Type|Data Store Variable Name|Query Value|
   |----------|-------------------|---------------|------------------------|-----------|
   |username  |y                  |scenario       |username                |N/A        |
   |password  |n                  |N/A            |N/A                     |Password1  |
* And the user set the path parameters using data stores as follows 

   |Path Name|Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value|
   |---------|-------------------|---------------|------------------------|----------|
   |#username|y                  |scenario       |username                |N/A       |
   |#password|n                  |N/A            |N/A                     |Password1 |



## Invoke PI API in Staging Environment using valid username and password using request attributes from text files

tags: get_pi_token, staging

* Given that a user needs to invoke "Get Staging PI Token"
* And the user save the values inside data stores as follows 

   |DataStore Type|Variable Name|Value To Be Stored |
   |--------------|-------------|-------------------|
   |Scenario      |username     |osanda12           |
   |Specification |variable6    |Osanda Nimalarathna|
   |Scenario      |variable7    |Software Automation|
* And the user set the request headers using data stores as follows 

   |Header Name|Is Data Store Used?|Data Store Type|Data Store Variable Name|Header Value                       |
   |-----------|-------------------|---------------|------------------------|-----------------------------------|
   |header1    |n                  |               |                        |<file:/resources/texts/header1.txt>|
   |header2    |n                  |               |                        |<file:/resources/texts/header1.txt>|
   |header3    |n                  |               |                        |<file:/resources/texts/header1.txt>|
* And the user set the request attributes using data stores as follows 

   |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name|Attribute Value To Be Set           |
   |--------------------------------|-------------------|---------------|------------------------|------------------------------------|
   |#username                       |y                  |scenario       |username                |N/A                                 |
   |#password                       |n                  |N/A            |N/A                     |<file:/resources/texts/password.txt>|
* When the user invokes the API
* Then the status code for the request is "201"
* And save the JSON Path values in the response inside the data stores 

   |DataStore Type|Variable Name|Value To Be Stored|
   |--------------|-------------|------------------|
   |Scenario      |status       |$.status          |
* And the JSON Path values of the response should contains the following 

   |JSON Path|isContains                                |
   |---------|------------------------------------------|
   |$.status |<file:/resources/texts/success_status.txt>|
* And the JSON Path values of the response should contains the values inside the data stores 

   |JSON Path|Is Data Store Used?|Data Store Type|Data Store Variable Name|Expected Value                            |
   |---------|-------------------|---------------|------------------------|------------------------------------------|
   |$.status |y                  |scenario       |status                  |N/A                                       |
   |$.status |n                  |               |                        |<file:/resources/texts/success_status.txt>|
* And the JSON Path values of the response should not contains the following 

   |JSON Path|notContains                               |
   |---------|------------------------------------------|
   |$.status |<file:/resources/texts/failure_status.txt>|
* And the JSON Path values of the response should not contains the values inside the data stores 

   |JSON Path|Is Data Store Used?|Data Store Type|Data Store Variable Name|Expected Value                            |
   |---------|-------------------|---------------|------------------------|------------------------------------------|
   |$.status |y                  |scenario       |variable7               |N/A                                       |
   |$.status |n                  |               |                        |<file:/resources/texts/failure_status.txt>|
* And the JSON Path Assertions for the response should be equal to the following 

   |JSON Path|Expected Result                           |
   |---------|------------------------------------------|
   |$.status |success                                   |
   |$.status |<file:/resources/texts/success_status.txt>|
* And the JSON Path Assertions for the response should not be equal to the following 

   |JSON Path|Expected Result                           |
   |---------|------------------------------------------|
   |$.status |fail                                      |
   |$.status |<file:/resources/texts/failure_status.txt>|
* And the JSON Path Assertions for the response should be equal to the values inside the data stores 

   |JSON Path|Is Data Store Used?|Data Store Type|Data Store Variable Name|Expected Value                            |
   |---------|-------------------|---------------|------------------------|------------------------------------------|
   |$.status |y                  |scenario       |status                  |N/A                                       |
   |$.status |n                  |N/A            |N/A                     |success                                   |
   |$.status |n                  |N/A            |N/A                     |<file:/resources/texts/success_status.txt>|
* And the JSON Path Assertions for the response should not be equal to the values inside the data stores 

   |JSON Path|Is Data Store Used?|Data Store Type|Data Store Variable Name|Expected Value                            |
   |---------|-------------------|---------------|------------------------|------------------------------------------|
   |$.status |n                  |N/A            |N/A                     |fail                                      |
   |$.status |n                  |N/A            |N/A                     |<file:/resources/texts/failure_status.txt>|
* And save the access token in the response which is located inside the JSON Path of "$.data"
* And the JSON Path Existence in the response should be equal to the following 

   |JSON Path|isExists|
   |---------|--------|
   |$.status |true    |
   |$.osa    |false   |
* And the user set the query parameters as follows 

   |Query Parameter|Query Value                         |
   |---------------|------------------------------------|
   |Id             |<file:/resources/texts/username.txt>|
* And the user set the path parameters as follows 

   |Path Parameter|Path Value                          |
   |--------------|------------------------------------|
   |Id            |<file:/resources/texts/username.txt>|
* And the user set the query parameters using data stores as follows 

   |Query Name|Is Data Store Used?|Data Store Type|Data Store Variable Name|Query Value                         |
   |----------|-------------------|---------------|------------------------|------------------------------------|
   |username  |y                  |scenario       |username                |N/A                                 |
   |password  |n                  |N/A            |N/A                     |<file:/resources/texts/password.txt>|
* And the user set the path parameters using data stores as follows 

   |Path Name|Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value                          |
   |---------|-------------------|---------------|------------------------|------------------------------------|
   |#username|y                  |scenario       |username                |N/A                                 |
   |#password|n                  |N/A            |N/A                     |<file:/resources/texts/password.txt>|



## Replace API Endpoint placeholders - Scenario 1
* Given that a user needs to invoke "Purchase Validator API"
* And the user set values to the API endpoint placeholders as follows 

   |Placeholder In JSON Template|Replacement Text                                      |
   |----------------------------|------------------------------------------------------|
   |#skuid                      |com.pearsoned.smartflashcards.expert.elementary       |
   |#purchaseToken              |<file:/resources/access_tokens/purchase_token.txt>    |
   |#access_token               |<file:/resources/access_tokens/google_drive_token.txt>|
* When the user invokes the API
* Then the status code for the request is "403"
* And the JSON Path Assertions for the response should be equal to the following 

   |JSON Path                |Expected Result        |
   |-------------------------|-----------------------|
   |$.error.errors[0].reason |insufficientPermissions|
   |$.error.errors[0].message|Insufficient Permission|
   |$.error.code             |403                    |



## Replace API Endpoint placeholders - Scenario 2
* Given that a user needs to invoke "Purchase Validator API"
* And the user save the values inside data stores as follows 

   |DataStore Type|Variable Name|Value To Be Stored                           |
   |--------------|-------------|---------------------------------------------|
   |Scenario      |purchaseToken|jghpbegbjgnpfdfgjjkhdpeo.AO-J1OwpcCUVIa0     |
   |Scenario      |accessToken  |ya29.GlzGBXmxF34s99wQ0o8ie7B4P85ld_FUNBZxizYB|
* And the user set values to the API endpoint placeholders using data stores as follows 

   |Placeholder In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name|Replacement Text                               |
   |----------------------------|-------------------|---------------|------------------------|-----------------------------------------------|
   |#skuid                      |n                  |               |                        |com.pearsoned.smartflashcards.expert.elementary|
   |#purchaseToken              |y                  |scenario       |purchaseToken           |                                               |
   |#access_token               |y                  |scenario       |accessToken             |                                               |
* When the user invokes the API
* Then the status code for the request is "401"
* And the JSON Path Assertions for the response should be equal to the following 

   |JSON Path                |Expected Result    |
   |-------------------------|-------------------|
   |$.error.errors[0].reason |authError          |
   |$.error.errors[0].message|Invalid Credentials|
   |$.error.code             |401                |



## Validate the data store values
* Given that a user needs to invoke "Get Staging PI Token"
* And the user set the request authentication configurations as follows 

   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |No                 |
   |Do you need to retrieve the access token from the text file?      |N/A                |
   |Provide the access token if you need to authorize the API manually|N/A                |
* And the user set the request payload as follows <file:/resources/payloads/login.txt>
* When the user invokes the API
* Then the status code for the request is "201"
* And save the JSON Path values in the response inside the data stores 

   |DataStore Type|Variable Name|Value To Be Stored|
   |--------------|-------------|------------------|
   |Scenario      |status       |$.status          |
* And the user save the values inside data stores as follows 

   |DataStore Type|Variable Name |Value To Be Stored|
   |--------------|--------------|------------------|
   |Scenario      |username      |osanda12          |
   |Scenario      |status        |success           |
   |Scenario      |mobileUserName|osanda12          |

* And the values inside the data stores equal to the following 

   |DataStore Type|Variable Name|Expected Value|
   |--------------|-------------|--------------|
   |Scenario      |username     |osanda12      |
   |Scenario      |status       |success       |
* And the values inside two data stores should be equal 

   |DataStore 1 Type|Variable 1 Name|DataStore 2 Type|Variable 2 Name|
   |----------------|---------------|----------------|---------------|
   |Scenario        |username       |Scenario        |mobileUserName |
* And the values inside the data stores not equal to the following 

   |DataStore Type|Variable Name|Expected Value|
   |--------------|-------------|--------------|
   |Scenario      |username     |osanda        |
   |Scenario      |status       |succes        |
* And the values inside two data stores should not be equal 

   |DataStore 1 Type|Variable 1 Name|DataStore 2 Type|Variable 2 Name|
   |----------------|---------------|----------------|---------------|
   |Scenario        |username       |Scenario        |status         |

* And the values inside the data stores contain the following 

   |DataStore Type|Variable Name|Expected Value|
   |--------------|-------------|--------------|
   |Scenario      |username     |osanda        |
   |Scenario      |status       |succes        |
* And the value inside a data store should contain the value of the other data store 

   |DataStore 1 Type|Variable 1 Name|DataStore 2 Type|Variable 2 Name|
   |----------------|---------------|----------------|---------------|
   |Scenario        |username       |Scenario        |mobileUserName |
* And the values inside the data stores not contain the following 

   |DataStore Type|Variable Name|Expected Value|
   |--------------|-------------|--------------|
   |Scenario      |username     |deshan        |
   |Scenario      |status       |fail          |
* And the value inside a data store should not contain the value of the other data store 

   |DataStore 1 Type|Variable 1 Name|DataStore 2 Type|Variable 2 Name|
   |----------------|---------------|----------------|---------------|
   |Scenario        |username       |Scenario        |status         |
