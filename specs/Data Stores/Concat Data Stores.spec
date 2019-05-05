# Concat Data Stores Specification

<pre>
Project Name    : MaxSoft-IntelliAPI
Developer       : Osanda Deshan
Version         : 1.0.0
Date            : 05/05/2019
Time            : 11:17
Description     : This is an executable specification file
</pre>


tags: data_store



## Concat Data Stores

* And the user saves the values inside data stores as follows

   |DataStore Type|Variable Name|Value To Be Stored|
   |--------------|-------------|------------------|
   |Scenario      |totalLabel   |Total is:         |
   |Scenario      |val2         |10                |
   |Scenario      |val3         |12                |

* Add the integer values in data stores and save it in a "Scenario" type data store named "totalVal"

   |DataStore Type|Variable Name|
   |--------------|-------------|
   |Scenario      |val2         |
   |Scenario      |val3         |

* Concat values in data stores and save it in a "Scenario" type data store named "newTotalLabel"

   |DataStore Type|Variable Name|
   |--------------|-------------|
   |Scenario      |totalLabel   |
   |Scenario      |${SPACE}     |

* Concat values in data stores and save it in a "Scenario" type data store named "finalString"

   |DataStore Type|Variable Name|
   |--------------|-------------|
   |Scenario      |newTotalLabel|
   |Scenario      |totalVal     |

* And the values inside the data stores equal to the following

   |DataStore Type|Variable Name|Expected Value|
   |--------------|-------------|--------------|
   |Scenario      |finalString  |Total is: 22  |