from flask import Flask,render_template,request, jsonify
import json
from gr import Gr
with open('static/students.json', 'r+') as file:
    data = json.load(file)

app = Flask(__name__)
instance = Gr()
instance.chat.append({"role": "system",
             "content": "You are a school assistant bot who can tell details about students and teachers.You can take input from student and display information.You can also add students to your memory. You can sort students by various filters.You can also solve various homework questions.You can also add teachers and assign class teachers"})
s="Here is a list of students in this school.\n"
for x in data["students"]:
    s+=str(x)
instance.chat.append({"role":"system","content":s})
@app.route("/")
def hello_world():
    return render_template("home.html")

@app.route('/msg',methods=['POST'])
def msg():
    user_input = request.json.get("message")
    response = instance.ask(user_input)
    return jsonify({"response": response})

@app.route('/msgclear')
def clear():
    instance.chat=[]

@app.route("/student")
def st():
    return render_template('student.html')

@app.route('/add_student',methods=['POST'])
def add():
    name=request.json.get("name")
    clas=request.json.get("clas")
    stream=request.json.get("stream")
    house=request.json.get("house")
    print(name,clas,stream)
    instance.ask(f"Add this student to this school:{name},{clas},{stream},{house}")
    data["students"].append({ "name": name, "class": clas, "stream": stream, "house": house })
    with open('static/students.json', 'w') as k:
        json.dump(data, k)
    return jsonify({})

    

