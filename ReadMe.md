# MaxSoft IntelliAPI

## Introduction
The main reason for developing this framework is to provide an easy way for Technical QA, Developer or Non-technical QA to perform API testing in an easy manner.

## Advantages
- Ability to implement automated tests for an API within few minutes.
- Codeless API automation.
- Ability to validate backend databases.
- Tests can be designed even by a non- technical person.
- Human readable tests in business language and markdown syntax.
- Generation of an executable document.
- Generate a HTML report with test details for every test execution.
- Parallel execution.
- Live execution report.
- Automated emails for test execution summary with graphical representations.

## Technologies/Frameworks Used
- Java
- Gauge Framework
- Rest Assured
- Apache POI
- Junit
- Apache Maven

## Supported Platforms
- Windows
- Linux
- Mac OS

## Supported Languages
- Java

## Design Diagram
![image](https://user-images.githubusercontent.com/9147189/104115454-a1ed7d00-5335-11eb-9e23-0f75137068af.png)

## Pre Requisites
1. Java
2. Maven

## Installing Gauge Core
**On Windows**
1. Install Chocolatey by executing the following command in an administrator command prompt. \
`@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "[System.Net.ServicePointManager]::SecurityProtocol = 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"`

2. Install Gauge by executing the following command in an administrator command prompt. \
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

## Installing Gauge Plugins
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

## Tested Versions
| OS 			    | Java Version   | Maven Version | Gauge Version | Gauge Java Version |
| ------------------------- | -------------- | ------------- | ------------ | ------------------- |
| Windows 10 Enterprise     | 1.8.0_181      | 3.6.1 	     | 1.1.6 	    | 0.7.13		  |
| Windows 10 Enterprise     | 1.8.0_181      | 3.6.1 	     | 1.2.1 	    | 0.7.15		  |
| Windows 10 Enterprise     | 1.8.0_131      | 3.5.0 	     | 1.1.7 	    | 0.7.13		  |
| Windows 10 		    | 1.8.0_271      | 3.6.3 	     | 1.1.6	    | 0.7.13 		  |
| Ubuntu 18.04 		    | 1.8  	     | 3.6.3 	     | 1.1.7 	    | 0.7.13 		  |
| MacOS Catalina v10.15.7   | 1.8.0_275      | 3.6.3 	     | 1.1.7 	    | 0.7.13 		  |

## MaxSoft IntelliAPI Tutorials
1. [MaxSoft IntelliAPI](https://medium.com/@osanda.deshan/maxsoft-ata-framework-for-api-test-automation-9cffd25a0b15 "MaxSoft — IntelliAPI")
2. [MaxSoft IntelliAPI Documentation](https://medium.com/intelliapi/maxsoft-intelliapi-step-implementations-usages-5cb9150e0106)
3. [How to use MaxSoft IntelliAPI for API Test Automation? — Tutorial 1](https://medium.com/@osanda.deshan/how-to-use-maxsoft-ata-framework-for-api-test-automation-e5966185fa33 "How to use MaxSoft IntelliAPI for API Test Automation? — Tutorial 1")
4. [How to use MaxSoft IntelliAPI for API Test Automation? — Tutorial 2](https://medium.com/@osanda.deshan/how-to-use-maxsoft-ata-framework-for-api-test-automation-tutorial-2-53b50c613f42 "How to use MaxSoft IntelliAPI for API Test Automation? — Tutorial 2")
5. [How to use MaxSoft IntelliAPI for API Test Automation? — Tutorial 3](https://medium.com/@osanda.deshan/how-to-use-maxsoft-ata-framework-for-api-test-automation-tutorial-3-160f81e404f1 "How to use MaxSoft IntelliAPI for API Test Automation? — Tutorial 3")
6. [How to use MaxSoft IntelliAPI for API Test Automation? — Tutorial 4](https://medium.com/@osanda.deshan/how-to-use-maxsoft-ata-framework-for-api-test-automation-tutorial-4-5fb265ca5eaf "How to use MaxSoft IntelliAPI for API Test Automation? — Tutorial 4")
7. [How to use MaxSoft IntelliAPI for API Test Automation? — Tutorial 5](https://medium.com/@osanda.deshan/how-to-use-maxsoft-ata-framework-for-api-test-automation-tutorial-5-3b2c22328233 "How to use MaxSoft IntelliAPI for API Test Automation? — Tutorial 5")

## Testing the Project
1) Go to **batch_files** folder in the project root directory.
2) Double click on **dev_regression_run.bat** file. \
OR \
Run below commands on the terminal \
`mvn test-compile gauge:execute -DspecsDir="specs" -Dtags="pre_requisites" -Denv="dev"` \
`mvn test-compile gauge:execute -DspecsDir="specs" -Denv="dev"`

## Support Forum
[Gitter](https://gitter.im/MaxSoft-IntelliAPI/community)

## License
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/License_icon-mit-2.svg/2000px-License_icon-mit-2.svg.png" alt="MIT License" width="100" height="100"/> [MaxSoft IntelliAPI](https://medium.com/intelliapi) is released under [MIT License](https://opensource.org/licenses/MIT)

## Copyright
Copyright 2021 [MaxSoft](https://maxsoftlk.github.io/).
