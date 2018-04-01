package com.maxsoft.intelliapi.test;

import com.maxsoft.intelliapi.util.Email;
import com.maxsoft.intelliapi.util.ExecutionResults;


/**
 * Created by Osanda on 3/31/2018.
 */


public class EmailSender {

    public static void main(String[] args) {
        Email.send(ExecutionResults.getTestResultsAsString());
    }


}
