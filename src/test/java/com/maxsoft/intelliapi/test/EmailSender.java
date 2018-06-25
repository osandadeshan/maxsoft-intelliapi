package com.maxsoft.intelliapi.test;

import com.maxsoft.intelliapi.util.Email;
import com.maxsoft.intelliapi.util.JsonReportReader;


/**
 * Created by Osanda on 3/31/2018.
 */


public class EmailSender {

    public static void main(String[] args) {
        Email.send(JsonReportReader.getExecutionResults());
    }


}
