@echo off
echo Executing MaxSoft IntelliAPI Dev BVT API Test Automation Suite.............

cd ..
cd .. 

call mvn test-compile gauge:execute -DspecsDir="specs\Pre Test" -Denv="dev"
call mvn test-compile gauge:execute -DspecsDir="specs\Access Token,specs\Data Stores,specs\Other" -Denv="dev"

call mvn clean -DemailConfigEnv=dev install exec:java
echo Exit Code = %ERRORLEVEL%
if not "%ERRORLEVEL%" == "0" exit /b
