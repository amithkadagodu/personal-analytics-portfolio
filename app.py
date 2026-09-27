from flask import Flask, render_template, request, flash, redirect, url_for
from database import update_basic_details, get_basic_details

app = Flask(__name__)

app.secret_key = "portfolio-secret-key-123"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/admin" , methods=["GET", "POST"])
def admin():
    message = None
    if request.method == "POST":
        first_name = request.form["firstname"]
        last_name = request.form["lastname"]
        phone_number = request.form["phone"]
        email_address =  request.form["email"]
        linkedin = request.form["linkedin"]
        github = request.form["github"]

        result = update_basic_details(first_name,last_name,phone_number,email_address,linkedin,github)

        if result == "success":
            flash("Successfully Updated!")

        return redirect(url_for("admin"))

    basic_details = get_basic_details()

    return render_template("admin/admin.html", basic_details=basic_details)

if __name__ == "__main__":
    app.run(debug=True)