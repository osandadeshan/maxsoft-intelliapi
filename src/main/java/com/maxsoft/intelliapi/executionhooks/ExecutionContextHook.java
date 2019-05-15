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
        logger.info(text);
    }

    @BeforeSpec
    public void logSpecInfo(ExecutionContext context) {
        String specName = context.getCurrentSpecification().getName();
        printInfo("Running Specification: " + specName + "\n\n\n\n");
    }

    @BeforeScenario
    public void logScenarioInfo(ExecutionContext context) {
        String scenarioName = context.getCurrentScenario().getName();
        printInfo("Running Scenario: " + scenarioName + "\n\n\n");
    }

    @BeforeStep
    public void logStepInfo(ExecutionContext context) {
        String stepName = context.getCurrentStep().getText();
        printInfo("Running Step: " + stepName + "\n");
    }

    @AfterSpec
    public void closeSpecInfo(ExecutionContext context) {
        String specName = context.getCurrentSpecification().getName();
        printInfo("Finished Execution of Specification: " + specName + "\n\n\n\n\n\n");
    }

    @AfterScenario
    public void closeScenarioInfo(ExecutionContext context) {
        String scenarioName = context.getCurrentScenario().getName();
        printInfo("Finished Execution of Scenario: " + scenarioName + "\n\n\n\n");
    }

    @AfterStep
    public void closeStepInfo(ExecutionContext context) {
        String stepName = context.getCurrentStep().getText();
        printInfo("\n");
        printInfo("Finished Execution of Step: " + stepName + "\n\n\n");
    }


}