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
     |#subject                        |n                  |               |                        |<subject>                |
     |#title                          |n                  |               |                        |<title>                  |
     |#status                         |n                  |               |                        |<status>                 |
     |#previewcards                   |n                  |               |                        |<previewcards>           |
     |#skuId                          |n                  |               |                        |<skuId>                  |
     |#bookAuthor                     |n                  |               |                        |<bookAuthor>             |
     |#bookTitle                      |n                  |               |                        |<bookTitle>              |
     |#description                    |n                  |               |                        |<description>            |
     |#id1                            |y                  |scenario       |id1                     |                         |
     |#id2                            |y                  |scenario       |id2                     |                         |
     |#userId                         |n                  |               |                        |<userId>                 |
     |#createdSource                  |n                  |               |                        |<createdSource>          |
     |#price                          |n                  |               |                        |<price>                  |
     |#keyword1                       |n                  |               |                        |<keyword1>               |
     |#keyword2                       |n                  |               |                        |<keyword2>               |
     |#noOfDecks                      |n                  |               |                        |<noOfDecks>              |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the values inside the data stores
      |JSON Path       |Is Data Store Used?|Data Store Type|Data Store Variable Name|Value                                       |
      |--------------  |-------------------|---------------|------------------------|--------------------------------------------|
      |$.subject       |n                  |               |                        |<subject>                                   |
      |$.title         |n                  |               |                        |<title>                                     |
      |$.status        |n                  |               |                        |<status>                                    |
      |$.previewcards  |n                  |               |                        |<previewcards>                              |
      |$.skuId         |n                  |               |                        |<skuId>                                     |
      |$.bookAuthor    |n                  |               |                        |<bookAuthor>                                |
      |$.bookTitle     |n                  |               |                        |<bookTitle>                                 |
      |$.description   |n                  |               |                        |<description>                               |
      |$.deckId[0]     |y                  |scenario       |id1                     |                                            |
      |$.deckId[1]     |y                  |scenario       |id2                     |                                            |
      |$.userId        |n                  |               |                        |<userId>                                    |
      |$.createdSource |n                  |               |                        |<createdSource>                             |
      |$.price         |n                  |               |                        |<price>                                     |
      |$.keyword1      |n                  |               |                        |<keyword1>                                  |
      |$.keyword2      |n                  |               |                        |<keyword2>                                  |
      |$.noOfDecks     |n                  |               |                        |<noOfDecks>                                 |

