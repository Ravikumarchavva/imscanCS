import os
import json
import pyodbc
from pathlib import Path
from config.settings import DATA_DIR

# Define the directory where JSON files are stored
output_mail_dir = DATA_DIR / 'output_mail_dir'

# Connect to SQL Server using Windows Authentication
conn = pyodbc.connect(
    'Driver={ODBC Driver 17 for SQL Server};'
    'Server=RAVIKUMAR;'
    'Database=dps_BI_lookup;'
    'Trusted_Connection=yes;'
)
cursor = conn.cursor()

# Insert function with added fields
def insert_to_db(data):
    sql = """
    INSERT INTO ProductQualityNotification (
        ID, NotificationType, DateTime, Location, Category, Product, 
        FocusProduct, Supplier, CountryOfOrigin, Variety, Grower, 
        PackagingCodes, Traceability, DateCode, DeliverySize, 
        CasesSampled, CasesRejected, UnitsRejected, RejectionLevel, 
        Details, ActionTaken, ContactsInformed
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    try:
        cursor.execute(sql, (
            data.get('ID', None),
            data.get('NotificationType', None),
            data.get('DateTime', None),
            data.get('Location', None),
            data.get('Category', None),
            data.get('Product', None),
            data.get('FocusProduct', None),
            data.get('Supplier', None),
            data.get('CountryOfOrigin', None),
            data.get('Variety', None),
            data.get('Grower', None),
            data.get('PackagingCodes', None),
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
        print(f"Inserted data for ID: {data.get('ID')}")
    except pyodbc.Error as e:
        print(f"Database error: {e}")

# Process JSON files from the directory
def process_json_files():
    for json_file in output_mail_dir.glob("*.json"):
        with open(json_file, 'r', encoding='utf-8') as file:
            try:
                data = json.load(file)
                insert_to_db(data)
            except json.JSONDecodeError:
                print(f"Skipping {json_file.name} - invalid JSON")
            except Exception as e:
                print(f"Error processing {json_file.name}: {e}")

# Execute the script
if __name__ == "__main__":
    process_json_files()
    cursor.close()
    conn.close()
    print("Data insertion complete.")
