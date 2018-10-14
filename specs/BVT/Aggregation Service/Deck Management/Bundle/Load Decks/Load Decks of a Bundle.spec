# Load Decks of a Bundle Specification
Date Created    : 05/24/2018
Version         : 1.0.0
Owner      	    : Osanda Deshan
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.


tags: load_decks_of_bundle



## Load decks of a new bundle which has two expert decks
* Create an expert bundle
* Given that a user needs to invoke "Load Decks of a Bundle"
* And the user set the path parameters using data stores as follows 

   |Path Name|Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value|
   |---------|-------------------|---------------|------------------------|----------|
   |bundleId |y                  |scenario       |bundleId                |          |
   |decks    |n                  |               |                        |decks     |
* And the user set the request authentication configurations as follows 

   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |Yes                |
   |Do you need to retrieve the access token from the text file?      |Yes                |
   |Provide the access token if you need to authorize the API manually|N/A                |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the values inside the data stores 

   |JSON Path |Is Data Store Used?|Data Store Type|Data Store Variable Name|Expected Result|
   |----------|-------------------|---------------|------------------------|---------------|
   |$.length()|n                  |               |                        |2              |
   |$[0].id   |y                  |scenario       |expertDeckId1           |               |
   |$[1].id   |y                  |scenario       |expertDeckId2           |               |

* Given that a user needs to invoke "Delete Expert Deck by ID using Expert Deck Service"
* And the user set the request authentication configurations as follows 

   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |Yes                |
   |Do you need to retrieve the access token from the text file?      |Yes                |
   |Provide the access token if you need to authorize the API manually|N/A                |
* And the user set the path parameters using data stores as follows 

   |Path Name|Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value|
   |---------|-------------------|---------------|------------------------|----------|
   |skuUUID  |y                  |scenario       |expertDeckId1           |N/A       |
* When the user invokes the API
* Then the status code for the request is "204"

* Given that a user needs to invoke "Delete Expert Deck by ID using Expert Deck Service"
* And the user set the request authentication configurations as follows 

   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |Yes                |
   |Do you need to retrieve the access token from the text file?      |Yes                |
   |Provide the access token if you need to authorize the API manually|N/A                |
* And the user set the path parameters using data stores as follows 

   |Path Name|Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value|
   |---------|-------------------|---------------|------------------------|----------|
   |skuUUID  |y                  |scenario       |expertDeckId2           |N/A       |
* When the user invokes the API
* Then the status code for the request is "204"

* Given that a user needs to invoke "Delete a Bundle"
* And the user set the request authentication configurations as follows 

   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |Yes                |
   |Do you need to retrieve the access token from the text file?      |Yes                |
   |Provide the access token if you need to authorize the API manually|N/A                |
* And the user set the path parameters using data stores as follows 

   |Path Name|Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value|
   |---------|-------------------|---------------|------------------------|----------|
   |bundleId |y                  |scenario       |bundleId                |N/A       |
* When the user invokes the API
* Then the status code for the request is "204"

## Load decks of a new bundle which has two expert decks and one is deleted
* Create an expert bundle

* Given that a user needs to invoke "Delete Expert Deck by ID using Expert Deck Service"
* And the user set the request authentication configurations as follows 

   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |Yes                |
   |Do you need to retrieve the access token from the text file?      |Yes                |
   |Provide the access token if you need to authorize the API manually|N/A                |
* And the user set the path parameters using data stores as follows 

   |Path Name   |Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value|
   |------------|-------------------|---------------|------------------------|----------|
   |expertDeckId|y                  |scenario       |expertDeckId1           |N/A       |
* When the user invokes the API
* Then the status code for the request is "204"

* Given that a user needs to invoke "Load Decks of a Bundle"
* And the user set the path parameters using data stores as follows 

   |Path Name|Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value|
   |---------|-------------------|---------------|------------------------|----------|
   |bundleId |y                  |scenario       |bundleId                |          |
   |decks    |n                  |               |                        |decks     |
* And the user set the request authentication configurations as follows 

   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |Yes                |
   |Do you need to retrieve the access token from the text file?      |Yes                |
   |Provide the access token if you need to authorize the API manually|N/A                |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the values inside the data stores 

   |JSON Path |Is Data Store Used?|Data Store Type|Data Store Variable Name|Expected Result|
   |----------|-------------------|---------------|------------------------|---------------|
   |$.length()|n                  |               |                        |1              |
   |$[0].id   |y                  |scenario       |expertDeckId2           |               |

* Given that a user needs to invoke "Delete Expert Deck by ID using Expert Deck Service"
* And the user set the request authentication configurations as follows 

   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |Yes                |
   |Do you need to retrieve the access token from the text file?      |Yes                |
   |Provide the access token if you need to authorize the API manually|N/A                |
* And the user set the path parameters using data stores as follows 

   |Path Name|Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value|
   |---------|-------------------|---------------|------------------------|----------|
   |skuUUID  |y                  |scenario       |expertDeckId2           |N/A       |
* When the user invokes the API
* Then the status code for the request is "204"

* Given that a user needs to invoke "Delete a Bundle"
* And the user set the request authentication configurations as follows 

   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |Yes                |
   |Do you need to retrieve the access token from the text file?      |Yes                |
   |Provide the access token if you need to authorize the API manually|N/A                |
* And the user set the path parameters using data stores as follows 

   |Path Name|Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value|
   |---------|-------------------|---------------|------------------------|----------|
   |bundleId |y                  |scenario       |bundleId                |N/A       |
