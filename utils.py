def read_file(file_name: str):
    import pandas as pd 
    # read the csv file 
    results = pd.read_csv(file_name) 
    # display dataset 
    print(results) 
    return results