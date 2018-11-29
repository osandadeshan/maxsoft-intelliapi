# Delete A Category using Deck Service - Negative Test Specification
Date Created    : 01/16/2018
Version   		: 1.0.0
Owner      		: Osanda Deshan
Description  	: This specification covers delete a deck scenarios from the aggregation service


tags: deck_service, deck_management, delete_a_category


* Given that a user needs to invoke "Delete A Category in Deck Service"
* And the user set the request authentication configurations as follows 

   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |Yes                |
   |Do you need to retrieve the access token from the text file?      |Yes                |
   |Provide the access token if you need to authorize the API manually|N/A                |



## Delete a category using already deleted categoryId
* And the user set the path parameters as follows 

   |Path Parameter|Path Value              |
   |--------------|------------------------|
   |categoryId    |5a5db30a12ef181b0af109ba|
* When the user invokes the API
* Then the status code for the request is "404"

## Delete a category using an invalid categoryId
* And the user set the path parameters as follows 

   |Path Parameter|Path Value              |
   |--------------|------------------------|
   |categoryId    |this is not a categoryId|
* When the user invokes the API
* Then the status code for the request is "404"

## Delete a category using an empty value as the categoryId
* And the user set the path parameters as follows 

   |Path Parameter|Path Value|
   |--------------|----------|
   |categoryId    |          |
* When the user invokes the API
* Then the status code for the request is "405"
* And the JSON Path Assertions for the response should be equal to the following 

   |JSON Path  |Value                                                         |
   |-----------|--------------------------------------------------------------|
   |$.status   |405                                                           |
   |$.message  |Request method 'DELETE' not supported                         |
   |$.exception|org.springframework.web.HttpRequestMethodNotSupportedException|
   |$.error    |Method Not Allowed                                            |



## Delete a category without categoryId path parameter
* When the user invokes the API
* Then the status code for the request is "405"
* And the JSON Path Assertions for the response should be equal to the following 

   |JSON Path  |Value                                                         |
   |-----------|--------------------------------------------------------------|
   |$.status   |405                                                           |
   |$.message  |Request method 'DELETE' not supported                         |
   |$.exception|org.springframework.web.HttpRequestMethodNotSupportedException|
   |$.error    |Method Not Allowed                                            |
