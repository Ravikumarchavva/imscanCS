import os
import json
import pyodbc
from pathlib import Path

# Change this to your actual data directory
from config.settings import DATA_DIR
output_mail_dir = DATA_DIR / 'output_mail_dir'

# Connect to your local SQL Server instance using Windows Authentication
conn = pyodbc.connect(
    'Driver={ODBC Driver 17 for SQL Server};'
    'Server=RAVIKUMAR;'
    'Database=dps_BI_lookup;'
    'Trusted_Connection=yes;'
)
cursor = conn.cursor()

def insert_to_db(data):
    sql = """
    INSERT INTO ProductQualityNotification (
        ID, NotificationType, DateTime, Location, Category, Product, 
        FocusProduct, Supplier, Traceability, DateCode, DeliverySize, 
        CasesSampled, CasesRejected, UnitsRejected, RejectionLevel, 
        Details, ActionTaken, ContactsInformed
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    
    cursor.execute(sql, (
        data.get('ID', None),
        data.get('NotificationType', None),
        data.get('DateTime', None),
        data.get('Location', None),
        data.get('Category', None),
        data.get('Product', None),
        data.get('FocusProduct', None),
        data.get('Supplier', None),
        data.get('Traceability', None),
        data.get('DateCode', None),
        data.get('DeliverySize', None),
        data.get('CasesSampled', None),
        data.get('CasesRejected', None),
        data.get('UnitsRejected', None),
        data.get('RejectionLevel', None),
        data.get('Details', None),
        data.get('ActionTaken', None),
        data.get('ContactsInformed', None)
    ))
    conn.commit()

def process_json_files():
    # Loop through all JSON files in the output_mail_dir
    for json_file in output_mail_dir.glob("*.json"):
        with open(json_file, 'r', encoding='utf-8') as file:
            try:
                data = json.load(file)
                # Insert the JSON data into the database
                print(data)
                insert_to_db(data)
                print(f"Inserted data from {json_file.name}")
            except json.JSONDecodeError:
                print(f"Skipping {json_file.name} - invalid JSON")

# Execute the function to process all JSON files
if __name__ == "__main__":
    process_json_files()
    cursor.close()
    conn.close()
    print("Data insertion complete.")
