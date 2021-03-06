from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
	name = 'index'
	return render_template("index.html",static_url_path="/static",name=name)

@app.route("/education")
def education():
	name = 'education'
	return render_template("education.html",static_url_path="/static",name=name)

@app.route("/projects")
def projects():
	name = 'projects'
	return render_template("projects.html",static_url_path="/static",name=name)


@app.route("/feedback", methods=["GET", "POST"])
def feedback():
    if request.method == "POST":
    	name = request.form.get("name")
    	email = request.form.get("email")
    	comment = request.form.get("comment")
    	return render_template("submit.html",static_url_path="/static",name=name,email = email, comment = comment)
    else:
    	name = 'feedback'
    	return render_template("feedback.html",static_url_path="/static",name=name)