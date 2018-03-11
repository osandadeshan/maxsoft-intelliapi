package com.maxsoft.ata.request;

import com.maxsoft.ata.util.ApiDocumentReader;
import java.io.IOException;


/**
 * Created by Osanda on 7/17/2017.
 */


public abstract class ApiEndpoints extends BaseClass{
	
	public static String getApiEndpointByName(String apiEndpointName) throws IOException {
		return ApiDocumentReader.getAPIEndpoint(apiEndpointName);
	}
	
	
}
