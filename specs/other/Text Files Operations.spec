# Text Files Operations Specification

Project Name : MaxSoft-IntelliAPI
Developer    : Osanda Deshan
Version      : 1.0.0
Date         : 6/17/2018
Time         : 2:06 PM
Description  : This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.

tags: text_file, regression


## Usage of authentication token from a text file

* Given that a user needs to invoke "Create a user"
* And the user saves test data inside excel file into data stores
   |DataStore Type|Variable Name      |Excel Sheet Name |Key Name         |
   |--------------|-------------------|-----------------|-----------------|
   |Scenario      |varName            |User_Test_Data   |name             |
   |Scenario      |varGender          |User_Test_Data   |gender           |
   |Scenario      |varStatus          |User_Test_Data   |status           |
* And generate random email and save it in a data store as follows
   |Data Store Type|Data Store Variable Name|Domain Name     |
   |---------------|------------------------|----------------|
   |Scenario       |varEmail                |mailinator.com  |
* And the user set the request attributes using data stores as follows
   |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name|Attibute Value To Be Set|
   |--------------------------------|-------------------|---------------|------------------------|------------------------|
   |#email                          |yes                |Scenario       |varEmail                |                        |
   |#name                           |yes                |Scenario       |varName                 |                        |
   |#gender                         |yes                |Scenario       |varGender               |                        |
   |#status                         |yes                |Scenario       |varStatus               |                        |
* And the user set the request authentication configurations as follows
   |Configuration                                                     |Configuration Value                                  |
   |------------------------------------------------------------------|-----------------------------------------------------|
   |Is authentication required?                                       |Yes                                                  |
   |Do you need to retrieve the access token from the text file?      |No                                                   |
   |Provide the access token if you need to authorize the API manually|<file:./src/test/resources/payloads/access_token.txt>|
* When the user invokes the API
* Then the status code for the request is "200"
* And save the JSON Path values in the response inside the data stores
   |DataStore Type|Variable Name|Value To Be Stored|
   |--------------|-------------|------------------|
   |Scenario      |varUserId    |$.data.id         |
* And the JSON Path Assertions for the response should be equal to the values inside the data stores
   |JSON Path    |Is Data Store Used?|Data Store Type|Data Store Variable Name|Expected Value|
   |-------------|-------------------|---------------|------------------------|--------------|
   |$.code       |no                 |               |                        |201           |
   |$.data.name  |yes                |Scenario       |varName                 |              |
   |$.data.email |yes                |Scenario       |varEmail                |              |


## Usage of request attributes from text files

* Given that a user needs to invoke "Create a user"
* And the user saves test data inside excel file into data stores
   |DataStore Type|Variable Name      |Excel Sheet Name |Key Name         |
   |--------------|-------------------|-----------------|-----------------|
   |Scenario      |varName            |User_Test_Data   |name             |
* And generate random email and save it in a data store as follows
   |Data Store Type|Data Store Variable Name|Domain Name     |
   |---------------|------------------------|----------------|
   |Scenario       |varEmail                |mailinator.com  |
* And the user set the request attributes using data stores as follows
   |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name|Attibute Value To Be Set                         |
   |--------------------------------|-------------------|---------------|------------------------|-------------------------------------------------|
   |#email                          |yes                |Scenario       |varEmail                |                                                 |
   |#name                           |yes                |Scenario       |varName                 |                                                 |
   |#gender                         |no                 |               |                        |<file:./src/test/resources/payloads/gender.txt>  |
   |#status                         |no                 |               |                        |<file:./src/test/resources/payloads/status.txt>  |
* And the user set the request authentication configurations as follows
   |Configuration                                                     |Configuration Value          |
   |------------------------------------------------------------------|-----------------------------|
   |Is authentication required?                                       |Yes                          |
   |Do you need to retrieve the access token from the text file?      |Yes                          |
   |Provide the access token if you need to authorize the API manually|N/A                          |
* When the user invokes the API
* Then the status code for the request is "200"
* And save the JSON Path values in the response inside the data stores
   |DataStore Type|Variable Name|Value To Be Stored|
   |--------------|-------------|------------------|
   |Scenario      |varUserId    |$.data.id         |
* And the JSON Path values of the response should contains the following
   |JSON Path    |isContains                                     |
   |-------------|-----------------------------------------------|
   |$.data.status|<file:./src/test/resources/payloads/status.txt>|
