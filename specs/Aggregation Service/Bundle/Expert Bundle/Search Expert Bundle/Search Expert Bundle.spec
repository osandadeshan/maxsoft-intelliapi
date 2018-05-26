Search Expert Bundle Specification
==================================
Date Created    : 05/09/2018
Version         : 1.0.0
Owner      	    : Kinkini Gamage
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.


tags: bundle, get_bundle



Get expert deck bundle by title
-------------------------------
* Create 3 expert bundles
* And the user set the path parameters using data stores as follows
    |Path Name      |Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value     |
    |---------------|-------------------|---------------|------------------------|---------------|
    |userId1        |n                  |scenario       |                        |osanda12       |
* And the user set the query parameters using data stores as follows
    |Query Name     |Is Data Store Used?|Data Store Type|Data Store Variable Name|Query Value    |
    |---------------|-------------------|---------------|------------------------|---------------|
    |searchQuery    |y                  |scenario       |title1                  |N/A            |
* Given that a user needs to invoke "Get Expert Bundle using Aggregation Service"
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                    |Expected Result             |
     |-----------------------------|----------------------------|
     |$.bundles[-1:].subjectId     |Information Technology1     |
     |$.bundles[-1:].title         |Network Security1           |


Get expert deck bundle by subject
---------------------------------
* Create 3 expert bundles
* And the user set the path parameters using data stores as follows
    |Path Name      |Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value     |
    |---------------|-------------------|---------------|------------------------|---------------|
    |userId1        |n                  |scenario       |                        |osanda12       |
* And the user set the query parameters using data stores as follows
    |Query Name     |Is Data Store Used?|Data Store Type|Data Store Variable Name|Query Value    |
    |---------------|-------------------|---------------|------------------------|---------------|
    |searchQuery    |y                  |scenario       |subject1                |N/A            |
* Given that a user needs to invoke "Get Expert Bundle using Aggregation Service"
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                    |Expected Result             |
     |-----------------------------|----------------------------|
     |$.bundles[-1:].subjectId     |Information Technology1     |
     |$.bundles[-1:].title         |Network Security1           |


Get expert deck bundle by bookAuthor
------------------------------------
* Create 3 expert bundles
* And the user set the path parameters using data stores as follows
    |Path Name      |Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value     |
    |---------------|-------------------|---------------|------------------------|---------------|
    |userId1        |n                  |scenario       |                        |osanda12       |
* And the user set the query parameters using data stores as follows
    |Query Name     |Is Data Store Used?|Data Store Type|Data Store Variable Name|Query Value    |
    |---------------|-------------------|---------------|------------------------|---------------|
    |searchQuery    |y                  |scenario       |bookAuthor1             |N/A            |
* Given that a user needs to invoke "Get Expert Bundle using Aggregation Service"
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                    |Expected Result             |
     |-----------------------------|----------------------------|
     |$.bundles[-1:].subjectId     |Information Technology1     |
     |$.bundles[-1:].title         |Network Security1           |


Get expert deck bundle by bookTitle
-----------------------------------
* Create 3 expert bundles
* And the user set the path parameters using data stores as follows
    |Path Name      |Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value     |
    |---------------|-------------------|---------------|------------------------|---------------|
    |userId1        |n                  |scenario       |                        |osanda12       |
* And the user set the query parameters using data stores as follows
    |Query Name     |Is Data Store Used?|Data Store Type|Data Store Variable Name|Query Value    |
    |---------------|-------------------|---------------|------------------------|---------------|
    |searchQuery    |y                  |scenario       |bookTitle1              |N/A            |
* Given that a user needs to invoke "Get Expert Bundle using Aggregation Service"
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                    |Expected Result             |
     |-----------------------------|----------------------------|
     |$.bundles[-1:].subjectId     |Information Technology1     |
     |$.bundles[-1:].title         |Network Security1           |


Get expert deck bundle by keyword
-----------------------------------
* Create 3 expert bundles
* And the user set the path parameters using data stores as follows
    |Path Name      |Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value     |
    |---------------|-------------------|---------------|------------------------|---------------|
    |userId1        |n                  |scenario       |                        |osanda12       |
* And the user set the query parameters using data stores as follows
    |Query Name     |Is Data Store Used?|Data Store Type|Data Store Variable Name|Query Value    |
    |---------------|-------------------|---------------|------------------------|---------------|
    |searchQuery    |y                  |scenario       |keyword1                |N/A            |
* Given that a user needs to invoke "Get Expert Bundle using Aggregation Service"
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                    |Expected Result             |
     |-----------------------------|----------------------------|
     |$.bundles[-1:].subjectId     |Information Technology1     |
     |$.bundles[-1:].title         |Network Security1           |




//___________________________
//
//* Given that a user needs to invoke "Delete a Deck using Deck Service"
//* And the user set the path parameters using data stores as follows
//    |Path Name      |Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value     |
//    |---------------|-------------------|---------------|------------------------|---------------|
//    |expertDeckId1  |y                  |spec           |expertDeckId1           |N/A            |
//* When the user invokes the API
//* Then the status code for the request is "204"
//
//* Given that a user needs to invoke "Delete a Deck using Deck Service"
//* And the user set the path parameters using data stores as follows
//    |Path Name      |Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value     |
//    |---------------|-------------------|---------------|------------------------|---------------|
//    |expertDeckId2  |y                  |spec           |expertDeckId2           |N/A            |
//* When the user invokes the API
//* Then the status code for the request is "204"
//
//* Given that a user needs to invoke "Delete a Deck using Deck Service"
//* And the user set the path parameters using data stores as follows
//    |Path Name      |Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value     |
//    |---------------|-------------------|---------------|------------------------|---------------|
//    |bundleId1      |y                  |spec           |bundleId1               |N/A            |
//* When the user invokes the API
//* Then the status code for the request is "204"
//
//* Given that a user needs to invoke "Delete a Deck using Deck Service"
//* And the user set the path parameters using data stores as follows
//    |Path Name      |Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value     |
//    |---------------|-------------------|---------------|------------------------|---------------|
//    |bundleId2      |y                  |spec           |dbundleId2              |N/A            |
//* When the user invokes the API
//* Then the status code for the request is "204"
//
//* Given that a user needs to invoke "Delete a Deck using Deck Service"
//* And the user set the path parameters using data stores as follows
//    |Path Name      |Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value     |
//    |---------------|-------------------|---------------|------------------------|---------------|
//    |bundleId3      |y                  |spec           |bundleId3               |N/A            |
//* When the user invokes the API
//* Then the status code for the request is "204"


