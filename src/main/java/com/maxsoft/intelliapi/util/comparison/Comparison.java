package com.maxsoft.intelliapi.util.comparison;

/**
 * Project Name : MaxSoft-IntelliAPI
 * Developer    : Osanda Deshan
 * Version      : 1.0.0
 * Date         : 6/30/2018
 * Time         : 3:51 PM
 * Description  :
 **/

import com.thoughtworks.gauge.Gauge;
import org.apache.log4j.Logger;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;


public class Comparison {

	static ArrayList<Record> mismatchedResultsInSpecFile = new ArrayList<Record>();
	static ArrayList<Record> mismatchedResultsInDb = new ArrayList<Record>();

	private final static Logger logger = Logger.getLogger(Comparison.class.getName());

	public static void printInfo(String text){
		logger.info(text +"\n");
		Gauge.writeMessage(text);
	}

	public static boolean compareLists(List list1, List list2){
		return list1.toString().contentEquals(list2.toString())?true:false;
	}

	public static void compareRecords(ArrayList<Record> recordListForSpec, ArrayList<Record> recordListForDb){
		Collections.sort(recordListForSpec);
		Collections.sort(recordListForDb);
		boolean loop = true;
		int i=0, j=0;

		while(loop){
			Record recordT1 = recordListForSpec.get(i);
			Record recordT2 = recordListForDb.get(j);
			if(!recordT1.equals(recordT2)){
				if(recordT1.compareTo(recordT2) < 0){
					mismatchedResultsInSpecFile.add(recordT1);
					i += 1;
				}else{
					mismatchedResultsInDb.add(recordT2);
					j += 1;
				}
			}else{
				i += 1;
				j += 1;
			}
			if(i >= recordListForSpec.size()){
				for(int k = j; k< recordListForDb.size(); k++){
					mismatchedResultsInDb.add(recordListForDb.get(k));
				}
				loop = false;
			}
			if(j >= recordListForDb.size()){
				for(int k = i; k< recordListForSpec.size(); k++){
					mismatchedResultsInSpecFile.add(recordListForSpec.get(k));
				}
				loop = false;
			}
		}
		printInfo("\nMismatched results in the specification file:");
		printInfo(String.valueOf(mismatchedResultsInSpecFile));
		printInfo("\nMismatched results in the database:");
		printInfo(String.valueOf(mismatchedResultsInDb));
	}


}
