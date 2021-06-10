# Data Store Arithmetic Operations Specification

Project Name : MaxSoft-IntelliAPI
Developer    : Osanda Deshan
Version      : 1.0.0
Date         : 12/24/2020
Time         : 10:13 AM
Description  : This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.

tags: data_store, regression


## Add integer values in data stores and save it in a new data store

* And the user saves the values inside data stores as follows

   |DataStore Type|Variable Name|Value To Be Stored|
   |--------------|-------------|------------------|
   |Scenario      |val1         |14                |
   |Scenario      |val2         |10                |
   |Scenario      |val3         |12                |
* And add the integer values in data stores and save it in a "Scenario" type data store named "totalVal"

   |DataStore Type|Variable Name|
   |--------------|-------------|
   |Scenario      |val1         |
   |Scenario      |val2         |
   |Scenario      |val3         |
* And the values inside the data stores equal to the following

   |DataStore Type|Variable Name|Expected Value|
   |--------------|-------------|--------------|
   |Scenario      |totalVal     |36            |


## Subtract integer values in data stores and save it in a new data store

* And the user saves the values inside data stores as follows

   |DataStore Type|Variable Name|Value To Be Stored|
   |--------------|-------------|------------------|
   |Scenario      |val1         |14                |
   |Scenario      |val2         |10                |
   |Scenario      |val3         |12                |
* And add the integer values in data stores and save it in a "Scenario" type data store named "val4"

   |DataStore Type|Variable Name|
   |--------------|-------------|
   |Scenario      |val1         |
   |Scenario      |val2         |
   |Scenario      |val3         |
* And subtract the integer values in data stores and save it in a new data store

   |First DataStore Type|First Variable Name|Second DataStore Type|Second Variable Name|New DataStore Type|New Variable Name|
   |--------------------|-------------------|---------------------|--------------------|------------------|-----------------|
   |Scenario            |val2               |Scenario             |val4                |Scenario          |totalVal2        |
* And the values inside the data stores equal to the following

   |DataStore Type|Variable Name|Expected Value|
   |--------------|-------------|--------------|
   |Scenario      |totalVal2    |-26           |


## Divide integer values in data stores and save it in a new data store

* And the user saves the values inside data stores as follows

   |DataStore Type|Variable Name|Value To Be Stored|
   |--------------|-------------|------------------|
   |Scenario      |val1         |14                |
   |Scenario      |val2         |10                |
   |Scenario      |val3         |12                |
* And divide the integer values in data stores and save it in a new data store

   |First DataStore Type|First Variable Name|Second DataStore Type|Second Variable Name|New DataStore Type|New Variable Name|
   |--------------------|-------------------|---------------------|--------------------|------------------|-----------------|
   |Scenario            |val1               |Scenario             |val2                |Scenario          |totalVal3        |
* And the values inside the data stores equal to the following

   |DataStore Type|Variable Name|Expected Value|
   |--------------|-------------|--------------|
   |Scenario      |totalVal3    |1.4           |


## Multiply integer values in data stores and save it in a new data store

* And the user saves the values inside data stores as follows

   |DataStore Type|Variable Name|Value To Be Stored|
   |--------------|-------------|------------------|
   |Scenario      |val1         |14                |
   |Scenario      |val2         |10                |
   |Scenario      |val3         |12                |
* And multiply the integer values in data stores and save it in a "Scenario" type data store named "totalVal4"

   |DataStore Type|Variable Name|
   |--------------|-------------|
   |Scenario      |val1         |
   |Scenario      |val2         |
   |Scenario      |val3         |
* And the values inside the data stores equal to the following

   |DataStore Type|Variable Name|Expected Value|
   |--------------|-------------|--------------|
   |Scenario      |totalVal4    |1680          |


## Add decimal values in data stores and save it in a new data store

