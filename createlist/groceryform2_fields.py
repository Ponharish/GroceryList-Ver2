import json
import os
import pyodbc

from django.conf import settings
from django import forms

def load_master_fields_2():
    conn = pyodbc.connect(
        f"DRIVER={os.getenv('DB_DRIVER')};"
        f"SERVER={os.getenv('DB_HOST')};"
        f"DATABASE={os.getenv('DB_NAME')};"
        f"UID={os.getenv('DB_USER')};"
        f"PWD={os.getenv('DB_PASSWORD')};"
        "Encrypt=yes;"
        "TrustServerCertificate=no;"
    )

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Groceries.MasterList2")
    rows = cursor.fetchall()
    cursor.close() 
    conn.close() 
    
    fields_to_add_2 = {}
    for row in rows:
        heading = ''.join(row[0].split()).lower()
        body = {'english_name' : row[0],
                'tamil_name'   : row[1],
                'quantity'     : '',
                'max_length'   : 100,
                'required'     : False}

        fields_to_add_2[heading] = body
        
    fields_to_add_2["notes"] = {
        "label": "Notes",
        "english_name": "Notes",
        "tamil_name": "குறிப்புகள்",
        "max_length": 200,
        "required": False,
        "widget": forms.Textarea(attrs={"rows": 5, "cols": 50}),
    }
    return fields_to_add_2