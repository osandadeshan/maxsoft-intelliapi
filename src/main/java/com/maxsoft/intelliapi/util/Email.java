package com.maxsoft.intelliapi.util;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Properties;
import javax.mail.Message;
import javax.mail.MessagingException;
import javax.mail.PasswordAuthentication;
import javax.mail.Session;
import javax.mail.Transport;
import javax.mail.internet.InternetAddress;
import javax.mail.internet.MimeMessage;


/**
 * Created by Osanda on 3/30/2018.
 */


public class Email {

//    public static final String IS_EMAIL_NOTIFICATIONS_NEEDED = System.getenv("is_email_notifications_needed");
//    public static final String SENDER_EMAIL_ADDRESS = System.getenv("sender_email_address");
//    public static final String SENDER_EMAIL_PASSWORD = System.getenv("sender_email_password");
//    public static final String RECIPIENTS_EMAIL_ADDRESSES = System.getenv("recipients_email_addresses");
//    public static final String EMAIL_SUBJECT = System.getenv("email_subject");
//    public static final String EMAIL_BODY = System.getenv("email_body");
    public static final String CURRENT_DIRECTORY = System.getProperty("user.dir");

    static Properties emailProperties = new Properties();
    static InputStream input = null;

    public static void send(String messageBody) {
        try {
            input = new FileInputStream(CURRENT_DIRECTORY + File.separator + "env" + File.separator + "email"
                                        + File.separator + "email.properties");
            // load a properties file
            emailProperties.load(input);
        } catch (IOException ex) {
            ex.printStackTrace();
        } finally {
            if (input != null) {
                try {
                    input.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }

        // Get the property values
        final String IS_EMAIL_NOTIFICATIONS_NEEDED = emailProperties.getProperty("is_email_notifications_needed");
        final String SENDER_EMAIL_ADDRESS = emailProperties.getProperty("sender_email_address");
        final String SENDER_EMAIL_PASSWORD = emailProperties.getProperty("sender_email_password");
        final String RECIPIENTS_EMAIL_ADDRESSES = emailProperties.getProperty("recipients_email_addresses");
        final String EMAIL_SUBJECT = emailProperties.getProperty("email_subject");
        final String EMAIL_BODY = emailProperties.getProperty("email_body");

        if (IS_EMAIL_NOTIFICATIONS_NEEDED.toLowerCase().equals("true")
                || IS_EMAIL_NOTIFICATIONS_NEEDED.toLowerCase().equals("yes")
                || IS_EMAIL_NOTIFICATIONS_NEEDED.toLowerCase().equals("y")) {

            Properties props = new Properties();
            props.put("mail.smtp.auth", "true");
            props.put("mail.smtp.starttls.enable", "true");
            props.put("mail.smtp.host", "smtp.gmail.com");
            props.put("mail.smtp.port", "587");

            Session session = Session.getInstance(props,
                    new javax.mail.Authenticator() {
                        protected PasswordAuthentication getPasswordAuthentication() {
                            return new PasswordAuthentication(SENDER_EMAIL_ADDRESS, SENDER_EMAIL_PASSWORD);
                        }
                    });

            try {

                Message message = new MimeMessage(session);
                message.setFrom(new InternetAddress(SENDER_EMAIL_ADDRESS));
                message.setRecipients(Message.RecipientType.TO,
                        InternetAddress.parse(RECIPIENTS_EMAIL_ADDRESSES));
                message.setSubject(EMAIL_SUBJECT + " - " + new SimpleDateFormat("dd/MMMM/YYYY").format(new Date()));
                message.setText(messageBody + "\n" + EMAIL_BODY);
                Transport.send(message);

                System.out.println("Successfully sent the email\n");

            } catch (MessagingException e) {
                throw new RuntimeException(e);
            }
        } else {
            System.out.println("\n\nEmail notifications are currently turned off. " +
                    "To turn on, go to <project_dir>/env/default/default.properties\n\n");
        }
    }


}