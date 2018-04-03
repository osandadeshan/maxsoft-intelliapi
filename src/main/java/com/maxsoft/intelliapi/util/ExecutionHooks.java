package com.maxsoft.intelliapi.util;

import java.text.ParseException;


/**
 * Created by Osanda on 3/31/2018.
 */


public class ExecutionHooks {

//    @AfterSuite
    public void sendEmail() throws ParseException {
        Email.send(ExecutionResults.getTestResultsAsString());
    }


}
