import tabula
import pandas as pd
import json

def pdf_to_json(pdf_file_path):
    # Read PDF file
    tables = tabula.read_pdf(pdf_file_path, pages='all', multiple_tables=True)
    
    # Initialize a list to store tables in JSON format
    json_tables = []
    
    # Convert each table to JSON and append to json_tables list
    for table in tables:
        output = table.to_dict(orient='records')
        json_tables = json_tables + output
        
    # Convert list of JSON tables to a JSON object
    json_data = json.dumps(json_tables)
    
    return json_data

# Example usage:
json_data = pdf_to_json('decrypted.pdf')
print(json_data)
