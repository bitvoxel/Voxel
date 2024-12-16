from mysql.connector import connect
class Db:
    def __init__(self):
        self.connection = connect(host='localhost',
                                  user='root',
                                  passwd='root',
                                  )
        init_sequence=['CREATE DATABASE IF NOT EXISTS school',
                       'USE school;',
                       'CREATE TABLE IF NOT EXISTS students(roll INT,name VARCHAR(25),class VARCHAR(4), join_date DATE, dob DATE);',
                       'CREATE TABLE IF NOT EXISTS teachers(empid INT,name VARCHAR(25),assigned_class VARCHAR(4), join_date DATE, dob DATE);']
        self.cursor=self.connection.cursor()
        for x in init_sequence:
            self.cursor.execute(x)

    def close(self):
        self.connection.commit()
        self.connection.close()
        return True

class Teachers(Db):
    def add_teacher(self, empid, name, assigned_class, join_date, dob):
        sql = "INSERT INTO teachers (empid, name, assigned_class, join_date, dob) VALUES (%s, %s, %s, %s, %s)"
        self.cursor.execute(sql, (empid, name, assigned_class, join_date, dob))
        self.connection.commit()

    def update_teacher(self, empid, name=None, assigned_class=None, join_date=None, dob=None):
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
        sql = "SELECT * FROM teachers"
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    
    def view_teacher(self,empid):
        sql="SELECT * FROM teacher WHERE empid=%s"
        self.cursor.execute(sql,(empid,))

    def delete_teacher(self, empid):
        sql = "DELETE FROM teachers WHERE empid = %s"
        self.cursor.execute(sql, (empid,))
        self.connection.commit()

class Students(Db):
    def add_student(self, roll, name, class_name, join_date, dob):
        sql = "INSERT INTO students (roll, name, class, join_date, dob) VALUES (%s, %s, %s, %s, %s)"
        self.cursor.execute(sql, (roll, name, class_name, join_date, dob))
        self.connection.commit()

    def update_student(self, roll, name=None, class_name=None, join_date=None, dob=None):
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
        sql = "SELECT * FROM students"
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    
    def view_student(self,roll):
        sql="SELECT * FROM students WHERE roll=%s"
        self.cursor.execute(sql,(roll,))
        return self.cursor.fetchall()

    def delete_student(self, roll):
        sql = "DELETE FROM students WHERE roll = %s"
        self.cursor.execute(sql, (roll,))
        self.connection.commit()