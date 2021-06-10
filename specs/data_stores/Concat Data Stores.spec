# Concat Data Stores Specification

Project Name : MaxSoft-IntelliAPI
Developer    : Osanda Deshan
Version      : 1.0.0
Date         : 12/24/2020
Time         : 9:45 AM
Description  : This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.

tags: data_store, regression


## Concat Data Stores

* And the user saves the values inside data stores as follows

   |DataStore Type|Variable Name|Value To Be Stored|
   |--------------|-------------|------------------|
   |Scenario      |totalLabel   |Total is:         |
   |Scenario      |val2         |10                |
   |Scenario      |val3         |12                |
* And add the integer values in data stores and save it in a "Scenario" type data store named "totalVal"

   |DataStore Type|Variable Name|
   |--------------|-------------|
   |Scenario      |val2         |
   |Scenario      |val3         |
* And concat values in data stores and save it in a "Scenario" type data store named "newTotalLabel"

   |DataStore Type|Variable Name|
   |--------------|-------------|
   |Scenario      |totalLabel   |
   |Scenario      |${SPACE}     |
* And concat values in data stores and save it in a "Scenario" type data store named "finalString"

   |DataStore Type|Variable Name|
   |--------------|-------------|
   |Scenario      |newTotalLabel|
   |Scenario      |totalVal     |
* And the values inside the data stores equal to the following

   |DataStore Type|Variable Name|Expected Value|
   |--------------|-------------|--------------|
   |Scenario      |finalString  |Total is: 22  |
