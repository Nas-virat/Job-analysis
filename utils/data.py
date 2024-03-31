from csv import DictWriter
import os 
 
 

def write_csv(
    data: dict = None, 
    filename: str = './data/result.csv', 
    field_names: list[str] = None
):
    # Check if the file does not exist
    if not os.path.exists(filename):
        # Create the folder if it doesn't exist
        folder = os.path.dirname(filename)
        os.makedirs(folder, exist_ok=True)
        
        # Create the file
        open(filename, 'w').close()

    # Check if the file is empty
    is_empty = os.stat(filename).st_size == 0
    
    # Open CSV file in append mode
    # Create a file object for this file
    with open(filename, 'a') as f_object:
        # Pass the file object and a list
        # of column names to DictWriter()
        # You will get a object of DictWriter
        dictwriter_object = DictWriter(f_object, fieldnames=field_names)
        
        # Write the field names if the file is empty
        if is_empty:
            dictwriter_object.writeheader()
        
        # Pass the dictionary as an argument to the Writerow()
        dictwriter_object.writerow(data)
    
    # Close the file object
    f_object.close()


















