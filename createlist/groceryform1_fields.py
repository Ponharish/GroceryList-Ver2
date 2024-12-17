import os
import json
from django.conf import settings
from django import forms

def load_master_fields_1():
    # Construct the path to the JSON file
    json_file_path = os.path.join(settings.BASE_DIR, 'masterlist', 'fields_to_add_1.json')

    try:
        # Open and load the JSON file
        with open(json_file_path, 'r', encoding='utf-8') as json_file:
            fields_to_add_1 =  json.load(json_file)
    except FileNotFoundError:
        print(f"Error: The file {json_file_path} does not exist.")
        return {}
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return {}
    
    fields_to_add_1["notes"] = {
        "label": "Notes",
        "english_name": "Notes",
        "tamil_name": "குறிப்புகள்",
        "max_length": 200,
        "required": False,
        "widget": forms.Textarea(attrs={"rows": 5, "cols": 50}),
    }
    return fields_to_add_1

