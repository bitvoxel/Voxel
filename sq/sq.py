from mysql.connector import connect

class Db:
    """
    A class representing a database connection.

    Attributes:
    connection (mysql.connector.connection.MySQLConnection): The database connection.
    cursor (mysql.connector.cursor.MySQLCursor): The cursor object to execute SQL queries.
    """

    def __init__(self):
        """
        Initializes the database connection and creates the necessary tables.
        """
        self.connection = connect(host='localhost',
                                  user='root',
                                  passwd='root',
                                  )
        init_sequence = ['CREATE DATABASE IF NOT EXISTS school',
                         'USE school;',
                         'CREATE TABLE IF NOT EXISTS students(roll INT UNIQUE PRIMARY KEY,name VARCHAR(25),class VARCHAR(4), join_date DATE, dob DATE);',
                         'CREATE TABLE IF NOT EXISTS teachers(empid INT UNIQUE PRIMARY KEY,name VARCHAR(25),assigned_class VARCHAR(4), join_date DATE, dob DATE);',
                         'CREATE TABLE IF NOT EXISTS school.marks (rollno INT NOT NULL,examid CHAR(4) NOT NULL,maths INT NULL DEFAULT NULL,physics INT NULL DEFAULT NULL, chemistry INT NULL DEFAULT NULL, english INT NULL DEFAULT NULL, computer INT NULL DEFAULT NULL, biology INT NULL DEFAULT NULL, PRIMARY KEY (examid, rollno), UNIQUE INDEX rollno_UNIQUE (rollno ASC) VISIBLE, UNIQUE INDEX examid_UNIQUE (examid ASC) VISIBLE, CONSTRAINT roll FOREIGN KEY (rollno) REFERENCES school.students (roll) ON DELETE CASCADE ON UPDATE CASCADE);'
                         ]
        self.cursor = self.connection.cursor()
        for x in init_sequence:
            self.cursor.execute(x)
        self.connection.commit()

    def close(self):
        """
        Commits the changes and closes the database connection.

        Returns:
        bool: True if the connection is closed successfully.
        """
        self.connection.commit()
        self.connection.close()
        return True


class Teachers(Db):
    """
    A class representing the teachers table in the database.

    Attributes:
    connection (mysql.connector.connection.MySQLConnection): The database connection.
    cursor (mysql.connector.cursor.MySQLCursor): The cursor object to execute SQL queries.
    """

    def add_teacher(self, empid, name, assigned_class, join_date, dob):
        """
        Adds a new teacher to the database.

        Args:
        empid (int): The employee ID of the teacher.
        name (str): The name of the teacher.
        assigned_class (str): The class assigned to the teacher.
        join_date (date): The date the teacher joined.
        dob (date): The date of birth of the teacher.
        """
        sql = "INSERT INTO teachers (empid, name, assigned_class, join_date, dob) VALUES (%s, %s, %s, %s, %s)"
        self.cursor.execute(sql, (empid, name, assigned_class, join_date, dob))
        self.connection.commit()

    def update_teacher(self, empid, name=None, assigned_class=None, join_date=None, dob=None):
        """
        Updates the details of a teacher in the database.

        Args:
        empid (int): The employee ID of the teacher.
        name (str, optional): The new name of the teacher. Defaults to None.
        assigned_class (str, optional): The new class assigned to the teacher. Defaults to None.
        join_date (date, optional): The new join date of the teacher. Defaults to None.
        dob (date, optional): The new date of birth of the teacher. Defaults to None.
        """
        updates = []
        params = []

        if name is not None:
            updates.append("name = %s")
            params.append(name)
        if assigned_class is not None:
            updates.append("assigned_class = %s")
            params.append(assigned_class)
        if join_date is not None:
            updates.append("join_date = %s")
            params.append(join_date)
        if dob is not None:
            updates.append("dob = %s")
            params.append(dob)

        if updates:
            sql = f"UPDATE teachers SET {', '.join(updates)} WHERE empid = %s"
            params.append(empid)
            self.cursor.execute(sql, params)
            self.connection.commit()

    def fetch_all_teachers(self):
        """
        Retrieves all teachers from the database.

        Returns:
        list: A list of tuples containing the details of all teachers.
        """
        sql = "SELECT * FROM teachers"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def view_teacher(self, empid):
        """
        Retrieves the details of a teacher from the database.

        Args:
        empid (int): The employee ID of the teacher.

        Returns:
        tuple: A tuple containing the details of the teacher.
        """
        sql = "SELECT * FROM teachers WHERE empid = %s"
        self.cursor.execute(sql, (empid,))

    def delete_teacher(self, empid):
        """
        Deletes a teacher from the database.

        Args:
        empid (int): The employee ID of the teacher.
        """
        sql = "DELETE FROM teachers WHERE empid = %s"
        self.cursor.execute(sql, (empid,))
        self.connection.commit()


