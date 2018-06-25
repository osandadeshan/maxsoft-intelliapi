/**
 * Project Name : MaxSoft Email Client For Gauge
 * Developer    : Osanda Deshan
 * Version      : 1.0.0
 * Date         : 6/23/2018
 * Time         : 2:56 PM
 * Description  :
 **/

package com.maxsoft.intelliapi.util;

import org.json.simple.parser.ParseException;
import java.io.IOException;
import static com.maxsoft.intelliapi.util.JsonReportReader.*;


public class EmailTemplate {

    static String template = "<!DOCTYPE html>\n" +
            "<html>\n" +
            "<head>\n" +
            "<style>\n" +
            "table {\n" +
            "    border-collapse: collapse;\n" +
            "    width: 70%;\n" +
            "    border: 1px solid black;\n" +
            "}\n" +
            "\n" +
            "th, td {\n" +
            "    text-align: left;\n" +
            "    padding: 8px;\n" +
            "    border: 1px solid black;\n" +
            "}\n" +
            "\n" +
            "tr:nth-child(even){background-color: #f2f2f2}\n" +
            "\n" +
            "th {\n" +
            "    background-color: #08A7CE;\n" +
            "    color: white;\n" +
            "}\n" +
            "</style>\n" +
            "</head>\n" +
            "<body>\n" +
            "\n" +
            "<table>\n" +
            "  <col width=\"45%\">\n" +
            "  <tr>\n" +
            "    <th colspan=\"3\"><b>Test Execution Summary</b></th>\n" +
            "  </tr>\n" +
            "  <tr>\n" +
            "    <td><b>Project Name</b></td>\n" +
            "    <td>#projectName</td>\n" +
            "  </tr>\n" +
            "  <tr>\n" +
            "    <td><b>Timestamp</b></td>\n" +
            "    <td>#timestamp</td>\n" +
            "  </tr>\n" +
            "  <tr>\n" +
            "    <td><b>Environment</b></td>\n" +
            "    <td>#environment</td>\n" +
            "  </tr>\n" +
            "  <tr>\n" +
            "    <td><b>Execution Time</b></td>\n" +
            "    <td>#executionTime</td>\n" +
            "  </tr>\n" +
            "  <tr>\n" +
            "    <td><b>Execution Status</b></td>\n" +
            "    <td>#executionStatus</td>\n" +
            "  </tr>\n" +
            "  <tr>\n" +
            "    <td><b>Success Rate</b></td>\n" +
            "    <td>#successRate</td>\n" +
            "  </tr>\n" +
            "  <tr>\n" +
            "    <td><b>Fail Rate</b></td>\n" +
            "    <td>#failRate</td>\n" +
            "  </tr>\n" +
            "</table>\n" +
            "\n" +
            "<br><br>\n" +
            "<table>\n" +
            "  <col width=\"45%\">\n" +
            "  <tr>\n" +
            "    <th colspan=\"3\"><b>Scenario Information</b></th>\n" +
            "  </tr>\n" +
            "  <tr>\n" +
            "    <td><b>Total Scenarios Count</b></td>\n" +
            "    <td>#totalScenariosCount</td>\n" +
            "  </tr>\n" +
            "  <tr>\n" +
            "    <td><b>Passed Scenarios Count</b></td>\n" +
            "    <td>#passedScenariosCount</td>\n" +
            "  </tr>\n" +
            "  <tr>\n" +
            "    <td><b>Failed Scenarios Count</b></td>\n" +
            "    <td>#failedScenariosCount</td>\n" +
            "  </tr>\n" +
            "  <tr>\n" +
            "    <td><b>Skipped Scenarios Count</b></td>\n" +
            "    <td>#skippedScenariosCount</td>\n" +
            "  </tr>\n" +
            "</table>\n" +
            "<br><br>\n" +
            "\n" +
            "<img src=\"cid:pie-chart\" alt=\"Pie Chart For Test Execution Results\" align=\"left\"> <br><br><br>\n" +
            "\n" +
            "<br><br><br><br>\n" +
            "<table>\n" +
            "  <col width=\"45%\">\n" +
            "  <tr>\n" +
            "    <th colspan=\"3\"><b>Specification Information</b></th>\n" +
            "  </tr>\n" +
            "  <tr>\n" +
            "    <td><b>Total Specs Count</b></td>\n" +
            "    <td>#totalSpecsCount</td>\n" +
            "  </tr>\n" +
            "  <tr>\n" +
            "    <td><b>Passed Specs Count</b></td>\n" +
            "    <td>#passedSpecsCount</td>\n" +
            "  </tr>\n" +
            "  <tr>\n" +
            "    <td><b>Failed Specs Count</b></td>\n" +
            "    <td>#failedSpecsCount</td>\n" +
            "  </tr>\n" +
            "  <tr>\n" +
            "    <td><b>Skipped Specs Count</b></td>\n" +
            "    <td>#skippedSpecsCount</td>\n" +
            "  </tr>\n" +
            "</table>\n" +
            "<br><br>\n";

    public static String appendToTemplate() throws IOException, ParseException {
        String appendHtml = "<table>\n" +
                "  <col width=\"45%\">\n" +
                "  <tr>\n" +
                "    <th colspan=\"5\"><b>Regression Testing Summary</b></th>\n" +
                "  </tr>\n" +
                "  <tr>\n" +
                "    <th><b>Module</b></th>\n" +
                "    <th><b>Total</b></th>\n" +
                "    <th><b>Passed</b></th>\n" +
                "    <th><b>Failed</b></th>\n" +
                "    <th><b>Skipped</b></th>\n" +
                "  </tr>";
        int iterator = getSpecHeadingList().size();
        for (int i=0; i < iterator; i++){
            appendHtml = appendHtml + "<tr>\n" +
                    "    <td><b>" + getSpecHeadingList().get(i) + "</b></td>\n" +
                    "    <td>" + (Integer.valueOf(getPassedScenarioCountList().get(i)) + Integer.valueOf(getFailedScenarioCountList().get(i)) +
                    Integer.valueOf(getSkippedScenarioCountList().get(i))) +"</td>\n" +
                    "    <td>" + getPassedScenarioCountList().get(i) + "</td>\n" +
                    "    <td>" + getFailedScenarioCountList().get(i) + "</td>\n" +
                    "    <td>" + getSkippedScenarioCountList().get(i) + "</td>\n" +
                    "  </tr>";
        }
        String lastAppend = "</table>\n" +
                "<br><br>\n" +
                "\n" +
                "\n" +
                "<img src=\"cid:bar-chart\" alt=\"Bar Chart For Test Execution Results\" align=\"left\"> \n" +
                "</body>\n" +
                "</html>";
        return appendHtml + lastAppend;
    }

    public static String get() throws IOException, ParseException {
        return template + appendToTemplate();
    }


}
