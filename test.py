from DB import DatabaseManager
if __name__ == "__main__":
    db_manager = DatabaseManager("localhost", "root", "root")  # Adjust credentials as needed
    db_manager.create_connection()
    db_manager.create_database("school")
    db_manager.create_tables()
    db_manager.close_connection()