# HTTP Methods Specification

Project Name    : MaxSoft-IntelliAPI
Developer       : Osanda Deshan
Version         : 1.0.0
Date            : 6/10/2021
Time            : 8:47 AM
Description     : This is an executable specification file

tags: http_methods, regression


## Invoke PATCH Request with headers, json request and authentication

* Given that a user needs to invoke "Edit a task (PATCH)"
* And the user set the request authentication configurations as follows

   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |Yes                |
   |Do you need to retrieve the access token from the text file?      |Yes                |
   |Provide the access token if you need to authorize the API manually|N/A                |
* And the user set the request headers using data stores as follows

   |Header Name |Is Data Store Used?|Data Store Type|Data Store Variable Name|Header Value|
   |------------|-------------------|---------------|------------------------|------------|
   |App-Name    |no                 |               |                        |IntelliAPI  |
   |Organization|no                 |               |                        |MaxSoft     |
* And the user set the request attributes using data stores as follows

   |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name|Attibute Value To Be Set|
   |--------------------------------|-------------------|---------------|------------------------|------------------------|
   |#name                           |no                 |               |                        |MaxSoft                 |
   |#category                       |no                 |               |                        |company                 |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the values inside the data stores

   |JSON Path|Is Data Store Used?|Data Store Type|Data Store Variable Name|Expected Value               |
   |---------|-------------------|---------------|------------------------|-----------------------------|
   |message  |no                 |               |                        |Task has updated successfully|


## Invoke PATCH Request with json request and authentication

* Given that a user needs to invoke "Edit a user (PATCH)"
* And the user set the request authentication configurations as follows

   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |Yes                |
   |Do you need to retrieve the access token from the text file?      |Yes                |
   |Provide the access token if you need to authorize the API manually|N/A                |
* And the user set the path parameters using data stores as follows

   |Path Name|Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value|
   |---------|-------------------|---------------|------------------------|----------|
   |userId   |no                 |               |                        |1         |
* And the user set the request attributes using data stores as follows

   |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name|Attibute Value To Be Set|
   |--------------------------------|-------------------|---------------|------------------------|------------------------|
   |#name                           |no                 |               |                        |Osanda                  |
   |#email                          |no                 |               |                        |osanda@gmail.com        |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the values inside the data stores

   |JSON Path   |Is Data Store Used?|Data Store Type|Data Store Variable Name|Expected Value  |
   |------------|-------------------|---------------|------------------------|----------------|
   |$.data.name |no                 |               |                        |Osanda          |
   |$.data.email|no                 |               |                        |osanda@gmail.com|
