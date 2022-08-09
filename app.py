import pyodbc
from datetime import datetime
from flask import Flask, Request,redirect, render_template, request, flash


app = Flask(__name__, template_folder="templates")
connection = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};Server=tcp:adbsai.database.windows.net,1433;Database=adb;Uid=sainath;Pwd=Shiro@2018;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30')
cursor = connection.cursor() 


@app.route('/', methods=['POST', 'GET'])
def Hello():
    return render_template('index.html')

@app.route('/Student', methods=['POST', 'GET'])
def Student():
    cursor = connection.cursor()
    query_str = "select * from MSGS a " 
    print(query_str)
    cursor.execute(query_str+" ORDER BY a.DATE")
    data = cursor.fetchall()
    return render_template('Student.html', data = data)

@app.route('/StudentMessage', methods=['POST', 'GET'])
def StudentMessage():
    cursor = connection.cursor()
    msg = request.form.get("Message")
    query_str = "select * from MSGS a " 
    now = datetime.now()
    formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
    query_str = "INSERT INTO MSGS(ROLE, MESSAGE, DATE) VALUES('STUDENT','"+msg+"','"+formatted_date+"')"
    print(query_str)
    cursor.execute(query_str)
    cursor.commit()

    # query_str = "select * from MSGS a " 
    # print(query_str)
    # cursor.execute(query_str+" ORDER BY a.DATE")
    # data = cursor.fetchall()


    return redirect("https://adbsainathquiz5.azurewebsites.net/Student")


@app.route('/TeacherMessage', methods=['POST', 'GET'])
def TeacherMessage():
    cursor = connection.cursor()
    msg = request.form.get("Message")
    query_str = "select * from MSGS a " 
    now = datetime.now()
    formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
    query_str = "INSERT INTO MSGS(ROLE, MESSAGE, DATE) VALUES('TEACHER','"+msg+"','"+formatted_date+"')"
    print(query_str)
    cursor.execute(query_str)
    cursor.commit()

    # query_str = "select * from MSGS a " 
    # print(query_str)
    # cursor.execute(query_str+" ORDER BY a.DATE")
    # data = cursor.fetchall()


    return redirect("https://adbsainathquiz5.azurewebsites.net/Teacher")

@app.route('/Teacher', methods=['POST', 'GET'])
def Teacher():
    cursor = connection.cursor()
    query_str = "select * from MSGS a " 
    print(query_str)
    cursor.execute(query_str+" ORDER BY a.DATE")
    data = cursor.fetchall()
    return render_template('teacher.html', data = data)

@app.route('/Admin', methods=['POST', 'GET'])
def Admin():
    cursor = connection.cursor()
    query_str = "select * from MSGS a " 
    print(query_str)
    cursor.execute(query_str+" ORDER BY a.DATE")
    data = cursor.fetchall()
    return render_template('Student.html', data = data)


    

if __name__ == '__main__':    
    app.run()

