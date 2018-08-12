package com.maxsoft.intelliapi.util.email;

/**
 * Project Name : MaxSoft-IntelliAPI
 * Developer    : Osanda Deshan
 * Version      : 1.0.0
 * Date         : 6/30/2018
 * Time         : 3:51 PM
 * Description  :
 **/

import org.json.simple.parser.ParseException;
import java.io.IOException;
import static com.maxsoft.intelliapi.util.reader.JsonReport.*;


public class EmailTemplate {

    static String template = "<!DOCTYPE html> \n" +
            "            <html> \n" +
            "            <head> \n" +
            "            </head> \n" +
            "            <body> \n" +
            "             \n" +
            "            <table style=\"width:70%; border:1px solid black; border-collapse:collapse;\"> \n" +
            "              <col width=45%> \n" +
            "              <tr> \n" +
            "                <th colspan=3 style=\"text-align: left; padding: 8px; border: 1px solid black; background-color: #08A7CE; color: white;\"><b>Test Execution Summary</b></th> \n" +
            "              </tr> \n" +
            "              <tr> \n" +
            "                <td style=\"text-align: left; padding: 8px; border: 1px solid black; background-color: #f2f2f2\"><b>Project Name</b></td> \n" +
            "                <td style=\"text-align: left; padding: 8px; border: 1px solid black; background-color: #f2f2f2\">#projectName</td> \n" +
            "              </tr> \n" +
            "              <tr> \n" +
            "                <td style=\"text-align: left; padding: 8px; border: 1px solid black;\"><b>Timestamp</b></td> \n" +
            "                <td style=\"text-align: left; padding: 8px; border: 1px solid black;\">#timestamp</td> \n" +
            "              </tr> \n" +
            "              <tr> \n" +
            "                <td style=\"text-align: left; padding: 8px; border: 1px solid black; background-color: #f2f2f2\"><b>Environment</b></td> \n" +
            "                <td style=\"text-align: left; padding: 8px; border: 1px solid black; background-color: #f2f2f2\">#environment</td> \n" +
            "              </tr> \n" +
            "              <tr> \n" +
            "                <td style=\"text-align: left; padding: 8px; border: 1px solid black;\"><b>Execution Time</b></td> \n" +
            "                <td style=\"text-align: left; padding: 8px; border: 1px solid black;\">#executionTime</td> \n" +
            "              </tr> \n" +
            "              <tr> \n" +
            "                <td style=\"text-align: left; padding: 8px; border: 1px solid black; background-color: #f2f2f2\"><b>Execution Status</b></td> \n" +
            "                <td style=\"text-align: left; padding: 8px; border: 1px solid black; background-color: #f2f2f2\">#executionStatus</td> \n" +
            "              </tr> \n" +
            "              <tr> \n" +
            "                <td style=\"text-align: left; padding: 8px; border: 1px solid black;\"><b>Success Rate</b></td> \n" +
            "                <td style=\"text-align: left; padding: 8px; border: 1px solid black;\">#successRate</td> \n" +
            "              </tr> \n" +
            "              <tr> \n" +
            "                <td style=\"text-align: left; padding: 8px; border: 1px solid black; background-color: #f2f2f2\"><b>Fail Rate</b></td> \n" +
            "                <td style=\"text-align: left; padding: 8px; border: 1px solid black; background-color: #f2f2f2\">#failRate</td> \n" +
            "              </tr> \n" +
            "            </table> \n" +
            "             \n" +
            "            <br><br> \n" +
            "            <table style=\"width:70%; border:1px solid black; border-collapse:collapse;\"> \n" +
            "              <col width=45%> \n" +
            "              <tr> \n" +
            "                <th colspan=3 style=\"text-align: left; padding: 8px; border: 1px solid black; background-color: #08A7CE; color: white;\"><b>Scenario Information</b></th> \n" +
            "              </tr> \n" +
            "              <tr> \n" +
            "                <td style=\"text-align: left; padding: 8px; border: 1px solid black; background-color: #f2f2f2\"><b>Total Scenarios Count</b></td> \n" +
            "                <td style=\"text-align: left; padding: 8px; border: 1px solid black; background-color: #f2f2f2\">#totalScenariosCount</td> \n" +
            "              </tr> \n" +
            "              <tr> \n" +
            "                <td style=\"text-align: left; padding: 8px; border: 1px solid black;\"><b>Passed Scenarios Count</b></td> \n" +
            "                <td style=\"text-align: left; padding: 8px; border: 1px solid black;\">#passedScenariosCount</td> \n" +
            "              </tr> \n" +
            "              <tr> \n" +
            "                <td style=\"text-align: left; padding: 8px; border: 1px solid black; background-color: #f2f2f2\"><b>Failed Scenarios Count</b></td> \n" +
            "                <td style=\"text-align: left; padding: 8px; border: 1px solid black; background-color: #f2f2f2\">#failedScenariosCount</td> \n" +
            "              </tr> \n" +
            "              <tr> \n" +
            "                <td style=\"text-align: left; padding: 8px; border: 1px solid black;\"><b>Skipped Scenarios Count</b></td> \n" +
            "                <td style=\"text-align: left; padding: 8px; border: 1px solid black;\">#skippedScenariosCount</td> \n" +
            "              </tr> \n" +
            "            </table> \n" +
            "             \n" +
            "            <img src=\"cid:pie-chart\" alt=\"Pie Chart For Test Execution Results\" align=\"left\" style=\"padding-top: 30px; padding-bottom: 35px;\"> <br><br><br>\n" +
            "             \n" +
            "            <br><br><br><br> \n" +
            "            <table style=\"width:70%; border:1px solid black; border-collapse:collapse;\"> \n" +
            "              <col width=45%> \n" +
            "              <tr> \n" +
            "                <th colspan=3 style=\"text-align: left; padding: 8px; border: 1px solid black; background-color: #08A7CE; color: white;\"><b>Specification Information</b></th> \n" +
            "              </tr> \n" +
            "              <tr> \n" +
            "                <td style=\"text-align: left; padding: 8px; border: 1px solid black; background-color: #f2f2f2\"><b>Total Specs Count</b></td> \n" +
            "                <td style=\"text-align: left; padding: 8px; border: 1px solid black; background-color: #f2f2f2\">#totalSpecsCount</td> \n" +
            "              </tr> \n" +
            "              <tr> \n" +
            "                <td style=\"text-align: left; padding: 8px; border: 1px solid black;\"><b>Passed Specs Count</b></td> \n" +
            "                <td style=\"text-align: left; padding: 8px; border: 1px solid black;\">#passedSpecsCount</td> \n" +
            "              </tr> \n" +
            "              <tr> \n" +
            "                <td style=\"text-align: left; padding: 8px; border: 1px solid black; background-color: #f2f2f2\"><b>Failed Specs Count</b></td> \n" +
            "                <td style=\"text-align: left; padding: 8px; border: 1px solid black; background-color: #f2f2f2\">#failedSpecsCount</td> \n" +
            "              </tr> \n" +
            "              <tr> \n" +
            "                <td style=\"text-align: left; padding: 8px; border: 1px solid black;\"><b>Skipped Specs Count</b></td> \n" +
            "                <td style=\"text-align: left; padding: 8px; border: 1px solid black;\">#skippedSpecsCount</td> \n" +
            "              </tr> \n" +
            "            </table> \n" +
            "            <br><br>";

