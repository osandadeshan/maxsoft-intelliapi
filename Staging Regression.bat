@echo off
echo Executing Pearson Prep Staging Regression API Test Automation Suite.............

call mvn gauge:execute -DspecsDir="specs\Staging Regression" -Denv="staging"
echo Exit Code = %ERRORLEVEL%
if not "%ERRORLEVEL%" == "0" exit /b

call mvn exec:java
echo Exit Code = %ERRORLEVEL%
if not "%ERRORLEVEL%" == "0" exit /b