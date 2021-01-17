# CRUD In One Scenario Specification

Project Name    : MaxSoft-IntelliAPI
Developer       : Osanda Deshan
Version         : 1.0.0
Date            : 28/04/2019
Time            : 20:09
Description     : This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.

tags: crud, regression


## CRUD operation for a user

* Create a user
* And save the JSON Path values in the response inside the data stores
   |DataStore Type|Variable Name|Value To Be Stored|
   |--------------|-------------|------------------|
   |Scenario      |varUserId    |$.data.id         |

* Given that a user needs to invoke "Edit a user"
* And the user set the path parameters using data stores as follows
   |Path Name|Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value|
   |---------|-------------------|---------------|------------------------|----------|
   |userId   |yes                |Scenario       |varUserId               |          |
* And generate random email and save it in a data store as follows
   |Data Store Type|Data Store Variable Name|Domain Name     |
   |---------------|------------------------|----------------|
   |Scenario       |varEmail                |mailinator.com  |
* And the user set the request attributes using data stores as follows
   |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name|Attibute Value To Be Set|
   |--------------------------------|-------------------|---------------|------------------------|------------------------|
   |#email                          |yes                |Scenario       |varEmail                |                        |
   |#name                           |no                 |               |                        |Tester                  |
   |#gender                         |no                 |               |                        |Female                  |
   |#status                         |no                 |               |                        |Active                  |
* And the user set the request authentication configurations as follows
   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |Yes                |
   |Do you need to retrieve the access token from the text file?      |Yes                |
   |Provide the access token if you need to authorize the API manually|N/A                |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the values inside the data stores
   |JSON Path    |Is Data Store Used?|Data Store Type|Data Store Variable Name|Expected Value|
   |-------------|-------------------|---------------|------------------------|--------------|
   |$.code       |no                 |               |                        |200           |
   |$.data.email |yes                |Scenario       |varEmail                |              |

* Given that a user needs to invoke "Get a user"
* And the user set the path parameters using data stores as follows
   |Path Name|Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value|
   |---------|-------------------|---------------|------------------------|----------|
   |userId   |yes                |Scenario       |varUserId               |          |
* And the user set the request authentication configurations as follows
   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |Yes                |
   |Do you need to retrieve the access token from the text file?      |Yes                |
   |Provide the access token if you need to authorize the API manually|N/A                |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the values inside the data stores
   |JSON Path    |Is Data Store Used?|Data Store Type|Data Store Variable Name|Expected Value|
   |-------------|-------------------|---------------|------------------------|--------------|
   |$.code       |no                 |               |                        |200           |
   |$.data.email |yes                |Scenario       |varEmail                |              |

* Delete a user by userId saved in "Scenario" type data store named "varUserId"
