@echo off
echo Executing Pearson Prep Dev Regression API Test Automation Suite.............

cd ..

call mvn gauge:execute -DspecsDir="specs\Staging Regression" -Denv="dev"

call mvn exec:java
echo Exit Code = %ERRORLEVEL%
if not "%ERRORLEVEL%" == "0" exit /b