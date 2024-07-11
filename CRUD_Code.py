import csv
import os

# Global variable for the CSV file path
CSV_FILE = r'C:\Users\prash\OneDrive\Desktop\assign\python\sales.csv'

# Function to create a new record in the dataset
def create_record(record):
    with open(CSV_FILE, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(record)
    print("Record added successfully.")

# Function to read and display specific records from the dataset
def read_records():
    with open(CSV_FILE, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        print("ID\tDate\t\tProduct\t\tQuantity\tPrice")
        print("-" * 60)
        for row in reader:
            print("\t".join(row))

# Function to update an existing record in the dataset
def update_record(record_id, updated_record):
    rows = []
    updated = False
    with open(CSV_FILE, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == record_id:
                rows.append(updated_record)
                updated = True
            else:
                rows.append(row)
    
    if updated:
        with open(CSV_FILE, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        print(f"Record with ID {record_id} updated successfully.")
    else:
        print(f"Record with ID {record_id} not found.")

# Function to delete a specific record from the dataset
def delete_record(record_id):
    rows = []
    deleted = False
    with open(CSV_FILE, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == record_id:
                deleted = True
            else:
                rows.append(row)
    
    if deleted:
        with open(CSV_FILE, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        print(f"Record with ID {record_id} deleted successfully.")
    else:
        print(f"Record with ID {record_id} not found.")

# Main function to demonstrate CRUD operations
def main():
    while True:
        print("\nCRUD Operations on Sales Dataset:")
        print("1. Create Record")
        print("2. Read Records")
        print("3. Update Record")
        print("4. Delete Record")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            # Create Record
            record_id = input("Enter ID: ")
            date = input("Enter Date (YYYY-MM-DD): ")
            product = input("Enter Product: ")
            quantity = input("Enter Quantity: ")
            price = input("Enter Price: ")
            record = [record_id, date, product, quantity, price]
            create_record(record)
            
        elif choice == '2':
            # Read Records
            read_records()
            
        elif choice == '3':
            # Update Record
            record_id = input("Enter ID of the record to update: ")
            date = input("Enter updated Date (YYYY-MM-DD): ")
            product = input("Enter updated Product: ")
            quantity = input("Enter updated Quantity: ")
            price = input("Enter updated Price: ")
            updated_record = [record_id, date, product, quantity, price]
            update_record(record_id, updated_record)
            
        elif choice == '4':
            # Delete Record
            record_id = input("Enter ID of the record to delete: ")
            delete_record(record_id)
            
        elif choice == '5':
            # Exit
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
