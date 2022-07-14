from flask_app import app
from flask_app.models.users_model import User
from flask import redirect, render_template, request


#always use the decorator
@app.route("/")
def show_all_users():
    list_users = User.get_all()
    return render_template("all_users.html",list_users = list_users)



@app.route("/add_user")
def show_add_user():
    return render_template("add_user.html")



@app.route("/add_user",methods = ["post"])
def add_user():
    # new_user = [{"f_name": request.form["f_name"]},
    #     {"l_name":request.form["l_name"]},
    #     {"email": request.form["email"]}]

    User.create_user(request.form)
    return redirect("/")