* And the user saves the values inside data stores as follows

   |DataStore Type|Variable Name|Value To Be Stored|
   |--------------|-------------|------------------|
   |Scenario      |val1         |14.2              |
   |Scenario      |val2         |10.326            |
   |Scenario      |val3         |12                |
* And add the decimal values in data stores and save it in a "Scenario" type data store named "totalVal"

   |DataStore Type|Variable Name|
   |--------------|-------------|
   |Scenario      |val1         |
   |Scenario      |val2         |
   |Scenario      |val3         |
* And the values inside the data stores equal to the following

   |DataStore Type|Variable Name|Expected Value|
   |--------------|-------------|--------------|
   |Scenario      |totalVal     |36.526        |


## Subtract decimal values in data stores and save it in a new data store

* And the user saves the values inside data stores as follows

   |DataStore Type|Variable Name|Value To Be Stored|
   |--------------|-------------|------------------|
   |Scenario      |val1         |14.2              |
   |Scenario      |val2         |10.326            |
   |Scenario      |val3         |12                |
* And add the decimal values in data stores and save it in a "Scenario" type data store named "val4"

   |DataStore Type|Variable Name|
   |--------------|-------------|
   |Scenario      |val1         |
   |Scenario      |val2         |
   |Scenario      |val3         |
* And subtract the decimal values in data stores and save it in a new data store

   |First DataStore Type|First Variable Name|Second DataStore Type|Second Variable Name|New DataStore Type|New Variable Name|
   |--------------------|-------------------|---------------------|--------------------|------------------|-----------------|
   |Scenario            |val2               |Scenario             |val4                |Scenario          |totalVal2        |
* And the values inside the data stores equal to the following

   |DataStore Type|Variable Name|Expected Value|
   |--------------|-------------|--------------|
   |Scenario      |totalVal2    |-26.2         |


## Divide decimal values in data stores and save it in a new data store

* And the user saves the values inside data stores as follows

   |DataStore Type|Variable Name|Value To Be Stored|
   |--------------|-------------|------------------|
   |Scenario      |val1         |14.125            |
   |Scenario      |val2         |10.23             |
   |Scenario      |val3         |0.125             |
* And divide the decimal values in data stores and save it in a new data store

   |First DataStore Type|First Variable Name|Second DataStore Type|Second Variable Name|New DataStore Type|New Variable Name|
   |--------------------|-------------------|---------------------|--------------------|------------------|-----------------|
   |Scenario            |val1               |Scenario             |val2                |Scenario          |totalVal3        |
* And the values inside the data stores equal to the following

   |DataStore Type|Variable Name|Expected Value|
   |--------------|-------------|--------------|
   |Scenario      |totalVal3    |1.380743      |
* And divide the decimal values in data stores and save it in a new data store

   |First DataStore Type|First Variable Name|Second DataStore Type|Second Variable Name|New DataStore Type|New Variable Name|
   |--------------------|-------------------|---------------------|--------------------|------------------|-----------------|
   |Scenario            |val1               |Scenario             |val3                |Scenario          |totalVal4        |
* And the values inside the data stores equal to the following

   |DataStore Type|Variable Name|Expected Value|
   |--------------|-------------|--------------|
   |Scenario      |totalVal4    |113.0         |


## Multiply decimal values in data stores and save it in a new data store

* And the user saves the values inside data stores as follows

   |DataStore Type|Variable Name|Value To Be Stored|
   |--------------|-------------|------------------|
   |Scenario      |val1         |14.023            |
   |Scenario      |val2         |10.108            |
   |Scenario      |val3         |12.1              |
* And multiply the decimal values in data stores and save it in a "Scenario" type data store named "totalVal4"

   |DataStore Type|Variable Name|
   |--------------|-------------|
   |Scenario      |val1         |
   |Scenario      |val2         |
   |Scenario      |val3         |
* And the values inside the data stores equal to the following

   |DataStore Type|Variable Name|Expected Value|
   |--------------|-------------|--------------|
   |Scenario      |totalVal4    |1715.1083     |
