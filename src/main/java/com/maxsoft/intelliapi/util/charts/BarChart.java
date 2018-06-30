package com.maxsoft.intelliapi.util.charts;

/**
 * Project Name : MaxSoft-IntelliAPI
 * Developer    : Osanda Deshan
 * Version      : 1.0.0
 * Date         : 6/30/2018
 * Time         : 3:51 PM
 * Description  :
 **/

import java.awt.*;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.Properties;
import org.jfree.chart.ChartFactory;
import org.jfree.chart.ChartPanel;
import org.jfree.chart.ChartUtilities;
import org.jfree.chart.JFreeChart;
import org.jfree.chart.axis.CategoryAxis;
import org.jfree.chart.axis.NumberAxis;
import org.jfree.chart.axis.ValueAxis;
import org.jfree.chart.labels.ItemLabelAnchor;
import org.jfree.chart.labels.ItemLabelPosition;
import org.jfree.chart.labels.StandardCategoryItemLabelGenerator;
import org.jfree.chart.plot.CategoryPlot;
import org.jfree.chart.plot.PlotOrientation;
import org.jfree.chart.renderer.AbstractRenderer;
import org.jfree.chart.title.LegendTitle;
import org.jfree.data.category.DefaultCategoryDataset;
import org.jfree.ui.TextAnchor;
import org.json.simple.parser.ParseException;
import static com.maxsoft.intelliapi.util.reader.JsonReport.*;


public class BarChart {

    public static final String CURRENT_DIRECTORY = System.getProperty("user.dir");

    static Properties barChartProperties = new Properties();
    static InputStream inputBarChartPropertyFile = null;

    public final static Color LIGHT_GRAY = new Color(223, 223, 223);

    public final static Color DARK_GRAY = new Color(96, 96, 96);
    public final static Color GREEN = new Color(76, 153, 0);
    public final static Color RED = new Color(205, 0, 0);

    static String BAR_CHART_TITLE = "";
    static String BAR_CHART_IMAGE_PATH = "";
    static String BAR_CHART_IMAGE_NAME = "";
    static String BAR_CHART_IMAGE_WIDTH = "";

    public static final String Y_AXIS_LABEL = "Specification Name/s";
    public static final String X_AXIS_LABEL = "Count";

    public static final String PASSED = "Passed";
    public static final String FAILED = "Failed";
    public static final String SKIPPED = "Skipped";


