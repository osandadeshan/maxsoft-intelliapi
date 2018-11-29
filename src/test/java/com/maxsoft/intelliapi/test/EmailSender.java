package com.maxsoft.intelliapi.test;

/**
 * Project Name : MaxSoft-IntelliAPI
 * Developer    : Osanda Deshan
 * Version      : 1.0.0
 * Date         : 6/30/2018
 * Time         : 3:51 PM
 * Description  :
 **/

import com.maxsoft.intelliapi.util.email.Email;
import com.maxsoft.intelliapi.util.reader.JsonReport;


public class EmailSender {

    public static void main(String[] args) {
        Email.send(JsonReport.getExecutionResults());
    }


}
