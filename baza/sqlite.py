import sqlite3


class Database:
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT,
            telegram_id INTEGER UNIQUE
        );
        """
        self.execute(sql, commit=True)

    def create_table_voice(self):
        sql = """
        CREATE TABLE IF NOT EXISTS voice(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            voice_file_id TEXT
        );
        """
        self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{key} = ?" for key in parameters
        ])
        return sql, tuple(parameters.values())

    def add_voice(self, name: str, voice_file_id: str):
        sql = """
        INSERT INTO voice(name, voice_file_id) VALUES(?, ?);
        """
        self.execute(sql, parameters=(name, voice_file_id), commit=True)

    def voice_data(self):
        sql = "SELECT * FROM voice;"
        return self.execute(sql, fetchall=True)

    def get_voices_by_name(self, name: str):
        sql = "SELECT * FROM voice WHERE name = ?;"
        return self.execute(sql, parameters=(name,), fetchall=True)

    async def search_voices_title(self, title: str):
        sql = """
        SELECT * FROM voice WHERE name LIKE ?;
        """
        return self.execute(sql, parameters=(f"%{title}%",), fetchall=True)

    def add_user(self, telegram_id: int, full_name: str):
        sql = """
        INSERT INTO users(full_name, telegram_id) VALUES(?, ?);
        """
        self.execute(sql, parameters=(full_name, telegram_id), commit=True)

    def select_all_users(self):
        sql = "SELECT * FROM users;"
        return self.execute(sql, fetchall=True)

    def select_user(self, **kwargs):
        sql = "SELECT * FROM users WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters=parameters, fetchone=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM users;", fetchone=True)

    def delete_users(self):
        self.execute("DELETE FROM users;", commit=True)

    def all_users_id(self):
        return self.execute("SELECT telegram_id FROM users;", fetchall=True)


def logger(statement):
    print(f"""
_____________________________________________________        
Executing: 
{statement}
_____________________________________________________
""")
