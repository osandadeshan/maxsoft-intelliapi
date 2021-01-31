# MongoDB Test Specification

Project Name : MaxSoft-IntelliAPI
Developer    : Osanda Deshan
Version      : 1.0.0
Date         : 6/30/2018
Time         : 9:14 PM
Description  : This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.

tags: database, mongo


* Given a user need to connect to the "tasksdb" Mongo database and "tasks" collection
* And the user set the MongoDB authentication as follows
   |Configuration                          |Configuration Value|
   |---------------------------------------|-------------------|
   |Is authentication credentials required?|No                 |
   |Username                               |N/A                |
   |Source                                 |N/A                |
   |Password                               |N/A                |


## MongoDB Test - Without data stores

* When the user executes the Mongo query using key as "name" and value as "Ron"
* And the JSON Path Assertions for the response should be equal to the values inside the data stores
   |JSON Path    |Is Data Store Used?|Data Store Type|Data Store Variable Name|Expected Value|
   |-------------|-------------------|---------------|------------------------|--------------|
   |$.name       |n                  |               |                        |Ron           |
   |$.category   |n                  |               |                        |Gauge         |


## MongoDB Test - With data stores

* And the user saves the values inside data stores as follows
   |DataStore Type|Variable Name|Value To Be Stored|
   |--------------|-------------|------------------|
   |Scenario      |name         |Ron               |
* When the user executes the Mongo query using data stores as follows
   |Key  |Is Data Store Used For Value?|Data Store Type|Data Store Variable Name|Value|
   |-----|-----------------------------|---------------|------------------------|-----|
   |name |y                            |Scenario       |name                    |N/A  |
* And the JSON Path Assertions for the response should be equal to the values inside the data stores
   |JSON Path    |Is Data Store Used?|Data Store Type|Data Store Variable Name|Expected Value|
   |-------------|-------------------|---------------|------------------------|--------------|
   |$.name       |y                  |Scenario       |name                    |              |
   |$.category   |n                  |               |                        |Gauge         |
