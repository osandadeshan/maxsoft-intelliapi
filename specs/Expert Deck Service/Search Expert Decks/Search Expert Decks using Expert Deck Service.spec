Search Expert Decks using Expert Deck Service Specification
===========================================================
Date Created    : 02/01/18
Version   		: 1.0.0
Owner      		: Dilanka Dias
Description  	: This specification covers search expert decks scenarios from the expert deck service


tags: deck_management, search_expert_decks, positive



Create an expert deck
---------------------
* Given that a user needs to invoke "Create An Expert Deck using Expert Deck Service"
* And the user set the request authentication configurations as follows
      |Configuration                                                     |Configuration Value|
      |------------------------------------------------------------------|-------------------|
      |Is authentication required?                                       |Yes                |
      |Do you need to retrieve the access token from the text file?      |Yes                |
      |Provide the access token if you need to authorize the API manually|N/A                |
* And the user set the request attributes as follows
      |Attribute Value In JSON Template|Attribute Value To Be Set|
      |--------------------------------|-------------------------|
      |#isArchived                     |true                     |
      |#bookAuthorName                 |Dilanka                  |
      |#bookTitle                      |Networking               |
      |#chapter                        |1                        |
      |#tags                           |API tag1                 |
      |#time                           |08:00 AM                 |
      |#chapter                        |Ch. 02                   |
      |#subjectId                      |IT                       |
      |#cardPreview                    |true                     |
      |#categoryId                     |1                        |
      |#createdAt                      |2018-01-30T04:03:33.042Z |
      |#deckAuthorName                 |Dilanka                  |
      |#deckAuthorId                   |1                        |
      |#description                    |Computer networking      |
      |#downloads                      |0                        |
      |#time                           |12.00                    |
      |#id                             |1                        |
      |#keywords                       |Networking               |
      |#noOfCards                      |0                        |
      |#areNotificationsEnabled        |true                     |
      |#notificationFrequency          |1                        |
      |#notificationTime               |12.00                    |
      |#parentDeckId                   |Parent                   |
      |#progress                       |0                        |
      |#price                          |0                        |
      |#sku                            |0                        |
      |#starred                        |true                     |
      |#status                         |available                |
      |#tags                           |networking               |
      |#tempDeckId                     |1                        |
      |#thumbnailUrl                   |www.google.com           |
      |#title                          |Networking               |
      |#userId                         |1                        |
* When the user invokes the API
* Then the status code for the request is "201"
* And the JSON Path Assertions for the response should be equal to the following
      |JSON Path                           |Expected Result       |
      |------------------------------------|----------------------|
      |$.title                             |Networking            |
      |$.userId                            |1                     |
      |$.archived                          |true                  |
      |$.book.bookTitle                    |Networking            |
* And save the JSON Path values in the response inside the data stores
      |DataStore Type |Variable Name  |Value To Be Stored     |
      |---------------|---------------|-----------------------|
      |spec           |updatedAt      |$.epochTime.updatedAt  |



Search expert decks only using expert deckTitle
-----------------------------------------------
* Given that a user needs to invoke "Search Expert Decks using Expert Deck Service"
* And the user set the request authentication configurations as follows
    |Configuration                                                          |Configuration Value            |
    |-----------------------------------------------------------------------|-------------------------------|
    |Is authentication required?                                            |Yes                            |
    |Do you need to retrieve the access token from the text file?           |Yes                            |
    |Provide the access token if you need to authorize the API manually     |N/A                            |
* And the user set the query parameters as follows
    |Query Parameter |Query Value                                      |
    |----------------|-------------------------------------------------|
    |deckTitle       |Networking                                       |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                           |Value                                              |
     |------------------------------------|---------------------------------------------------|
     |$.[-1:].title                       |Networking                                         |
     |$.[-1:].deckAuthor                  |Dilanka                                            |
     |$.[-1:].description                 |Computer networking                                |
     |$.[-1:].status                      |available                                          |
     |$.[-1:].book.bookAuthor             |Dilanka                                            |
     |$.[-1].book.bookTitle               |Networking                                         |



