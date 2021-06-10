# Creating A List From Data Store Values Specification

Project Name : MaxSoft-IntelliAPI
Developer    : Osanda Deshan
Version      : 1.0.0
Date         : 12/24/2020
Time         : 9:57 AM
Description  : This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.

tags: data_store, regression


## Create a list from data store values

* And the user saves the values inside data stores as follows

   |DataStore Type|Variable Name|Value To Be Stored |
   |--------------|-------------|-------------------|
   |Scenario      |variable1    |Osanda Deshan      |
   |Specification |variable2    |Osanda Nimalarathna|
   |Scenario      |variable3    |Software Automation|
* And the user saves the values inside data stores as a "String" data type list into "Scenario" type data store by referencing the variable name as "var1"

   |DataStore Type|Variable Name|
   |--------------|-------------|
   |Scenario      |variable1    |
   |Specification |variable2    |
   |Scenario      |variable3    |
* And the user read the values from data stores as follows

   |DataStore Type|Variable Name|
   |--------------|-------------|
   |Scenario      |var1         |
* And the values inside the data stores equal to the following

   |DataStore Type|Variable Name|Expected Value                                             |
   |--------------|-------------|-----------------------------------------------------------|
   |Scenario      |var1         |"Osanda Deshan","Osanda Nimalarathna","Software Automation"|
