Edit Bundle - Positive Tests Specification
==========================================
Date Created    : 05/09/2018
Version         : 1.0.0
Owner      	    : Kinkini Gamage
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.


tags: bundle, edit_bundle


table: /resources/data_driven_test_csv/edit_bundle/edit_an_expert_bundle.csv



Edit expert bundle
------------------
* Create an expert bundle
* And save the JSON Path values in the response inside the data stores
    |DataStore Type |Variable Name  |Value To Be Stored     |
    |---------------|---------------|-----------------------|
    |scenario       |id             |$.id                   |
* Given that a user needs to invoke <api>
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |
* And the user set the path parameters using data stores as follows
    |Path Name      |Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value     |
    |---------------|-------------------|---------------|------------------------|---------------|
    |id             |y                  |scenario       |id                      |N/A            |
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name|Attribute Value To Be Set|
     |--------------------------------|-------------------|---------------|------------------------|-------------------------|
     |#subjectId                      |n                  |               |                        |<subjectId>              |
     |#title                          |n                  |               |                        |<title>                  |
     |#status                         |n                  |               |                        |<status>                 |
     |#skuId                          |n                  |               |                        |<skuId>                  |
     |#price                          |n                  |               |                        |<price>                  |
     |#purchaseStatus                 |n                  |               |                        |<purchaseStatus>         |
     |#bookAuthor                     |n                  |               |                        |<bookAuthor>             |
     |#bookTitle                      |n                  |               |                        |<bookTitle>              |
     |#description                    |n                  |               |                        |<description>            |
     |#createdSource                  |n                  |               |                        |<createdSource>          |
     |#keyword1                       |n                  |               |                        |<keyword1>               |
     |#keyword2                       |n                  |               |                        |<keyword2>               |
     |#noOfDecks                      |n                  |               |                        |<noOfDecks>              |
     |#authorId                       |n                  |               |                        |<authorId>               |
     |#noOfDecks                      |n                  |               |                        |<noOfDecks>              |
//     |#previewcards                   |n                  |               |                        |<previewcards>           |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the values inside the data stores
      |JSON Path              |Is Data Store Used?|Data Store Type|Data Store Variable Name|Value                                       |
      |-----------------------|-------------------|---------------|------------------------|--------------------------------------------|
      |$.subjectId            |n                  |               |                        |<subjectId>                                 |
      |$.title                |n                  |               |                        |<title>                                     |
      |$.status               |n                  |               |                        |<status>                                    |
      |$.purchaseInfo.sku     |n                  |               |                        |<skuId>                                     |
      |$.book.bookAuthor      |n                  |               |                        |<bookAuthor>                                |
      |$.book.bookTitle       |n                  |               |                        |<bookTitle>                                 |
      |$.description          |n                  |               |                        |<description>                               |
      |$.authorId             |n                  |               |                        |<authorId>                                  |
      |$.purchaseInfo.price   |n                  |               |                        |<price>                                     |
      |$.purchaseInfo.status  |n                  |               |                        |<purchaseStatus>                            |
      |$.keywords[0]          |n                  |               |                        |<keyword1>                                  |
      |$.keywords[1]          |n                  |               |                        |<keyword2>                                  |
      |$.noOfDecks            |n                  |               |                        |<noOfDecks>                                 |
      |$.createdSource        |n                  |               |                        |<createdSource>                             |



_________________________________________________________________________________________________________
* Given that a user needs to invoke "Delete Expert Deck by ID using Expert Deck Service"
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |
* And the user set the path parameters using data stores as follows
    |Path Name      |Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value     |
    |---------------|-------------------|---------------|------------------------|---------------|
    |skuUUID        |y                  |scenario       |expertDeckId1           |N/A            |
* When the user invokes the API
* Then the status code for the request is "204"

* Given that a user needs to invoke "Delete Expert Deck by ID using Expert Deck Service"
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |
* And the user set the path parameters using data stores as follows
    |Path Name      |Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value     |
    |---------------|-------------------|---------------|------------------------|---------------|
    |skuUUID        |y                  |scenario       |expertDeckId2           |N/A            |
* When the user invokes the API
* Then the status code for the request is "204"