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

    private static String template = "<!DOCTYPE html>" +
            "            <html>" +
            "            <head>" +
            "            </head>" +
            "            <body>" +
            "            <table style=\"width:70%; border:1px solid black; border-collapse:collapse;\">" +
            "              <col width=45%>" +
            "              <tr>" +
            "                <th colspan=3 style=\"text-align: left; padding: 8px; border: 1px solid black; background-color: #08A7CE; color: white;\"><b>Test Execution Summary</b></th>" +
            "              </tr>" +
            "              <tr>" +
            "                <td style=\"text-align: left; padding: 8px; border: 1px solid black; background-color: #f2f2f2\"><b>Project Name</b></td>" +
            "                <td style=\"text-align: left; padding: 8px; border: 1px solid black; background-color: #f2f2f2\">#projectName</td>" +
            "              </tr>" +
            "              <tr>" +
            "                <td style=\"text-align: left; padding: 8px; border: 1px solid black;\"><b>Timestamp</b></td>" +
            "                <td style=\"text-align: left; padding: 8px; border: 1px solid black;\">#timestamp</td>" +
            "              </tr>" +
            "              <tr>" +
            "                <td style=\"text-align: left; padding: 8px; border: 1px solid black; background-color: #f2f2f2\"><b>Environment</b></td>" +
            "                <td style=\"text-align: left; padding: 8px; border: 1px solid black; background-color: #f2f2f2\">#environment</td>" +
            "              </tr>" +
            "              <tr>" +
            "                <td style=\"text-align: left; padding: 8px; border: 1px solid black;\"><b>Execution Time</b></td>" +
            "                <td style=\"text-align: left; padding: 8px; border: 1px solid black;\">#executionTime</td>" +
            "              </tr>" +
            "              <tr>" +
            "                <td style=\"text-align: left; padding: 8px; border: 1px solid black; background-color: #f2f2f2\"><b>Execution Status</b></td>" +
            "                <td style=\"text-align: left; padding: 8px; border: 1px solid black; background-color: #f2f2f2\">#executionStatus</td>" +
            "              </tr>" +
            "              <tr>" +
            "                <td style=\"text-align: left; padding: 8px; border: 1px solid black;\"><b>Success Rate</b></td>" +
            "                <td style=\"text-align: left; padding: 8px; border: 1px solid black;\">#successRate</td>" +
            "              </tr>" +
            "              <tr>" +
            "                <td style=\"text-align: left; padding: 8px; border: 1px solid black; background-color: #f2f2f2\"><b>Fail Rate</b></td>" +
            "                <td style=\"text-align: left; padding: 8px; border: 1px solid black; background-color: #f2f2f2\">#failRate</td>" +
            "              </tr>" +
            "            </table>" +
            "            <br><br>" +
            "           <table style=\"width:70%; border:1px solid black; border-collapse:collapse;\">" +
            "               <col width=45%>" +
            "               <tr>" +
            "                   <th colspan=3 style=\"text-align: left; padding: 8px; border: 1px solid black; background-color: #08A7CE; color: white;\"><b>Scenario Information</b></th>" +
            "               </tr>" +
            "               <tr>" +
            "                   <th style=\"text-align: left; padding: 8px; border: 1px solid black; background-color: #08A7CE; color: white;\"><b></b></th>" +
            "                   <th style=\"text-align: left; padding: 8px; border: 1px solid black; background-color: #08A7CE; color: white;\"><b>Scenario Count</b></th>" +
            "                   <th style=\"text-align: left; padding: 8px; border: 1px solid black; background-color: #08A7CE; color: white;\"><b>Percentage (%)</b></th>" +
            "               </tr>" +
            "               <tr>" +
            "                   <td style=\"text-align: left; padding: 8px; border: 1px solid black; background-color: #f2f2f2\"><b>Total Scenarios</b></td>" +
            "                   <td style=\"text-align: left; padding: 8px; border: 1px solid black; background-color: #f2f2f2\">#totalScenariosCount</td>" +
            "                   <td style=\"text-align: left; padding: 8px; border: 1px solid black; background-color: #f2f2f2\"></td>" +
            "               </tr>" +
            "               <tr>" +
            "                   <td style=\"text-align: left; padding: 8px; border: 1px solid black;\"><b>Passed Scenarios</b></td>" +
            "                   <td style=\"text-align: left; padding: 8px; border: 1px solid black;\">#passedScenariosCount</td>" +
            "                   <td style=\"text-align: left; padding: 8px; border: 1px solid black;\">#passedScenarioPercentage</td>" +
            "               </tr>" +
            "               <tr>" +
            "                   <td style=\"text-align: left; padding: 8px; border: 1px solid black; background-color: #f2f2f2\"><b>Failed Scenarios</b></td>" +
            "                   <td style=\"text-align: left; padding: 8px; border: 1px solid black; background-color: #f2f2f2\">#failedScenariosCount</td>" +
            "                   <td style=\"text-align: left; padding: 8px; border: 1px solid black; background-color: #f2f2f2\">#failedScenarioPercentage</td>" +
            "               </tr>" +
            "               <tr>" +
            "                   <td style=\"text-align: left; padding: 8px; border: 1px solid black;\"><b>Skipped Scenarios</b></td>" +
            "                   <td style=\"text-align: left; padding: 8px; border: 1px solid black;\">#skippedScenariosCount</td>" +
            "                   <td style=\"text-align: left; padding: 8px; border: 1px solid black;\">#skippedScenarioPercentage</td>" +
            "               </tr>" +
            "           </table>" +
            "            <img src=\"cid:pie-chart\" alt=\"Pie Chart For Test Execution Results\" align=\"left\" style=\"padding-top: 30px; padding-bottom: 35px;\"> <br><br><br>" +
            "            <br><br><br><br>" +
            "            <table style=\"width:70%; border:1px solid black; border-collapse:collapse;\">" +
            "              <col width=45%>" +
            "              <tr>" +
            "                <th colspan=3 style=\"text-align: left; padding: 8px; border: 1px solid black; background-color: #08A7CE; color: white;\"><b>Specification Information</b></th>" +
            "              </tr>" +
            "              <tr>" +
            "                <th style=\"text-align: left; padding: 8px; border: 1px solid black; background-color: #08A7CE; color: white;\"><b></b></th>" +
            "                <th style=\"text-align: left; padding: 8px; border: 1px solid black; background-color: #08A7CE; color: white;\"><b>Specification Count</b></th>" +
            "                <th style=\"text-align: left; padding: 8px; border: 1px solid black; background-color: #08A7CE; color: white;\"><b>Percentage (%)</b></th>" +
            "              </tr>" +
            "              <tr>" +
            "                <td style=\"text-align: left; padding: 8px; border: 1px solid black; background-color: #f2f2f2\"><b>Total Specifications</b></td>" +
            "                <td style=\"text-align: left; padding: 8px; border: 1px solid black; background-color: #f2f2f2\">#totalSpecsCount</td>" +
            "                <td style=\"text-align: left; padding: 8px; border: 1px solid black; background-color: #f2f2f2\"></td>" +
            "              </tr>" +
            "              <tr>" +
            "                <td style=\"text-align: left; padding: 8px; border: 1px solid black;\"><b>Passed Specifications</b></td>" +
            "                <td style=\"text-align: left; padding: 8px; border: 1px solid black;\">#passedSpecsCount</td>" +
            "                <td style=\"text-align: left; padding: 8px; border: 1px solid black;\">#passedSpecsPercentage</td>" +
            "              </tr>" +
            "              <tr>" +
            "                <td style=\"text-align: left; padding: 8px; border: 1px solid black; background-color: #f2f2f2\"><b>Failed Specifications</b></td>" +
            "                <td style=\"text-align: left; padding: 8px; border: 1px solid black; background-color: #f2f2f2\">#failedSpecsCount</td>" +
            "                <td style=\"text-align: left; padding: 8px; border: 1px solid black; background-color: #f2f2f2\">#failedSpecsPercentage</td>" +
            "              </tr>" +
            "              <tr>" +
            "                <td style=\"text-align: left; padding: 8px; border: 1px solid black;\"><b>Skipped Specifications</b></td>" +
            "                <td style=\"text-align: left; padding: 8px; border: 1px solid black;\">#skippedSpecsCount</td>" +
            "                <td style=\"text-align: left; padding: 8px; border: 1px solid black;\">#skippedSpecsPercentage</td>" +
            "              </tr>" +
            "            </table>" +
            "            <br><br>";

    private static String appendToTemplate() throws IOException, ParseException {
        String appendHtml = "<style>" +
                "       table#regression_table tr:nth-child(odd){background-color: #f2f2f2}" +
                "   </style>" +
                "            <table id=\"regression_table\" style=\"width:70%; border:1px solid black; border-collapse:collapse;\">" +
                "               <col width=\"45%\">" +
                "                   <tr>" +
                "                       <th colspan=\"8\" style=\"text-align: left; padding: 8px; border: 1px solid black; background-color: #08A7CE; color: white;\">" +
                "                           <b>Regression Testing Summary</b></th>" +
                "                   </tr>" +
                "                   <tr>" +
                "                       <th style=\"text-align: left; padding: 8px; border: 1px solid black; background-color: #08A7CE; color: white;\">" +
                "                           <b>Specification</b></th>" +
                "                       <th style=\"text-align: left; padding: 8px; border: 1px solid black; background-color: #08A7CE; color: white;\">" +
                "                           <b>Total Scenarios</b></th>" +
                "                       <th style=\"text-align: left; padding: 8px; border: 1px solid black; background-color: #08A7CE; color: white;\">" +
                "                           <b>Passed Scenario Count</b></th>" +
                "                       <th style=\"text-align: left; padding: 8px; border: 1px solid black; background-color: #08A7CE; color: white;\">" +
                "                           <b>Passed Scenario Percentage (%)</b></th>" +
                "                       <th style=\"text-align: left; padding: 8px; border: 1px solid black; background-color: #08A7CE; color: white;\">" +
                "                           <b>Failed Scenario Count</b></th>" +
                "                       <th style=\"text-align: left; padding: 8px; border: 1px solid black; background-color: #08A7CE; color: white;\">" +
                "                           <b>Failed Scenario Percentage (%)</b></th>" +
                "                       <th style=\"text-align: left; padding: 8px; border: 1px solid black; background-color: #08A7CE; color: white;\">" +
                "                           <b>Skipped Scenario Count</b></th>" +
                "                       <th style=\"text-align: left; padding: 8px; border: 1px solid black; background-color: #08A7CE; color: white;\">" +
                "                           <b>Skipped Scenario Percentage (%)</b></th>" +
                "                   </tr>";
        int iterator = getSpecHeadingList().size();
        for (int i=0; i < iterator; i++){
            appendHtml = appendHtml.concat("<tr>" +
                    "<td style=\"text-align: left; padding: 8px; border: 1px solid black;\"><b>" + getSpecHeadingList().get(i) +
                    "   </b></td>" +
                    "<td style=\"text-align: left; padding: 8px; border: 1px solid black;\">" +
                    (Integer.valueOf(getPassedScenarioCountList().get(i)) + Integer.valueOf(getFailedScenarioCountList().get(i)) +
                            Integer.valueOf(getSkippedScenarioCountList().get(i))) + "</td>" +
                    "<td style=\"text-align: left; padding: 8px; border: 1px solid black;\">" + getPassedScenarioCountList().get(i) +
                    "   </td>" +
                    "<td style=\"text-align: left; padding: 8px; border: 1px solid black;\">" + getPassedScenarioPercentageList().get(i) +
                    "   </td>" +
                    "<td style=\"text-align: left; padding: 8px; border: 1px solid black;\">" + getFailedScenarioCountList().get(i) +
                    "   </td>" +
                    "<td style=\"text-align: left; padding: 8px; border: 1px solid black;\">" + getFailedScenarioPercentageList().get(i) +
                    "   </td>" +
                    "<td style=\"text-align: left; padding: 8px; border: 1px solid black;\">" + getSkippedScenarioCountList().get(i) +
                    "   </td>" +
                    "<td style=\"text-align: left; padding: 8px; border: 1px solid black;\">" + getSkippedScenarioPercentageList().get(i) +
                    "   </td>" +
                    "</tr>");
        }
        String lastAppend = "</table>" +
                "<br><br>" +
                "<img src=\"cid:bar-chart\" alt=\"Bar Chart For Test Execution Results\" align=\"left\" style=\"border: 1px solid black;\">" +
                "</body>" +
                "</html>";
        return appendHtml + lastAppend;
    }

    public static String get() throws IOException, ParseException {
        return template + appendToTemplate();
    }


}