import sqlite3


def connect_to_database(database):
    conn = sqlite3.connect(database)
    print("Successfully opened a database")


def create_table(database, table_name):
    try:
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        print("Connected to db")
        create_table_query = f'''CREATE TABLE IF NOT EXISTS {table_name} (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            model TEXT NOT NULL,
                            renderer TEXT NOT NULL);
                            '''
        cursor.execute(create_table_query)
        conn.commit()
        print("Query has been executed")
        cursor.close()

    except sqlite3.Error as error:
        print("Error while trying to connect to sqlite", error)

    finally:
        if (conn):
            conn.close()
            print("Connection closed")


def insert_data(database, table_name, data_to_insert):
    try:
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        print("Connected to db")
        create_table_query = f'''INSERT INTO {table_name} (model, renderer) VALUES {data_to_insert};
                            '''
        cursor.execute(create_table_query)
        conn.commit()
        print("Query has been executed")
        cursor.close()

    except sqlite3.Error as error:
        print("Error while trying to connect to sqlite", error)

    finally:
        if (conn):
            conn.close()
            print("Connection closed")
