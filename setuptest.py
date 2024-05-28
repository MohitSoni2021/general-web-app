import sqlite3

query_list = {
    'website_link_page':{
        'table_structure':'CREATE TABLE website_links_table (id INTEGER PRIMARY KEY AUTOINCREMENT , web_title VARCHAR(60), web_link VARCHAR(550), web_desv VARCHAR(750) )',
        'insert_query':'INSERT INTO website_links_table (web_title, web_link, web_desc, user) VALUES ("{title}","{link}","{desc}", "{user}")',
        'select_query':'SELECT * FROM website_links_table',
        'delete_query':'DELETE FROM website_links_table WHERE id = {id}',
        'update_query':'UPDATE website_links_table SET web_title = "{title}", web_link = "{link}", web_desc = "{desc}" WHERE id = {id}',
        'get_single_record':'SELECT * FROM website_links_table WHERE id = {id}'
    },
    
    'common_query':{
        'delete_query': 'DELETE FROM {tablename} WHERE id = {id}',
        'select_query' : 'SELECT * FROM {tablename}',
        'special_select' : 'SELECT * FROM {tablename} WHERE user = "{user}"',
        'singe_record_query' : 'SELECT * FROM {tablename} WHERE id = {id}'
    },
    
    'notepad_page':{
        'structure' : 'CREATE TABLE notepad_table (id INTEGER PRIMARY KEY AUTOINCREMENT , note_heading VARCHAR(160), note_content VARCHAR(60000))',
        'insert_query' : 'INSERT INTO notepad_table (note_heading, note_content, user) VALUES ("{heading}","{content}", "{user}")',
        'update_query' : 'UPDATE notepad_table SET note_heading = "{heading}", note_content = "{content}" WHERE id = {id}',
    },
    
    'user_table':{
        'structure' : 'CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT , username VARCHAR(50), password VARCHAR(50))',
        'insert_query' : 'INSERT INTO users (username, password) VALUES ("{username}","{password}")',
        'update_query' : 'UPDATE users SET username = "{username}", password = "{password}" WHERE id = {id}',
    }
}

class generalDatabase:
    def __init__(self) -> None:
        self.database = "general.db"
        
    def Insert_data(self, query:str):
        self.connection = sqlite3.connect(self.database)
        self.cursor = self.connection.cursor()
        self.cursor.execute(query)
        self.connection.commit()
        self.connection.close()
        
    def get_data(self, query):
        self.connection = sqlite3.connect(self.database)
        self.cursor = self.connection.cursor()
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        self.connection.commit()
        self.connection.close()
        return data
    
    def delete_record(self, query):
        self.connection = sqlite3.connect(self.database)
        self.cursor = self.connection.cursor()
        self.cursor.execute(query)
        self.connection.commit()
        self.connection.close()
        
    def get_single(self, query):
        self.connection = sqlite3.connect(self.database)
        self.cursor = self.connection.cursor()
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        self.connection.commit()
        self.connection.close()
        return data
    
    def update_value(self, query):
        self.connection = sqlite3.connect(self.database)
        self.cursor = self.connection.cursor()
        self.cursor.execute(query)
        self.connection.commit()
        self.connection.close()
        
    def avg_sugar_value(self):
        self.connection = sqlite3.connect(self.database)
        self.cursor = self.connection.cursor()
        query = f'SELECT AVG(value) FROM sugarData'
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        self.connection.commit()
        self.connection.close()
        return data
    
if __name__ == '__main__':
    pass