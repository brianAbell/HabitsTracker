import json
from datetime import datetime

def add_leetcode_entry(problem_name, status):
    # Read the existing JSON data
    with open('tracking.json', 'r') as file:
        data = json.load(file)

    # Create a new entry
    new_entry = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "problem": problem_name,
        "status": status
    }

    # Append the new entry to the LeetCode array
    data['LeetCode'].append(new_entry)

    # Write the updated JSON data back to the file
    with open('tracking.json', 'w') as file:
        json.dump(data, file, indent=4)

    print(f"Added new entry for problem '{problem_name}' with status '{status}'")

if __name__ == "__main__":
    problem_name = input("Enter the problem name: ")
    status = input("Enter the status (Completed/In Progress): ")
    add_leetcode_entry(problem_name, status)
