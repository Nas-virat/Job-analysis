from csv import DictWriter
 
# list of column names
field_names = ['title', 'company', 'company_link',
               'date', 'link','insights','description']
 
 

def write_csv(
    data:dict = None, 
    filename: str = 'result.csv', 
    field_names : list[str] = ['title', 'company', 'company_link','date', 'link','insights','description']
    ):
    
    # Open CSV file in append mode
    # Create a file object for this file
    with open(filename, 'a') as f_object:
 
        # Pass the file object and a list
        # of column names to DictWriter()
        # You will get a object of DictWriter
        dictwriter_object = DictWriter(f_object, fieldnames=field_names)
    
        # Pass the dictionary as an argument to the Writerow()
        dictwriter_object.writerow(data)
    
        # Close the file object
        f_object.close()


















