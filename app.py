from flask import Flask, render_template, request, jsonify
import json
from gr import Gr
from sq.sq import Students, Teachers

app = Flask(__name__)
instance = Gr()
instance.chat.append(
    {
        "role": "system",
        "content": "ALWAYS REPLY IN HTML.DO NOT TAKE ANY INPUTS FROM USERS.FOLLOW UNIFORM STYLING.You are a school assistant bot of sainik school kazhakootam who can tell details about students and teachers.You cannot modify or add students.You can display information.You can sort students by various filters.You can also solve various homework questions.You can give any details about the school.",
    }
)
k="""### **Sainik School Kazhakootam Overview**
- **Location**: Kazhakootam, Thiruvananthapuram, Kerala, India
- **Established**: January 20, 1962
- **Campus Size**: 225 acres
- **Affiliation**: Ministry of Defence, Government of India

---

### **Purpose and Concept**
- **Objective**: The school was established to prepare boys for admission to the **National Defence Academy (NDA)**, rectifying regional and class imbalances in India's officer cadre.
- The idea was proposed by **V. K. Krishna Menon**, India's first Defence Minister, in the 1950s.

### **History and Inception**
- The school started its operations in **1962** at the Pangode Army Camp, Thiruvananthapuram, with an initial intake of students in classes V to VIII.
- In **1964**, the school moved to its present campus in **Kazhakootam**, situated on a 170-foot-high laterite cliff between the **Western Ghats** and the **Arabian Sea**.
- The land was acquired with the help of **Pattom Thanu Pillai**, the then Chief Minister of Kerala.
- **Foundation Stone**: Laid by **V. K. Krishna Menon** on **February 5, 1962**.

### **School Crest, Motto, and Flag**
- **Crest Colors**:
  - **Red**: Represents the **Indian Army**.
  - **Blue**: Represents the **Indian Navy**.
  - **Sky Blue**: Represents the **Indian Air Force**.
- **Motto**: *Gyaan, Anushasan, Sahyog* (Knowledge, Discipline, Cooperation)
- **Flag**: Features horizontal stripes of red, blue, and sky blue, with the school crest in the center.

### **Governance and Administration**
- The school is managed by the **Sainik Schools Society**, an autonomous body under the **Ministry of Defence**.
- The **Board of Governors** oversees the functioning, with the **Union Defence Minister** at the helm.
- The school is led by a **Principal** of **Colonel** rank (or equivalent in the Navy or Air Force), supported by the **Vice Principal** (former Headmaster) and **Administrative Officer** (formerly the Registrar).
- The **Air Officer Commanding-in-Chief** of the Southern Air Command is the local head of the school.
  
### **Academics**
- The school offers a structured curriculum with **21 classrooms** and **state-of-the-art laboratories** for Physics, Chemistry, and Biology.
- **Computer Center** and **Science Park** are available to foster hands-on learning.
- The school has a **well-stocked library** offering a variety of books, magazines, and journals for academic and extracurricular enrichment.
  
### **Extra-Curricular Activities**
- The school provides exceptional facilities for **sports** and **arts**:
  - **Equestrian Club**: Kerala's first-ever equestrian club with riding facilities.
  - **Sports Facilities**: Swimming pool, clay tennis courts, basketball courts, volleyball courts, two FIFA-standard football grounds, two hockey courts, and gymnastics facilities.
  - **National Cadet Corps (NCC)**: A dedicated NCC unit called **SS COY NCC**.
  
### **Auxiliary Facilities**
- **Mess**: A state-of-the-art cadet’s mess can accommodate over 700 cadets at a time. The mess has an in-house bakery.
- **Other Facilities**: 
  - Laundry (Dhobi Ghat)
  - Barber Shop
  - Post Office
  - CSD Canteen
  - Cobbler services
  - Green initiatives like **pig farming** using food waste from the mess.

### **Water & Power**
- The school has a **direct water supply** pipeline from the **Aruvikkara River**.
- Dedicated **transformer facilities** ensure uninterrupted power supply.
- Potential for **solar** and **wind energy** utilization is high, and **rainwater harvesting** is implemented.

---

### **Houses (Dormitories)**
The school follows a **residential system** with cadets divided into dormitories called **Houses**. Each house is named after a significant figure in Indian history:

1. **Azad** - Chandra Shekhar Azad
2. **Veluthampi** - Velu Thampi Dalawa
3. **Manekshaw** - Sam Manekshaw
4. **Nehru** - Jawaharlal Nehru
5. **Shivaji** - Shivaji
6. **Prasad** - Rajendra Prasad
7. **Ashoka** - Ashoka the Great
8. **Rajaji** - C. Rajagopalachari
9. **Tagore** - Rabindranath Tagore
10. **Cariappa** - K. M. Cariappa
11. **Patel** - Vallabhbhai Patel
12. **Manikarnika** - Rani of Jhansi

- **Structure**: 
  - Each house consists of two wings, with approximately **60 cadets** per dormitory.
  - Every house has study halls, office rooms, and a faculty member (House Master) residing on the first floor.

### **Admission Process**
- **Classes**: Admission to **Class VI** and **Class IX** only.
- **AISSEE**: The entrance exam (All India Sainik Schools Entrance Examination) is conducted annually, typically in **January**.
- **Age Limits**: 
  - **Class VI**: Age between **10-11 years** on July 1 of the year of admission.
  - **Class IX**: Age between **13-14 years** on July 1.
- **Tests**:
  - For **Class VI**: Mathematical Knowledge Test, Language Ability Test, and Intelligence Test (based on Class V CBSE syllabus).
  - For **Class IX**: Mathematics & Science and English & Social Studies (based on Class VIII CBSE syllabus).
  
### **Notable Alumni**
- **Military and Defence**:
  - **Lt. Gen. G. M. Nair**: Commander-in-Chief of the 9 Corps.
  - **Vice Admiral Ajit Kumar P.**: Former Vice Chief of Naval Staff.
  - **Lt. Gen. Sarath Chand**: Former Vice Chief of Army Staff.
  
- **Actors**:
  - **Prithviraj Sukumaran**: Malayalam film actor, director, and producer.
  - **Indrajith Sukumaran**: Malayalam actor.
  - **Madhu Warrier**: Malayalam film actor and producer.
  
- **Other Notable Alumni**:
  - **Josy Joseph**: Investigative journalist and author.
  - **Mini Vasudevan**: Animal rights activist and Nari Shakti Puraskar winner.

---

### **Cultural Influence**
- **Films**: The school has been featured in Malayalam films like *F.I.R.* (1999) and *The Truth* (1998).
- **Documentary**: *Marching Ahead* (2014) by alumnus Jubith Namradath highlights the school’s culture and discipline.
- **Short Film**: *Neerthulliye Kaanathaya Divasam* (2017), a water conservation film directed by faculty member **Smt. Sandhya R.**, won the **Bharathan Memorial Award**.

---

Sainik School Kazhakootam continues to be a hub for fostering discipline, leadership, and academic excellence, contributing significantly to India's defence and civilian sectors.
ALWAYS GIVE DETAILS IN HTML WHEN ASKED FOR DETAILS.
"""
instance.chat.append(
    {
        "role": "system",
        "content": k,
    }
)
k=Students()
instance.chat.append(
    {
        "role": "system",
        "content": "Here is a list of students in roll, name, class_name, join_date, dob format :\n"+str(k.fetch_all_students()),
    }
)
k=Teachers()

instance.chat.append(
    {
        "role": "system",
        "content": "Here is a list of teachers in empid, name, assigned_class, join_date, dob format:\n"+str(k.fetch_all_teachers()),
    }
)

instance.chat.append(
    {
        "role": "system",
        "content": "ALWAYS REPLY IN HTML WITHOUT COLORS.GIVE ANSWER AS HTML LISTS WHEN NEEDED.TABLES MUST BE BORDERED AND ALIGNED. DO NOT TAKE ANY INPUTS FROM USERS.FOLLOW UNIFORM STYLING.",
    }
)
k.close()
del k

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
    return jsonify(Students().fetch_student_by_id(student_id))

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



if __name__ == "__main__":
    app.run(debug=True)
