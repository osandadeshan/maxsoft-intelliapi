package com.maxsoft.ata.util;

import com.mongodb.*;
import org.testng.Assert;

public class MongoDBConnector {

    MongoClient mongoClient;
    DB db;
    DBCursor cursor;
    DBCollection dbCollection;
    String response;

    public void loadMongoInstance(String host, int port){
        try {
            //Connecting to the mongoDB instance
            mongoClient = new MongoClient(host, port);
        } catch (Exception ex) {
            System.out.println(ex.getMessage());
        }
    }

    public void connectDatabase(String databaseName) {
        try {
            //Selecting the database
            DB db = mongoClient.getDB(databaseName);
        } catch (Exception ex) {
            System.out.println(ex.getMessage());
        }
    }

    public void selectCollection(String collectionName) {
        try {
            //Selecting the collection
            dbCollection = db.getCollection(collectionName);
        } catch (Exception ex) {
            System.out.println(ex.getMessage());
        }
    }

    public void setSearchQuery(String key, String value) {
        try {
            //Setting search query with the required key-value pair
            BasicDBObject searchQuery = new BasicDBObject();
            searchQuery.put(key, value);
            //DBCursor with the find query result
            cursor = dbCollection.find(searchQuery);
        } catch (Exception ex) {
            System.out.println(ex.getMessage());
        }
    }

    public void getQueryResults() {
        //Fetching the response
        response = null;
        try {
            while(cursor.hasNext()) {
                response = response.concat(cursor.next().toString());
            }
        }
        finally {
            cursor.close();
        }
    }

    public void assertQueryResults(String expectedValue){
        //Asserting the fetched response with expected value
        Assert.assertTrue(response.contains(expectedValue));
    }


    public static void main(String[] args) {
        MongoDBConnector mongoDBConnector = new MongoDBConnector();

        mongoDBConnector.loadMongoInstance("10.199.240.67", 27017);
        mongoDBConnector.connectDatabase("flashcardservice");
        mongoDBConnector.selectCollection("questions");
        mongoDBConnector.setSearchQuery("", "");
        mongoDBConnector.getQueryResults();
        mongoDBConnector.assertQueryResults("");
    }


}
