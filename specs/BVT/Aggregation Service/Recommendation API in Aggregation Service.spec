Recommendation API in Aggregation Service Specification
=======================================================
Date Created    : 01/17/2018
Version   		: 1.0.0
Owner      		: Osanda Deshan
Description  	: This specification covers recommendation scenarios from the aggregation service


tags: aggregation_service, recommendation


* Given that a user needs to invoke "Recommendation API in Aggregation Service"
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |



Recommendation for the next cards using valid personId and valid deckId
-----------------------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set               |
     |--------------------------------|----------------------------------------|
     |#personId                       |personId1                               |
     |#deckId                         |deckId3                                 |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                         |Value                                   |
     |--------------------------------------------------|----------------------------------------|
     |$.person                                          |personId3                               |
     |$.deck                                            |deckId4                                 |
     |$.session.cards[0]                                |cardId4                                 |
     |$.session.cards[1]                                |cardId3                                 |
     |$.session.cards[2]                                |cardId2                                 |
     |$.session.cards[3]                                |cardId1                                 |
     |$.session.sessionSize                             |20                                      |
     |$.groups[0].groupId                               |0                                       |
     |$.groups[0].groupType                             |UNPLAYED                                |
     |$.groups[1].groupId                               |1                                       |
     |$.groups[1].groupType                             |INPLAY                                  |
     |$.groups[1].minPercent                            |0.0                                     |
     |$.groups[1].maxPercent                            |0.33333                                 |
     |$.groups[2].groupId                               |2                                       |
     |$.groups[2].groupType                             |INPLAY                                  |
     |$.groups[2].minPercent                            |0.33333                                 |
     |$.groups[2].maxPercent                            |0.46941                                 |
     |$.groups[3].groupId                               |3                                       |
     |$.groups[3].groupType                             |INPLAY                                  |
     |$.groups[3].minPercent                            |0.46941                                 |
     |$.groups[3].maxPercent                            |0.51941                                 |
     |$.groups[4].groupId                               |4                                       |
     |$.groups[4].groupType                             |MASTERED                                |
     |$.cards[0].cardId                                 |cardId1                                 |
     |$.cards[0].cardType                               |cardType1                               |
     |$.cards[0].group                                  |0                                       |
     |$.cards[0].cardTypes[0]                           |cardType1                               |
     |$.cards[0].cardTypes[1]                           |cardType2                               |
     |$.cards[0].cardTypes[2]                           |cardType3                               |
     |$.cards[1].cardId                                 |cardId2                                 |
     |$.cards[1].cardType                               |cardType1                               |
     |$.cards[1].group                                  |0                                       |
     |$.cards[1].cardTypes[0]                           |cardType1                               |
     |$.cards[1].cardTypes[1]                           |cardType2                               |
     |$.cards[1].cardTypes[2]                           |cardType3                               |
     |$.cards[2].cardId                                 |cardId3                                 |
     |$.cards[2].cardType                               |cardType1                               |
     |$.cards[2].group                                  |0                                       |
     |$.cards[2].cardTypes[0]                           |cardType1                               |
     |$.cards[2].cardTypes[1]                           |cardType2                               |
     |$.cards[2].cardTypes[2]                           |cardType3                               |
     |$.cards[3].cardId                                 |cardId4                                 |
     |$.cards[3].cardType                               |cardType1                               |
     |$.cards[3].group                                  |0                                       |
     |$.cards[3].cardTypes[0]                           |cardType1                               |
     |$.cards[3].cardTypes[1]                           |cardType2                               |
     |$.cards[3].cardTypes[2]                           |cardType3                               |



Recommendation for the next cards using invalid personId and valid deckId
-------------------------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set               |
     |--------------------------------|----------------------------------------|
     |#personId                       |person                                  |
     |#deckId                         |deckId2                                 |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                         |Value                                   |
     |--------------------------------------------------|----------------------------------------|
     |$.person                                          |person                                  |
     |$.deck                                            |deckId2                                 |
     |$.session.cards[0]                                |cardId4                                 |
     |$.session.cards[1]                                |cardId3                                 |
     |$.session.cards[2]                                |cardId2                                 |
     |$.session.cards[3]                                |cardId1                                 |
     |$.session.sessionSize                             |20                                      |
     |$.groups[0].groupId                               |0                                       |
     |$.groups[0].groupType                             |UNPLAYED                                |
     |$.groups[1].groupId                               |1                                       |
     |$.groups[1].groupType                             |INPLAY                                  |
     |$.groups[1].minPercent                            |0.0                                     |
     |$.groups[1].maxPercent                            |0.33333                                 |
     |$.groups[2].groupId                               |2                                       |
     |$.groups[2].groupType                             |INPLAY                                  |
     |$.groups[2].minPercent                            |0.33333                                 |
     |$.groups[2].maxPercent                            |0.46941                                 |
     |$.groups[3].groupId                               |3                                       |
     |$.groups[3].groupType                             |INPLAY                                  |
     |$.groups[3].minPercent                            |0.46941                                 |
     |$.groups[3].maxPercent                            |0.51941                                 |
     |$.groups[4].groupId                               |4                                       |
     |$.groups[4].groupType                             |MASTERED                                |



