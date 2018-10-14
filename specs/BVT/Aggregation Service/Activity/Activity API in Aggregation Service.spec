# Activity API in Aggregation Service Specification
Date Created    : 01/18/2018
Version   		: 1.0.0
Owner      		: Osanda Deshan
Description  	: This specification covers recommendation scenarios from the aggregation service


tags: aggregation_service, activity, ci_ready, bvt, regression



## Sending a new activity information using valid payload
* Create a my deck with all types of 9 questions
* Given that a user needs to invoke "Activity API in Aggregation Service"
* And the user set the request authentication configurations as follows 

   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |Yes                |
   |Do you need to retrieve the access token from the text file?      |Yes                |
   |Provide the access token if you need to authorize the API manually|N/A                |
* And the user set the request attributes using data stores as follows 

   |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name|Attribute Value To Be Set           |
   |--------------------------------|-------------------|---------------|------------------------|------------------------------------|
   |#personId                       |n                  |               |                        |ffffffff59db8f51e4b0c1f4de01b2e2    |
   |#deckId                         |y                  |spec           |myDeckIdWith9Questions  |deckId2                             |
   |#isRefreshDeck                  |n                  |               |                        |true                                |
   |#activity1Id                    |n                  |               |                        |4868b82a-24a1-4e03-b45a-c11e616ad28c|
   |#activity1CardId                |y                  |scenario       |cardId2                 |                                    |
   |#activity1CardType              |n                  |               |                        |Manual                              |
   |#activity1StartTime             |n                  |               |                        |2017-10-31T12:15:00.000Z            |
   |#activity1EndTime               |n                  |               |                        |2017-10-31T12:15:00.000Z            |
   |#activity1SessionId             |n                  |               |                        |4868b82a-24a1-4e03-b45a-c11e616ad28c|
   |#activity1EventType1            |n                  |               |                        |FAVORITE                            |
   |#activity1EventTime1            |n                  |               |                        |2017-10-31T12:15:00.000Z            |
   |#activity1EventType2            |n                  |               |                        |ANSWERED                            |
   |#activity1EventTime2            |n                  |               |                        |2017-10-31T12:15:00.000Z            |
   |#score                          |n                  |               |                        |1                                   |
   |#activity2Id                    |n                  |               |                        |4868b82a-24a1-4e03-b45a-c11e616ad28c|
   |#activity2CardId                |y                  |scenario       |cardId8                 |                                    |
   |#activity2CardType              |n                  |               |                        |multipleChoice                      |
   |#activity2StartTime             |n                  |               |                        |2017-10-31T12:15:00.000Z            |
   |#activity2EndTime               |n                  |               |                        |2017-10-31T12:15:00.000Z            |
   |#activity2SessionId             |n                  |               |                        |4868b82a-24a1-4e03-b45a-c11e616ad28c|
   |#activity2EventType1            |n                  |               |                        |SKIPPED                             |
   |#activity2EventTime1            |n                  |               |                        |2017-10-31T12:15:00.000Z            |
* When the user invokes the API
* Then the status code for the request is "201"
* And the JSON Path Assertions for the response should be equal to the following 

   |JSON Path|Value                           |
   |---------|--------------------------------|
   |$.mastery|0.037037                        |
   |$.message|Number of activities processed 2|
