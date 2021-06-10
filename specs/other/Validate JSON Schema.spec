# Validate JSON Schema Specification

Project Name    : MaxSoft-IntelliAPI
Developer       : Osanda Deshan
Version         : 1.0.0
Date            : 2/1/2021
Time            : 11:43 PM
Description     : This is an executable specification file

tags: json_schema_validation, regression


## Validate JSON Schema Scenario

* Given that a user needs to invoke "Get metrics"
* And the user saves the values inside data stores as follows

   |DataStore Type|Variable Name|Value To Be Stored|
   |--------------|-------------|------------------|
   |Scenario      |version      |v2                |
   |Scenario      |jsonFile     |metrics.json      |
* And the user set values to the API endpoint placeholders using data stores as follows

   |Placeholder In JSON Template|Is Data Store Used?|Data Store Type|Data Store Variable Name|Replacement Text|
   |----------------------------|-------------------|---------------|------------------------|----------------|
   |#version                    |n                  |               |                        |v2              |
   |#jsonFile                   |y                  |Scenario       |jsonFile                |                |
* When the user invokes the API
* Then the status code for the request is "200"
* And validate the response against the JSON Schema saved in "metrics-schema.json"
