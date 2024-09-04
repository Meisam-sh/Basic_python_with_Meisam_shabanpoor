import hashlib
import csv

def hash_password_hack(input_file_name, output_file_name):
    with open(input_file_name, 'r') as file:
        reader = csv.reader(file)
        data = {rows[0]: rows[1] for rows in reader}
    
    output = {}
    for i in range(10000):
        value = str(i).zfill(4)
        hashed = hashlib.sha256(value.encode('utf-8')).hexdigest()
        
        if hashed in data.values():
            key = list(data.keys())[list(data.values()).index(hashed)]
            output[key] = value
    
    with open(output_file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        for key, value in output.items():
            writer.writerow([key, value])