from mysql.connector import MySQLConnection, Error
import database
from database.parse_configuration import parse_config


def query():
    query = ['SELECT count(*) FROM list', 'SELECT count(*) FROM content', 'SELECT count(*) FROM register', \
    'INSERT INTO list(filename, url, url_text, modifiedon) VALUES(%s, %s, %s, %s)', \
    'INSERT INTO content(filename, category, category_slug, title, publishedby, createdby, publishedon, modifiedby, modifiedon, modifiedurl, article) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', \
    'INSERT INTO register(operation, title, section, modifiedby, modifiedon, url) VALUES(%s, %s, %s, %s, %s, %s)']
    return query

def is_empty(query):
    isEmpty = False
    try:
        dbconfig = parse_config()
        conn = MySQLConnection(**dbconfig)
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute(query)
            rows = cursor.fetchone()
            for row in rows:
                if row == 0:
                    isEmpty = True
                else:
                    isEmpty = False
            cursor.close()
            conn.close()
    except Error as e:
        print(e)
    return isEmpty

def insert_data(query, dataset):
    try:
        db_config = parse_config()
        conn = MySQLConnection(**db_config)
        cursor = conn.cursor()
        cursor.executemany(query, dataset)
        conn.commit()
        cursor.close()
        conn.close()
    except Error as e:
        print('Error:', e)

def insert_all_data(list_results, content_results, register_results):
    if is_empty(query()[0]):
        insert_data(query()[3], list_results)
    else:
        print('W tabeli "list" istnieją już dane.')
    if is_empty(query()[1]):
        insert_data(query()[4], content_results)
    else:
        print('W tabeli "content" istnieją już dane.')
    if is_empty(query()[2]):
        insert_data(query()[5], register_results)
    else:
        print('W tabeli "register" istnieją już dane.')