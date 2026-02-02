import json
import re

# Drill 1: The "Serializer" (Dictionary to JSON)

user_data={
    "name":"Sania Zafar",
    "topic":"JSON in Python",
    "level":"medium"
}

json_string=json.dumps(user_data)

print("Type of dictionary: ",type(user_data))
print("Type of JSON variable: ",type(json_string))


print("\n")


# Drill 2: The "Deserializer" (JSON to Dictionary)

json_input = '{"course": "Python", "status": "Active", "score": 95}'
python_dictionary=json.loads(json_input)
print(python_dictionary["course"])


print("\n")


# Drill 3: The "Pretty Printer"

new_json_string=json.dumps(user_data, indent=4)
print(new_json_string)


print("\n")


# Drill 4: The "Value Updater"

data_str = '{"user": "Sania", "level": "Medium", "score": 85}'
pd=json.loads(data_str)
pd["score"]=100
pd["level"]="Expert"
js=json.dumps(pd)
print(js)


print("\n")


# Drill 5: The "Grand Task" (The Profile Manager)

raw_text= "Contact the admin at sania@example.com for access."

extract_email_address=re.search(r"[\w\.-]+@[\w\.-]+",raw_text)
print(extract_email_address)
profile={
    "username":"Sania",
    "email":"sania@example.com",
    "status":"Verified"
}

jss=json.dumps(profile, indent=4)
print(jss)
