package com.maxsoft.intelliapi.executionhooks;

import com.thoughtworks.gauge.*;
import org.apache.log4j.Logger;

/**
 * Project Name : MaxSoft-IntelliAPI
 * Developer    : Osanda Deshan
 * Version      : 1.0.0
 * Date         : 14/05/2019
 * Time         : 09:50
 * Description  :
 **/


public class ExecutionContextHook {

    private final static Logger logger = Logger.getLogger(ExecutionContextHook.class.getName());

    public static void printInfo(String text){
        logger.info(text +"\n");
    }

    @BeforeSpec
    public void logSpecInfo(ExecutionContext context) {
        String specName = context.getCurrentSpecification().getName();
        printInfo("#########################################################################################################################################################################################");
        printInfo("Running Specification: " + specName);
        printInfo("#########################################################################################################################################################################################");
    }

    @BeforeScenario
    public void logScenarioInfo(ExecutionContext context) {
        String scenarioName = context.getCurrentScenario().getName();
        printInfo("_________________________________________________________________________________________________________________________________________________________________________________________");
        printInfo("Running Scenario: " + scenarioName);
        printInfo("_________________________________________________________________________________________________________________________________________________________________________________________");
    }

    @BeforeStep
    public void logStepInfo(ExecutionContext context) {
        String stepName = context.getCurrentStep().getText();
        printInfo("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------");
        printInfo("Running Step: " + stepName);
        printInfo("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------");
    }

    @AfterSpec
    public void closeSpecInfo(ExecutionContext context) {
        String specName = context.getCurrentSpecification().getName();
        printInfo("Finished Execution of Specification: " + specName);
        printInfo("#########################################################################################################################################################################################" + "\n\n\n");
    }

    @AfterScenario
    public void closeScenarioInfo(ExecutionContext context) {
        String scenarioName = context.getCurrentScenario().getName();
        printInfo("Finished Execution of Scenario: " + scenarioName);
        printInfo("_________________________________________________________________________________________________________________________________________________________________________________________" + "\n\n");
    }

    @AfterStep
    public void closeStepInfo(ExecutionContext context) {
        String stepName = context.getCurrentStep().getText();
        printInfo("Finished Execution of Step: " + stepName);
        printInfo("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------" + "\n");
    }


}