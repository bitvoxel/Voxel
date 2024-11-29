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
            print(f"The error '{e}' occurred while connecting to the database.")

    def create_database(self, database_name):
        if self.connection is None:
            print("No connection established. Cannot create database.")
            return

        with self.connection.cursor() as cursor:
            try:
                cursor.execute(f"CREATE DATABASE {database_name};")
                print(f"Database '{database_name}' created successfully.")
            except Error as e:
                print(f"The error '{e}' occurred while creating the database.")

    def create_tables(self):
        if self.connection is None:
            print("No connection established. Cannot create tables.")
            return

        with self.connection.cursor() as cursor:
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
                print(f"The error '{e}' occurred while creating tables.")

    def close_connection(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("MySQL connection is closed.")
        else:
            print("No connection to close.")

# Example usage
if __name__ == "__main__":
    db_manager = DatabaseManager("localhost", "root", "root")  # Adjust credentials as needed
    db_manager.create_connection()
    db_manager.create_database("school")
    db_manager.create_tables()
    db_manager.close_connection()