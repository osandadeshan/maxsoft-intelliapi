# Read CSV File Saved In Pre Test Specification

<pre>
Project Name    : MaxSoft-IntelliAPI
Developer       : Osanda Deshan
Version         : 1.0.0
Date            : 28/04/2019
Time            : 19:36
Description     : This is an executable specification file
</pre>


table: /resources/csv/questionIds.csv



## Delete questions by questionIds which was saved in a CSV file from the pre test

* Given that a user needs to invoke "Delete Question"
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
