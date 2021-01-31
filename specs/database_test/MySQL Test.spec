# MySQL Test Specification

Project Name : MaxSoft-IntelliAPI
Developer    : Osanda Deshan
Version      : 1.0.0
Date         : 6/30/2018
Time         : 9:14 PM
Description  : This is an executable specification file which follows markdown syntax. Every heading in this file denotes a scenario. Every bulleted point denotes a step.

tags: database, mysql


* Given a user successfully connected to the MySQL Driver
* And the user need to connect to the "empdb" MySQL database using username as "root" and password as "root"
* When the user executes the MySQL query as "select * from employee"


## Validate specific users information in the users table

* Then the results obtained from the MySQL database should contain the following
     |Employee Id|First Name|Last Name     |Age|
     |-----------|----------|--------------|---|
     |2          |Eranga    |Nimalarathna  |27 |
     |1          |Osanda    |Nimalarathna  |28 |


## Validate all users information in the users table

* Then the results obtained from the MySQL database should equal to the following
     |Employee Id|First Name|Last Name     |Age|
     |-----------|----------|--------------|---|
     |1          |Osanda    |Nimalarathna  |28 |
     |2          |Eranga    |Nimalarathna  |27 |
     |3          |Gemunu    |Priyadarshana |32 |


__________________________________________________
* And the user close the MySQL database connection
