package com.maxsoft.intelliapi.stepimpl.api;

import com.maxsoft.intelliapi.util.FrameworkUtil;
import com.thoughtworks.gauge.Step;

import static com.maxsoft.intelliapi.Constants.CURRENT_DIRECTORY;

/**
 * Project Name    : MaxSoft-IntelliAPI
 * Developer       : Osanda Deshan
 * Version         : 1.0.0
 * Date            : 12/24/2020
 * Time            : 12:10 AM
 * Description     :
 **/

public class OtherStepImpl {

    // Use this method to print the testing environment name in the HTML report
    @Step("Print configuration details of the testing environment")
    public void printTestingEnvDetails() {
        FrameworkUtil.printTestingEnvDetails();
    }

    // Use this method to replace the rows of a column in a given CSV with the timestamp
    @Step("And replace the row values in <columnName> column of the CSV <filePath> into the <timestampPattern> timestamp pattern")
    public void replaceAllColumnValuesToCurrentTimestamp(String columnName, String filePath, String timestampPattern) {
        FrameworkUtil.replaceAllColumnValuesToCurrentTimestamp(CURRENT_DIRECTORY + filePath, columnName, timestampPattern);
    }

    // Use this method to wait for a given time period
    @Step("And the user waits <seconds> seconds")
    public void waitBySeconds(String seconds) {
        FrameworkUtil.waitBySeconds(Integer.parseInt(seconds));
    }
}
