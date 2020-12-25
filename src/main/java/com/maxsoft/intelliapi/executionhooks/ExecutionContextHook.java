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

    @BeforeSpec
    public void beforeSpec(ExecutionContext context) {
        logger.info("Running Specification: " + context.getCurrentSpecification().getName() + "\n\n\n\n");
    }

    @BeforeScenario
    public void beforeScenario(ExecutionContext context) {
        logger.info("Running Scenario: " + context.getCurrentScenario().getName() + "\n\n\n");
    }

    @BeforeStep
    public void beforeStep(ExecutionContext context) {
        logger.info("Running Step: " + context.getCurrentStep().getText() + "\n");
    }

    @AfterStep
    public void afterStep(ExecutionContext context) {
        logger.info("\n");
        logger.info("Finished Execution of Step: " + context.getCurrentStep().getText() + "\n\n\n");
    }

    @AfterScenario
    public void afterScenario(ExecutionContext context) {
        logger.info("Finished Execution of Scenario: " + context.getCurrentScenario().getName() + "\n\n\n\n");
    }

    @AfterSpec
    public void afterSpec(ExecutionContext context) {
        logger.info("Finished Execution of Specification: " + context.getCurrentSpecification().getName() + "\n\n\n\n\n\n");
    }
}
