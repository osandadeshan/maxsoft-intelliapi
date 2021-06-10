# Reading Values From Data Stores Specification

Project Name : MaxSoft-IntelliAPI
Developer    : Osanda Deshan
Version      : 1.0.0
Date         : 12/24/2020
Time         : 10:39 AM
Description  : This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.

tags: data_store, regression


## Saving values to data stores

* And the user saves the values inside data stores as follows

   |DataStore Type|Variable Name|Value To Be Stored|
   |--------------|-------------|------------------|
   |Scenario      |variable1    |Osanda Deshan     |
   |Spec          |variable2    |Gauge Framework   |


## Reading values from data stores

* And the user read the values from data stores as follows

   |DataStore Type|Variable Name|
   |--------------|-------------|
   |Spec          |variable2    |
* And the values inside the data stores equal to the following

   |DataStore Type|Variable Name|Expected Value |
   |--------------|-------------|---------------|
   |Spec          |variable2    |Gauge Framework|
* And the values inside the data stores not equal to the following

   |DataStore Type|Variable Name|Expected Value|
   |--------------|-------------|--------------|
   |Spec          |variable2    |Gauge Framewor|
