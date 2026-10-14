import json

# Example JSON string
json_data = '''
{
    "employee": {
        "name": "John",
        "age": 30,
        "skills": ["Python", "ML", "SQL"],
        "address": {
            "city": "Mumbai",
            "zip": 400001
        }
    }
}
'''

# 1. Parse JSON string into Python dictionary
data = json.loads(json_data)

# 2. Add a new skill
data["employee"]["skills"].append("Java")

# 3. Update the city name
data["employee"]["address"]["city"] = "Delhi"

# 4. Convert the updated dictionary to a JSON string
updated_json = json.dumps(data, indent=4)

# 5. Pretty print the updated JSON
print(updated_json)