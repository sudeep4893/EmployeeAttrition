from flask import Flask
from flask import render_template
from flask import request
#from flask import jsonify

app = Flask(__name__)
    
@app.route("/")
def show_home():
    return render_template("login.html")

@app.route("/page_case_eval", methods=["GET"])
def server_page_case_eval():
    # check cookie, fill template
    return render_template("case_eval.html")

@app.route("/page_eda", methods=["GET"])
def server_page_eda():
    # check cookie, fill template
    return render_template("eda.html")

@app.route("/page_dynamic_prediction", methods=["GET"])
def server_page_dynamic_prediction():
    # check cookie, fill template
    return render_template("dynamic_prediction.html")    
  
@app.route("/logout", methods=["GET"])
def server_logout():
    # check cookie, fill template
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def server_login():
    email = str(request.form["email"])
    password = str(request.form["password"])
    print ("email : " + str(email))
    print ("password : " + str(password))
    # query db here and return appropriate template
    # start session
    if email == "pranav_kelkar@persistent.com" and password == "password":
        return render_template("eda.html")
    else:
        return render_template("relogin.html")

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0',port=8880)
    
