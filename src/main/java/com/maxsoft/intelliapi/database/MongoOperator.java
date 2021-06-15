package com.maxsoft.intelliapi.database;

import com.mongodb.MongoClient;
import com.mongodb.MongoCredential;
import com.mongodb.ServerAddress;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoDatabase;
import org.bson.Document;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.Collections;

import static com.maxsoft.intelliapi.Constants.*;
import static com.maxsoft.intelliapi.util.DataStoreProcessor.saveValueForScenario;
import static com.maxsoft.intelliapi.util.LogUtil.printInfo;
import static com.mongodb.client.model.Filters.eq;

/**
 * Project Name : MaxSoft-IntelliAPI
 * Developer    : Osanda Deshan
 * Version      : 1.0.0
 * Date         : 6/30/2018
 * Time         : 3:51 PM
 * Description  :
 **/

public class MongoOperator {

    private static MongoClient mongoClient = null;

    public static void executeQuery(boolean isAuthenticated, String userName, String source, String password,
                                    String databaseName, String collectionName, String key, String value) {
        try {
            if (isAuthenticated) {
                MongoCredential mongoCredential = MongoCredential
                        .createScramSha1Credential(userName, source, password.toCharArray());
                try {
                    mongoClient = new MongoClient(new ServerAddress(MONGO_DB_SERVER_HOST, MONGO_DB_PORT)
                            , Collections.singletonList(mongoCredential));
                } catch (Exception e) {
                    e.printStackTrace();
                }

            } else {
                try {
                    mongoClient = new MongoClient(new ServerAddress(MONGO_DB_SERVER_HOST, MONGO_DB_PORT));
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
            Document document;
            MongoDatabase database = mongoClient.getDatabase(databaseName);
            MongoCollection<Document> mongoCollection = database.getCollection(collectionName);
            document = mongoCollection.find(eq(key, value)).first();
            JSONObject json = new JSONObject(document.toJson());
            printInfo("Results for the given query is:\n" + json.toString(4), MongoOperator.class);
            saveValueForScenario(VAR_API_RESPONSE_BODY, json.toString());
        } catch (JSONException e) {
            e.printStackTrace();
        }
    }
}
