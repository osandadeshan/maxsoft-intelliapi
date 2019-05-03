# CRUD In One Scenario Specification

<pre>
Project Name    : MaxSoft-IntelliAPI
Developer       : Osanda Deshan
Version         : 1.0.0
Date            : 28/04/2019
Time            : 20:09
Description     : This is an executable specification file
</pre>



## CRUD operation for a deck

* Create a deck
* And save the JSON Path values in the response inside the data stores 

   |DataStore Type|Variable Name|Value To Be Stored|
   |--------------|-------------|------------------|
   |Scenario      |varDeckId    |$.id              |

* Given that a user needs to invoke "Edit Deck"
* And the user saves test data inside excel file into data stores 

   |DataStore Type|Variable Name     |Excel Sheet Name|Key Name       |
   |--------------|------------------|----------------|---------------|
   |Scenario      |varUserId         |Deck_Test_Data  |userId         |
   |Scenario      |varEditedDeckTitle|Deck_Test_Data  |editedDeckTitle|
* And the user set the path parameters using data stores as follows 

   |Path Name|Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value|
   |---------|-------------------|---------------|------------------------|----------|
   |deckId   |yes                |Scenario       |varDeckId               |          |
* And the user set the request attributes using data stores as follows 

   |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name|Attibute Value To Be Set|
   |--------------------------------|-------------------|---------------|------------------------|------------------------|
   |#deckTitle                      |yes                |Scenario       |varEditedDeckTitle      |                        |
   |#userId                         |yes                |Scenario       |varUserId               |                        |
* And the user set the request authentication configurations as follows 

   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |Yes                |
   |Do you need to retrieve the access token from the text file?      |Yes                |
   |Provide the access token if you need to authorize the API manually|N/A                |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the values inside the data stores 

   |JSON Path|Is Data Store Used?|Data Store Type|Data Store Variable Name|Expected Value|
   |---------|-------------------|---------------|------------------------|--------------|
   |$.title  |yes                |Scenario       |varEditedDeckTitle      |              |
   |$.userId |yes                |Scenario       |varUserId               |              |

* Given that a user needs to invoke "Get Deck"
* And the user set the path parameters using data stores as follows 

   |Path Name|Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value|
   |---------|-------------------|---------------|------------------------|----------|
   |deckId   |yes                |Scenario       |varDeckId               |          |
* And the user set the request authentication configurations as follows 

   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |Yes                |
   |Do you need to retrieve the access token from the text file?      |Yes                |
   |Provide the access token if you need to authorize the API manually|N/A                |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the values inside the data stores 

   |JSON Path|Is Data Store Used?|Data Store Type|Data Store Variable Name|Expected Value|
   |---------|-------------------|---------------|------------------------|--------------|
   |$.title  |yes                |Scenario       |varEditedDeckTitle      |              |
   |$.userId |yes                |Scenario       |varUserId               |              |

* Delete deck by deckId saved in "Scenario" type data store named "varDeckId"