Search expert decks only using expert bookAuthorName
----------------------------------------------------
* Given that a user needs to invoke "Search Expert Decks using Expert Deck Service"
* And the user set the request authentication configurations as follows
    |Configuration                                                          |Configuration Value            |
    |-----------------------------------------------------------------------|-------------------------------|
    |Is authentication required?                                            |Yes                            |
    |Do you need to retrieve the access token from the text file?           |Yes                            |
    |Provide the access token if you need to authorize the API manually     |N/A                            |
* And the user set the query parameters as follows
    |Query Parameter |Query Value                                      |
    |----------------|-------------------------------------------------|
    |bookAuthorName  |Dilanka                                          |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                           |Value                                              |
     |------------------------------------|---------------------------------------------------|
     |$.[-1:].book.bookAuthor             |Dilanka                                            |
     |$.[-1:].title                       |Networking                                         |
     |$.[-1:].deckAuthor                  |Dilanka                                            |
     |$.[-1:].description                 |Computer networking                                |
     |$.[-1:].status                      |available                                          |
     |$.[-1].book.bookTitle               |Networking                                         |



Search expert decks only using expert subjectName
-------------------------------------------------
* Given that a user needs to invoke "Search Expert Decks using Expert Deck Service"
* And the user set the request authentication configurations as follows
    |Configuration                                                          |Configuration Value            |
    |-----------------------------------------------------------------------|-------------------------------|
    |Is authentication required?                                            |Yes                            |
    |Do you need to retrieve the access token from the text file?           |Yes                            |
    |Provide the access token if you need to authorize the API manually     |N/A                            |
* And the user set the query parameters as follows
     |Query Parameter |Query Value                                      |
     |----------------|-------------------------------------------------|
     |subjectName     |IT                                               |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                           |Value                                              |
     |------------------------------------|---------------------------------------------------|
     |$.[-1:].book.bookAuthor             |Dilanka                                            |
     |$.[-1:].title                       |Networking                                         |
     |$.[-1:].description                 |Computer networking                                |
     |$.[-1:].status                      |available                                          |
     |$.[-1:].subjectId                   |IT                                                 |
     |$.[-1:].book.bookTitle              |Networking                                         |



Search expert decks only using updatedAfter
-------------------------------------------
* Given that a user needs to invoke "Search Expert Decks using Expert Deck Service"
* And the user set the request authentication configurations as follows
    |Configuration                                                          |Configuration Value            |
    |-----------------------------------------------------------------------|-------------------------------|
    |Is authentication required?                                            |Yes                            |
    |Do you need to retrieve the access token from the text file?           |Yes                            |
    |Provide the access token if you need to authorize the API manually     |N/A                            |
* And the user set the query parameters using data stores as follows
    |Query Name     |Is Data Store Used?|Data Store Type|Data Store Variable Name|Query Value|
    |---------------|-------------------|---------------|------------------------|-----------|
    |updatedAfter   |y                  |spec           |updatedAt               |N/A        |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the values inside the data stores
    |JSON Path                     |Is Data Store Used?|Data Store Type|Data Store Variable Name|Expected Value      |
    |------------------------------|-------------------|---------------|------------------------|--------------------|
    |$.[-1].epochTime.updatedAt    |y                  |spec           |updatedAt               |N/A                 |
    |$.[-1].book.bookAuthor        |n                  |               |                        |Dilanka             |
    |$.[-1].description            |n                  |               |                        |Computer networking |
    |$.[-1].title                  |n                  |               |                        |Networking          |
    |$.[-1].status                 |n                  |               |                        |available           |
    |$.[-1].subjectId              |n                  |               |                        |IT                  |
    |$.[-1].book.bookTitle         |n                  |               |                        |Networking          |



