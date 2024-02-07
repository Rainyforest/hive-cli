import sqlite3
from constants import DB_FILE_NAME
from sqlalchemy import create_engine, MetaData, Table, select

engine = create_engine("sqlite:///{}".format(DB_FILE_NAME), echo=True)

# Create a MetaData instance
metadata = MetaData()

# Reflect an existing table
words_reflected = Table('words', metadata, autoload_with=engine)

# Construct a SELECT statement
select_stmt = select(words_reflected)

# Execute the query
with engine.connect() as connection:
    result = connection.execute(select_stmt)
    for row in result:
        print(row)  # Each 'row' is a RowProxy object that allows you to access row data by column name or position


## Helper function that directly uses sqlite3 library
def update_db():
    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect(DB_FILE_NAME)
    c = conn.cursor()
    
    c.execute('''CREATE TABLE IF NOT EXISTS words
                (id INTEGER PRIMARY KEY, word TEXT, last_access_date TEXT, book INTEGER)''')
    conn.commit()
    conn.close()


def insert_dataframe_db(df, table_name):
    conn = sqlite3.connect(DB_FILE_NAME)
    df.to_sql(table_name, conn, if_exists='append', index=False)
    conn.close()
