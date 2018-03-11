package com.maxsoft.ata.util;

import com.mongodb.MongoClient;
import com.mongodb.DB;
import com.mongodb.DBCollection;
import com.mongodb.BasicDBObject;
import com.mongodb.DBCursor;
import org.testng.Assert;


public class MongoDBAutomation{

    public static void main( String args[] ){
        try{

            //Connecting to the mongoDB instance
            MongoClient mongoClient = new MongoClient( "10.199.240.67" , 27017 );

            //Selecting the database
            DB db = mongoClient.getDB("flashcardservice");

            //Selecting the collection
            DBCollection dbCollection = db.getCollection("questions");

            //Setting search query with the required key-value pair
            BasicDBObject searchQuery = new BasicDBObject();
            searchQuery.put("key", "value");

            //DBCursor with the find query result
            DBCursor cursor = dbCollection.find(searchQuery);

            //Fetching the response
            String response = null;
            try {
                while(cursor.hasNext()) {
                    response = response.concat(cursor.next().toString());
                }
            }
            finally {
                cursor.close();
            }

            //Asserting the fetched response with expected value
            Assert.assertTrue(response.contains("ExpectedValue"));
        }
        catch(Exception e){
            System.out.println(e.getMessage());
        }
    }
}