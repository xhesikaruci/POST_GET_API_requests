# POST_GET_API_requests
Python automation of sending a POST request to an API, use information from the response to send another GET request and save the response in text file. 

1. Loads data from four text files(pue, temperature, humidity, wind_speed, Wind_Direction) into data.json file and sends POST request to an API
2. Extract information from the response to send another GET request with modified URL from that information.
3. Extracts data from the GET response and saves it text file PUEpredicted.txt

Text files contain data samples of sensor reading from Facebook datacenter in Lulea. 
This is integrated into another project which I will be uploading soon, consisting of a Belief-Rule-Base Expert System that predicts 
PUE parameter(energy efficiency parameter for datacenters).
