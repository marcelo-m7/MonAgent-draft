import json


def generate_function_json(input_path):
    with open(input_path, 'r') as file:
        data = json.load(file)

    # Define the structure of the output JSON
    function_json = {
        "type": "function",
        "function": {
            "name": "Bibliography organizer",
            "description": "Set the paths bibliography to the subject associated based on the files path tree.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": list(data.keys())
            }
        }
    }

    # Fill the properties field
    for key, value in data.items():
        property_type = "string"
        if isinstance(value, int) or isinstance(value, float):
            property_type = "number"

        function_json["function"]["parameters"]["properties"][key] = {
            "type": property_type,
            "description": f"The {key.replace('_', ' ')}."
        }

    return function_json


# Usage
input_path = 'dossier_structure.json'  # Path to your input JSON file
result = generate_function_json(input_path)

# Print or save the result
print(json.dumps(result, indent=4))

# Optionally, save the result to a file
output_path = 'function_description.json'
with open(output_path, 'w') as file:
    json.dump(result, file, ensure_ascii=False, indent=4)
