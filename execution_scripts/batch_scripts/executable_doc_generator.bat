@echo off
echo Executable Document Generation .............

cd .. 
cd ..

gauge docs spectacle specs

echo Exit Code = %ERRORLEVEL%
if not "%ERRORLEVEL%" == "0" exit /b
