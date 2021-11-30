# Unsetting profile properties in Klaviyo
You can use this Python script to unset the values of default profile properties and removing custom profile properties in Klaviyo. 

## How

You will want to replace the values of LIST_ID and PRIVATE_API:
	
	# fill in the blank with your list/segment id
	LIST_ID = " "

	# fill in the blank with your private api
	PRIVATE_API = " "

Then, replace the values of the `$unset` attribute in the `profiles_querystring` object with the names of the properties that you actually want to unset:

	# replace $first_name/$last_name or add any properties you want unset
	profiles_querystring = {
	  "$unset": "[\"$first_name\", \"$last_name\"]", 
	  "api_key": PRIVATE_API
	  }

Make sure you have the requests library installed before running the script. 