Search expert decks only using updatedAfter and deckTitle
---------------------------------------------------------
* Given that a user needs to invoke "Search Expert Decks using Expert Deck Service"
* And the user set the request authentication configurations as follows
    |Configuration                                                          |Configuration Value            |
    |-----------------------------------------------------------------------|-------------------------------|
    |Is authentication required?                                            |Yes                            |
    |Do you need to retrieve the access token from the text file?           |Yes                            |
    |Provide the access token if you need to authorize the API manually     |N/A                            |
* And the user set the query parameters using data stores as follows
    |Query Name     |Is Data Store Used?|Data Store Type|Data Store Variable Name|Query Value|
    |---------------|-------------------|---------------|------------------------|-----------|
    |updatedAfter   |y                  |spec           |updatedAt               |N/A        |
    |deckTitle      |n                  |               |                        |Networking |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the values inside the data stores
    |JSON Path                     |Is Data Store Used?|Data Store Type|Data Store Variable Name|Expected Value      |
    |------------------------------|-------------------|---------------|------------------------|--------------------|
    |$.[-1].epochTime.updatedAt    |y                  |spec           |updatedAt               |N/A                 |
    |$.[-1].book.bookAuthor        |n                  |               |                        |Dilanka             |
    |$.[-1].description            |n                  |               |                        |Computer networking |
    |$.[-1].title                  |n                  |               |                        |Networking          |
    |$.[-1].status                 |n                  |               |                        |available           |
    |$.[-1].subjectId              |n                  |               |                        |IT                  |
    |$.[-1].book.bookTitle         |n                  |               |                        |Networking          |



Search expert decks only using updatedAfter and bookAuthorName
--------------------------------------------------------------
* Given that a user needs to invoke "Search Expert Decks using Expert Deck Service"
* And the user set the request authentication configurations as follows
    |Configuration                                                          |Configuration Value            |
    |-----------------------------------------------------------------------|-------------------------------|
    |Is authentication required?                                            |Yes                            |
    |Do you need to retrieve the access token from the text file?           |Yes                            |
    |Provide the access token if you need to authorize the API manually     |N/A                            |
* And the user set the query parameters using data stores as follows
    |Query Name     |Is Data Store Used?|Data Store Type|Data Store Variable Name|Query Value|
    |---------------|-------------------|---------------|------------------------|-----------|
    |updatedAfter   |y                  |spec           |updatedAt               |N/A        |
    |bookAuthorName |n                  |               |                        |Dilanka    |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the values inside the data stores
    |JSON Path                     |Is Data Store Used?|Data Store Type|Data Store Variable Name|Expected Value      |
    |------------------------------|-------------------|---------------|------------------------|--------------------|
    |$.[-1].epochTime.updatedAt    |y                  |spec           |updatedAt               |N/A                 |
    |$.[-1].book.bookAuthor        |n                  |               |                        |Dilanka             |
    |$.[-1].description            |n                  |               |                        |Computer networking |
    |$.[-1].title                  |n                  |               |                        |Networking          |
    |$.[-1].status                 |n                  |               |                        |available           |
    |$.[-1].subjectId              |n                  |               |                        |IT                  |
    |$.[-1].book.bookTitle         |n                  |               |                        |Networking          |



Search expert decks only using updatedAfter and subjectName
-----------------------------------------------------------
* Given that a user needs to invoke "Search Expert Decks using Expert Deck Service"
* And the user set the request authentication configurations as follows
    |Configuration                                                          |Configuration Value            |
    |-----------------------------------------------------------------------|-------------------------------|
    |Is authentication required?                                            |Yes                            |
    |Do you need to retrieve the access token from the text file?           |Yes                            |
    |Provide the access token if you need to authorize the API manually     |N/A                            |
