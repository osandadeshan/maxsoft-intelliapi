package com.maxsoft.intelliapi.util;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.Properties;
import javax.activation.DataHandler;
import javax.activation.DataSource;
import javax.activation.FileDataSource;
import javax.mail.*;
import javax.mail.internet.InternetAddress;
import javax.mail.internet.MimeBodyPart;
import javax.mail.internet.MimeMessage;
import javax.mail.internet.MimeMultipart;
import static com.maxsoft.intelliapi.util.Chart.getSavedPieChartImageName;
import static com.maxsoft.intelliapi.util.Chart.getSavedPieChartImagePath;
import static com.maxsoft.intelliapi.util.JsonReader.getFailedScenarioCount;
import static com.maxsoft.intelliapi.util.JsonReader.getPassedScenarioCount;
import static com.maxsoft.intelliapi.util.JsonReader.getSkippedScenarioCount;


/**
 * Created by Osanda on 3/30/2018.
 */


public class Email {

    public static final String CURRENT_DIRECTORY = System.getProperty("user.dir");

    static Properties emailProperties = new Properties();
    static InputStream inputEmailPropertyFile = null;

    public static void send(String executionResults) {
        try {
            inputEmailPropertyFile = new FileInputStream(CURRENT_DIRECTORY + File.separator + "env" + File.separator + "email"
                    + File.separator + "email.properties");
            // load a properties file
            emailProperties.load(inputEmailPropertyFile);
        } catch (IOException ex) {
            ex.printStackTrace();
        } finally {
            if (inputEmailPropertyFile != null) {
                try {
                    inputEmailPropertyFile.close();
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
        final String EMAIL_BODY_TITLE_HEADING_SIZE = emailProperties.getProperty("email_body_title_heading_size");
        final String EMAIL_BODY_TITLE = emailProperties.getProperty("email_body_title");
        final String EMAIL_BODY = emailProperties.getProperty("email_body");
        final String EMAIL_FOOTER_LINE1 = emailProperties.getProperty("email_footer_line1");
        final String EMAIL_FOOTER_LINE2 = emailProperties.getProperty("email_footer_line2");
        final String EMAIL_FOOTER_LINE3 = emailProperties.getProperty("email_footer_line3");

        if (IS_EMAIL_NOTIFICATIONS_NEEDED.toLowerCase().equals("true") || IS_EMAIL_NOTIFICATIONS_NEEDED.toLowerCase().equals("yes")
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
                // Create a default MimeMessage object.
                Message message = new MimeMessage(session);

                // Set From: header field of the header.
                message.setFrom(new InternetAddress(SENDER_EMAIL_ADDRESS));

                // Set To: header field of the header.
                message.setRecipients(Message.RecipientType.TO,
                        InternetAddress.parse(RECIPIENTS_EMAIL_ADDRESSES));

                // Set Subject: header field
                message.setSubject(EMAIL_SUBJECT);

                // This mail has 2 parts, the BODY and the embedded image
                MimeMultipart multipart = new MimeMultipart("related");

                // first part (the html)
                BodyPart messageBodyPart = new MimeBodyPart();
                String htmlText = "<h" + EMAIL_BODY_TITLE_HEADING_SIZE + ">" + EMAIL_BODY_TITLE + "</h" + EMAIL_BODY_TITLE_HEADING_SIZE + ">" + executionResults +
                        "<br /><br />" + EMAIL_BODY + "<br /><br /><br />" + EMAIL_FOOTER_LINE1 + "<br />" + EMAIL_FOOTER_LINE2 + "<br />" + EMAIL_FOOTER_LINE3;
                messageBodyPart.setContent(htmlText, "text/html");
                // add it
                multipart.addBodyPart(messageBodyPart);

                // second part (the image)
                messageBodyPart = new MimeBodyPart();
                Chart.savePieChart(getPassedScenarioCount(), getFailedScenarioCount(), getSkippedScenarioCount());
                DataSource fds = new FileDataSource(
                        getSavedPieChartImagePath());

                messageBodyPart.setDataHandler(new DataHandler(fds));
                messageBodyPart.setHeader("Content-ID", "<image>");
                messageBodyPart.setFileName(getSavedPieChartImageName());

                // add image to the multipart
                multipart.addBodyPart(messageBodyPart);

                // put everything together
                message.setContent(multipart);
                // Send message
                Transport.send(message);

                System.out.println("Sent message successfully....");


            } catch (MessagingException e) {
                throw new RuntimeException(e);
            } catch (IOException e) {
                e.printStackTrace();
            }

        } else {
            System.out.println("\n\nEmail notifications are currently turned off. " +
                    "To turn on, go to <project_dir>/env/default/default.properties\n\n");
        }
    }


}