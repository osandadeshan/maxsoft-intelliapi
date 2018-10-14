# Get the default 9 decks using Aggregation Service Specification
Date Created    : 4/11/2018
Version   		: 1.0.0
Owner      		: Kinkini Gamage
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.


* Given that a user needs to invoke "Get the default 9 decks using Aggregation Service"
* And the user set the request authentication configurations as follows 

   |Configuration                                                     |Configuration Value|
   |------------------------------------------------------------------|-------------------|
   |Is authentication required?                                       |Yes                |
   |Do you need to retrieve the access token from the text file?      |Yes                |
   |Provide the access token if you need to authorize the API manually|N/A                |



## Get onboarding 9 decks
* And the user set the path parameters as follows 

   |Path Parameter|Path Value|
   |--------------|----------|
   |userId        |api_user21|
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following 

   |JSON Path |Value|
   |----------|-----|
   |$.length()|9    |



## Verify that the notifications are disable for onboarding decks
* Get the default 9 decks
* And the JSON Path Assertions for the response should be equal to the following 

   |JSON Path                                        |Expected Result|
   |-------------------------------------------------|---------------|
   |$[0].notificationSettings.areNotificationsEnabled|false          |
   |$[1].notificationSettings.areNotificationsEnabled|false          |
   |$[2].notificationSettings.areNotificationsEnabled|false          |
   |$[3].notificationSettings.areNotificationsEnabled|false          |
   |$[4].notificationSettings.areNotificationsEnabled|false          |
   |$[5].notificationSettings.areNotificationsEnabled|false          |
   |$[6].notificationSettings.areNotificationsEnabled|false          |
   |$[7].notificationSettings.areNotificationsEnabled|false          |
   |$[8].notificationSettings.areNotificationsEnabled|false          |