* And the user set the query parameters using data stores as follows
    |Query Name     |Is Data Store Used?|Data Store Type|Data Store Variable Name|Query Value|
    |---------------|-------------------|---------------|------------------------|-----------|
    |updatedAfter   |y                  |spec           |updatedAt               |N/A        |
    |subjectName    |n                  |               |                        |IT         |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the values inside the data stores
    |JSON Path                     |Is Data Store Used?|Data Store Type|Data Store Variable Name|Expected Value      |
    |------------------------------|-------------------|---------------|------------------------|--------------------|
    |$.[-1].epochTime.updatedAt    |y                  |spec           |updatedAt               |N/A                 |
    |$.[-1].book.bookAuthor        |n                  |               |                        |Dilanka             |
    |$.[-1].description            |n                  |               |                        |Computer networking |
    |$.[-1].title                  |n                  |               |                        |Networking          |
    |$.[-1].status                 |n                  |               |                        |available           |
    |$.[-1].subjectId              |n                  |               |                        |IT                  |
    |$.[-1].book.bookTitle         |n                  |               |                        |Networking          |



Search expert decks only using expert deckTitle and bookAuthorName
------------------------------------------------------------------
* Given that a user needs to invoke "Search Expert Decks using Expert Deck Service"
* And the user set the request authentication configurations as follows
    |Configuration                                                          |Configuration Value            |
    |-----------------------------------------------------------------------|-------------------------------|
    |Is authentication required?                                            |Yes                            |
    |Do you need to retrieve the access token from the text file?           |Yes                            |
    |Provide the access token if you need to authorize the API manually     |N/A                            |
* And the user set the query parameters as follows
     |Query Parameter |Query Value                                      |
     |----------------|-------------------------------------------------|
     |deckTitle       |Networking                                       |
     |bookAuthorName  |Dilanka                                          |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                           |Value                                              |
     |------------------------------------|---------------------------------------------------|
     |$.[-1:].title                       |Networking                                         |
     |$.[-1:].deckAuthor                  |Dilanka                                            |
     |$.[-1:].description                 |Computer networking                                |
     |$.[-1:].status                      |available                                          |
     |$.[-1:].book.bookAuthor             |Dilanka                                            |
     |$.[-1].book.bookTitle               |Networking                                         |



Search expert decks only using subjectName and bookAuthorName
-------------------------------------------------------------
* Given that a user needs to invoke "Search Expert Decks using Expert Deck Service"
* And the user set the request authentication configurations as follows
    |Configuration                                                          |Configuration Value            |
    |-----------------------------------------------------------------------|-------------------------------|
    |Is authentication required?                                            |Yes                            |
    |Do you need to retrieve the access token from the text file?           |Yes                            |
    |Provide the access token if you need to authorize the API manually     |N/A                            |
* And the user set the query parameters as follows
     |Query Parameter |Query Value                                      |
     |----------------|-------------------------------------------------|
     |bookAuthorName  |Dilanka                                          |
     |subjectName     |IT                                               |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                           |Value                                              |
     |------------------------------------|---------------------------------------------------|
     |$.[-1:].title                       |Networking                                         |
     |$.[-1:].deckAuthor                  |Dilanka                                            |
     |$.[-1:].description                 |Computer networking                                |
     |$.[-1:].status                      |available                                          |
     |$.[-1:].book.bookAuthor             |Dilanka                                            |
     |$.[-1:].subjectId                   |IT                                                 |
     |$.[-1].book.bookTitle               |Networking                                         |



Search expert decks only using expert subjectName and deckTitle
---------------------------------------------------------------
* Given that a user needs to invoke "Search Expert Decks using Expert Deck Service"
* And the user set the request authentication configurations as follows
    |Configuration                                                          |Configuration Value            |
    |-----------------------------------------------------------------------|-------------------------------|
    |Is authentication required?                                            |Yes                            |
    |Do you need to retrieve the access token from the text file?           |Yes                            |
    |Provide the access token if you need to authorize the API manually     |N/A                            |
* And the user set the query parameters as follows
     |Query Parameter |Query Value                                      |
     |----------------|-------------------------------------------------|
     |deckTitle       |Networking                                       |
     |subjectName     |IT                                               |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                           |Value                                              |
     |------------------------------------|---------------------------------------------------|
     |$.[-1:].title                       |Networking                                         |
     |$.[-1:].deckAuthor                  |Dilanka                                            |
     |$.[-1:].description                 |Computer networking                                |
     |$.[-1:].status                      |available                                          |
     |$.[-1:].book.bookAuthor             |Dilanka                                            |
     |$.[-1:].subjectId                   |IT                                                 |
     |$.[-1].book.bookTitle               |Networking                                         |



