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

       
def importbooks():
    from db import insert_dataframe_db
    from utils import concat_dataframes, get_date, read_file
    dfs = []
    book_names = ["N1", "N2", "N3", "N4", "N5"]
    for book_name in book_names:  
        df = read_file('words/{}.csv'.format(book_name.lower())) # Type: DataFrame
        df.rename(columns={0: 'book', 1: 'word'}, inplace=True)
        df['last_access_date'] = [get_date()]*df.shape[0]
        dfs.append(df)
    insert_dataframe_db(concat_dataframes(dfs), 'words')