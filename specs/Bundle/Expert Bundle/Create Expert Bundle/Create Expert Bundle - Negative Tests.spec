Create Expert Bundle - Negative Tests Specification
===================================================
Date Created    : 05/09/2018
Version         : 1.0.0
Owner      	    : Kinkini Gamage
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.


tags: bundle, create_bundle


table: /resources/data_driven_test_csv/create_bundle/create_an_expert_bundle.csv



Create bundle using expert deck service all the attributes in the contract
--------------------------------------------------------------------------
* Create an expert deck
* And save the JSON Path values in the response inside the data stores
    |DataStore Type |Variable Name  |Value To Be Stored     |
    |---------------|---------------|-----------------------|
    |scenario       |id1             |$.id                  |
* Given that a user needs to invoke <api>
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |
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
     |,"#id2"                         |n                  |               |                        |                         |
     |#userId                         |n                  |               |                        |<userId>                 |
     |#createdSource                  |n                  |               |                        |<createdSource>          |
     |#price                          |n                  |               |                        |<price>                  |
     |#keyword1                       |n                  |               |                        |<keyword1>               |
     |#keyword2                       |n                  |               |                        |<keyword2>               |
     |#noOfDecks                      |n                  |               |                        |<noOfDecks>              |
* When the user invokes the API
* Then the status code for the request is "400"


