from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
    {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 1,00,000'
    },

    {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Delhi, India',
    'salary': 'Rs. 1,30,000'
    },

    {
    'id': 3,
    'title': 'Frontend Engineer ',
    'location': 'Remote',

    },

    {
        'id': 4,
        'title': 'Backend Engineer ',
        'location': 'Remote',
        'salary': 'Rs. 1,80,000'
    }
]

@app.route("/")
def hello_world():
   return render_template('home.html', jobs=JOBS)
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
