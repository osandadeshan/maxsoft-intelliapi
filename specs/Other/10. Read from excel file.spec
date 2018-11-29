# Read From Excel File Specification
Project Name : MaxSoft-IntelliAPI
Developer    : Osanda Deshan
Version      : 1.0.0
Date         : 6/17/2018
Time         : 2:06 PM
Description  : This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.



## Invoke PI API using the test data in excel file
* And the user saves test data inside excel file into data stores

   |DataStore Type|Variable Name|Excel Sheet Name |Key Name         |
   |--------------|-------------|-----------------|-----------------|
   |Scenario      |username     |TestData         |username         |
   |Specification |password     |TestData         |password         |

* Given that a user needs to invoke "Get Staging PI Token"
* And the user set the request authentication configurations as follows

   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |Yes                |
   |Do you need to retrieve the access token from the text file?      |Yes                |
   |Provide the access token if you need to authorize the API manually|N/A                |

* And the user set the request attributes using data stores as follows

   |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name|Attribute Value To Be Set           |
   |--------------------------------|-------------------|---------------|------------------------|------------------------------------|
   |#username                       |y                  |Scenario       |username                |N/A                                 |
   |#password                       |y                  |Specification  |password                |N/A                                 |
* When the user invokes the API
* Then the status code for the request is "201"
* And the JSON Path Assertions for the response should be equal to the following

   |JSON Path|Expected Result|
   |---------|---------------|
   |$.status |success        |
* And save the access token in the response which is located inside the JSON Path of "$.data"