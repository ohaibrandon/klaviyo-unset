import requests
import json

# 1. Add/change values of these editable fields

list_id = " "
private_api = " "
unsettable_props = "[\"$first_name\", \"$last_name\"]"


# 2. Make a GET request to fetch all profile objects

list_url = "https://a.klaviyo.com/api/v2/group/"+list_id+"/members/all"

list_querystring = {
  "api_key": private_api
  }

headers = { 
  "content-type": "application/json",
  "cache-control": "no-cache",
  }

response = requests.request("GET", list_url, headers=headers, params=list_querystring).json()


# 3. Loop through the profile objects to append each profile ID into an empty array

profiles_arr = []

for record in response["records"]:
  profiles_arr.append(record["id"])


# 4. Iterate through the array of profile IDs to make a PUT request to unset properties

profiles_url = "https://a.klaviyo.com/api/v1/person/"

profiles_querystring = {
  "$unset": unsettable_props, 
  "api_key": private_api
  }
 
count = 0

for profileid in range(len(profiles_arr)):
    response = requests.request("PUT", profiles_url+profiles_arr[profileid], headers=headers, params=profiles_querystring)
    count += 1
    
    print(response.text)
    print(count)