package com.maxsoft.intelliapi.test;

import com.maxsoft.intelliapi.util.Email;
import com.maxsoft.intelliapi.util.JsonReader;
import java.text.ParseException;


/**
 * Created by Osanda on 3/31/2018.
 */


public class EmailSender {

    public static void main(String[] args) throws ParseException {
        Email.send(JsonReader.getExecutionResults());
    }


}