* When the user invokes the API
* Then the status code for the request is "204"

## Load decks of a new bundle which has two expert decks and one is edited
* Create an expert bundle

* Given that a user needs to invoke "Edit An Expert Deck using Expert Deck Service"
* And the user set the request authentication configurations as follows 

   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |Yes                |
   |Do you need to retrieve the access token from the text file?      |Yes                |
   |Provide the access token if you need to authorize the API manually|N/A                |
* And the user set the path parameters using data stores as follows 

   |Path Name   |Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value|
   |------------|-------------------|---------------|------------------------|----------|
   |expertDeckId|y                  |scenario       |expertDeckId1           |N/A       |
* And the user set the request attributes as follows 

   |Attribute Value In JSON Template|Attribute Value To Be Set                    |
   |--------------------------------|---------------------------------------------|
   |#isArchived                     |false                                        |
   |#bookAuthorName                 |Osanda Deshan                                |
   |#bookTitle                      |API Deck3                                    |
   |#chapter                        |Ch. 02                                       |
   |#tags                           |API tag1                                     |
   |#time                           |08:00 AM                                     |
   |#chapter                        |Ch. 02                                       |
   |#subjectId                      |21312wrwe23423df                             |
   |#cardPreview                    |true                                         |
   |#categoryId                     |345345345345                                 |
   |#deckAuthorName                 |Osanda Nimalarathna                          |
   |#deckAuthorId                   |234325345345                                 |
   |#description                    |Deck has been created via an automated script|
   |#downloads                      |328                                          |
   |#examDate                       |2018-01-19T07:10:20.943Z                     |
   |#keywords                       |API                                          |
   |#noOfCards                      |12                                           |
   |#areNotificationsEnabled        |false                                        |
   |#notificationFrequency          |3 times a day                                |
   |#notificationTime               |09.30 AM                                     |
   |#parentDeckId                   |13123123dsfsd231                             |
   |#progress                       |45                                           |
   |#price                          |99                                           |
   |#purchasedDate                  |2018-01-19T07:10:20.943Z                     |
   |#sku                            |test.purchase1                               |
   |#starred                        |false                                        |
   |#status                         |In Progress                                  |
   |#tags1                          |API tag                                      |
   |#tempDeckId                     |3242dfs435fdgdfg34                           |
   |#thumbnailUrl                   |http://somehost/someimg.jpg                  |
   |#title                          |API Automation using MaxSoft ATA Framework   |
   |#userId                         |osan                                         |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following 

   |JSON Path|Expected Result                           |
   |---------|------------------------------------------|
   |$.title  |API Automation using MaxSoft ATA Framework|
   |$.userId |osan                                      |


* Given that a user needs to invoke "Load Decks of a Bundle"
* And the user set the path parameters using data stores as follows 

   |Path Name|Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value|
   |---------|-------------------|---------------|------------------------|----------|
   |bundleId |y                  |scenario       |bundleId                |          |
   |decks    |n                  |               |                        |decks     |
* And the user set the request authentication configurations as follows 

   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |Yes                |
   |Do you need to retrieve the access token from the text file?      |Yes                |
   |Provide the access token if you need to authorize the API manually|N/A                |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the values inside the data stores 

   |JSON Path  |Is Data Store Used?|Data Store Type|Data Store Variable Name|Expected Result                           |
   |-----------|-------------------|---------------|------------------------|------------------------------------------|
   |$.length() |n                  |               |                        |2                                         |
   |$[0].id    |y                  |scenario       |expertDeckId1           |                                          |
   |$[0].title |n                  |               |                        |API Automation using MaxSoft ATA Framework|
   |$[0].userId|n                  |               |                        |osan                                      |
   |$[1].id    |y                  |scenario       |expertDeckId2           |                                          |

* Given that a user needs to invoke "Delete Expert Deck by ID using Expert Deck Service"
* And the user set the request authentication configurations as follows 

   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |Yes                |
   |Do you need to retrieve the access token from the text file?      |Yes                |
   |Provide the access token if you need to authorize the API manually|N/A                |
* And the user set the path parameters using data stores as follows 

   |Path Name|Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value|
   |---------|-------------------|---------------|------------------------|----------|
   |skuUUID  |y                  |scenario       |expertDeckId1           |N/A       |
* When the user invokes the API
* Then the status code for the request is "204"

* Given that a user needs to invoke "Delete Expert Deck by ID using Expert Deck Service"
* And the user set the request authentication configurations as follows 

   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |Yes                |
   |Do you need to retrieve the access token from the text file?      |Yes                |
   |Provide the access token if you need to authorize the API manually|N/A                |
* And the user set the path parameters using data stores as follows 

   |Path Name|Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value|
   |---------|-------------------|---------------|------------------------|----------|
   |skuUUID  |y                  |scenario       |expertDeckId2           |N/A       |
* When the user invokes the API
* Then the status code for the request is "204"

* Given that a user needs to invoke "Delete a Bundle"
* And the user set the request authentication configurations as follows 

   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |Yes                |
   |Do you need to retrieve the access token from the text file?      |Yes                |
   |Provide the access token if you need to authorize the API manually|N/A                |
* And the user set the path parameters using data stores as follows 

   |Path Name|Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value|
   |---------|-------------------|---------------|------------------------|----------|
   |bundleId |y                  |scenario       |bundleId                |N/A       |
* When the user invokes the API
* Then the status code for the request is "204"
