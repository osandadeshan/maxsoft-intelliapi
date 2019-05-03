# Text Files Operations Specification

Project Name : MaxSoft-IntelliAPI
Developer    : Osanda Deshan
Version      : 1.0.0
Date         : 6/17/2018
Time         : 2:06 PM
Description  : This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.



## Get all decks of a user

* Given that a user needs to invoke "Get All Decks Of User"
* And the user saves test data inside excel file into data stores 

   |DataStore Type|Variable Name     |Excel Sheet Name|Key Name       |
   |--------------|------------------|----------------|---------------|
   |Scenario      |varUserId         |Deck_Test_Data  |userId         |
   |Scenario      |varSampleDeckTitle|Deck_Test_Data  |sampleDeckTitle|
* And the user set the path parameters using data stores as follows 

   |Path Name|Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value|
   |---------|-------------------|---------------|------------------------|----------|
   |userId   |yes                |Scenario       |varUserId               |          |
* And the user set the request authentication configurations as follows 

   |Configuration                                                     |Configuration Value                                 |
   |------------------------------------------------------------------|----------------------------------------------------|
   |Is authentication required?                                       |Yes                                                 |
   |Do you need to retrieve the access token from the text file?      |No                                                  |
   |Provide the access token if you need to authorize the API manually|<file:/resources/text_files/response_data/token.txt>|
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the values inside the data stores 

   |JSON Path    |Is Data Store Used?|Data Store Type|Data Store Variable Name|Expected Value|
   |-------------|-------------------|---------------|------------------------|--------------|
   |$[0].title   |yes                |Scenario       |varSampleDeckTitle      |              |
   |$[0].userId  |yes                |Scenario       |varUserId               |              |
   |$[0].archived|no                 |               |                        |false         |



## Invoke Auth API using valid username and password using request attributes from text files

tags: get_auth_token

* Given that a user needs to invoke "Get Auth Token"
* And the user saves the values inside data stores as follows 

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



## Replace API Endpoint placeholders

* Given that a user needs to invoke "Purchase Validator API"
* And the user set values to the API endpoint placeholders as follows 

   |Placeholder In JSON Template|Replacement Text                                      |
   |----------------------------|------------------------------------------------------|
   |#skuid                      |com.pearsoned.smartflashcards.expert.elementary       |
   |#purchaseToken              |<file:/resources/access_tokens/purchase_token.txt>    |
   |#access_token               |<file:/resources/access_tokens/google_drive_token.txt>|
* When the user invokes the API
* Then the status code for the request is "401"
* And the JSON Path Assertions for the response should be equal to the following 

   |JSON Path                |Expected Result    |
   |-------------------------|-------------------|
   |$.error.errors[0].reason |authError          |
   |$.error.errors[0].message|Invalid Credentials|
   |$.error.code             |401                |
