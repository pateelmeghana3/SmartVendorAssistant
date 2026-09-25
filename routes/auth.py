from flask import Blueprint, render_template, request, redirect, session

from models.user import (
    user_exists,
    create_user,
    login_user,
    verify_security_answer,
    update_password
)

# ==========================================================
# CREATE BLUEPRINT
# ==========================================================

auth_bp = Blueprint("auth", __name__)


# ==========================================================
# HOME
# ==========================================================

@auth_bp.route("/")
def home():
    return redirect("/login")


# ==========================================================
# SIGNUP (UPDATED WITH SECURITY QUESTION)
# ==========================================================

@auth_bp.route("/signup", methods=["GET", "POST"])
def signup():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]
        security_question = request.form["security_question"]
        security_answer = request.form["security_answer"]

        if user_exists(username):
            return "User already exists"

        create_user(username, password, security_question, security_answer)

        return redirect("/login")

    return render_template("signup.html")


# ==========================================================
# LOGIN
# ==========================================================

@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        user = login_user(username, password)

        if user:
            session["user"] = username
            return redirect("/dashboard")

        return "Invalid Username or Password"

    return render_template("login.html")


# ==========================================================
# FORGOT PASSWORD (NEW)
# ==========================================================

@auth_bp.route("/forgot_password", methods=["GET", "POST"])
def forgot_password():

    if request.method == "POST":

        username = request.form["username"]
        answer = request.form["security_answer"]
        new_password = request.form["new_password"]

        user = verify_security_answer(username, answer)

        if not user:
            return "❌ Invalid username or security answer"

        update_password(username, new_password)

        return redirect("/login")

    return render_template("forgot_password.html")


# ==========================================================
# LOGOUT
# ==========================================================

@auth_bp.route("/logout")
def logout():

    session.pop("user", None)

    return redirect("/login")