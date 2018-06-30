package com.maxsoft.intelliapi.api;

/**
 * Project Name : MaxSoft-IntelliAPI
 * Developer    : Osanda Deshan
 * Version      : 1.0.0
 * Date         : 6/30/2018
 * Time         : 3:51 PM
 * Description  :
 **/

import com.maxsoft.intelliapi.util.reader.ApiDocument;
import java.io.IOException;


public abstract class Endpoints extends Base {

	public static String getApiEndpointByName(String apiEndpointName) throws IOException {
		return ApiDocument.getAPIEndpoint(apiEndpointName);
	}


}
