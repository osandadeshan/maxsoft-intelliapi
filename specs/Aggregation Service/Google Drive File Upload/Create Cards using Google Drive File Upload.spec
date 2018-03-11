Create Cards using Google Drive File Upload Specification
=========================================================
Date Created    : 02/26/2018
Version   		: 1.0.0
Owner      		: Osanda Deshan
Description  	: This specification covers google drive file upload scenarios from the aggregation service


tags: aggregation_service, google_drive_file_upload


table: /resources/data_driven_test_csv/google_drive_file_upload/google_drive_file_upload.csv



* Create a deck using aggregation service
* And save the JSON Path values in the response inside the data stores
    |DataStore Type |Variable Name        |Value To Be Stored     |
    |---------------|---------------------|-----------------------|
    |scenario       |deckId               |$.id                   |
* Given that a user needs to invoke <api>
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |



Creating questions using google drive file upload feature
---------------------------------------------------------
* And the user set the request attributes using data stores as follows
     |Attribute Value In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name|Attribute Value To Be Set                                |
     |--------------------------------|-------------------|---------------|------------------------|---------------------------------------------------------|
     |#accessToken                    |n                  |               |                        |<file:/resources/access_tokens/google_drive_token.txt>   |
     |#contextId                      |n                  |               |                        |Questions                                                |
     |#creatorId                      |n                  |               |                        |osanda                                                   |
     |#creatorPlatform                |n                  |               |                        |Mobile                                                   |
     |#creatoredSource                |n                  |               |                        |Gdrive                                                   |
     |#creatoredType                  |n                  |               |                        |Auto                                                     |
     |#deckId                         |y                  |scenario       |deckId                  |                                                         |
     |"#examDate"                     |n                  |               |                        |""                                                       |
     |#isExpert                       |n                  |               |                        |false                                                    |
     |#fileId                         |n                  |               |                        |<fileId>                                                 |
     |#title                          |n                  |               |                        |<title>                                                  |
     |#type                           |n                  |               |                        |GoogleDrive                                              |
     |#userId                         |n                  |               |                        |<userId>                                                 |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Existence in the response should be equal to the following
     |JSON Path                                         |isExists?                               |
     |--------------------------------------------------|----------------------------------------|
     |$[0].question                                     |true                                    |
