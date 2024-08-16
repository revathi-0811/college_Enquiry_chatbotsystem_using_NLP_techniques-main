from flask import *
import sqlite3
from flask_cors import CORS

# Import the get_response function from the chat module
# Replace 'chat' with the actual module name.
from chat import get_response

app = Flask(_name_)
CORS(app)

@app.route("/")  # Use the route decorator instead of app.get
def index_get():
    return render_template("main.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle the login form submission here
        pass
    return render_template('login.html')

@app.route("/base")
def base():
    return render_template("base.html")


@app.route("/feedback")
def feedback():
    return render_template("feedback.html")


'''
@app.route("/predict", methods=["POST"])  # Specify the HTTP method
def predict():
    # Get the message from the JSON request
    data = request.get_json()
    message = data.get("message")

    # Call the get_response function to get a response
    response = get_response(message)

    if response=="Sorry I do not understand...":
        try:
            query = request.form["query"]
            with sqlite3.connect("college.db") as con:
                cur = con.cursor()
                cur.execute("INSERT into unanswered (question) VALUES (?)", (query))
                con.commit()
                msg = "Question successfully Added"
        except sqlite3.Error as e:
            con.rollback()
            msg = "Error: " + str(e)
        finally:
            con.close()
            return render_template("base.html")
         
    # Create a response dictionary
   
   
    result = {"answer": response}
    

    # Return the response as JSON
    return jsonify(result)
   
'''
#exatra
@app.route("/feedbacksave",methods = ["GET","POST"])  
def feedBackSave():  
    msg = "msg"  
    if request.method == "POST":  
        try:  
            query = request.form["query"]

            with sqlite3.connect("college.db") as con:  
                cur = con.cursor()  
                cur.execute("INSERT into Unanswereds (question) VALUES (?)",(query,))  
                con.commit()  
                msg = "query successfully Added"  
        except sqlite3.Error as e:  
            con.rollback()  
            msg = "We can not add the query to the list " + str(e)
        finally:  
            return render_template("success_unanswered_queries.html", msg=msg)  
            con.close()  

#extra  
            
@app.route("/feedbackdlt", methods=["POST"])
def feedbackdlt():

    id = request.form["query"]
    try:
        with sqlite3.connect("college.db") as con:
            cur = con.cursor()
            cur.execute("DELETE FROM Unanswereds WHERE serial_no = ?", (id,))
            con.commit()  # Commit the changes to the database
            msg = "Record successfully deleted"
    except sqlite3.Error as e:
        msg = "Can't be deleted: " + str(e)
    else:
        con.close()
        return render_template("unanswered_queries.html")






@app.route("/predict", methods=["POST"])
def predict():
    # Get the message from the JSON request
    data = request.get_json()
    message = data.get("message")

    # Call the get_response function to get a response
    response = get_response(message)

    if response == "Sorry I do not understand...":
        try:
            query = message  # Use the message instead of request.form["query"]

            with sqlite3.connect("college.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO unanswered (question) VALUES (?)", (query))
                con.commit()
                msg = "Question successfully Added to unanswered queries"
        except sqlite3.Error as e:
            con.rollback()
            msg = "Error: " + str(e)
        finally:
            con.close()
    
    result = {"answer": response}

    # Return the response as JSON
    return jsonify(result)

@app.route("/admin_login")
def admin_login():
    return render_template("admin_login.html")


@app.route("/savedetails", methods=["GET", "POST"])  # Specify the allowed methods
def add():
    if request.method == "POST":
        try:
            User = request.form["userid"]
            password = request.form["pass"]

            with sqlite3.connect("college.db") as con:
                cur = con.cursor()
                cur.execute("INSERT into students (UserId, password) VALUES (?, ?)", (User, password))
                con.commit()
                msg = "Student successfully Added"
        except sqlite3.Error as e:
            con.rollback()
            msg = "Error: " + str(e)
        finally:
            con.close()
            return render_template("success.html", msg=msg)
    return render_template("add.html")
#list of users

@app.route("/view")
def view():
    con = sqlite3.connect("college.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    con.close()
    return render_template("view.html", rows=rows)
#view queries
@app.route("/unanswered")
def unanswered():
    con = sqlite3.connect("college.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM Unanswereds")
    rows = cur.fetchall()
    con.close()
    return render_template("unanswered_queries.html", rows=rows)


@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/delete")
def delete():
    return render_template("delete.html")

@app.route("/deleterecord", methods=["POST"])
def deleterecord():
    id = request.form["userid"]
    try:
        with sqlite3.connect("college.db") as con:
            cur = con.cursor()
            cur.execute("DELETE FROM students WHERE UserId = ?", (id,))
            con.commit()  # Commit the changes to the database
            msg = "Record successfully deleted"
    except sqlite3.Error as e:
        msg = "Can't be deleted: " + str(e)
    else:
        con.close()
        return render_template("delete_record.html", msg=msg)




if _name_ == "_main_":
    app.run(debug=True)