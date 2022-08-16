def open_dataset(file_name='AppleStore.csv', header=True):        
    opened_file = open(file_name)
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)
    
    if header:
        return data[0], data[1:]
    else:
        return data
    
header, apps_data = open_dataset(file_name='AppleStore.csv', header=True)
