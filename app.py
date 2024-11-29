from flask import Flask, render_template, request, jsonify
from DB import DatabaseManager
from gr import Gr

app = Flask(__name__)
instance = Gr(api_key="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")
DBM = DatabaseManager(host="localhost", user="root", password="root")
DBM.create_connection()
DBM.create_database("school")
DBM.create_tables()

@app.route("/")
def home():
    return render_template("home.html")

@app.route('/student')
def st():
    return render_template('student.html')

@app.route('/teacher')
def teacher():
    return render_template('teacher.html')

@app.route('/add_student', methods=['POST'])
def add_student():
    data = request.get_json()
    name = data.get("name")
    clas = data.get("class")
    stream = data.get("stream")
    house = data.get("house")
    instance.ask(f"Add this student to this school: {name}, {clas}, {stream}, {house}")
    
    # Add student to the database
    DBM.add_student(name, clas, stream, house)
    return jsonify({"message": "Student added successfully!"})

@app.route('/add_teacher', methods=['POST'])
def add_teacher():
    data = request.get_json()
    name = data.get("name")
    subject = data.get("subject")
    clas = data.get("class")
    stream = data.get("stream")
    instance.ask(f"Add this teacher to the school: {name}, Subject: {subject}, Class: {clas}, Stream: {stream}")
    
    # Add teacher to the database
    DBM.add_teacher(name, subject, clas, stream)
    return jsonify({"message": "Teacher added successfully!"})

@app.route('/msg', methods=['POST'])
def msg():
    data = request.get_json()
    user_input = data.get("message")
    response = instance.ask(user_input)
    
    # Fetch current student and teacher lists from the database
    students_data = DBM.fetch_all_students()
    teachers_data = DBM.fetch_all_teachers()
    
    # Prepare the data to send back
    students_list = instance.ask("Give a eval compatible list of students with their details as a list of tuples")
    teachers_list = instance.ask("Give a eval compatible list of teachers with their details as a list of tuples")
    students_list = eval(students_list)
    teachers_list = eval(teachers_list)

    DBM.update_all_students(students_list)
    DBM.update_all_teachers(teachers_list)
    
    return jsonify({"response": response})

if __name__ == "__main__":
    print("HI")
    app.run(host='0.0.0.0', port=5000)