Database Validation Specification
=================================
Date Created    : 07/13/2017
Version   		: 1.0.0
Owner      		: Osanda Deshan
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.


tags: database_test


* Given a user successfully loaded the MySQL Driver



Validate specific users information in the users table
------------------------------------------------------
* When the user connects to the database of "user" using username as "root" and password as "osanda92"
* Then the user executes query of "select * from userinfo"
* And the results obtained from the database should contain the following
     |FirstName|LastName     |
     |---------|-------------|
     |Gemunu   |Priyadarshana|
     |Osanda   |Nimalarathna |
     |Eranga   |Nimalarathna |



Validate all users information in the users table
-------------------------------------------------
* When the user connects to the database of "user" using username as "root" and password as "osanda92"
* Then the user executes query of "select * from userinfo"
* And the results obtained from the database should equal to the following
     |FirstName|LastName     |
     |---------|-------------|
     |Gemunu   |Priyadarshana|
     |Osanda   |Nimalarathna |
     |Thilina  |Jayasinghe   |




_______________________________
* Close the database connection
