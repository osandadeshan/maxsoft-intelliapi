# Data Store Comparison Specification

<pre>
Project Name    : MaxSoft-IntelliAPI
Developer       : Osanda Deshan
Version         : 1.0.0
Date            : 27/04/2019
Time            : 21:18
Description     : This is an executable specification file
</pre>


tags: data_store



* Given that a user needs to invoke "Get Auth Token"
* And the user set the request authentication configurations as follows 

   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |No                 |
   |Do you need to retrieve the access token from the text file?      |N/A                |
   |Provide the access token if you need to authorize the API manually|N/A                |
* And the user set the request payload as follows <file:/resources/payloads/login.txt>
* When the user invokes the API
* Then the status code for the request is "201"
* And save the JSON Path values in the response inside the data stores 

   |DataStore Type|Variable Name|Value To Be Stored|
   |--------------|-------------|------------------|
   |Scenario      |status       |$.status          |
* And the user saves the values inside data stores as follows 

   |DataStore Type|Variable Name |Value To Be Stored|
   |--------------|--------------|------------------|
   |Scenario      |username      |osanda12          |
   |Scenario      |mobileUserName|osanda12          |



## Equality of data store values with hard coded values

* And the values inside the data stores equal to the following 

   |DataStore Type|Variable Name|Expected Value|
   |--------------|-------------|--------------|
   |Scenario      |username     |osanda12      |
   |Scenario      |status       |success       |



## Equality of data store values with another data store values

* And the values inside two data stores should be equal 

   |DataStore 1 Type|Variable 1 Name|DataStore 2 Type|Variable 2 Name|
   |----------------|---------------|----------------|---------------|
   |Scenario        |username       |Scenario        |mobileUserName |



## Not equality of data store values with hard coded values

* And the values inside the data stores not equal to the following 

   |DataStore Type|Variable Name|Expected Value|
   |--------------|-------------|--------------|
   |Scenario      |username     |osanda        |
   |Scenario      |status       |succes        |



## Not equality of data store values with another data store values

* And the values inside two data stores should not be equal 

   |DataStore 1 Type|Variable 1 Name|DataStore 2 Type|Variable 2 Name|
   |----------------|---------------|----------------|---------------|
   |Scenario        |username       |Scenario        |status         |



## Contains of data store values with hard coded values

* And the values inside the data stores contain the following 

   |DataStore Type|Variable Name|Expected Value|
   |--------------|-------------|--------------|
   |Scenario      |username     |osanda        |
   |Scenario      |status       |succes        |



## Contains of data store values with another data store values

* And the value inside a data store should contain the value of the other data store 

   |DataStore 1 Type|Variable 1 Name|DataStore 2 Type|Variable 2 Name|
   |----------------|---------------|----------------|---------------|
   |Scenario        |username       |Scenario        |mobileUserName |



## Not contains of data store values with hard coded values

* And the values inside the data stores not contain the following 

   |DataStore Type|Variable Name|Expected Value|
   |--------------|-------------|--------------|
   |Scenario      |username     |deshan        |
   |Scenario      |status       |fail          |



## Not contains of data store values with another data store values

* And the value inside a data store should not contain the value of the other data store 

   |DataStore 1 Type|Variable 1 Name|DataStore 2 Type|Variable 2 Name|
   |----------------|---------------|----------------|---------------|
   |Scenario        |username       |Scenario        |status         |
