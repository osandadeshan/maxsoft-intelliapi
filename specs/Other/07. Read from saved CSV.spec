# Read from saved CSV Specification
Project Name : MaxSoft-IntelliAPI
Developer    : Osanda Deshan
Version      : 1.0.0
Date         : 6/7/2018
Time         : 9:30 PM
Description  : This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.


table: /resources/csv/questionIds.csv



## Delete the created questions
* Given that a user needs to invoke "Delete a Question using Question Service"
* And the user set the request authentication configurations as follows 

   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |Yes                |
   |Do you need to retrieve the access token from the text file?      |Yes                |
   |Provide the access token if you need to authorize the API manually|N/A                |
* And the user set the path parameters as follows 

   |Path Parameter|Path Value  |
   |--------------|------------|
   |questionId    |<questionId>|
* When the user invokes the API
* Then the status code for the request is "204"
