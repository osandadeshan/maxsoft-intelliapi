package com.maxsoft.intelliapi.util;


/**
 * Created by Osanda on 3/31/2018.
 */


public class ExecutionHooks {

//    @AfterSuite
    public void sendEmail() {
        Email.send(ExecutionResults.getTestResultsAsString());
    }


}
