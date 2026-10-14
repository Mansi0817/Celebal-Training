import json

class EmployeeManager:
    def __init__(self, json_data):
        # Load JSON string into Python dictionary
        self.data = json.loads(json_data)

    def add_employee(self, employee):
        try:
            emp_id = employee["id"]
            employee["name"]
            employee["salary"]

            if emp_id in self.data:
                print("Employee ID already exists!")
                return

            self.data[emp_id] = employee
            print("Employee added successfully!")

        except KeyError as e:
            print("Missing key:", e)

    def update_employee(self, emp_id, name=None, salary=None):
        try:
            if emp_id not in self.data:
                print("Employee not found!")
                return

            if name is not None:
                self.data[emp_id]["name"] = name

            if salary is not None:
                self.data[emp_id]["salary"] = salary

            print("Employee updated successfully!")

        except KeyError as e:
            print("Missing key:", e)

    def delete_employee(self, emp_id):
        if emp_id in self.data:
            del self.data[emp_id]
            print("Employee deleted successfully!")
        else:
            print("Employee not found!")

    def save_to_file(self, filename):
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(self.data, file, indent=4)

        print("Data saved to file successfully!")


# Initial JSON string
json_data = '''
{
    "101": {
        "id": "101",
        "name": "John",
        "salary": 30000
    },
    "102": {
        "id": "102",
        "name": "Alice",
        "salary": 40000
    }
}
'''

# Create EmployeeManager object
manager = EmployeeManager(json_data)

# Add an employee
manager.add_employee({
    "id": "103",
    "name": "Rahul",
    "salary": 35000
})

# Update an employee
manager.update_employee("101", salary=45000)

# Delete an employee
manager.delete_employee("102")

# Save updated data to a JSON file
manager.save_to_file("employees.json")