import requests
import json
import csv

# 1. Export a list/segment (only select Klaviyo ID) and download CSV


# 2. Add/change values of these editable fields

private_api = " "
unsettable_props = "[\"$first_name\", \"$last_name\"]"

filename = "List Export 2022-08-15"
folder_path = "/Users/brandon.park/Desktop/"


#. 3. Make a PUT request to unset properties for each profile ID that gets returned from looping through the rows in CSV

url = "https://a.klaviyo.com/api/v1/person/"
 
headers = { 
  "content-type": "application/json",
  "cache-control": "no-cache",
  }

querystring = {
  "$unset": unsettable_props, 
  "api_key": private_api
  }

with open(folder_path+filename+".csv", "r") as f:
    reader = csv.reader(f)
    count = 0
    for row in reader:
        if row[0] == "Klaviyo ID":
            continue
        response = requests.request("PUT", url+row[0], headers=headers, params=querystring)
        count += 1
        print(response.text)
        print(count)