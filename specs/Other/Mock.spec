# Mock Specification
Created by onimalarat on 1/19/2020

This is an executable specification file which follows markdown syntax.
Every heading in this file denotes a scenario. Every bulleted point denotes a step.
     
## Get mobile number by id
* Given that a user needs to invoke "Mock Contacts"
* When the user invokes the API
* Then the status code for the request is "200"
* And the JSON Path Assertions for the response should be equal to the following

   |JSON Path              |Expected Result|
   |-----------------------|---------------|
   |$[?(@.id=='2')].mobile |["0715676891"] |