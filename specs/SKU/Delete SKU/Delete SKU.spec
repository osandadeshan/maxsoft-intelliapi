Delete SKU Specification
========================
Date Created    : 05/23/2018
Version         : 1.0.0
Owner      	    : Osanda Deshan
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.


tags: sku, delete_sku



Delete SKU using valid SKU Id
-----------------------------
* Create a sku
* And save the JSON Path values in the response inside the data stores
    |DataStore Type |Variable Name  |Value To Be Stored     |
    |---------------|---------------|-----------------------|
    |scenario       |skuUUID        |$.id                   |
* Given that a user needs to invoke "Delete SKU"
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |
* And the user set the path parameters using data stores as follows
    |Path Name      |Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value     |
    |---------------|-------------------|---------------|------------------------|---------------|
    |skuUUID        |y                  |scenario       |skuUUID                 |N/A            |
* When the user invokes the API
* Then the status code for the request is "204"



Delete SKU using already deleted SKU Id
---------------------------------------
* Given that a user needs to invoke "Delete SKU"
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |
* And the user set the path parameters using data stores as follows
    |Path Name      |Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value               |
    |---------------|-------------------|---------------|------------------------|-------------------------|
    |skuUUID        |n                  |               |                        |5b06e0ff2e02d830640d05df |
* When the user invokes the API
* Then the status code for the request is "404"



Delete SKU using invalid SKU Id
-------------------------------
* Given that a user needs to invoke "Delete SKU"
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |
* And the user set the path parameters using data stores as follows
    |Path Name      |Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value               |
    |---------------|-------------------|---------------|------------------------|-------------------------|
    |skuUUID        |n                  |               |                        |osanda                   |
* When the user invokes the API
* Then the status code for the request is "404"