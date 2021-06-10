# Epoch Time Specification

Project Name : MaxSoft-IntelliAPI
Developer    : Osanda Deshan
Version      : 1.0.0
Date         : 9/25/2018
Time         : 12:28 PM
Description  : This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.

tags: epoch_time, regression


## Current Epoch time

* And the user saves the current epoch time in "Seconds" inside data stores

   |Data Store Type|Data Store Variable Name|
   |---------------|------------------------|
   |scenario       |currentEpochTime        |
* And the user saves the current epoch time in "Milliseconds" inside data stores

   |Data Store Type|Data Store Variable Name|
   |---------------|------------------------|
   |suite          |currentEpochTime        |


## Epoch time for a given timestamp

* And the user converts a timestamp into epoch time and saves inside data stores

   |Timestamp Pattern         |Is Timestamp Retrieve From Data Store?|Data Store Type|Data Store Variable Name|Timestamp                   |Seconds/Miliseconds|Epoch Time Saving Data Store Type|Epoch Time Saving Data Store Variable Name|
   |--------------------------|--------------------------------------|---------------|------------------------|----------------------------|-------------------|---------------------------------|------------------------------------------|
   |yyyy-MM-dd'T'HH:mm:ss.SSSZ|no                                    |               |                        |2018-09-25T11:56:00.000-0000|Seconds            |scenario                         |epochTime                                 |
* And the user waits "10" seconds
* And the user converts a timestamp into epoch time and saves inside data stores

   |Timestamp Pattern         |Is Timestamp Retrieve From Data Store?|Data Store Type|Data Store Variable Name|Timestamp                   |Seconds/Miliseconds|Epoch Time Saving Data Store Type|Epoch Time Saving Data Store Variable Name|
   |--------------------------|--------------------------------------|---------------|------------------------|----------------------------|-------------------|---------------------------------|------------------------------------------|
   |yyyy-MM-dd'T'HH:mm:ss.SSSZ|no                                    |               |                        |2018-09-25T11:56:00.000-0000|Milliseconds       |suite                            |epochTime                                 |
