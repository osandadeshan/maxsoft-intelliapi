package com.maxsoft.intelliapi.util.database.mongo;

/**
 * Project Name : MaxSoft-IntelliAPI
 * Developer    : Osanda Deshan
 * Version      : 1.0.0
 * Date         : 6/30/2018
 * Time         : 3:51 PM
 * Description  :
 **/

import com.mongodb.MongoClient;
import com.mongodb.MongoCredential;
import com.mongodb.ServerAddress;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoDatabase;
import org.bson.Document;
import org.json.JSONException;
import org.json.JSONObject;
import java.util.Arrays;
import static com.mongodb.client.model.Filters.eq;


public class MongoDbDemo {

    private static final String DB_SERVER_HOST = "10.199.253.208";
    private static final int DB_PORT = 27017;

    private static MongoClient mongoClient = null;

    public static void main(String[] args) throws JSONException {
        mongoTest(false);
    }

    public static void mongoTest(boolean isAuthenticated) throws JSONException {

        if (isAuthenticated == Boolean.TRUE) {
            MongoCredential mongoCredential = MongoCredential
                    .createScramSha1Credential("user", "admin","sanjhtrewrer".toCharArray());
            try {
                mongoClient = new MongoClient(new ServerAddress(DB_SERVER_HOST, DB_PORT)
                        ,Arrays.asList(mongoCredential));
            } catch (Exception e) {
                e.printStackTrace();
            }
            Document document = new Document();
            MongoDatabase database = mongoClient.getDatabase("deckservice_qaint");
            MongoCollection<Document> collection = database.getCollection("expert_decks");
            document = collection.find(eq("title", "Expert Deck using only userId and title")).first();
            JSONObject json = new JSONObject(document.toJson()); // Convert text to object
            System.out.println(json.toString(4)); // Print it with specified indentation

        } else {
            try {
                mongoClient = new MongoClient(new ServerAddress(DB_SERVER_HOST, DB_PORT));
            } catch (Exception e) {
                e.printStackTrace();
            }
            Document document = new Document();
            MongoDatabase database = mongoClient.getDatabase("deckservice_qaint");
            MongoCollection<Document> collection = database.getCollection("expert_decks");
            document = collection.find(eq("title", "Expert Deck using only userId and title")).first();
            JSONObject json = new JSONObject(document.toJson()); // Convert text to object
            System.out.println(json.toString(4)); // Print it with specified indentation
        }
    }


}
