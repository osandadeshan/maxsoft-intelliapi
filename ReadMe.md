# MaxSoft IntelliAPI
<br />

## Introduction
The main reason for developing this framework is to provide an easy way for Technical QA, Developer or Non-technical QA to perform API testing in an easy manner.
<br />

## Technologies/Frameworks used
- Java
- Gauge Framework
- Rest Assured
- Apache POI
- Junit
- Apache Maven
<br />

## Supported Platforms
- Windows
- Linux
- Mac OS
<br />

## Supported Languages
- Java
<br />

## Advantages
- Generation of an executable document.
- Human readable tests, business language and Mark-down syntax.
- Tests can be designed even by a non- technical person.
- Ability to validate backend databases.
- Generate a HTML report with test details for every test execution.
- Parallel execution.
- Live execution report.
- Automated emails for test execution summary with graphical representations.
<br />

## Pre Requisites
1. Java
2. Maven
<br />

## How to Install Gauge Core

**On Windows**
1. Install Chocolatey by executing the following command. \
` @"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString(‘https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"`

2. Install Gauge by executing the following command. \
`choco install gauge`

**On MacOS**
1. Update Homebrew. \
`brew update`

2. Install Gauge using Homebrew. \
`brew install gauge`

**On Linux**
1. First, add Gauge’s GPG key with this command. \
`sudo apt-key adv --keyserver hkp://pool.sks-keyservers.net --recv-keys 023EDB0B`

2. Then add Gauge to the repository list using this command. \
`echo deb https://dl.bintray.com/gauge/gauge-deb nightly main | sudo tee -a /etc/apt/sources.list`

3. Finally, install Gauge using these commands. \
`sudo apt-get update` \
`sudo apt-get install gauge`
<br />

## How to Install Gauge Plugins
1. Open Command Prompt and execute following commands. \
`gauge install java` \
`gauge install html-report` \
`gauge install json-report` \
`gauge install xml-report` \
`gauge install spectacle` \
`gauge install flash`

2. You can check the installation using the following command. \
`gauge -v`

	If the installation is success, it will output like this:

```markdown
    Gauge version: <version number>
    Plugins
    -------
    flash (<version number>)
    html-report (<version number>)
    java (<version number>)
    json-report (<version number>)
    spectacle (<version number>)
    xml-report (<version number>)
```
<br />

## MaxSoft IntelliAPI Tutorials
1. [MaxSoft IntelliAPI](https://medium.com/@osanda.deshan/maxsoft-ata-framework-for-api-test-automation-9cffd25a0b15 "MaxSoft — IntelliAPI")
2. [MaxSoft IntelliAPI Documentation](https://medium.com/intelliapi/maxsoft-intelliapi-step-implementations-usages-5cb9150e0106)
3. [How to use MaxSoft IntelliAPI for API Test Automation? — Tutorial 1](https://medium.com/@osanda.deshan/how-to-use-maxsoft-ata-framework-for-api-test-automation-e5966185fa33 "How to use MaxSoft IntelliAPI for API Test Automation? — Tutorial 1")
4. [How to use MaxSoft IntelliAPI for API Test Automation? — Tutorial 2](https://medium.com/@osanda.deshan/how-to-use-maxsoft-ata-framework-for-api-test-automation-tutorial-2-53b50c613f42 "How to use MaxSoft IntelliAPI for API Test Automation? — Tutorial 2")
5. [How to use MaxSoft IntelliAPI for API Test Automation? — Tutorial 3](https://medium.com/@osanda.deshan/how-to-use-maxsoft-ata-framework-for-api-test-automation-tutorial-3-160f81e404f1 "How to use MaxSoft IntelliAPI for API Test Automation? — Tutorial 3")
6. [How to use MaxSoft IntelliAPI for API Test Automation? — Tutorial 4](https://medium.com/@osanda.deshan/how-to-use-maxsoft-ata-framework-for-api-test-automation-tutorial-4-5fb265ca5eaf "How to use MaxSoft IntelliAPI for API Test Automation? — Tutorial 4")
7. [How to use MaxSoft IntelliAPI for API Test Automation? — Tutorial 5](https://medium.com/@osanda.deshan/how-to-use-maxsoft-ata-framework-for-api-test-automation-tutorial-5-3b2c22328233 "How to use MaxSoft IntelliAPI for API Test Automation? — Tutorial 5")
<br />

## How to build the MaxSoft IntelliAPI JAR file
1) Get a clone of this project.
2) Open the command prompt. 
3) Navigate to the project directory. \
`cd <project_dir>`
4) Execute this command. \
`mvn clean install -DskipTests`
<br />

## How to test the project code
1) Open the command prompt.
2) Navigate to the directory of the **Dev BVT.bat** file. \
`cd <project_dir\bat_files\test_runner_bats>`
3) Enter the name of the **.bat** file and the extension. \
`Dev BVT.bat`
4) Press **Enter**.
<br />

## License
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/License_icon-mit-2.svg/2000px-License_icon-mit-2.svg.png" alt="MIT License" width="100" height="100"/> [MaxSoft IntelliAPI](https://medium.com/intelliapi) is released under [MIT License](https://opensource.org/licenses/MIT)

<br />

## Copyright
Copyright 2018 MaxSoft.
