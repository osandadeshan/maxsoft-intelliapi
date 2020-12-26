@echo off
echo Executable Document Generation.............

cd .. 
gauge docs spectacle specs

echo Exit Code = %ERRORLEVEL%
if not "%ERRORLEVEL%" == "0" exit /b
