import com.thoughtworks.gauge.Gauge;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;


/**
 * Created by Osanda on 7/31/2017.
 */


public class Compare {
	
	static ArrayList<Record> mismatchedResultsInSpecFile = new ArrayList<Record>();
	static ArrayList<Record> mismatchedResultsInDb = new ArrayList<Record>();
	
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
				if(!mismatchedResultsInSpecFile.isEmpty() || !mismatchedResultsInDb.isEmpty()) {
                    System.out.println("________________________________________________________________________________________");
                    Gauge.writeMessage("________________________________________________________________________________________");
                    System.out.println("Mismatched results in the specification file:");
                    Gauge.writeMessage("Mismatched results in the specification file:");
                    System.out.println(mismatchedResultsInSpecFile);
                    Gauge.writeMessage(String.valueOf(mismatchedResultsInSpecFile));
                    System.out.println("________________________________________________________________________________________");
                    Gauge.writeMessage("________________________________________________________________________________________");
                    System.out.println("Mismatched results in the database:");
                    Gauge.writeMessage("Mismatched results in the database:");
                    System.out.println(mismatchedResultsInDb);
                    Gauge.writeMessage(String.valueOf(mismatchedResultsInDb));
                }
	}
	
	
}
