@echo off
echo Making MaxSoft IntelliAPI JAR .............

cd .. 

mvn clean install -DskipTests

echo Exit Code = %ERRORLEVEL%
if not "%ERRORLEVEL%" == "0" exit /b