Activity API in Aggregation Service Specification
=================================================
Date Created    : 01/18/2018
Version   		: 1.0.0
Owner      		: Osanda Deshan
Description  	: This specification covers recommendation scenarios from the aggregation service


tags: aggregation_service, activity


* Given that a user needs to invoke "Activity API in Aggregation Service"
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |



Sending a new activity information using valid payload
------------------------------------------------------
* And the user set the request attributes as follows
     |Attribute Value In JSON Template|Attribute Value To Be Set               |
     |--------------------------------|----------------------------------------|
     |#personId                       |personId7                               |
     |#deckId                         |deckId2                                 |
     |#isRefreshDeck                  |false                                   |
     |#activity1Id                    |activityId1                             |
     |#activity1CardId                |cardId1                                 |
     |#activity1CardType              |flashCard                               |
     |#activity1StartTime             |2017-10-31T12:15:00.000Z                |
     |#activity1EndTime               |2017-10-31T12:15:00.000Z                |
     |#activity1SessionId             |sessionId1                              |
     |#activity1EventType1            |FAVORITE                                |
     |#activity1EventTime1            |2017-10-31T12:15:00.000Z                |
     |#activity1EventType2            |ANSWERED                                |
     |#activity1EventTime2            |2017-10-31T12:15:00.000Z                |
     |#score                          |1                                       |
     |#activity2Id                    |activityId2                             |
     |#activity2CardId                |cardId2                                 |
     |#activity2CardType              |multipleChoice                          |
     |#activity2StartTime             |2017-10-31T12:15:00.000Z                |
     |#activity2EndTime               |2017-10-31T12:15:00.000Z                |
     |#activity2SessionId             |sessionId2                              |
     |#activity2EventType1            |SKIPPED                                 |
     |#activity2EventTime1            |2017-10-31T12:15:00.000Z                |
* When the user invokes the API
* Then the status code for the request is "201"
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                                         |Value                                   |
     |--------------------------------------------------|----------------------------------------|
     |$.mastery                                         |0.083333                                |
     |$.message                                         |Number of activities processed 2        |