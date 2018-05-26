Edit SKU - Positive Tests Specification
=======================================
Date Created    : 05/20/2018
Version         : 1.0.0
Owner      	    : Osanda Deshan
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.


tags: sku, edit_sku, positive



Edit a sku for a deck without price attribute
---------------------------------------------
* Create a sku
* And save the JSON Path values in the response inside the data stores
    |DataStore Type |Variable Name  |Value To Be Stored     |
    |---------------|---------------|-----------------------|
    |scenario       |skuUUID1       |$.id                   |
* Given that a user needs to invoke "Edit SKU"
* And the user set the path parameters using data stores as follows
    |Path Name      |Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value     |
    |---------------|-------------------|---------------|------------------------|---------------|
    |skuUUID        |y                  |scenario       |skuUUID1                |N/A            |
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set|
     |--------------------------------|-------------------------|
     |#skuId                          |AAPIPH5-DC2-W            |
     |"price":#price,                 |                         |
     |#type                           |DECK                     |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path     |Expected Result|
     |--------------|---------------|
     |$.skuId       |AAPIPH5-DC2-W  |
     |$.price       |0.0            |
     |$.type        |DECK           |

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
    |skuUUID        |y                  |scenario       |skuUUID1                |N/A            |
* When the user invokes the API
* Then the status code for the request is "204"



Edit a sku for a deck with empty price
--------------------------------------
* Create a sku
* And save the JSON Path values in the response inside the data stores
    |DataStore Type |Variable Name  |Value To Be Stored     |
    |---------------|---------------|-----------------------|
    |scenario       |skuUUID1       |$.id                   |
* Given that a user needs to invoke "Edit SKU"
* And the user set the path parameters using data stores as follows
    |Path Name      |Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value     |
    |---------------|-------------------|---------------|------------------------|---------------|
    |skuUUID        |y                  |scenario       |skuUUID1                |N/A            |
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set|
     |--------------------------------|-------------------------|
     |#skuId                          |AAPIPH5-DC2-W            |
     |#price                          |""                       |
     |#type                           |DECK                     |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path     |Expected Result|
     |--------------|---------------|
     |$.skuId       |AAPIPH5-DC2-W  |
     |$.price       |0.0            |
     |$.type        |DECK           |

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
    |skuUUID        |y                  |scenario       |skuUUID1                |N/A            |
* When the user invokes the API
* Then the status code for the request is "204"



Edit a sku for a bundle without price attribute
-----------------------------------------------
* Create a sku
* And save the JSON Path values in the response inside the data stores
    |DataStore Type |Variable Name  |Value To Be Stored     |
    |---------------|---------------|-----------------------|
    |scenario       |skuUUID1       |$.id                   |
* Given that a user needs to invoke "Edit SKU"
* And the user set the path parameters using data stores as follows
    |Path Name      |Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value     |
    |---------------|-------------------|---------------|------------------------|---------------|
    |skuUUID        |y                  |scenario       |skuUUID1                |N/A            |
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set|
     |--------------------------------|-------------------------|
     |#skuId                          |AAPIPH5-DC2-W            |
     |"price":#price,                 |                         |
     |#type                           |BUNDLE                   |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path     |Expected Result|
     |--------------|---------------|
     |$.skuId       |AAPIPH5-DC2-W  |
     |$.price       |0.0            |
     |$.type        |BUNDLE         |

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
    |skuUUID        |y                  |scenario       |skuUUID1                |N/A            |
* When the user invokes the API
* Then the status code for the request is "204"



Edit a sku for a bundle with empty price
----------------------------------------
* Create a sku
* And save the JSON Path values in the response inside the data stores
    |DataStore Type |Variable Name  |Value To Be Stored     |
    |---------------|---------------|-----------------------|
    |scenario       |skuUUID1       |$.id                   |
* Given that a user needs to invoke "Edit SKU"
* And the user set the path parameters using data stores as follows
    |Path Name      |Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value     |
    |---------------|-------------------|---------------|------------------------|---------------|
    |skuUUID        |y                  |scenario       |skuUUID1                |N/A            |
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set|
     |--------------------------------|-------------------------|
     |#skuId                          |AAPIPH5-DC2-W            |
     |#price                          |""                       |
     |#type                           |BUNDLE                   |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path     |Expected Result|
     |--------------|---------------|
     |$.skuId       |AAPIPH5-DC2-W  |
     |$.price       |0.0            |
     |$.type        |BUNDLE         |

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
    |skuUUID        |y                  |scenario       |skuUUID1                |N/A            |
* When the user invokes the API
* Then the status code for the request is "204"



Edit a sku for a bundle which has the price similar to a deck
-------------------------------------------------------------
* Given that a user needs to invoke "Create SKU"
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set|
     |--------------------------------|-------------------------|
     |#skuId                          |AAPIPH5-DC2-W            |
     |#price                          |23.12                    |
     |#type                           |DECK                     |
