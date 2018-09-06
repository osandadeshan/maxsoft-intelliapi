Saving to Data Stores Specification
===================================
Project Name : MaxSoft-IntelliAPI
Developer    : Osanda Deshan
Version      : 1.0.0
Date         : 9/6/2018
Time         : 3:25 PM
Description  : This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.



Saving to Data Stores 
---------------------
* And the user save the values inside data stores as follows
    |DataStore Type |Variable Name  |Value To Be Stored     |
    |---------------|---------------|-----------------------|
    |Scenario       |variable1      |Osanda Deshan          |
    |Specification  |variable2      |Osanda Nimalarathna    |
    |Scenario       |variable3      |Software Automation    |
    |Suite          |variable4      |Gauge Framework        |
* And the values inside the data stores equal to the following
    |DataStore Type |Variable Name  |Expected Value         |
    |---------------|---------------|-----------------------|
    |Scenario       |variable1      |Osanda Deshan          |
    |Specification  |variable2      |Osanda Nimalarathna    |
    |Scenario       |variable3      |Software Automation    |
    |Suite          |variable4      |Gauge Framework        |



Reading values from Data Store
------------------------------
* And the user read the values from data stores as follows
    |DataStore Type |Variable Name  |
    |---------------|---------------|
    |Scenario       |variable1      |
    |Specification  |variable2      |
    |Scenario       |variable3      |
    |Suite          |variable4      |
* And the values inside the data stores equal to the following
    |DataStore Type |Variable Name  |Expected Value         |
    |---------------|---------------|-----------------------|
    |Specification  |variable2      |Osanda Nimalarathna    |
    |Suite          |variable4      |Gauge Framework        |
* And the values inside the data stores not equal to the following
    |DataStore Type |Variable Name  |Expected Value         |
    |---------------|---------------|-----------------------|
    |Scenario       |variable1      |Osanda Deshan          |
    |Scenario       |variable3      |Software Automation    |