Search expert decks only using subjectName, deckTitle and bookAuthorName
------------------------------------------------------------------------
* Given that a user needs to invoke "Search Expert Decks using Expert Deck Service"
* And the user set the request authentication configurations as follows
    |Configuration                                                          |Configuration Value            |
    |-----------------------------------------------------------------------|-------------------------------|
    |Is authentication required?                                            |Yes                            |
    |Do you need to retrieve the access token from the text file?           |Yes                            |
    |Provide the access token if you need to authorize the API manually     |N/A                            |
* And the user set the query parameters as follows
     |Query Parameter |Query Value                                      |
     |----------------|-------------------------------------------------|
     |deckTitle       |Networking                                       |
     |subjectName     |IT                                               |
     |bookAuthorName  |Dilanka                                          |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                           |Value                                              |
     |------------------------------------|---------------------------------------------------|
     |$.[-1:].title                       |Networking                                         |
     |$.[-1:].deckAuthor                  |Dilanka                                            |
     |$.[-1:].description                 |Computer networking                                |
     |$.[-1:].status                      |available                                          |
     |$.[-1:].book.bookAuthor             |Dilanka                                            |
     |$.[-1:].subjectId                   |IT                                                 |
     |$.[-1].book.bookTitle               |Networking                                         |



Search expert decks using all search criterias of updatedAfter, deckTitle, bookAuthorName and subjectName
---------------------------------------------------------------------------------------------------------
* Given that a user needs to invoke "Search Expert Decks using Expert Deck Service"
* And the user set the request authentication configurations as follows
    |Configuration                                                          |Configuration Value            |
    |-----------------------------------------------------------------------|-------------------------------|
    |Is authentication required?                                            |Yes                            |
    |Do you need to retrieve the access token from the text file?           |Yes                            |
    |Provide the access token if you need to authorize the API manually     |N/A                            |
* And the user set the query parameters using data stores as follows
    |Query Name     |Is Data Store Used?|Data Store Type|Data Store Variable Name|Query Value|
    |---------------|-------------------|---------------|------------------------|-----------|
    |updatedAfter   |y                  |spec           |updatedAt               |N/A        |
    |bookAuthorName |n                  |               |                        |Dilanka    |
    |deckTitle      |n                  |               |                        |Networking |
    |subjectName    |n                  |               |                        |IT         |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the values inside the data stores
    |JSON Path                     |Is Data Store Used?|Data Store Type|Data Store Variable Name|Expected Value      |
    |------------------------------|-------------------|---------------|------------------------|--------------------|
    |$.[-1].epochTime.updatedAt    |y                  |spec           |updatedAt               |N/A                 |
    |$.[-1].book.bookAuthor        |n                  |               |                        |Dilanka             |
    |$.[-1].description            |n                  |               |                        |Computer networking |
    |$.[-1].title                  |n                  |               |                        |Networking          |
    |$.[-1].status                 |n                  |               |                        |available           |
    |$.[-1].subjectId              |n                  |               |                        |IT                  |
    |$.[-1].book.bookTitle         |n                  |               |                        |Networking          |



Search expert decks only using empty bookAuthorName
---------------------------------------------------
* Given that a user needs to invoke "Create An Expert Deck using Expert Deck Service"
* And the user set the request authentication configurations as follows
      |Configuration                                                     |Configuration Value|
      |------------------------------------------------------------------|-------------------|
      |Is authentication required?                                       |Yes                |
      |Do you need to retrieve the access token from the text file?      |Yes                |
      |Provide the access token if you need to authorize the API manually|N/A                |
