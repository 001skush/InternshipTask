from flask import Flask, render_template, request, redirect, url_for
import pymysql

app = Flask(__name__)

host = "students.cszdt2jowlxz.us-east-2.rds.amazonaws.com"
port = 3306
user = "sarvesh"
password = "Sarvesh001"
db = "students"


@app.route("/add", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        student_id = request.form.get("student_id")
        # getting input with name = fname in HTML form
        first_name = request.form.get("first_name")
        # getting input with name = lname in HTML form
        last_name = request.form.get("last_name")
        current_job = request.form.get("current_job")
        location = request.form.get("location")
        if(student_id == "" or student_id == None): return render_template("Addstudenthtml.html")
        conn = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            db=db,
        )
        print(conn)
        cur=conn.cursor()
        cur.execute("INSERT INTO students (StudentID,FirstName,LastName,CurrentJob, Location) VALUES (%s,%s,%s,%s,%s)", (student_id,first_name,last_name,current_job,location))
        conn.commit()
        print(student_id + first_name + last_name + current_job + location)
        return redirect(url_for('about'))
    return render_template("Addstudenthtml.html")


@app.route("/view", methods=["GET", "POST"])
def about():
    conn = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            db=db,
        )
    cur=conn.cursor()
    query = "SELECT * from students"
    cur.execute(query)
    data = cur.fetchall()
    print(data)
    conn.close()
    return render_template("AddStudentOutputhtml.html", data=data)


if __name__ == "__main__":
    app.run(debug=True,host= '0.0.0.0')
