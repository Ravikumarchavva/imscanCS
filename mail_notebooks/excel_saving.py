import os
import json
import pandas as pd
from pathlib import Path
from config.settings import DATA_DIR

# Define paths
output_mail_dir = DATA_DIR / 'output_mail_dir'
output_mail_dir.mkdir(exist_ok=True)
excel_file_path = DATA_DIR / 'output_mail_excel_dir'/ "ProductQualityNotifications.xlsx"
excel_file_path.parent.mkdir(exist_ok=True)

# Function to update Excel file when new JSON arrives
def update_excel_from_json(data):
    # Define required columns (ensure consistency)
    columns = [
        "ID", "NotificationType", "DateTime", "Location", "Category", "Product", 
        "FocusProduct", "Supplier", "CountryOfOrigin", "Variety", "Grower", 
        "PackagingCodes", "DateCode", "DeliverySize", 
        "CasesSampled", "CasesRejected", "UnitsRejected", "RejectionLevel", 
        "Details", "ActionTaken", "ContactsInformed"
    ]
    
    # Convert JSON data to DataFrame, ensuring missing fields are handled
    new_data_df = pd.DataFrame([{col: data.get(col, None) for col in columns}])
    
    # If Excel file exists, read existing data
    if excel_file_path.exists():
        existing_df = pd.read_excel(excel_file_path, dtype=str)  # Read as string to prevent conversion issues
        
        # Check if ID already exists to prevent duplication
        if str(data.get("ID")) in existing_df["ID"].astype(str).values:
            print(f"Skipping ID {data.get('ID')} - Already exists in Excel.")
            return
        
        # Append new data and save
        updated_df = pd.concat([existing_df, new_data_df], ignore_index=True)
    else:
        updated_df = new_data_df  # Create new file if it doesn’t exist

    # Save the updated DataFrame to Excel
    updated_df.to_excel(excel_file_path, index=False)
    print(f"Excel updated with ID: {data.get('ID')}")

# Process JSON files and update Excel
def process_json_files():
    for json_file in output_mail_dir.glob("*.json"):
        with open(json_file, "r", encoding="utf-8") as file:
            try:
                data = json.load(file)
                update_excel_from_json(data)
            except json.JSONDecodeError:
                print(f"Skipping {json_file.name} - invalid JSON")
            except Exception as e:
                print(f"Error processing {json_file.name}: {e}")

# Execute script
if __name__ == "__main__":
    process_json_files()
    print("Excel update complete.")
