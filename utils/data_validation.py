import jsonschema
import re


def validate_data_type(data, schema):
    try:
        jsonschema.validate(data, schema)
        return True
    except jsonschema.exceptions.ValidationError:
        return False

def format_data(data):
    formatted_data = {}
    for key, value in data.items():
        if isinstance(value, str):
            formatted_data[key] = value.strip()
        else:
            formatted_data[key] = value
    return formatted_data


def validate_and_format_wrapper(data,schema_file_name):
    with open(schema_file_name, 'r') as schema_file:
        schema = json.load(schema_file)

    if validate_data_type(data_to_validate, schema):
        formatted_data = format_data(data_to_validate)
        print("Validated and formatted data:")
        print(formatted_data)
    else:
        print("Data validation failed.")
    return formatted_data
