# Unsetting profile properties in Klaviyo
You can use this Python script to unset the values of default profile properties and removing custom profile properties in Klaviyo. 

## What does unsetting do?

Unsetting a profile property removes both the key and value from the profiles that you run this script for. Only exception is Klaviyo's default properties (ones with a `$` prefix). When unsetting a Klaviyo property, only the values are unset. Further, not all Klaviyo properties are unsettable (i.e. `$longitude` and `$latitude`).

**Please note, this does not work on event properties.**

## Option 1 - Without Downloading a CSV File (Slower)

You will want to replace the values of `list_id` and `private_api`:

```
# 1. Add/change values of these editable fields

list_id = " "
private_api = " "
unsettable_props = "[\"$first_name\", \"$last_name\"]"
```

Then, in `unsettable_props`, replace `$first_name` and/or `$last_name` (unless you specifically want to unset those) with the names of the profile properties you want to unset.

Save the file, then `cd` into the file's location and then execute the script with the `python unset.py` command.

## Oprion 2 - With a CSV File (Faster)

Replace the value of `private_api` and then replace `$first_name` and/or `$last_name` (unless you specifically want to unset those) in `unsettable_props` with the names of the profile properties you actually want to unset.

```
# 2. Add/change values of these editable fields

private_api = " "
unsettable_props = "[\"$first_name\", \"$last_name\"]"

filename = "List Export 2022-08-15"
folder_path = "/Users/brandon.park/Desktop/"
```

CSV exports are always formatted as "List Export YYYY-MM-DD", change the date in `filename` accordingly. 

Change `folder_path` depending on where the CSV file is located.

Save the file, then `cd` into the file's location and then execute the script with the `python csv_unset.py` command.