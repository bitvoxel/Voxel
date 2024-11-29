import mysql.connector
from mysql.connector import Error

class DatabaseManager:
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        self.connection = None

    def create_connection(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                passwd=self.password
            )
            if self.connection.is_connected():
                print("Connection to MySQL DB successful.")
        except Error as e:
            print(f"The error '{e}' occurred")

    def create_database(self, database_name):
        cursor = self.connection.cursor()
        try:
            cursor.execute(f"CREATE DATABASE {database_name};")
            print(f"Database '{database_name}' created successfully.")
        except Error as e:
            print(f"The error '{e}' occurred")

    def create_tables(self):
        cursor = self.connection.cursor()
        try:
            cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS student (
                rollno INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                class VARCHAR(50) NOT NULL,
                stream VARCHAR(50),
                house VARCHAR(50)
            );
            """)
            print("Student table created successfully.")

            cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS teacher (
                employee_id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                subject VARCHAR(100) NOT NULL,
                class_teacher_of VARCHAR(50)
            );
            """)
            print("Teacher table created successfully.")

        except Error as e:
            print(f"The error '{e}' occurred")

    def close_connection(self):
        if self.connection.is_connected():
            self.connection.close()
            print("MySQL connection is closed.")

# Example usage
if __name__ == "__main__":
    db_manager = DatabaseManager("localhost", "root", "root")
    db_manager.create_connection()
    db_manager.create_database("school")
    db_manager.create_tables()
    db_manager.close_connection()