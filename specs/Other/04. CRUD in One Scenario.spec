# CRUD in One Scenario Specification
Created by Osanda Deshan on 5/26/2018

This is an executable specification file which follows markdown syntax.
Every heading in this file denotes a scenario. Every bulleted point denotes a step.



## CRUD operation for a sku and get all the 9 questions in a deck
* Given that a user needs to invoke "Create SKU"
* And the user set the request authentication configurations as follows 

   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |Yes                |
   |Do you need to retrieve the access token from the text file?      |Yes                |
   |Provide the access token if you need to authorize the API manually|N/A                |
* And the user set the request attributes as follows 

   |Attribute Value In JSON Template|Attribute Value To Be Set|
   |--------------------------------|-------------------------|
   |#skuId                          |sampleSkuId1             |
   |#price                          |1.19                     |
   |#type                           |DECK                     |
* When the user invokes the API
* Then the status code for the request is "201"
* And the JSON Path Assertions for the response should be equal to the following 

   |JSON Path|Expected Result|
   |---------|---------------|
   |$.skuId  |sampleSkuId1   |
   |$.price  |1.19           |
   |$.type   |DECK           |
* And save the JSON Path values in the response inside the data stores 

   |DataStore Type|Variable Name|Value To Be Stored|
   |--------------|-------------|------------------|
   |scenario      |skuUUID1     |$.id              |

* Create a sku
* And save the JSON Path values in the response inside the data stores 

   |DataStore Type|Variable Name|Value To Be Stored|
   |--------------|-------------|------------------|
   |scenario      |skuUUID2     |$.id              |

* Given that a user needs to invoke "Edit SKU"
* And the user set the path parameters using data stores as follows 

   |Path Name|Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value|
   |---------|-------------------|---------------|------------------------|----------|
   |skuUUID  |y                  |scenario       |skuUUID2                |N/A       |
* And the user set the request authentication configurations as follows 

   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |Yes                |
   |Do you need to retrieve the access token from the text file?      |Yes                |
   |Provide the access token if you need to authorize the API manually|N/A                |
* And the user set the request attributes as follows 

   |Attribute Value In JSON Template|Attribute Value To Be Set|
   |--------------------------------|-------------------------|
   |#skuId                          |sampleSkuId2             |
   |#price                          |1.07                     |
   |#type                           |DECK                     |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following 

   |JSON Path|Expected Result|
   |---------|---------------|
   |$.skuId  |sampleSkuId2   |
   |$.price  |1.07           |
   |$.type   |DECK           |

* Given that a user needs to invoke "Delete SKU"
* And the user set the request authentication configurations as follows 

   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |Yes                |
   |Do you need to retrieve the access token from the text file?      |Yes                |
   |Provide the access token if you need to authorize the API manually|N/A                |
* And the user set the path parameters using data stores as follows 

   |Path Name|Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value|
   |---------|-------------------|---------------|------------------------|----------|
   |skuUUID  |y                  |scenario       |skuUUID1                |N/A       |
* When the user invokes the API
* Then the status code for the request is "204"

* Given that a user needs to invoke "Delete SKU"
* And the user set the request authentication configurations as follows 

   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |Yes                |
   |Do you need to retrieve the access token from the text file?      |Yes                |
   |Provide the access token if you need to authorize the API manually|N/A                |
* And the user set the path parameters using data stores as follows 

   |Path Name|Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value|
   |---------|-------------------|---------------|------------------------|----------|
   |skuUUID  |y                  |scenario       |skuUUID2                |N/A       |
* When the user invokes the API
* Then the status code for the request is "204"

* Create a my deck with all types of 9 questions
* Given that a user needs to invoke "Get all Questions using Aggregation Service"
* And the user set the request authentication configurations as follows 

   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |Yes                |
   |Do you need to retrieve the access token from the text file?      |Yes                |
   |Provide the access token if you need to authorize the API manually|N/A                |
* And the user set the query parameters using data stores as follows 

   |Query Name|Is Data Store Used?|Data Store Type|Data Store Variable Name|Query Value|
   |----------|-------------------|---------------|------------------------|-----------|
   |deckId    |y                  |spec           |myDeckIdWith9Questions  |N/A        |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following 

   |JSON Path                           |Value|
   |------------------------------------|-----|
   |$.questions.length()                |9    |
   |$.questions.[-1].question.media     |TEXT |
   |$.questions.[-1].question.promptType|TEXT |
   |$.questions.[-1].creatoredSource    |App  |
   |$.questions.[-1].answers.[0].type   |TEXT |
