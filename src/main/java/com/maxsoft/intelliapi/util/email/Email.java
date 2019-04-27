package com.maxsoft.intelliapi.util.email;

/**
 * Project Name : MaxSoft-IntelliAPI
 * Developer    : Osanda Deshan
 * Version      : 1.0.0
 * Date         : 6/30/2018
 * Time         : 3:51 PM
 * Description  :
 **/

import com.maxsoft.intelliapi.util.charts.BarChart;
import com.maxsoft.intelliapi.util.charts.PieChart;
import com.maxsoft.intelliapi.util.reader.JsonReport;
import org.json.simple.parser.ParseException;
import org.testng.Assert;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.Properties;
import java.util.logging.FileHandler;
import java.util.logging.Logger;
import java.util.logging.SimpleFormatter;
import javax.activation.DataHandler;
import javax.activation.DataSource;
import javax.activation.FileDataSource;
import javax.mail.*;
import javax.mail.internet.InternetAddress;
import javax.mail.internet.MimeBodyPart;
import javax.mail.internet.MimeMessage;
import javax.mail.internet.MimeMultipart;
import static com.maxsoft.intelliapi.api.Base.INTELLIAPI_LOGS_FILE_PATH;


public class Email {

    public static final String CURRENT_DIRECTORY = System.getProperty("user.dir");

    private static final String DEV = "dev";
    private static final String QA = "qa";
    private static final String UAT = "uat";
    private static final String PROD = "prod";

    private static Properties emailProperties = new Properties();
    private static InputStream inputEmailPropertyFile = null;

    private static String environment = "";
    private static String isEmailNeeded = "";
    private static String senderEmailAddress = "";
    private static String senderEmailPassword = "";
    private static String recipientsEmailAddresses = "";
    private static String emailSubject = "";
    private static String emailBodyTitleHeadingSize = "";
    private static String emailBodyTitle = "";
    private static String emailBody = "";
    private static String emailFooterLine1 = "";
    private static String emailFooterLine2 = "";
    private static String emailFooterLine3 = "";

    private static Logger logger = Logger.getLogger(Email.class.getName());
    private static FileHandler fileHandler;
    private static SimpleFormatter formatter = new SimpleFormatter();

