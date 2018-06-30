package com.maxsoft.intelliapi.database.mongo;

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


public class MongoConnector {

    private static final String DB_SERVER_HOST = System.getenv("mongo_database_host");
    private static final int DB_PORT = Integer.valueOf(System.getenv("mongo_database_port"));

    private static MongoClient mongoClient = null;

    public static void executeQuery(boolean isAuthenticated, String userName, String source, String password,
                                 String databaseName, String collectionName, String key, String value) throws JSONException {

        if (isAuthenticated == Boolean.TRUE) {
            MongoCredential mongoCredential = MongoCredential
                    .createScramSha1Credential(userName, source, password.toCharArray());
            try {
                mongoClient = new MongoClient(new ServerAddress(DB_SERVER_HOST, DB_PORT)
                        ,Arrays.asList(mongoCredential));
            } catch (Exception e) {
                e.printStackTrace();
            }

        } else {
            try {
                mongoClient = new MongoClient(new ServerAddress(DB_SERVER_HOST, DB_PORT));
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
        Document document = new Document();
        MongoDatabase database = mongoClient.getDatabase(databaseName);
        MongoCollection<Document> mongoCollection = database.getCollection(collectionName);
        document = mongoCollection.find(eq(key, value)).first();
        JSONObject json = new JSONObject(document.toJson()); // Convert text to object
        System.out.println(json.toString(4)); // Print it with specified indentation

    }


}
