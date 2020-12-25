# Headers Specification

Project Name    : MaxSoft-IntelliAPI
Developer       : Osanda Deshan
Version         : 1.0.0
Date            : 28/04/2019
Time            : 20:09
Description     : This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.

tags: headers


* Given that a user needs to invoke "Get auth token"
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path     |Expected Result|
     |--------------|---------------|
     |$.status      |success        |
* And save the JSON Path values in the response inside the data stores
   |DataStore Type|Variable Name|Value To Be Stored|
   |--------------|-------------|------------------|
   |Scenario      |varToken     |$.token           |


## Invoke Create a user API with authentication header separately

* Given that a user needs to invoke "Create a user"
* And the user saves environment property file data into data stores
   |DataStore Type|Variable Name  |Attribute Name In Property File|
   |--------------|---------------|-------------------------------|
   |Scenario      |authFirstValue |authentication_first_value     |
* And concat values in data stores and save it in a "Scenario" type data store named "AuthToken"
   |DataStore Type|Variable Name  |
   |--------------|---------------|
   |Scenario      |authFirstValue |
   |Scenario      |varToken       |
* And the user set the request headers using data stores as follows
   |Header Name  |Is Data Store Used?|Data Store Type|Data Store Variable Name|Header Value                       |
   |-------------|-------------------|---------------|------------------------|-----------------------------------|
   |Authorization|y                  |Scenario       |AuthToken               |                                   |
* And the user saves test data inside excel file into data stores
   |DataStore Type|Variable Name      |Excel Sheet Name |Key Name         |
   |--------------|-------------------|-----------------|-----------------|
   |Scenario      |varGender          |User_Test_Data   |gender           |
   |Scenario      |varStatus          |User_Test_Data   |status           |
* And concat random text and save it in a data store as follows
   |Is Data Store Used?|Data Store Type|Data Store Variable Name|Original Text |Save To New Data Store?|New Data Store Type|New Data Store Variable Name|
   |-------------------|---------------|------------------------|--------------|-----------------------|-------------------|----------------------------|
   |no                 |               |                        |Tester_       |yes                    |Scenario           |varNewName                  |
* And generate random email and save it in a data store as follows
   |Data Store Type|Data Store Variable Name|Domain Name     |
   |---------------|------------------------|----------------|
   |Scenario       |varEmail                |mailinator.com  |
* And the user set the request attributes using data stores as follows
   |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name|Attibute Value To Be Set|
   |--------------------------------|-------------------|---------------|------------------------|------------------------|
   |#email                          |yes                |Scenario       |varEmail                |                        |
   |#name                           |yes                |Scenario       |varNewName              |                        |
   |#gender                         |yes                |Scenario       |varGender               |                        |
   |#status                         |yes                |Scenario       |varStatus               |                        |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the values inside the data stores
   |JSON Path    |Is Data Store Used?|Data Store Type|Data Store Variable Name|Expected Value  |
   |-------------|-------------------|---------------|------------------------|----------------|
   |$.code       |no                 |               |                        |201             |
   |$.data.email |yes                |Scenario       |varEmail                |                |


## Invoke Task API with valid headers

* Given that a user needs to invoke "Create task"
* And the user saves environment property file data into data stores
   |DataStore Type|Variable Name  |Attribute Name In Property File|
   |--------------|---------------|-------------------------------|
   |Scenario      |authFirstValue |authentication_first_value     |
* And concat values in data stores and save it in a "Scenario" type data store named "AuthToken"
   |DataStore Type|Variable Name  |
   |--------------|---------------|
   |Scenario      |authFirstValue |
   |Scenario      |varToken       |
* And the user set the request headers using data stores as follows
   |Header Name  |Is Data Store Used?|Data Store Type|Data Store Variable Name|Header Value                       |
   |-------------|-------------------|---------------|------------------------|-----------------------------------|
   |Authorization|yes                |Scenario       |AuthToken               |                                   |
   |tenant       |no                 |               |                        |taskdb                             |
* And the user set the request attributes using data stores as follows
   |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name|Attibute Value To Be Set|
   |--------------------------------|-------------------|---------------|------------------------|------------------------|
   |#app                            |no                 |               |                        |IntelliAPI              |
* When the user invokes the API
* Then the status code for the request is "201"
* And the JSON Path Assertions for the response should be equal to the values inside the data stores
   |JSON Path    |Is Data Store Used?|Data Store Type|Data Store Variable Name|Expected Value  |
   |-------------|-------------------|---------------|------------------------|----------------|
   |$.message    |no                 |               |                        |Success         |


## Invoke Task API with invalid headers

* Given that a user needs to invoke "Create task"
* And the user saves environment property file data into data stores
   |DataStore Type|Variable Name  |Attribute Name In Property File|
   |--------------|---------------|-------------------------------|
   |Scenario      |authFirstValue |authentication_first_value     |
* And concat values in data stores and save it in a "Scenario" type data store named "AuthToken"
   |DataStore Type|Variable Name  |
   |--------------|---------------|
   |Scenario      |authFirstValue |
   |Scenario      |varToken       |
* And the user set the request headers using data stores as follows
   |Header Name  |Is Data Store Used?|Data Store Type|Data Store Variable Name|Header Value                       |
   |-------------|-------------------|---------------|------------------------|-----------------------------------|
   |Authorization|yes                |Scenario       |AuthToken               |                                   |
   |tenant       |no                 |               |                        |taskdb                             |
* And the user set the request attributes using data stores as follows
   |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name|Attibute Value To Be Set|
   |--------------------------------|-------------------|---------------|------------------------|------------------------|
   |#app                            |no                 |               |                        |GReporter               |
* When the user invokes the API
* Then the status code for the request is "404"


## Invoke Task API without authentication header

* Given that a user needs to invoke "Create task"
* And the user set the request headers using data stores as follows
   |Header Name  |Is Data Store Used?|Data Store Type|Data Store Variable Name|Header Value                       |
   |-------------|-------------------|---------------|------------------------|-----------------------------------|
   |tenant       |no                 |               |                        |taskdb                             |
* And the user set the request attributes using data stores as follows
   |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name|Attibute Value To Be Set|
   |--------------------------------|-------------------|---------------|------------------------|------------------------|
   |#app                            |no                 |               |                        |GReporter               |
* When the user invokes the API
* Then the status code for the request is "404"


## Invoke Task API without tenant header

* Given that a user needs to invoke "Create task"
* And the user saves environment property file data into data stores
   |DataStore Type|Variable Name  |Attribute Name In Property File|
   |--------------|---------------|-------------------------------|
   |Scenario      |authFirstValue |authentication_first_value     |
* And concat values in data stores and save it in a "Scenario" type data store named "AuthToken"
   |DataStore Type|Variable Name  |
   |--------------|---------------|
   |Scenario      |authFirstValue |
   |Scenario      |varToken       |
* And the user set the request headers using data stores as follows
   |Header Name  |Is Data Store Used?|Data Store Type|Data Store Variable Name|Header Value                       |
   |-------------|-------------------|---------------|------------------------|-----------------------------------|
   |Authorization|yes                |Scenario       |AuthToken               |                                   |
* And the user set the request attributes using data stores as follows
   |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name|Attibute Value To Be Set|
   |--------------------------------|-------------------|---------------|------------------------|------------------------|
   |#app                            |no                 |               |                        |GReporter               |
* When the user invokes the API
* Then the status code for the request is "404"