* And the JSON Path values of the response should contains the values inside the data stores
   |JSON Path    |Is Data Store Used?|Data Store Type|Data Store Variable Name|Expected Value                                 |
   |-------------|-------------------|---------------|------------------------|-----------------------------------------------|
   |$.code       |no                 |               |                        |20                                             |
   |$.data.name  |yes                |Scenario       |varName                 |                                               |
   |$.data.email |yes                |Scenario       |varEmail                |                                               |
   |$.data.gender|no                 |               |                        |<file:./src/test/resources/payloads/gender.txt>|
   |$.data.status|no                 |               |                        |Acti                                           |
* And the JSON Path values of the response should not contains the following
   |JSON Path    |notContains                                     |
   |-------------|------------------------------------------------|
   |$.data.status|<file:./src/test/resources/payloads/gender.txt> |
* And the JSON Path values of the response should not contains the values inside the data stores 
   |JSON Path    |Is Data Store Used?|Data Store Type|Data Store Variable Name|Expected Value                                 |
   |-------------|-------------------|---------------|------------------------|-----------------------------------------------|
   |$.code       |no                 |               |                        |204                                            |
   |$.data.name  |no                 |               |                        |Osanda                                         |
   |$.data.email |no                 |               |                        |osanda@maxsoft.com                             |
   |$.data.gender|no                 |               |                        |<file:./src/test/resources/payloads/status.txt>|
   |$.data.status|no                 |               |                        |<file:./src/test/resources/payloads/gender.txt>|
* And the JSON Path Assertions for the response should be equal to the following
   |JSON Path    |Expected Value                                 |
   |-------------|-----------------------------------------------|
   |$.code       |201                                            |
   |$.data.status|<file:./src/test/resources/payloads/status.txt>|
* And the JSON Path Assertions for the response should not be equal to the following
   |JSON Path    |Expected Value                                 |
   |-------------|-----------------------------------------------|
   |$.code       |204                                            |
   |$.data.gender|<file:./src/test/resources/payloads/status.txt>|
* And the JSON Path Assertions for the response should be equal to the values inside the data stores
   |JSON Path    |Is Data Store Used?|Data Store Type|Data Store Variable Name|Expected Value                                 |
   |-------------|-------------------|---------------|------------------------|-----------------------------------------------|
   |$.code       |no                 |               |                        |201                                            |
   |$.data.name  |yes                |Scenario       |varName                 |                                               |
   |$.data.email |yes                |Scenario       |varEmail                |                                               |
   |$.data.gender|no                 |               |                        |<file:./src/test/resources/payloads/gender.txt>|
   |$.data.status|no                 |               |                        |<file:./src/test/resources/payloads/status.txt>|
* And the JSON Path Assertions for the response should not be equal to the values inside the data stores 
   |JSON Path    |Is Data Store Used?|Data Store Type|Data Store Variable Name|Expected Value                                 |
   |-------------|-------------------|---------------|------------------------|-----------------------------------------------|
   |$.code       |no                 |               |                        |204                                            |
   |$.data.name  |no                 |               |                        |Osanda                                         |
   |$.data.email |no                 |               |                        |osanda@maxsoft.com                             |
   |$.data.gender|no                 |               |                        |<file:./src/test/resources/payloads/status.txt>|
   |$.data.status|no                 |               |                        |<file:./src/test/resources/payloads/gender.txt>|
* And the JSON Path Existence in the response should be equal to the following
   |JSON Path       |isExists|
   |----------------|--------|
   |$.data.status   |true    |
   |$.status        |false   |
* And the user set the query parameters as follows
   |Query Parameter|Query Value                                    |
   |---------------|-----------------------------------------------|
   |Id             |<file:./src/test/resources/payloads/gender.txt>|
* And the user set the path parameters as follows
   |Path Parameter|Path Value                                      |
   |---------------|-----------------------------------------------|
   |status         |<file:./src/test/resources/payloads/status.txt>|
* And the user set the query parameters using data stores as follows
   |Query Name|Is Data Store Used?|Data Store Type|Data Store Variable Name|Query Value                                    |
   |----------|-------------------|---------------|------------------------|-----------------------------------------------|
   |name      |y                  |Scenario       |varName                 |                                               |
   |email     |y                  |Scenario       |varEmail                |                                               |
   |status    |n                  |               |                        |<file:./src/test/resources/payloads/status.txt>|
* And the user set the path parameters using data stores as follows
   |Path Name |Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value                                     |
   |----------|-------------------|---------------|------------------------|-----------------------------------------------|
   |name      |y                  |Scenario       |varName                 |                                               |
   |email     |y                  |Scenario       |varEmail                |                                               |
   |status    |n                  |               |                        |<file:./src/test/resources/payloads/status.txt>|
   |gender    |n                  |               |                        |<file:./src/test/resources/payloads/gender.txt>|


_______________________________________________________________________________
* Delete a user by userId saved in "Scenario" type data store named "varUserId"
