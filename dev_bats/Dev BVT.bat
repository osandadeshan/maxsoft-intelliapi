@echo off
echo Executing MaxSoft IntelliAPI Dev BVT API Test Automation Suite.............

cd ..

call mvn gauge:execute -DspecsDir="specs\Access Token\Get Staging PI Token.spec,specs\BVT" -Denv="dev"

call mvn clean -DemailConfigEnv=dev install exec:java
echo Exit Code = %ERRORLEVEL%
if not "%ERRORLEVEL%" == "0" exit /b