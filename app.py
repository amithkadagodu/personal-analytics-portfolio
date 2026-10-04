from flask import Flask, render_template, request, flash, redirect, url_for
from database import update_basic_details, get_basic_details, get_edu, update_edu, get_exp, update_exp, get_certi, update_certi, get_projects, update_projects

app = Flask(__name__)

app.secret_key = "portfolio-secret-key-123"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/admin" , methods=["GET", "POST"])
def admin():


    
    if request.method == "POST":

        form_type = request.form.get("form_type")

        if form_type=="basic_details":
            first_name = request.form["firstname"]
            last_name = request.form["lastname"]
            phone_number = request.form["phone"]
            email_address =  request.form["email"]
            linkedin = request.form["linkedin"]
            github = request.form["github"]

            if all([first_name.strip(),last_name.strip(),phone_number.strip(),email_address.strip(),linkedin.strip(),github.strip()]):
                result = update_basic_details(first_name,last_name,phone_number,email_address,linkedin,github)

                if result == "success":
                    flash("Successfully Updated!","basic_details")

            else:
                flash("All Fields are Mandatory","basic_details")
               
            return redirect(url_for("admin"))

        elif form_type=="edu_details":
            university_name = request.form["university"]
            degree_name = request.form["degree"]
            year_com = request.form["year"]


            if all([university_name.strip(),degree_name.strip(),year_com.strip()]):
                add_edu = update_edu(university_name,degree_name,year_com)
            
                if add_edu=="success":
                    flash("Education Updated!","edu_details")
            
            else:
                flash("All Fields are Mandatory. Empty Fields are not allowed","edu_details")
            
            return redirect(url_for("admin")+"#edu")

        elif form_type=="exp_details":
            company_name = request.form["company_name"]
            role = request.form["role"]
            start = request.form["start_year"]
            end = request.form["end_year"]
            current_job = request.form.get("current_job")

            if current_job=="True":
                end="Present"

            if all([company_name,role,start]):

                add_exp = update_exp(company_name,role,start,end)
                if add_exp == "success":
                    flash("Work Experience Updated!","exp_details")
            else:
                flash("Company, Role, Start are Mandatory Fields and Cannot be Empty!", "exp_details")
            
            return redirect(url_for("admin")+"#exp")

        elif form_type=="certi_details":
            certification = request.form["certification_name"]
            by = request.form["certification_with"]
            year = request.form["completed_year"]
            url = request.form["certi_url"]

            if all([certification,by,year,url]):
                add_certi = update_certi(certification,by,year,url)
                if add_certi == "success":
                    flash("Certification Added!","certi_details")
            
            else:
                flash("Fields Cannot be Empty!","certi_details")
            
            return redirect(url_for("admin")+"#certi")

        elif form_type=="proj_details":
            name = request.form["project_name"]
            url = request.form["project_url"]

            if all([name,url]):
                add_proj = update_projects(name,url)
                if add_proj =="success":
                    flash("Project Added!","proj_details")
            else:
                flash("Both Fields are Mandatory! Cannot be left empty while Submitting","proj_details")

            return redirect(url_for("admin")+"#proj")


    basic_details = get_basic_details()

    edu_details = get_edu()

    exp_details = get_exp()

    certi_details = get_certi()

    proj_details = get_projects()

    return render_template("admin/admin.html", basic_details=basic_details, edu_details = edu_details, exp_details=exp_details, certi_details=certi_details, proj_details=proj_details)

if __name__ == "__main__":
    app.run(debug=True)