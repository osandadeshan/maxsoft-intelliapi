@echo off
echo Executing MaxSoft IntelliAPI Dev BVT API Test Automation Suite.............

cd ..
cd .. 

call mvn gauge:execute -DspecsDir="specs\Pre Test" -Denv="qa"
call mvn gauge:execute -DspecsDir="specs\Data Stores,specs\Other" -Denv="qa"

call mvn clean -DemailConfigEnv=qa install exec:java
echo Exit Code = %ERRORLEVEL%
if not "%ERRORLEVEL%" == "0" exit /b