class Students(Db):
    """
    A class representing the students table in the database.

    Attributes:
    connection (mysql.connector.connection.MySQLConnection): The database connection.
    cursor (mysql.connector.cursor.MySQLCursor): The cursor object to execute SQL queries.
    """

    def add_student(self, roll, name, class_name, join_date, dob):
        """
        Adds a new student to the database.

        Args:
        roll (int): The roll number of the student.
        name (str): The name of the student.
        class_name (str): The class of the student.
        join_date (date): The date the student joined.
        dob (date): The date of birth of the student.
        """
        sql = "INSERT INTO students (roll, name, class, join_date, dob) VALUES (%s, %s, %s, %s, %s)"
        self.cursor.execute(sql, (roll, name, class_name, join_date, dob))
        self.connection.commit()

    def update_student(self, roll, name=None, class_name=None, join_date=None, dob=None):
        """
        Updates the details of a student in the database.

        Args:
        roll (int): The roll number of the student.
        name (str, optional): The new name of the student. Defaults to None.
        class_name (str, optional): The new class of the student. Defaults to None.
        join_date (date, optional): The new join date of the student. Defaults to None.
        dob (date, optional): The new date of birth of the student. Defaults to None.
        """
        updates = []
        params = []

        if name is not None:
            updates.append("name = %s")
            params.append(name)
        if class_name is not None:
            updates.append("class = %s")
            params.append(class_name)
        if join_date is not None:
            updates.append("join_date = %s")
            params.append(join_date)
        if dob is not None:
            updates.append("dob = %s")
            params.append(dob)

        if updates:
            sql = f"UPDATE students SET {', '.join(updates)} WHERE roll = %s"
            params.append(roll)
            self.cursor.execute(sql, params)
            self.connection.commit()

    def fetch_all_students(self):
        """
        Retrieves all students from the database.

        Returns:
        list: A list of tuples containing the details of all students.
        """
        sql = "SELECT * FROM students"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def view_student(self, roll):
        """
        Retrieves the details of a student from the database.

        Args:
        roll (int): The roll number of the student.

        Returns:
        tuple: A tuple containing the details of the student.
        """
        sql = "SELECT * FROM students WHERE roll = %s"
        self.cursor.execute(sql, (roll,))
        return self.cursor.fetchall()

    def delete_student(self, roll):
        """
        Deletes a student from the database.

        Args:
        roll (int): The roll number of the student.
        """
        sql = "DELETE FROM students WHERE roll = %s"
        self.cursor.execute(sql, (roll,))
        self.connection.commit()

class Marks(Db):
    """
    A class representing the marks table in the database.

    Attributes:
    connection (mysql.connector.connection.MySQLConnection): The database connection.
    cursor (mysql.connector.cursor.MySQLCursor): The cursor object to execute SQL queries.
    """

    def add_marks(self, roll, examid, maths=None, physics=None, chemistry=None, english=None, computer=None, biology=None):
        """
        Adds new marks to the database.

        Args:
        roll (int): The roll number of the student.
        examid (str): The exam ID.
        maths (int, optional): The marks in maths. Defaults to None.
        physics (int, optional): The marks in physics. Defaults to None.
        chemistry (int, optional): The marks in chemistry. Defaults to None.
        english (int, optional): The marks in english. Defaults to None.
        computer (int, optional): The marks in computer. Defaults to None.
        biology (int, optional): The marks in biology. Defaults to None.
        """
        sql = "INSERT INTO marks (roll, examid, maths, physics, chemistry, english, computer, biology) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        self.cursor.execute(sql, (roll, examid, maths, physics, chemistry, english, computer, biology))
        self.connection.commit()

    def update_marks(self, roll, examid, maths=None, physics=None, chemistry=None, english=None, computer=None, biology=None):
        """
        Updates the marks in the database.

        Args:
        roll (int): The roll number of the student.
        examid (str): The exam ID.
        maths (int, optional): The new marks in maths. Defaults to None.
        physics (int, optional): The new marks in physics. Defaults to None.
        chemistry (int, optional): The new marks in chemistry. Defaults to None.
        english (int, optional): The new marks in english. Defaults to None.
        computer (int, optional): The new marks in computer. Defaults to None.
        biology (int, optional): The new marks in biology. Defaults to None.
        """
        updates = []
        params = []

        if maths is not None:
            updates.append("maths = %s")
            params.append(maths)
        if physics is not None:
            updates.append("physics = %s")
            params.append(physics)
        if chemistry is not None:
            updates.append("chemistry = %s")
            params.append(chemistry)
        if english is not None:
            updates.append("english = %s")
            params.append(english)
        if computer is not None:
            updates.append("computer = %s")
            params.append(computer)
        if biology is not None:
            updates.append("biology = %s")
            params.append(biology)

        if updates:
            sql = f"UPDATE marks SET {', '.join(updates)} WHERE roll = %s AND examid = %s"
            params.extend([roll, examid])
            self.cursor.execute(sql, params)
            self.connection.commit()

    def fetch_all_marks(self):
        """
        Retrieves all marks from the database.

        Returns:
        list: A list of tuples containing the marks of all students.
        """
        sql = "SELECT * FROM marks"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def view_marks(self, roll, examid):
        """
        Retrieves the marks of a student from the database.

        Args:
        roll (int): The roll number of the student.
        examid (str): The exam ID.

        Returns:
        tuple: A tuple containing the marks of the student.
        """
        sql = "SELECT * FROM marks WHERE roll = %s AND examid = %s"
        self.cursor.execute(sql, (roll, examid))
        return self.cursor.fetchall()

    def delete_marks(self, roll, examid):
        """
        Deletes the marks of a student from the database.

        Args:
        roll (int): The roll number of the student.
        examid (str): The exam ID.
        """
        sql = "DELETE FROM marks WHERE roll = %s AND examid = %s"
        self.cursor.execute(sql, (roll, examid))
        self.connection.commit()

    def fetch_marks_by_exam(self, examid):
        sql = "SELECT * FROM marks WHERE examid = %s"
        self.cursor.execute(sql, (examid,))
        return self.cursor.fetchall()

    def fetch_marks_by_student(self, roll):
        sql = "SELECT * FROM marks where roll={}".format(roll)
        print(sql)
        self.cursor.execute(sql)
        return self.cursor.fetchall()


