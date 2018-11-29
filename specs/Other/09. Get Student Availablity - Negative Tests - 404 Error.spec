# Get Student Availability - Negative Tests Specification - 404 Error
Project Name : MaxSoft-IntelliAPI
Developer    : Osanda Deshan
Version      : 1.0.0
Date         : 6/17/2018
Time         : 2:06 PM
Description  : This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.



## Get Student Availability 404 Not Found
* Given that a user needs to invoke "Get Student Availability"
* And the user set the request authentication configurations as follows 

   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |Yes                |
   |Do you need to retrieve the access token from the text file?      |Yes                |
   |Provide the access token if you need to authorize the API manually|N/A                |
* And the user set the path parameters using data stores as follows 

   |Path Name   |Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value  |
   |------------|-------------------|---------------|------------------------|------------|
   |availability|n                  |               |                        |availability|
* And the user set the request attributes using data stores as follows 

   |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name|Attibute Value To Be Set|
   |--------------------------------|-------------------|---------------|------------------------|------------------------|
   |#courseId                       |n                  |scenario       |courseId                |1235                    |
   |#userId1                        |n                  |scenario       |userId1                 |1                       |
   |#userId2                        |n                  |scenario       |userId2                 |116                     |
* When the user invokes the API
* Then the status code for the request is "404"
* And the JSON Path Assertions for the response should be equal to the following 

   |JSON Path|Expected Result           |
   |---------|--------------------------|
   |$.message|Invalid student Ids: [116]|
