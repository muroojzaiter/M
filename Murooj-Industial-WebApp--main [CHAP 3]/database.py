import psycopg2

class Database:
    def __init__(self, host, username, password, dbname):
        self.host = host
        self.username = username
        self.password = password
        self.dbname = dbname
        self.conn = None
        self.cur = None

    def connect(self):
        try:
            self.conn = psycopg2.connect(
                host=self.host,
                user=self.username,
                password=self.password,
                dbname=self.dbname
            )
            self.cur = self.conn.cursor()
            print("Connected to the database")
        except psycopg2.Error as e:
            print(f"Error connecting to the database: {e}")

    def execute_query(self, query):
        try:
            self.cur.execute(query)
            self.conn.commit()
            print("Query executed successfully")
        except psycopg2.Error as e:
            print(f"Error executing query: {e}")

    def insert_user(self, username, password):
        try:
            insert_query = f"INSERT INTO users (username, password) VALUES ('{username}', '{password}')"
            self.cur.execute(insert_query)
            self.conn.commit()
            print(f"User '{username}' added successfully")
        except psycopg2.Error as e:
            print(f"Error inserting user: {e}")

    def close_connection(self):
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()
        print("Connection closed")

# Example usage:
if __name__ == "__main__":
    db = Database(host='localhost', username='your_username', password='your_password', dbname='your_dbname')
    db.connect()

    # Insert five users
    users = [
        ("user1", "password1"),
        ("user2", "password2"),
        ("user3", "password3"),
        ("user4", "password4"),
        ("user5", "password5")
    ]
    for user, password in users:
        db.insert_user(user, password)

    db.close_connection()
