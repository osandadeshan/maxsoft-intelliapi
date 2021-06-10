# Write to CSV Specification

Project Name : MaxSoft-IntelliAPI
Developer    : Osanda Deshan
Version      : 1.0.0
Date         : 6/7/2018
Time         : 9:30 PM
Description  : This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.

tags: csv, pre_requisites, regression


## Get all users and save userIds greater than 16

* Create a user
* Create a user
* Create a user
* Create a user
* Given that a user needs to invoke "Get all users"
* And the user set the request authentication configurations as follows

   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |Yes                |
   |Do you need to retrieve the access token from the text file?      |Yes                |
   |Provide the access token if you need to authorize the API manually|N/A                |
* When the user invokes the API
* Then the status code for the request is "200"
* And save the JSON Array values of the response into CSV files

   |JSON Path              |Header Name|CSV File Path                      |
   |-----------------------|-----------|-----------------------------------|
   |$.data[?(@.id > 16)].id|userId     |/src/test/resources/csv/userIds.csv|


## Replace CSV column with timestamp
* And replace the row values in "timestamp" column of the CSV "/src/test/resources/csv/timestamp.csv" into the "yyyy-MM-dd'T'HH:mm:ss.SSS'Z'" timestamp pattern
