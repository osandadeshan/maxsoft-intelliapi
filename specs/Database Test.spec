Database Validation Specification
=================================
Date Created    : 07/13/2017
Version   		: 1.0.0
Owner      		: Osanda Deshan
Description  	: This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.


tags: database_test


* Given a user successfully connected to the MySQL Driver



Validate specific users information in the users table
------------------------------------------------------
* When the user connects to the database of "testdb" using username as "root" and password as "root"
* Then the user executes the query as "select * from userinfo"
* And the results obtained from the database should contain the following
     |FirstName|LastName     |
     |---------|-------------|
     |Osanda   |Nimalarathna |
     |Gemunu   |Priyadarshana|
     |Thilina  |Jayasinghe   |



Validate all users information in the users table
-------------------------------------------------
* When the user connects to the database of "testdb" using username as "root" and password as "root"
* Then the user executes the query as "select * from userinfo"
* And the results obtained from the database should equal to the following
     |FirstName|LastName     |
     |---------|-------------|
     |Osanda   |Nimalarathna |
     |Gemunu   |Priyadarshana|
     |Thilina  |Jayasinghe   |




____________________________________________
* And the user close the database connection
