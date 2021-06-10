@echo off
echo Formating Specifications .............

cd .. 
gauge format specs

echo Exit Code = %ERRORLEVEL%
if not "%ERRORLEVEL%" == "0" exit /b
