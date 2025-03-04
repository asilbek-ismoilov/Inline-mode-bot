import sqlite3


class Database:
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = (), fetchone=False, fetchall=False, commit=False):
        connection = self.connection
        connection.set_trace_callback(self.logger)
        cursor = connection.cursor()
        cursor.execute(sql, parameters)

        data = None
        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()

        cursor.close()
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
            name TEXT PRIMARY KEY,
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
        INSERT OR IGNORE INTO voice(name, voice_file_id) VALUES(?, ?);
        """
        self.execute(sql, parameters=(name, voice_file_id), commit=True)

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
        INSERT OR IGNORE INTO users(full_name, telegram_id) VALUES(?, ?);
        """
        self.execute(sql, parameters=(full_name, telegram_id), commit=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM users;", fetchone=True)

    def all_users_id(self):
        return self.execute("SELECT telegram_id FROM users;", fetchall=True)

    @staticmethod
    def logger(statement):
        print(f"""
_____________________________________________________        
Executing: 
{statement}
_____________________________________________________
""")