    public static void save() throws IOException, ParseException {

        try {
            inputBarChartPropertyFile = new FileInputStream(CURRENT_DIRECTORY + File.separator + "env" + File.separator + "chart"
                    + File.separator + "barchart.properties");
            // load a properties file
            barChartProperties.load(inputBarChartPropertyFile);
        } catch (IOException ex) {
            ex.printStackTrace();
        } finally {
            if (inputBarChartPropertyFile != null) {
                try {
                    inputBarChartPropertyFile.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }

        // Get the property values
        BAR_CHART_TITLE = barChartProperties.getProperty("bar_chart_title");
        BAR_CHART_IMAGE_PATH = barChartProperties.getProperty("bar_chart_image_path");
        BAR_CHART_IMAGE_NAME = barChartProperties.getProperty("bar_chart_image_name");
        BAR_CHART_IMAGE_WIDTH = barChartProperties.getProperty("bar_chart_image_width");

        String barChartDir = CURRENT_DIRECTORY + File.separator + BAR_CHART_IMAGE_PATH;

        final DefaultCategoryDataset dataset = new DefaultCategoryDataset( );

        int iterator = getSpecHeadingList().size();

        for (int i=0; i<iterator; i++){
            dataset.addValue( Integer.valueOf(getPassedScenarioCountList().get(i)) , PASSED , getSpecHeadingList().get(i) );
            dataset.addValue( Integer.valueOf(getFailedScenarioCountList().get(i)) , FAILED , getSpecHeadingList().get(i) );
            dataset.addValue( Integer.valueOf(getSkippedScenarioCountList().get(i)) , SKIPPED , getSpecHeadingList().get(i) );
        }

        JFreeChart barChart = ChartFactory.createBarChart(
                BAR_CHART_TITLE,
                Y_AXIS_LABEL, X_AXIS_LABEL,
                dataset,PlotOrientation.HORIZONTAL,
                true, true, false);

        CategoryPlot plot = barChart.getCategoryPlot();
        plot.getRangeAxis().setStandardTickUnits(NumberAxis.createIntegerTickUnits());

        plot.getRenderer().setSeriesPaint(0, GREEN);
        plot.getRenderer().setSeriesPaint(1, RED);
        plot.getRenderer().setSeriesPaint(2, DARK_GRAY);

        ChartPanel chartPanel = new ChartPanel(barChart, false);

        chartPanel.setBackground( Color.WHITE );
        barChart.getPlot().setBackgroundPaint( LIGHT_GRAY );
        barChart.setBorderVisible(true);
        barChart.setBorderPaint(Color.BLACK);
        ((AbstractRenderer) plot.getRenderer()).setBaseLegendShape(new Rectangle(20,20));
        LegendTitle legend = barChart.getLegend();
        Font labelFont = new Font("SansSerif", Font.TYPE1_FONT, 14);
        legend.setItemFont(labelFont);

        Font categoryAxisFont = new Font("SansSerif", Font.TYPE1_FONT, 14);
        CategoryAxis categoryAxis = plot.getDomainAxis();
        categoryAxis.setTickLabelFont(categoryAxisFont);
        categoryAxis.setLabelFont(new Font("Dialog", Font.TRUETYPE_FONT, 14));

        Font rangeAxisFont = new Font("SansSerif", Font.TYPE1_FONT, 16);
        ValueAxis rangeAxis = plot.getRangeAxis();
        rangeAxis.setTickLabelFont(rangeAxisFont);
        rangeAxis.setLabelFont(new Font("Dialog", Font.TRUETYPE_FONT, 14));

        // Value on the bars
        plot.getRenderer().setBaseItemLabelGenerator(new StandardCategoryItemLabelGenerator());
        plot.getRenderer().setBaseItemLabelsVisible(true);
        plot.getRenderer().setItemLabelFont(new Font("Dialog",Font.BOLD,12));
        ItemLabelPosition position = new ItemLabelPosition(ItemLabelAnchor.INSIDE12,
                TextAnchor.TOP_CENTER);
        plot.getRenderer().setBasePositiveItemLabelPosition(position);

        int width = Integer.valueOf(BAR_CHART_IMAGE_WIDTH);
        int height = setBarChartHeight(iterator);

        // Save it, if the pi-chart directory is not there create it
        File directory = new File(barChartDir);
        if (! directory.exists()){
            directory.mkdirs();
        }

        File BarChart = new File( getSavedBarChartImagePath() );
        ChartUtilities.saveChartAsPNG( BarChart , barChart , width , height );
    }

    public static int setBarChartHeight(int noOfSpecs){
        try {
            inputBarChartPropertyFile = new FileInputStream(CURRENT_DIRECTORY + File.separator + "env" + File.separator + "chart"
                    + File.separator + "barchart.properties");
            // load a properties file
            barChartProperties.load(inputBarChartPropertyFile);
        } catch (IOException ex) {
            ex.printStackTrace();
        } finally {
            if (inputBarChartPropertyFile != null) {
                try {
                    inputBarChartPropertyFile.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }

        return noOfSpecs * Integer.valueOf(barChartProperties.getProperty("bar_chart_height_for_one_spec"));
    }


    public static String getSavedBarChartImageName(){
        return BAR_CHART_IMAGE_NAME;
    }

    public static String getSavedBarChartImagePath(){
        return CURRENT_DIRECTORY + File.separator + BAR_CHART_IMAGE_PATH + File.separator + BAR_CHART_IMAGE_NAME + ".PNG";
    }


}