from flask import Flask, render_template, request, jsonify
import json
from groq_wrapper.gr import Gr
from sql_wrapper.sq import Students, Teachers, Marks

"""
This is the main application file for the school assistant bot.
It initializes the Flask application and defines routes for various operations.
"""
app = Flask(__name__)
"""
Initialize the Flask application.
"""

instance = Gr()
"""
Initialize the Gr instance, which handles the chat functionality.
"""

def init():
    """
    Initialize the chat with system messages.
    """
    instance.chat.append(
        {
            "role": "system",
            "content": "ALWAYS REPLY IN HTML.DO NOT TAKE ANY INPUTS FROM USERS.FOLLOW UNIFORM STYLING.You are a school assistant bot of sainik school kazhakootam who can tell details about students and teachers.You cannot modify or add students.You can display information.You can sort students by various filters.You can also solve various homework questions.You can give any details about the school.",
        }
    )
    instance.chat.append(
        {
            "role": "system",
            "content": open('static/details.txt').read(),
        }
    )
    k = Students()
    """
    Initialize the Students instance, which handles student data.
    """
    instance.chat.append(
        {
            "role": "system",
            "content": "Here is a list of students in roll, name, class_name, join_date, dob format :\n" + str(k.fetch_all_students()),
        }
    )
    k = Teachers()
    """
    Initialize the Teachers instance, which handles teacher data.
    """
    instance.chat.append(
        {
            "role": "system",
            "content": "Here is a list of teachers in empid, name, assigned_class, join_date, dob format:\n" + str(k.fetch_all_teachers()),
        }
    )


    k.close()

    k=Marks()
    instance.chat.append(
    {
        "role": "system",
        "content": "Here is a list of all marks in roll no, exam id, maths, physics, chemistry, english,computer,biology format:\n" + str(k.fetch_all_marks()),
    }
)

    instance.chat.append(
    {
        "role": "system",
        "content": "ALWAYS REPLY IN HTML WITHOUT COLORS.GIVE ANSWER AS HTML LISTS WHEN NEEDED.TABLES MUST BE BORDERED AND ALIGNED. DO NOT TAKE ANY INPUTS FROM USERS.FOLLOW UNIFORM STYLING.",
    }
)
    del k
init()


@app.route("/")
def hello_world():
    return render_template("home.html")


@app.route("/msg", methods=["POST"])
def msg():
    user_input = request.json.get("message")
    response = instance.ask(user_input)
    return jsonify({"response": response})


@app.route("/student")
def st():
    return render_template("student.html")


@app.route("/teacher")
def te():
    return render_template("teacher.html")


@app.route("/add_student", methods=["POST"])
def add_st():
    rollno = request.json.get("roll")
    name = request.json.get("name")
    clas = request.json.get("class")
    jd = request.json.get("join_date")
    dob = request.json.get("dob")
    k=Students()
    k.add_student(rollno, name, clas, jd, dob)
    instance.ask(f"Add this student {rollno}, {name}, {clas}, {jd}, {dob}")
    return jsonify({})


@app.route("/add_teacher", methods=["POST"])
def add_te():
    empid = request.json.get("roll")
    name = request.json.get("name")
    assgn_class = request.json.get("class")
    jd = request.json.get("join_date")
    dob = request.json.get("dob")
    k=Teachers()
    k.add_teacher(empid, name, assgn_class, jd, dob)
    instance.ask(f"Add this teacher {empid}, {name}, {assgn_class}, {jd}, {dob}")
    return jsonify({})


@app.route("/update_student", methods=["POST"])
def up_st():
    student_id = request.json.get("roll") if request.json.get("roll") else None
    name = request.json.get("name") if request.json.get("name") else None
    assigned_class = request.json.get("class") if request.json.get("class") else None
    join_date = request.json.get("join_date") if request.json.get("join_date") else None
    dob = request.json.get("dob") if request.json.get("dob") else None
    k = Students()
    k.update_student(student_id, name, assigned_class, join_date, dob)
    k.close()
    instance.ask(f"Update student detail - {student_id}, {name}, {assigned_class}, {join_date}, {dob}")
    return jsonify({})

@app.route("/update_teacher", methods=["POST"])
def up_te():
    empid = request.json.get("roll") if request.json.get("roll") else None
    name = request.json.get("name") if request.json.get("name") else None
    assgn_class = request.json.get("class") if request.json.get("class") else None
    jd = request.json.get("join_date") if request.json.get("join_date") else None
    dob = request.json.get("dob") if request.json.get("dob") else None
    k=Teachers()
    k.update_teacher(empid, name, assgn_class, jd, dob)
    instance.ask(f"Update teacher detail - {empid}, {name}, {assgn_class}, {jd}, {dob}")
    return jsonify({})


