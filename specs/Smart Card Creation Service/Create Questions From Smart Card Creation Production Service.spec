Create Questions From Smart Card Creation Production Service Specification
==========================================================================
Date Created    : 05/23/2018
Version   		: 1.0.0
Owner      		: Osanda Deshan
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.


tags: create_questions_from_text, create_questions_from_text-positive_tests, positive, ci_ready



Get PI Token
------------
* Invoke PI API in Production Environment using valid username and password and save the access token inside the text file



Create Questions from Text using one paragraph
----------------------------------------------
* Given that a user needs to invoke "Smart Card Creation Production Service"
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |
* And the user set the request attributes as follows
     |Attribute Value In JSON Template |Path Value                                       |
     |---------------------------------|-------------------------------------------------|
     |#timeout                         |200                                              |
     |#media                           |TEXT                                             |
     |#imageUrl                        |http://somehost/someimg.jpg                      |
     |#promptType                      |TEXT                                             |
     |#creatorId                       |osanda                                           |
     |#creatorPlatform                 |Mobile                                           |
     |#creatoredSource                 |Clipper                                          |
     |#creatoredType                   |Auto                                             |
     |#title                           |Cards from text                                  |
     |#userId                          |osan                                             |
     |#isExpert                        |false                                            |
     |#questionText                    |<file:/resources/text_files/paragraphs2.txt>     |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Existence in the response should be equal to the following
     |JSON Path                              |isExists       |
     |---------------------------------------|---------------|
     |$.results[0].result.id                 |true           |
     |$.results[0].result.original_text      |true           |
     |$.results[0].result.score              |true           |
     |$.results[0].result.sides[0].text      |true           |
     |$.results[0].result.sides[1].text      |true           |
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                   |Value          |
     |----------------------------|---------------|
     |$.results[0].succeeded      |true           |



Create Questions from Text using multiple paragraphs
----------------------------------------------------
* Given that a user needs to invoke "Smart Card Creation Production Service"
* And the user set the request authentication configurations as follows
     |Configuration                                                     |Configuration Value            |
     |------------------------------------------------------------------|-------------------------------|
     |Is authentication required?                                       |Yes                            |
     |Do you need to retrieve the access token from the text file?      |Yes                            |
     |Provide the access token if you need to authorize the API manually|N/A                            |
* And the user set the request attributes as follows
     |Attribute Value In JSON Template |Path Value                                       |
     |---------------------------------|-------------------------------------------------|
     |#timeout                         |200                                              |
     |#media                           |TEXT                                             |
     |#imageUrl                        |http://somehost/someimg.jpg                      |
     |#promptType                      |TEXT                                             |
     |#creatorId                       |osanda                                           |
     |#creatorPlatform                 |Mobile                                           |
     |#creatoredSource                 |Clipper                                          |
     |#creatoredType                   |Auto                                             |
     |#title                           |Cards from text                                  |
     |#userId                          |osan                                             |
     |#isExpert                        |false                                            |
     |#questionText                    |<file:/resources/text_files/paragraphs1.txt>     |
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Existence in the response should be equal to the following
     |JSON Path                              |isExists       |
     |---------------------------------------|---------------|
     |$.results[0].result.id                 |true           |
     |$.results[0].result.original_text      |true           |
     |$.results[0].result.score              |true           |
     |$.results[0].result.sides[0].text      |true           |
     |$.results[0].result.sides[1].text      |true           |
* And the JSON Path Assertions for the response should be equal to the following
     |JSON Path                   |Value          |
     |----------------------------|---------------|
     |$.results[0].succeeded      |true           |