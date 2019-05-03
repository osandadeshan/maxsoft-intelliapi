# Headers Specification

<pre>
Project Name    : MaxSoft-IntelliAPI
Developer       : Osanda Deshan
Version         : 1.0.0
Date            : 28/04/2019
Time            : 20:09
Description     : This is an executable specification file
</pre>



## Get all decks of a user with auth header

* Given that a user needs to invoke "Get All Decks Of User"
* And the user saves test data inside excel file into data stores 

   |DataStore Type|Variable Name     |Excel Sheet Name|Key Name       |
   |--------------|------------------|----------------|---------------|
   |Scenario      |varUserId         |Deck_Test_Data  |userId         |
   |Scenario      |varSampleDeckTitle|Deck_Test_Data  |sampleDeckTitle|
* And the user set the path parameters using data stores as follows 

   |Path Name|Is Data Store Used?|Data Store Type|Data Store Variable Name|Path Value|
   |---------|-------------------|---------------|------------------------|----------|
   |userId   |yes                |Scenario       |varUserId               |          |
* And the user set the request headers as follows 

   |Header Name    |Header Value                                        |
   |---------------|----------------------------------------------------|
   |x-Authorization|<file:/resources/text_files/response_data/token.txt>|
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the values inside the data stores 

   |JSON Path    |Is Data Store Used?|Data Store Type|Data Store Variable Name|Expected Value|
   |-------------|-------------------|---------------|------------------------|--------------|
   |$[0].title   |yes                |Scenario       |varSampleDeckTitle      |              |
   |$[0].userId  |yes                |Scenario       |varUserId               |              |
   |$[0].archived|no                 |               |                        |false         |