    static {
        try {
            fileHandler = new FileHandler(INTELLIAPI_LOGS_FILE_PATH, true);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void printInfo(String text){
        logger.addHandler(fileHandler);
        fileHandler.setFormatter(formatter);
        logger.info(text +"\n");
    }

    private static void setEmailConfigurations(){
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

        if(System.getProperty("emailConfigEnv") == null){
            environment = DEV;
        } else {
            environment = System.getProperty("emailConfigEnv");
        }

        switch (environment.toLowerCase()) {

            case DEV:
                isEmailNeeded = emailProperties.getProperty("dev_is_email_notifications_needed");
                senderEmailAddress = emailProperties.getProperty("dev_sender_email_address");
                senderEmailPassword = emailProperties.getProperty("dev_sender_email_password");
                recipientsEmailAddresses = emailProperties.getProperty("dev_recipients_email_addresses");
                emailSubject = emailProperties.getProperty("dev_email_subject");
                emailBodyTitleHeadingSize = emailProperties.getProperty("dev_email_body_title_heading_size");
                emailBodyTitle = emailProperties.getProperty("dev_email_body_title");
                emailBody = emailProperties.getProperty("dev_email_body");
                emailFooterLine1 = emailProperties.getProperty("dev_email_footer_line1");
                emailFooterLine2 = emailProperties.getProperty("dev_email_footer_line2");
                emailFooterLine3 = emailProperties.getProperty("dev_email_footer_line3");
                break;

            case QA:
                isEmailNeeded = emailProperties.getProperty("qa_is_email_notifications_needed");
                senderEmailAddress = emailProperties.getProperty("qa_sender_email_address");
                senderEmailPassword = emailProperties.getProperty("qa_sender_email_password");
                recipientsEmailAddresses = emailProperties.getProperty("qa_recipients_email_addresses");
                emailSubject = emailProperties.getProperty("qa_email_subject");
                emailBodyTitleHeadingSize = emailProperties.getProperty("qa_email_body_title_heading_size");
                emailBodyTitle = emailProperties.getProperty("qa_email_body_title");
                emailBody = emailProperties.getProperty("qa_email_body");
                emailFooterLine1 = emailProperties.getProperty("qa_email_footer_line1");
                emailFooterLine2 = emailProperties.getProperty("qa_email_footer_line2");
                emailFooterLine3 = emailProperties.getProperty("qa_email_footer_line3");
                break;

            case UAT:
                isEmailNeeded = emailProperties.getProperty("uat_is_email_notifications_needed");
                senderEmailAddress = emailProperties.getProperty("uat_sender_email_address");
                senderEmailPassword = emailProperties.getProperty("uat_sender_email_password");
                recipientsEmailAddresses = emailProperties.getProperty("uat_recipients_email_addresses");
                emailSubject = emailProperties.getProperty("uat_email_subject");
                emailBodyTitleHeadingSize = emailProperties.getProperty("uat_email_body_title_heading_size");
                emailBodyTitle = emailProperties.getProperty("uat_email_body_title");
                emailBody = emailProperties.getProperty("uat_email_body");
                emailFooterLine1 = emailProperties.getProperty("uat_email_footer_line1");
                emailFooterLine2 = emailProperties.getProperty("uat_email_footer_line2");
                emailFooterLine3 = emailProperties.getProperty("uat_email_footer_line3");
                break;

            case PROD:
                isEmailNeeded = emailProperties.getProperty("prod_is_email_notifications_needed");
                senderEmailAddress = emailProperties.getProperty("prod_sender_email_address");
                senderEmailPassword = emailProperties.getProperty("prod_sender_email_password");
                recipientsEmailAddresses = emailProperties.getProperty("prod_recipients_email_addresses");
                emailSubject = emailProperties.getProperty("prod_email_subject");
                emailBodyTitleHeadingSize = emailProperties.getProperty("prod_email_body_title_heading_size");
                emailBodyTitle = emailProperties.getProperty("prod_email_body_title");
                emailBody = emailProperties.getProperty("prod_email_body");
                emailFooterLine1 = emailProperties.getProperty("prod_email_footer_line1");
                emailFooterLine2 = emailProperties.getProperty("prod_email_footer_line2");
                emailFooterLine3 = emailProperties.getProperty("prod_email_footer_line3");
                break;

            default:
                Assert.fail("\n\nPlease enter an valid environment dev|qa|uat|prod " +
                        "into the \"emailConfigEnv\" property in <project_dir>/pom.xml\n\n");
        }
    }

    public static void send(String executionResults) {
        setEmailConfigurations();

        if (isEmailNeeded.toLowerCase().equals("true") || isEmailNeeded.toLowerCase().equals("yes")
                || isEmailNeeded.toLowerCase().equals("y")) {

            Properties props = new Properties();
            props.put("mail.smtp.auth", "true");
            props.put("mail.smtp.starttls.enable", "true");
            props.put("mail.smtp.host", "smtp.gmail.com");
            props.put("mail.smtp.port", "587");

            Session session = Session.getInstance(props,
                    new javax.mail.Authenticator() {
                        protected PasswordAuthentication getPasswordAuthentication() {
                            return new PasswordAuthentication(senderEmailAddress, senderEmailPassword);
                        }
                    });

            try {
                // Create a default MimeMessage object.
                Message message = new MimeMessage(session);

                // Set From: header field of the header.
                message.setFrom(new InternetAddress(senderEmailAddress));

                // Set To: header field of the header.
                message.setRecipients(Message.RecipientType.TO,
                        InternetAddress.parse(recipientsEmailAddresses));

                // Set Subject: header field
                message.setSubject(emailSubject);

                // This mail has 2 parts, the BODY and the embedded image
                MimeMultipart multipart = new MimeMultipart("related");

                // first part (the html)
                BodyPart messageBodyPart = new MimeBodyPart();
                String htmlText = "<h" + emailBodyTitleHeadingSize + ">" + emailBodyTitle + "</h" + emailBodyTitleHeadingSize + ">" +
                        "<br />" + emailBody + "<br /><br /><br />" + executionResults;
                messageBodyPart.setContent(htmlText, "text/html");
                // add it
                multipart.addBodyPart(messageBodyPart);

                // second part (the pie chart)
                messageBodyPart = new MimeBodyPart();
                PieChart.save(JsonReport.getPassedScenarioCount(), JsonReport.getFailedScenarioCount(), JsonReport.getSkippedScenarioCount());
                DataSource fds = new FileDataSource(
                        PieChart.getSavedPieChartImagePath());

                messageBodyPart.setDataHandler(new DataHandler(fds));
                messageBodyPart.setHeader("Content-ID", "<pie-chart>");
                messageBodyPart.setFileName(PieChart.getSavedPieChartImageName());

                // add pie chart to the multipart
                multipart.addBodyPart(messageBodyPart);

                // third part (the bar chart)
                messageBodyPart = new MimeBodyPart();
                BarChart.save();
                DataSource fds2 = new FileDataSource(
                        BarChart.getSavedBarChartImagePath());

                messageBodyPart.setDataHandler(new DataHandler(fds2));
                messageBodyPart.setHeader("Content-ID", "<bar-chart>");
                messageBodyPart.setFileName(BarChart.getSavedBarChartImageName());

                // add bar chart to the multipart
                multipart.addBodyPart(messageBodyPart);

                // put everything together
                message.setContent(multipart);
                // Send message
                Transport.send(message);

                printInfo("Sent message successfully....");


            } catch (MessagingException e) {
                throw new RuntimeException(e);
            } catch (IOException e) {
                e.printStackTrace();
            } catch (ParseException e) {
                e.printStackTrace();
            }

        } else {
            printInfo("\n\nEmail notifications are currently turned off. " +
                    "To turn on, go to <project_dir>/env/email/email.properties\n\n");
        }
    }


}