    public static String appendToTemplate() throws IOException, ParseException {
        String appendHtml = "<style>\n" +
                "       table#regression_table tr:nth-child(odd){background-color: #f2f2f2}\n" +
                "   </style>\n" +
                "            <table id=\"regression_table\" style=\"width:70%; border:1px solid black; border-collapse:collapse;\">\n" +
                "               <col width=\"45%\">\n" +
                "                   <tr>\n" +
                "                       <th colspan=\"5\" style=\"text-align: left; padding: 8px; border: 1px solid black; background-color: #08A7CE; color: white;\">\n" +
                "                           <b>Regression Testing Summary</b></th>\n" +
                "                   </tr>\n" +
                "                   <tr>\n" +
                "                       <th style=\"text-align: left; padding: 8px; border: 1px solid black; background-color: #08A7CE; color: white;\">\n" +
                "                           <b>Module</b></th>\n" +
                "                       <th style=\"text-align: left; padding: 8px; border: 1px solid black; background-color: #08A7CE; color: white;\">\n" +
                "                           <b>Total</b></th>\n" +
                "                       <th style=\"text-align: left; padding: 8px; border: 1px solid black; background-color: #08A7CE; color: white;\">\n" +
                "                           <b>Passed</b></th>\n" +
                "                       <th style=\"text-align: left; padding: 8px; border: 1px solid black; background-color: #08A7CE; color: white;\">\n" +
                "                           <b>Failed</b></th>\n" +
                "                       <th style=\"text-align: left; padding: 8px; border: 1px solid black; background-color: #08A7CE; color: white;\">\n" +
                "                           <b>Skipped</b></th>\n" +
                "                   </tr>";
        int iterator = getSpecHeadingList().size();
        for (int i=0; i < iterator; i++){
            appendHtml = appendHtml.concat("<tr>\n" +
                    "<td style=\"text-align: left; padding: 8px; border: 1px solid black;\"><b>\n" + getSpecHeadingList().get(i) +
                    "   </b></td>\n" +
                    "<td style=\"text-align: left; padding: 8px; border: 1px solid black;\">\n" +
                       String.valueOf(Integer.valueOf(getPassedScenarioCountList().get(i)) + Integer.valueOf(getFailedScenarioCountList().get(i)) +
                               Integer.valueOf(getSkippedScenarioCountList().get(i))) + "</td>\n" +
                    "<td style=\"text-align: left; padding: 8px; border: 1px solid black;\">\n" + String.valueOf(getPassedScenarioCountList().get(i)) +
                    "   </td>\n" +
                    "<td style=\"text-align: left; padding: 8px; border: 1px solid black;\">\n" + String.valueOf(getFailedScenarioCountList().get(i)) +
                    "   </td>\n" +
                    "<td style=\"text-align: left; padding: 8px; border: 1px solid black;\">\n" + String.valueOf(getSkippedScenarioCountList().get(i)) +
                    "   </td>\n" +
                    "</tr>");
        }
        String lastAppend = "</table>\n" +
                "<br><br>\n" +
                "\n" +
                "\n" +
                "<img src=\"cid:bar-chart\" alt=\"Bar Chart For Test Execution Results\" align=\"left\" style=\"border: 1px solid black;\"> \n" +
                "</body>\n" +
                "</html>";
        return appendHtml + lastAppend;
    }

    public static String get() throws IOException, ParseException {
        return template + appendToTemplate();
    }


}
