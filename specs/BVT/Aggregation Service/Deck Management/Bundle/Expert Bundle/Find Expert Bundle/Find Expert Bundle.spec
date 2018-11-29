# Find Expert Bundle Specification
Date Created    : 05/30/2018
Version         : 1.0.0
Owner      	    : Kinkini Gamage
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.


tags: bundle, get_bundle



## Find expert bundle
* Create 3 expert bundles
* And the user set the path parameters using data stores as follows 

   |Query Name|Is Data Store Used?|Data Store Type|Data Store Variable Name|Query Value|
   |----------|-------------------|---------------|------------------------|-----------|
   |ID        |y                  |scenario       |bundleId1               |N/A        |
* Given that a user needs to invoke "Find a Bundle using Aggregation Service"
* And the user set the request authentication configurations as follows 

   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |Yes                |
   |Do you need to retrieve the access token from the text file?      |Yes                |
   |Provide the access token if you need to authorize the API manually|N/A                |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the values inside the data stores 

   |JSON Path        |Is Data Store Used?|Data Store Type|Data Store Variable Name|Value                  |
   |-----------------|-------------------|---------------|------------------------|-----------------------|
   |$.subjectId      |n                  |               |                        |Information Technology1|
   |$.title          |n                  |               |                        |Network Security1      |
   |$.deckId.length()|n                  |               |                        |2                      |
   |$.deckId[0]      |y                  |               |deckId1-1               |                       |
   |$.deckId[1]      |y                  |               |deckId1-2               |                       |

* Delete 3 expert bundles and associated 6 expert decks
