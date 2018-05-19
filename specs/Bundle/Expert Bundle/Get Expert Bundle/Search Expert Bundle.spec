Search Expert Bundle Specification
==================================
Date Created    : 05/09/2018
Version         : 1.0.0
Owner      	    : Kinkini Gamage
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.


tags: bundle, get_bundle




Get expert deck bundle
----------------------
* Create 3 expert deck bundles
* And the user set the path parameters using data stores as follows
    |Path Name      |Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value     |
    |---------------|-------------------|---------------|------------------------|---------------|
    |title          |y                  |scenario       |title                 |N/A            |
* And the user set the query parameters using data stores as follows
    |Query Name     |Is Data Store Used?|Data Store Type|Data Store Variable Name|Query Value    |
    |---------------|-------------------|---------------|------------------------|---------------|
    |searchQuery    |n                  |               |                        |Java           |
* Given that a user needs to invoke "Get Expert Bundle"
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                 |Expected Result             |
     |----------- --------------|----------------------------|
     |$.subject                 |Information Technology      |
     |$.title                   |Java                        |
     |$.status                  |true                        |
     |$.previewcards            |true                        |
     |$.skuId                   |1234                        |
     |$.bookAuthor              |Kinkini Gamage              |
     |$.bookTitle               |Java Language               |
     |$.description             |Learn Java                  |
     |$.userId                  |osanda12                    |
     |$.createdSource           |web                         |
     |$.price                   |500.0                       |
     |$.noOfDecks               |20                          |

