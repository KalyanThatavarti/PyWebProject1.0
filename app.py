from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db, load_job_from_db

app = Flask(__name__, template_folder='templates')


@app.route("/")
def hello_world():
    jobs = load_jobs_from_db()
    return render_template('home.html', jobs=jobs)

@app.route("/sitemap.xml")
def sitemap_xml():
    return render_template('sitemap.xml')

@app.route("/services")
def services():
    return render_template('services.html')


@app.route("/technologies")
def technologies():
    return render_template('technologies.html')


@app.route("/verticals")
def verticals():
    return render_template('verticals.html')


@app.route("/job/<id>", methods=['POST', 'GET'])
def show_job(id):
    job = load_job_from_db(id)
    if not job:
        return "Not Found", 404
    return render_template('jobpage.html', job=job)
@app.route("/job/<id>/apply", methods=['POST', 'GET'])
def apply_to_job(id):
    data = request.form
    jobs = load_job_from_db(id)
    return render_template('application_submitted.html', application=data, jobs=jobs)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
