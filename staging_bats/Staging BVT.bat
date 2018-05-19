@echo off
echo Executing Pearson Prep Staging BVT API Test Automation Suite.............

cd ..

call mvn gauge:execute -DspecsDir="specs\Staging BVT" -Denv="staging"

call mvn exec:java
echo Exit Code = %ERRORLEVEL%
if not "%ERRORLEVEL%" == "0" exit /b