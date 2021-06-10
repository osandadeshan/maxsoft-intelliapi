# Saving To Data Stores Specification

Project Name : MaxSoft-IntelliAPI
Developer    : Osanda Deshan
Version      : 1.0.0
Date         : 12/24/2020
Time         : 11:11 AM
Description  : This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.

tags: data_store, regression


## Saving to Data Stores

* And the user saves the values inside data stores as follows

   |DataStore Type|Variable Name|Value To Be Stored |
   |--------------|-------------|-------------------|
   |Scenario      |variable1    |Osanda Deshan      |
   |Specification |variable2    |Osanda Nimalarathna|
   |Scenario      |variable3    |Software Automation|
   |Suite         |variable4    |Gauge Framework    |
* And the values inside the data stores equal to the following

   |DataStore Type|Variable Name|Expected Value     |
   |--------------|-------------|-------------------|
   |Scenario      |variable1    |Osanda Deshan      |
   |Specification |variable2    |Osanda Nimalarathna|
   |Scenario      |variable3    |Software Automation|
   |Suite         |variable4    |Gauge Framework    |
* And the user saves environment property file data into data stores

   |DataStore Type|Variable Name|Attribute Name In Property File|
   |--------------|-------------|-------------------------------|
   |Scenario      |mongoHost    |mongo_database_host            |
   |Specification |mongoPort    |mongo_database_port            |
   |Scenario      |mysqlUrl     |mysql_database_url             |
   |Suite         |headerName   |header_name_for_authorization  |
* And the values inside the data stores equal to the following

   |DataStore Type|Variable Name|Expected Value             |
   |--------------|-------------|---------------------------|
   |Scenario      |mongoHost    |127.0.0.1                  |
   |Specification |mongoPort    |27017                      |
   |Scenario      |mysqlUrl     |jdbc:mysql://localhost:3306|
   |Suite         |headerName   |Authorization              |


## Reading values from Data Store

* And the user saves the values inside data stores as follows

   |DataStore Type|Variable Name|Value To Be Stored |
   |--------------|-------------|-------------------|
   |Scenario      |variable1    |Osanda Deshan      |
   |Specification |variable2    |Osanda Nimalarathna|
   |Scenario      |variable3    |Software Automation|
   |Suite         |variable4    |Gauge Framework    |
* And the user read the values from data stores as follows

   |DataStore Type|Variable Name|
   |--------------|-------------|
   |Scenario      |variable1    |
   |Specification |variable2    |
   |Scenario      |variable3    |
   |Suite         |variable4    |
* And the values inside the data stores equal to the following

   |DataStore Type|Variable Name|Expected Value     |
   |--------------|-------------|-------------------|
   |Scenario      |variable1    |Osanda Deshan      |
   |Specification |variable2    |Osanda Nimalarathna|
   |Scenario      |variable3    |Software Automation|
   |Suite         |variable4    |Gauge Framework    |
* And the values inside the data stores not equal to the following

   |DataStore Type|Variable Name|Expected Value    |
   |--------------|-------------|------------------|
   |Scenario      |variable1    |Osanda Desha      |
   |Scenario      |variable3    |Software Automatio|