* When the user invokes the API
* Then the status code for the request is "201"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path     |Expected Result|
     |--------------|---------------|
     |$.skuId       |AAPIPH5-DC2-W  |
     |$.price       |23.12          |
     |$.type        |DECK           |
* And save the JSON Path values in the response inside the data stores
    |DataStore Type |Variable Name  |Value To Be Stored     |
    |---------------|---------------|-----------------------|
    |scenario       |skuUUID1       |$.id                   |

* Create a sku
* And save the JSON Path values in the response inside the data stores
    |DataStore Type |Variable Name  |Value To Be Stored     |
    |---------------|---------------|-----------------------|
    |scenario       |skuUUID2       |$.id                   |
* Given that a user needs to invoke "Edit SKU"
* And the user set the path parameters using data stores as follows
    |Path Name      |Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value     |
    |---------------|-------------------|---------------|------------------------|---------------|
    |skuUUID        |y                  |scenario       |skuUUID2                |N/A            |
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set|
     |--------------------------------|-------------------------|
     |#skuId                          |AAPIPH5-DC2-Q            |
     |#price                          |23.12                    |
     |#type                           |BUNDLE                   |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path     |Expected Result|
     |--------------|---------------|
     |$.skuId       |AAPIPH5-DC2-Q  |
     |$.price       |23.12          |
     |$.type        |BUNDLE         |

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
    |skuUUID        |y                  |scenario       |skuUUID1                |N/A            |
* When the user invokes the API
* Then the status code for the request is "204"

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
    |skuUUID        |y                  |scenario       |skuUUID2                |N/A            |
* When the user invokes the API
* Then the status code for the request is "204"



Edit a sku for a deck which has the price similar to a bundle
-------------------------------------------------------------
* Given that a user needs to invoke "Create SKU"
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set|
     |--------------------------------|-------------------------|
     |#skuId                          |AAPIPH5-DC2-W            |
     |#price                          |23.12                    |
     |#type                           |BUNDLE                   |
* When the user invokes the API
* Then the status code for the request is "201"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path     |Expected Result|
     |--------------|---------------|
     |$.skuId       |AAPIPH5-DC2-W  |
     |$.price       |23.12          |
     |$.type        |BUNDLE         |
* And save the JSON Path values in the response inside the data stores
    |DataStore Type |Variable Name  |Value To Be Stored     |
    |---------------|---------------|-----------------------|
    |scenario       |skuUUID1       |$.id                   |

* Create a sku
* And save the JSON Path values in the response inside the data stores
    |DataStore Type |Variable Name  |Value To Be Stored     |
    |---------------|---------------|-----------------------|
    |scenario       |skuUUID2       |$.id                   |
* Given that a user needs to invoke "Edit SKU"
* And the user set the path parameters using data stores as follows
    |Path Name      |Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value     |
    |---------------|-------------------|---------------|------------------------|---------------|
    |skuUUID        |y                  |scenario       |skuUUID2                |N/A            |
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set|
     |--------------------------------|-------------------------|
     |#skuId                          |AAPIPH5-DC2-Q            |
     |#price                          |23.12                    |
     |#type                           |DECK                     |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path     |Expected Result|
     |--------------|---------------|
     |$.skuId       |AAPIPH5-DC2-Q  |
     |$.price       |23.12          |
     |$.type        |DECK           |

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
    |skuUUID        |y                  |scenario       |skuUUID1                |N/A            |
* When the user invokes the API
* Then the status code for the request is "204"

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
    |skuUUID        |y                  |scenario       |skuUUID2                |N/A            |
* When the user invokes the API
* Then the status code for the request is "204"


//_________________________________________________________________________________________________________
//* Given that a user needs to invoke "Delete SKU"
//* And the user set the request authentication configurations as follows
//     |Configuration                                                     |Configuration Value            |
//     |------------------------------------------------------------------|-------------------------------|
//     |Is authentication required?                                       |Yes                            |
//     |Do you need to retrieve the access token from the text file?      |Yes                            |
//     |Provide the access token if you need to authorize the API manually|N/A                            |
//* And the user set the path parameters using data stores as follows
//    |Path Name      |Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value     |
//    |---------------|-------------------|---------------|------------------------|---------------|
//    |skuUUID        |y                  |scenario       |skuUUID1                |N/A            |
//* When the user invokes the API
//* Then the status code for the request is "204"
//
//* Given that a user needs to invoke "Delete SKU"
//* And the user set the request authentication configurations as follows
//     |Configuration                                                     |Configuration Value            |
//     |------------------------------------------------------------------|-------------------------------|
//     |Is authentication required?                                       |Yes                            |
//     |Do you need to retrieve the access token from the text file?      |Yes                            |
//     |Provide the access token if you need to authorize the API manually|N/A                            |
//* And the user set the path parameters using data stores as follows
//    |Path Name      |Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value     |
//    |---------------|-------------------|---------------|------------------------|---------------|
//    |skuUUID        |y                  |scenario       |skuUUID2                |N/A            |
//* When the user invokes the API
//* Then the status code for the request is "204"