Recommendation for the next cards using empty personId and valid deckId
-----------------------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set               |
     |--------------------------------|----------------------------------------|
     |#personId                       |                                        |
     |#deckId                         |deckId2                                 |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                         |Value                                                          |
     |--------------------------------------------------|---------------------------------------------------------------|
     |$.status                                          |400                                                            |
     |$.error                                           |Bad Request                                                    |
     |$.exception                                       |org.springframework.web.bind.MethodArgumentNotValidException   |



Recommendation for the next cards using null personId and valid deckId
----------------------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set               |
     |--------------------------------|----------------------------------------|
     |#personId                       |"null"                                  |
     |#deckId                         |deckId2                                 |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                         |Value                                                          |
     |--------------------------------------------------|---------------------------------------------------------------|
     |$.status                                          |400                                                            |
     |$.error                                           |Bad Request                                                    |
     |$.exception                                       |org.springframework.web.bind.MethodArgumentNotValidException   |



Recommendation for the next cards using valid personId and invalid deckId
-------------------------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set               |
     |--------------------------------|----------------------------------------|
     |#personId                       |personId1                               |
     |#deckId                         |deckId999                               |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                         |Value                                                          |
     |--------------------------------------------------|---------------------------------------------------------------|
     |$.status                                          |400                                                            |
     |$.error                                           |Bad Request                                                    |
     |$.exception                                       |com.pearson.question.aggregator.exceptions.BaseException       |



Recommendation for the next cards using valid personId and non-existing deckId
------------------------------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set               |
     |--------------------------------|----------------------------------------|
     |#personId                       |personId3                               |
     |#deckId                         |deckId4                                 |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                         |Value                                                          |
     |--------------------------------------------------|---------------------------------------------------------------|
     |$.status                                          |400                                                            |
     |$.error                                           |Bad Request                                                    |
     |$.exception                                       |com.pearson.question.aggregator.exceptions.BaseException       |



Recommendation for the next cards using valid personId and empty deckId
-----------------------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set               |
     |--------------------------------|----------------------------------------|
     |#personId                       |personId1                               |
     |#deckId                         |                                        |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                         |Value                                                          |
     |--------------------------------------------------|---------------------------------------------------------------|
     |$.status                                          |400                                                            |
     |$.error                                           |Bad Request                                                    |
     |$.exception                                       |org.springframework.web.bind.MethodArgumentNotValidException   |



Recommendation for the next cards using valid personId and null deckId
----------------------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set               |
     |--------------------------------|----------------------------------------|
     |#personId                       |personId1                               |
     |#deckId                         |"null"                                  |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                         |Value                                                          |
     |--------------------------------------------------|---------------------------------------------------------------|
     |$.status                                          |400                                                            |
     |$.error                                           |Bad Request                                                    |
     |$.exception                                       |org.springframework.web.bind.MethodArgumentNotValidException   |



Recommendation for the next cards only using valid personId
-----------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set               |
     |--------------------------------|----------------------------------------|
     |#personId                       |personId1                               |
     |,                               |                                        |
     |"deck": "#deckId"               |                                        |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                         |Value                                                          |
     |--------------------------------------------------|---------------------------------------------------------------|
     |$.status                                          |400                                                            |
     |$.error                                           |Bad Request                                                    |
     |$.exception                                       |org.springframework.web.bind.MethodArgumentNotValidException   |



Recommendation for the next cards only using valid deckId
---------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set               |
     |--------------------------------|----------------------------------------|
     |"person": "#personId",          |                                        |
     |#deckId                         |deckId2                                 |
* When the user invokes the API
* Then the status code for the request is "400"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                         |Value                                                          |
     |--------------------------------------------------|---------------------------------------------------------------|
     |$.status                                          |400                                                            |
     |$.error                                           |Bad Request                                                    |
     |$.exception                                       |org.springframework.web.bind.MethodArgumentNotValidException   |