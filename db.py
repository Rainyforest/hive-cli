import sqlite3
def update_db(sqls):
    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('words.db')
    c = conn.cursor()
    for sql in sqls:
        c.execute(sql)
    conn.commit()
    conn.close()

def query_db(sqls):
    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('words.db')
    c = conn.cursor()
    for sql in sqls:
        c.execute(sql)
    results = c.fetchall()
    conn.close()
    return results

def insert_dataframe_db(df, table_name):
    conn = sqlite3.connect('words.db')
    df.to_sql(table_name, conn, if_exists='append', index=False)
    conn.close()
