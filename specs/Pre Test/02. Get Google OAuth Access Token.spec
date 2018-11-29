# Get Google OAuth Access Token Specification
Project Name : MaxSoft-IntelliAPI
Developer    : Osanda Deshan
Version      : 1.0.0
Date         : 8/6/2018
Time         : 3:02 PM
Description  : This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.



## Get Google OAuth Access token
* Given that a user needs to invoke "Get OAuth Access Token from Refresh Token"
* And the user set the form-data key value pairs as follows 

   |Key          |Value                                                                    |
   |-------------|-------------------------------------------------------------------------|
   |grant_type   |refresh_token                                                            |
   |client_id    |1072307075112-fposi9hgskm5uud3239f6gbfpkf6dfpk.apps.googleusercontent.com|
   |client_secret|dgUqQzhUfgbJ6YKiE_9U_rW8                                                 |
   |refresh_token|1/Hen2_CfJpxfkfHQ-EWvnI1sTbOQNCj-amx0-WPYv2A_AMTSRkuIjHHaHLDcuBSB2       |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following 

   |JSON Path   |Expected Result|
   |------------|---------------|
   |$.expires_in|3600           |
   |$.token_type|Bearer         |
* And save the JSON Path values of the response into text files 

   |JSON Path     |Text File Path                                 |
   |--------------|-----------------------------------------------|
   |$.access_token|/resources/access_tokens/google_drive_token.txt|
