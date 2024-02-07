def read_file(file_name: str):
    import pandas as pd 
    # read the csv file 
    results = pd.read_csv(file_name, header=None) 
    # display dataset 
    return results

def get_date():
    from datetime import datetime
    return datetime.today().strftime('%Y-%m-%d')

def concat_dataframes(dfs):
    import pandas as pd 
    return pd.concat(dfs, axis=0, ignore_index=True)

    