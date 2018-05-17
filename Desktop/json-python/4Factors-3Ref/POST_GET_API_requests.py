import requests
import json


t=open('temperature','r')  #open temperature.txt file with temperature data
x=t.readlines()	#read the file line by line and save them in list x
#print(x[8])

d=open('humidity','r')	 #open temperature.txt file with humidity data
y=d.readlines()		#read the file line by line and save them in list y
#print(y[8])

windspeed=open('wind_speed','r')	 #open temperature.txt file with humidity data
wind_speed=windspeed.readlines()		#read the file line by line and save them in list y
#print(wind_speed[8])

windir=open('WindDirDegrees','r')	 #open temperature.txt file with humidity data
wind_dir=windir.readlines()		#read the file line by line and save them in list y
#print(wind_dir[8])
for i in range(0,273):		
    with open('data.json', 'r+') as f:
       data = json.load(f)

       data['x2']['input_val']= x[i] # <--- add `id` value.
       print(data['x2']['input_val'])		#replace temp and humid input_val of data.json file with the x,y lists of temp and humid data
       data['x3']['input_val']=y[i]
       print(data['x3']['input_val'])

       data['x4']['input_val']=wind_speed[i]
       print(data['x4']['input_val'])

       data['x5']['input_val']=wind_dir[i]
       print(data['x5']['input_val'])



       f.seek(0)        # <--- should reset file position to the begincd ning.
       json.dump(data, f, indent=4)
       f.truncate() 


       url='http://130.240.134.31:8080/api/v1/initiate_brb/' #URL of the API you need to access
       headers = {'content-type': 'application/json'}
       response = requests.post(url, data=open('data.json','rb'), headers=headers)   #send the POST request
       print(response.text)
       print(response.json()["access_key"])



    URL = "http://130.240.134.31:8080/api/v1/" + str(response.json()["access_key"]) +"/get_aggregated_rule"   #attach the access_key from the POST response to the url of GET request
    r=requests.get(url=URL)
    response =r.json()
    temp = response[1]
    print(response[1])
    with open("PUE_Predic_3.txt", "a") as outfile:
         json.dump(response[1], outfile, sort_keys = True, indent = 0, ensure_ascii = False)  #write the output in file PUE_Predic which is created if it doesnt exist.
         outfile.write("\n")
i=i+1