* And the user set the request attributes as follows
      |Attribute Value In JSON Template|Attribute Value To Be Set|
      |--------------------------------|-------------------------|
      |#isArchived                     |true                     |
      |#bookAuthorName                 |                         |
      |#bookTitle                      |Networking               |
      |#chapter                        |1                        |
      |#tags                           |API tag1                 |
      |#time                           |08:00 AM                 |
      |#subjectId                      |IT                       |
      |#cardPreview                    |true                     |
      |#categoryId                     |1                        |
      |#createdAt                      |2018-01-30T04:03:33.042Z |
      |#deckAuthor                     |Dilanka                  |
      |#deckAuthorId                   |1                        |
      |#description                    |Computer networking      |
      |#downloads                      |0                        |
      |#time                           |12.00                    |
      |#id                             |1                        |
      |#keywords                       |Networking               |
      |#noOfCards                      |0                        |
      |#areNotificationsEnabled        |true                     |
      |#notificationFrequency          |1                        |
      |#notificationTime               |12.00                    |
      |#parentDeckId                   |Parent                   |
      |#progress                       |0                        |
      |#price                          |0                        |
      |#sku                            |0                        |
      |#starred                        |true                     |
      |#status                         |available                |
      |#tags                           |networking               |
      |#tempDeckId                     |1                        |
      |#thumbnailUrl                   |www.google.com           |
      |#title                          |Networking               |
      |#userId                         |1                        |
* When the user invokes the API
* Then the status code for the request is "201"
* And the JSON Path Assertions for the response should be equal to the following
      |JSON Path                           |Expected Result       |
      |------------------------------------|----------------------|
      |$.title                             |Networking            |
      |$.userId                            |1                     |
      |$.archived                          |true                  |
      |$.book.bookTitle                    |Networking            |

* Given that a user needs to invoke "Search Expert Decks using Expert Deck Service"
* And the user set the request authentication configurations as follows
    |Configuration                                                          |Configuration Value            |
    |-----------------------------------------------------------------------|-------------------------------|
    |Is authentication required?                                            |Yes                            |
    |Do you need to retrieve the access token from the text file?           |Yes                            |
    |Provide the access token if you need to authorize the API manually     |N/A                            |
* And the user set the query parameters as follows
     |Query Parameter |Query Value                                      |
     |----------------|-------------------------------------------------|
     |bookAuthorName  |                                                 |
     |bookTitle       |Networking                                       |
     |deckTitle       |Networking                                       |
     |subjectName     |IT                                               |
     |updatedAfter    |1517904261                                       |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                           |Value                                              |
     |------------------------------------|---------------------------------------------------|
     |$.[-1:].title                       |Networking                                         |
     |$.[-1:].description                 |Computer networking                                |
     |$.[-1:].status                      |available                                          |
     |$.[-1:].subjectId                   |IT                                                 |
     |$.[-1:].book.bookTitle              |Networking                                         |



Search expert decks only using empty updatedAfter
-------------------------------------------------
* Given that a user needs to invoke "Search Expert Decks using Expert Deck Service"
* And the user set the request authentication configurations as follows
    |Configuration                                                          |Configuration Value            |
    |-----------------------------------------------------------------------|-------------------------------|
    |Is authentication required?                                            |Yes                            |
    |Do you need to retrieve the access token from the text file?           |Yes                            |
    |Provide the access token if you need to authorize the API manually     |N/A                            |
* And the user set the query parameters as follows
     |Query Parameter |Query Value                                      |
     |----------------|-------------------------------------------------|
     |bookAuthorName  |Dilanka                                          |
     |bookTitle       |Networking                                       |
     |deckTitle       |Networking                                       |
     |subjectName     |IT                                               |
     |updatedAfter    |                                                 |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                           |Value                                              |
     |------------------------------------|---------------------------------------------------|
     |$.[-1:].book.bookAuthor             |Dilanka                                            |
     |$.[-1:].title                       |Networking                                         |
     |$.[-1:].description                 |Computer networking                                |
     |$.[-1:].status                      |available                                          |
     |$.[-1:].subjectId                   |IT                                                 |
     |$.[-1:].book.bookTitle              |Networking                                         |
//   |$.[-1].epochTime.updatedAt          |                                                   |



