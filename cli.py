from db import insert_dataframe_db, query_db, update_db
from utils import concat_dataframes, get_date, read_file
       
def health():
    print("Hello, world!")

def quest():
    from InquirerPy import prompt

    questions = [
        # {"type": "input", "message": "What's your name:", "name": "name"},
        {
            "type": "list",
            "message": "What word book are you choosing?",
            "choices": ["N1", "N2", "N3", "N4", "N5"]
        }
        # {"type": "confirm", "message": "Confirm?"}
    ]
    result = prompt(questions)
    book_name = result[0]
    read_file('words/{}.csv'.format(book_name.lower()))

def initdb():
    update_db([
    # Create a new table
    '''CREATE TABLE IF NOT EXISTS words
                (id INTEGER PRIMARY KEY, word TEXT, last_access_date TEXT, book INTEGER)'''
    ])
    
def importbooks():
    dfs = []
    book_names = ["N1", "N2", "N3", "N4", "N5"]
    for book_name in book_names: # , "N2", "N3", "N4", "N5"
        df = read_file('words/{}.csv'.format(book_name.lower())) # Type: DataFrame
        df.rename(columns={0: 'book', 1: 'word'}, inplace=True)
        df['last_access_date'] = [get_date()]*df.shape[0]
        dfs.append(df)
    insert_dataframe_db(concat_dataframes(dfs), 'words')


def rand():
    words = query_db(["SELECT * FROM words;"])
    import random
    # Get a random element from the list
    random_element = random.choice(words)
    book, text, date = random_element
    return text