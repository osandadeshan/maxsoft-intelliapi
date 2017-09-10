import com.thoughtworks.gauge.Gauge;
import java.io.IOException;


/**
 * Created by Osanda on 8/5/2017.
 */


public abstract class RequestCreator extends BaseClass {
	
	static String apiName = getSavedValueForScenario("API_NAME"); // Fetching Value from the Data Store
	static String request;
	static {
		try {
			request = ReadDataFromApiDoc.getRequestTemplate(apiName);
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	
	protected RequestCreator() throws IOException {
	}
	
	public static String setRequestAttributeValueAs(String attributeValueInJSONTemplate, String attributeValueToBeSet) throws IOException {
		String replaceWithAttributeValue = request.replace(attributeValueInJSONTemplate, attributeValueToBeSet);
		request = replaceWithAttributeValue;
		return request;
	}
	
	public static void getFinalJsonRequestBody(){
		saveValueForScenario("finalJsonRequestBody", request);
		System.out.println("The JSON request body that you are going to use for the API is:\n" + request);
		Gauge.writeMessage("The JSON request body that you are going to use for the API is:\n" + request);
	}
	
	public static void setRequestToDefault() throws IOException {
		request = ReadDataFromApiDoc.getRequestTemplate(getSavedValueForScenario("API_NAME"));
	}
	
	
}
