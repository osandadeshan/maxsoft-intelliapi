# Get All SKUs Specification
Date Created    : 05/23/2018
Version         : 1.0.0
Owner      	    : Osanda Deshan
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.


tags: sku, get_sku


table: /resources/data_driven_test_csv/SKUs/SKUs.csv


## Get all skus
* Create a sku
* And save the JSON Path values in the response inside the data stores 

   |DataStore Type|Variable Name|Value To Be Stored|
   |--------------|-------------|------------------|
   |scenario      |skuUUID      |$.id              |
* Given that a user needs to invoke "Get All SKUs using Aggregation Service"
* And the user set the request authentication configurations as follows 

   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |Yes                |
   |Do you need to retrieve the access token from the text file?      |Yes                |
   |Provide the access token if you need to authorize the API manually|N/A                |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the values inside the data stores 

   |JSON Path   |Is Data Store Used?|DataStore Type|Variable Name|Expected Result|
   |------------|-------------------|--------------|-------------|---------------|
   |$[-1:].id   |y                  |scenario      |skuUUID      |               |
   |$[-1:].skuId|n                  |              |             |AAPIPH5-DC2-Y  |
   |$.[-1].price|n                  |              |             |3.99           |
   |$[-1:].type |n                  |              |             |DECK           |

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
   |skuUUID  |y                  |scenario       |skuUUID                 |N/A       |
* When the user invokes the API
* Then the status code for the request is "204"

## Validate all skus for decks and bundles
* Given that a user needs to invoke "Get All SKUs using Aggregation Service"
* And the user set the request authentication configurations as follows 

   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |Yes                |
   |Do you need to retrieve the access token from the text file?      |Yes                |
   |Provide the access token if you need to authorize the API manually|N/A                |
* When the user invokes the API
* Then the status code for the request is "200"
//* And the JSON Path Assertions for the response should be equal to the "\\resources\\data_driven_test_csv\\SKUs\\SKUs.csv" data set, counter is "x"
//    |CSV Column Name |JSON Path    |
//    |----------------|-------------|
//    |SKU             |$[x].skuId   |
//    |Price           |$[x].price   |
//    |Type            |$[x].type    |
* test data set, counter is "x" 

   |JSON Path |Expected Value|
   |----------|--------------|
   |$[x].skuId|<SKU>         |
   |$[x].price|<Price>       |
   |$[x].type |<Type>        |
