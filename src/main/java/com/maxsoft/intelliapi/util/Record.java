package com.maxsoft.intelliapi.util;

import java.util.ArrayList;


/**
 * Created by Osanda Deshan on 7/30/17.
 */


public class Record implements Comparable<Record>{
	private ArrayList<String> record;
	private int factor = 0;
	
	public Record(ArrayList<String> record) {
		this.record = record;
	}
	
	public String get(int i){
		if(record.size() > i && i >= 0)
			return record.get(i);
		return null;
	}
	
	public String getString(int i){
		return String.valueOf(get(i));
	}
	
	public String toString() {
		String str ="";
		for(int i=0; i<size(); i++){
			str += getString(i) + ",";
		}
		return str.substring(0,str.length()-1);
	}
	
	public int size(){
		return record.size();
	}
	
	// factor is either 1 or next prime beginning with 31
	private int nextFactor(){
		if(factor == 0){
			factor = 1;
		}else if(factor == 1){
			factor = 31;
		}else{
			int m = factor + 2;
			boolean loop = true;
			while(loop){
				for(int i=2; i<=m/i; i++){
					if(m%i == 0){
						m += 2;
						break;
					}
				}
				loop = false;
			}
			factor = m;
		}
		return factor;
	}
	
	@Override
	public boolean equals(final Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		final Record newRecord = (Record) obj;
		if(newRecord.size() != size())
			return false;
		for(int i=0; i<size(); i++) {
			if (!get(i).equals(newRecord.get(i)))
				return false;
		}
		return true;
	}
	
	@Override
	public int hashCode() {
		int hashVal = 0;
		for(int i=0; i<size(); i++){
			hashVal += nextFactor() * getString(i).hashCode();
		}
		return hashVal;
	}
	
	public int compareTo(Record r) {
		int cmp = getString(0).compareTo(r.getString(0));
		for(int i=1; i<size(); i++){
			if(cmp != 0)
				return cmp;
			cmp = getString(i).compareTo(r.getString(i));
		}
		return cmp;
	}
	
	
}
