'''JSON stands for JavaScript Object Notation.
Data is stored as key-value pairs.
Keys and string values must be enclosed in double quotes (").
JSON supports nested objects and arrays.'''

import json

# Python dictionary
student = {
    "name": "John",
    "age": 20,
    "course": "BIT",
    "city": "Pokhara"
}

# Convert dictionary to JSON string
json_string = json.dumps(student, indent=4)
print("JSON String:")
print(json_string)

# Write dictionary to a JSON file
with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

print("\nData has been written to student.json")

# Read data from the JSON file
with open("student.json", "r") as file:
    data = json.load(file)

print("\nData read from JSON file:")
print(data)

# Access specific values
print("\nStudent Name:", data["name"])
print("Course:", data["course"])
print("City:", data["city"])

import requests

# API URL
url = "https://official-joke-api.appspot.com/random_joke"

# Send GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:

    # Convert JSON response to Python dictionary
    data = response.json()

    # Print the joke
    print("Setup     :", data["setup"])
    print("Punchline :", data["punchline"])

else:
    print("Request Failed!")


