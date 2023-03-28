from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Account Manager',
    'location': 'United States',
    'salary': 'Commission Based'
  },
]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name='Miles Agency')


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
