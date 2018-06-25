/**
 * Project Name : MaxSoft Email Client For Gauge
 * Developer    : Osanda Deshan
 * Version      : 1.0.0
 * Date         : 6/23/2018
 * Time         : 2:56 PM
 * Description  :
 **/

package com.maxsoft.intelliapi.util;

import org.knowm.xchart.BitmapEncoder;
import org.knowm.xchart.PieChartBuilder;
import org.knowm.xchart.style.PieStyler;
import org.knowm.xchart.style.Styler;
import java.awt.*;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.Properties;


public class PieChart {

    public static final String CURRENT_DIRECTORY = System.getProperty("user.dir");

    static Properties pieChartProperties = new Properties();
    static InputStream inputPieChartPropertyFile = null;

    public final static Color DARK_GRAY = new Color(96, 96, 96);
    public final static Color GREEN = new Color(76, 153, 0);
    public final static Color RED = new Color(205, 0, 0);

    static String PIE_CHART_TITLE = "";
    static String PIE_CHART_IMAGE_PATH = "";
    static String PIE_CHART_IMAGE_NAME = "";

    public static void save(String passedCount, String failedCount, String skippedCount)
            throws IOException {

        try {
            inputPieChartPropertyFile = new FileInputStream(CURRENT_DIRECTORY + File.separator + "env" + File.separator + "chart"
                    + File.separator + "piechart.properties");
            // load a properties file
            pieChartProperties.load(inputPieChartPropertyFile);
        } catch (IOException ex) {
            ex.printStackTrace();
        } finally {
            if (inputPieChartPropertyFile != null) {
                try {
                    inputPieChartPropertyFile.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }

        // Get the property values
        PIE_CHART_TITLE = pieChartProperties.getProperty("pie_chart_title");
        PIE_CHART_IMAGE_PATH = pieChartProperties.getProperty("pie_chart_image_path");
        PIE_CHART_IMAGE_NAME = pieChartProperties.getProperty("pie_chart_image_name");

        String pieChartDir = CURRENT_DIRECTORY + File.separator + PIE_CHART_IMAGE_PATH;
        String imageDir = pieChartDir + File.separator + PIE_CHART_IMAGE_NAME;

        // Create PieChart
        org.knowm.xchart.PieChart chart = new PieChartBuilder().width(640).height(480).title(PIE_CHART_TITLE).theme(Styler.ChartTheme.GGPlot2).build();

        // Customize PieChart
        chart.getStyler().setLegendVisible(true);
        chart.getStyler().setLegendLayout(Styler.LegendLayout.Horizontal);
        chart.getStyler().setLegendBorderColor(Color.BLACK);
        chart.getStyler().setLegendPosition(Styler.LegendPosition.OutsideS);
        chart.getStyler().setAnnotationType(PieStyler.AnnotationType.LabelAndPercentage);
        chart.getStyler().setAnnotationDistance(1.15);
        chart.getStyler().setPlotContentSize(.6);
        chart.getStyler().setStartAngleInDegrees(90);
        chart.getStyler().setPlotBorderVisible(true);
        chart.getStyler().setPlotBorderColor(Color.BLACK);
        chart.getStyler().setChartTitleBoxBorderColor(Color.BLACK);

        // Series
        chart.addSeries("Passed", Integer.valueOf(passedCount)).setFillColor(GREEN);
        chart.addSeries("Failed", Integer.valueOf(failedCount)).setFillColor(RED);
        chart.addSeries("Skipped", Integer.valueOf(skippedCount)).setFillColor(DARK_GRAY);

        // Show it
        //new SwingWrapper(chart).displayChart();

        // Save it, if the pi-chart directory is not there create it
        File directory = new File(pieChartDir);
        if (! directory.exists()){
            directory.mkdirs();
        }
        BitmapEncoder.saveBitmap(chart, imageDir, BitmapEncoder.BitmapFormat.PNG);

        // or save it in high-res
        //BitmapEncoder.saveBitmapWithDPI(chart, filePath, BitmapEncoder.BitmapFormat.PNG, 300);
    }

    public static String getSavedPieChartImageName(){
        return PIE_CHART_IMAGE_NAME;
    }

    public static String getSavedPieChartImagePath(){
        return CURRENT_DIRECTORY + File.separator + PIE_CHART_IMAGE_PATH + File.separator + PIE_CHART_IMAGE_NAME + ".PNG";
    }


}