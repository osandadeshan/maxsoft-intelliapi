package com.maxsoft.intelliapi.util.comparison;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

import static com.maxsoft.intelliapi.util.LogUtil.printInfo;

/**
 * Project Name : MaxSoft-IntelliAPI
 * Developer    : Osanda Deshan
 * Version      : 1.0.0
 * Date         : 6/30/2018
 * Time         : 3:51 PM
 * Description  :
 **/

public class RecordsChecker {

    static final ArrayList<Record> mismatchedResultsInSpecFile = new ArrayList<>();
    static final ArrayList<Record> mismatchedResultsInDb = new ArrayList<>();

    public static boolean compare(List list1, List list2) {
        return list1.toString().contentEquals(list2.toString());
    }

    public static void compare(ArrayList<Record> recordListForSpec, ArrayList<Record> recordListForDb) {
        Collections.sort(recordListForSpec);
        Collections.sort(recordListForDb);
		boolean loop = true;
        int i = 0, j = 0;

        while (loop) {
            Record recordT1 = recordListForSpec.get(i);
            Record recordT2 = recordListForDb.get(j);
            if (!recordT1.equals(recordT2)) {
                if (recordT1.compareTo(recordT2) < 0) {
                    mismatchedResultsInSpecFile.add(recordT1);
                    i += 1;
                } else {
                    mismatchedResultsInDb.add(recordT2);
                    j += 1;
                }
            } else {
                i += 1;
                j += 1;
            }
            if (i >= recordListForSpec.size()) {
                for (int k = j; k < recordListForDb.size(); k++) {
                    mismatchedResultsInDb.add(recordListForDb.get(k));
                }
                loop = false;
            }
            if (j >= recordListForDb.size()) {
                for (int k = i; k < recordListForSpec.size(); k++) {
                    mismatchedResultsInSpecFile.add(recordListForSpec.get(k));
                }
                loop = false;
            }
        }
        printInfo("\n");
        printInfo("Mismatched results in the specification file:");
        printInfo(String.valueOf(mismatchedResultsInSpecFile));
        printInfo("\n");
        printInfo("Mismatched results in the database:");
        printInfo(String.valueOf(mismatchedResultsInDb));
    }
}