@app.route("/fetch_all_teachers")
def fetch_all_teachers():
    return jsonify(Teachers().fetch_all_teachers())


@app.route("/fetch_all_students")
def fetch_all_students():
    return jsonify(Students().fetch_all_students())


@app.route("/fetch_teacher_by_id", methods=["POST"])
def fetch_teacher_by_id():
    empid = request.json.get("roll")
    return jsonify(Teachers().fetch_teacher_by_id(empid))


@app.route("/fetch_student_by_id", methods=["POST"])
def fetch_student_by_id():
    student_id = request.json.get("roll")
    return jsonify(Students().view_student(student_id))

@app.route("/delete_teacher_by_id", methods=["POST"])
def delete_teacher_by_id():
    empid = request.json.get("roll")
    k = Teachers()
    k.delete_teacher(empid)
    instance.ask('Remove teacher '+request.json.get("roll"))

    return jsonify({}) # Return 204 No Content on successful deletion


@app.route("/delete_student_by_id", methods=["POST"])
def delete_student_by_id():
    k = Students()
    k.delete_student(request.json.get("roll"))
    instance.ask('Remove student '+request.json.get("roll"))
    return jsonify({}) ## Return 204 No Content on successful deletion


@app.route("/add_marks", methods=["POST"])
def add_marks():
    rollno = request.json.get("rollno")
    examid = request.json.get("examid")
    maths = request.json.get("maths")
    physics = request.json.get("physics")
    chemistry = request.json.get("chemistry")
    english = request.json.get("english")
    computer = request.json.get("computer")
    biology = request.json.get("biology")
    instance.ask('Add marks rollno, examid, maths, physics, chemistry, english, computer, biology - {rollno}, {examid}, {maths}, {physics}, {chemistry}, {english}, {computer},{ biology}')
    k = Marks()
    k.add_marks(rollno, examid, maths, physics, chemistry, english, computer, biology)
    return jsonify({})  # Return 204 No Content on successful addition


@app.route("/update_marks", methods=["POST"])
def update_marks():
    rollno = request.json.get("rollno")
    examid = request.json.get("examid")
    maths = request.json.get("maths")
    physics = request.json.get("physics")
    chemistry = request.json.get("chemistry")
    english = request.json.get("english")
    computer = request.json.get("computer")
    biology = request.json.get("biology")
    
    k = Marks()
    
    # Only update the fields that are provided (not None)
    k.update_marks(
        rollno,
        examid,
        maths=maths if maths is not None else None,
        physics=physics if physics is not None else None,
        chemistry=chemistry if chemistry is not None else None,
        english=english if english is not None else None,
        computer=computer if computer is not None else None,
        biology=biology if biology is not None else None
    )

    instance.ask('Update marks  '+str(k.view_marks(rollno,examid)))
    
    return jsonify({})  # Return 204 No Content on successful update

@app.route("/fetch_all_marks")
def fetch_all_marks():
    k = Marks()
    marks = k.fetch_all_marks()
    return jsonify(marks)  # Return all marks


@app.route("/fetch_marks_by_student_and_exam", methods=["POST"])
def fetch_marks_by_student_and_exam():
    rollno = request.json.get("rollno")
    examid = request.json.get("examid")
    
    k = Marks()
    marks = k.view_marks(rollno, examid)
    return jsonify(marks)  # Return marks for the specific student and exam

@app.route("/fetch_marks_by_exam", methods=["POST"])
def fetch_marks_by_exam():
    examid = request.json.get("examid")
    k = Marks()
    marks = k.fetch_marks_by_exam(examid)
    return jsonify(marks)  # Return marks for the specific exam

@app.route("/fetch_marks_by_student", methods=["POST"])
def fetch_marks_by_student():
    rollno = request.json.get("rollno")
    k = Marks()
    marks = k.fetch_marks_by_student(rollno)
    print(marks)
    return jsonify(marks)  # Return marks for the specific student


@app.route("/delete_marks", methods=["POST"])
def delete_marks():
    rollno = request.json.get("rollno")
    examid = request.json.get("examid")
    instance.ask('delete marks of rollno '+str(rollno)+' examid '+str(examid))
    k = Marks()
    k.delete_marks(rollno, examid)
    return jsonify({})



@app.route('/profile/<roll>')
def prof(roll):
    return render_template('profile.html', roll=str(roll))

if __name__ == "__main__":
    app.run(debug=True)
