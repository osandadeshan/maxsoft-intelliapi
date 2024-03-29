@echo off
echo Executing MaxSoft IntelliAPI Dev BVT API Test Automation Suite .............

cd .. 
cd ..

call mvn test-compile gauge:execute -DspecsDir="specs" -Dtags="pre_requisites" -Denv="dev"
call mvn test-compile gauge:execute -DspecsDir="specs" -Denv="dev"

call mvn clean -DemailConfigEnv=dev install exec:java

echo Exit Code = %ERRORLEVEL%
if not "%ERRORLEVEL%" == "0" exit /b