Search expert decks only using empty subjectName
------------------------------------------------
* Given that a user needs to invoke "Create An Expert Deck using Expert Deck Service"
* And the user set the request authentication configurations as follows
      |Configuration                                                     |Configuration Value|
      |------------------------------------------------------------------|-------------------|
      |Is authentication required?                                       |Yes                |
      |Do you need to retrieve the access token from the text file?      |Yes                |
      |Provide the access token if you need to authorize the API manually|N/A                |
* And the user set the request attributes as follows
      |Attribute Value In JSON Template|Attribute Value To Be Set|
      |--------------------------------|-------------------------|
      |#isArchived                     |true                     |
      |#bookAuthorName                 |Dilanka                  |
      |#bookTitle                      |Networking               |
      |#chapter                        |1                        |
      |#tags                           |API tag1                 |
      |#time                           |08:00 AM                 |
      |#cardPreview                    |true                     |
      |#categoryId                     |1                        |
      |#createdAt                      |2018-01-30T04:03:33.042Z |
      |#deckAuthor                     |Dilanka                  |
      |#deckAuthorId                   |1                        |
      |#description                    |Computer networking      |
      |#downloads                      |0                        |
      |#time                           |12.00                    |
      |#id                             |1                        |
      |#keywords                       |Networking               |
      |#noOfCards                      |0                        |
      |#areNotificationsEnabled        |true                     |
      |#notificationFrequency          |1                        |
      |#notificationTime               |12.00                    |
      |#parentDeckId                   |Parent                   |
      |#progress                       |0                        |
      |#price                          |0                        |
      |#sku                            |0                        |
      |#starred                        |true                     |
      |#status                         |available                |
      |#subjectId                      |                         |
      |#tags                           |networking               |
      |#tempDeckId                     |1                        |
      |#thumbnailUrl                   |www.google.com           |
      |#title                          |Networking               |
      |#userId                         |1                        |
* When the user invokes the API
* Then the status code for the request is "201"
* And the JSON Path Assertions for the response should be equal to the following
      |JSON Path                           |Expected Result       |
      |------------------------------------|----------------------|
      |$.title                             |Networking            |
      |$.userId                            |1                     |
      |$.archived                          |true                  |
      |$.book.bookTitle                    |Networking            |
      |$.subjectId                         |                      |

* Given that a user needs to invoke "Search Expert Decks using Expert Deck Service"
* And the user set the request authentication configurations as follows
    |Configuration                                                          |Configuration Value            |
    |-----------------------------------------------------------------------|-------------------------------|
    |Is authentication required?                                            |Yes                            |
    |Do you need to retrieve the access token from the text file?           |Yes                            |
    |Provide the access token if you need to authorize the API manually     |N/A                            |
* And the user set the query parameters as follows
     |Query Parameter |Query Value                                      |
     |----------------|-------------------------------------------------|
     |bookAuthorName  |Dilanka                                          |
     |bookTitle       |Networking                                       |
     |deckTitle       |Networking                                       |
     |updatedAfter    |1517904261                                       |
     |subjectName     |                                                 |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                           |Value                                              |
     |------------------------------------|---------------------------------------------------|
     |$.[-1:].book.bookTitle              |Networking                                         |
     |$.[-1:].title                       |Networking                                         |
     |$.[-1:].book.bookAuthor             |Dilanka                                            |



Search expert decks only using invalid deckTitle
------------------------------------------------
* Given that a user needs to invoke "Search Expert Decks using Expert Deck Service"
* And the user set the request authentication configurations as follows
    |Configuration                                                          |Configuration Value            |
    |-----------------------------------------------------------------------|-------------------------------|
    |Is authentication required?                                            |Yes                            |
    |Do you need to retrieve the access token from the text file?           |Yes                            |
    |Provide the access token if you need to authorize the API manually     |N/A                            |
* And the user set the query parameters as follows
     |Query Parameter |Query Value                                      |
     |----------------|-------------------------------------------------|
     |deckTitle       |Invalid deck                                     |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                           |Value                                              |
     |------------------------------------|---------------------------------------------------|
     |$                                   |[]                                                 |
