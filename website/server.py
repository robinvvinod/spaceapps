from flask import Flask, render_template, request, redirect, jsonify

app = Flask(__name__)


@app.route("/")
def root():
    return render_template("projectionmap.html")


@app.route('/pred')
def pred():
    return render_template('predictionmap.html')


@app.route('/risk')
def risk():
    return render_template('riskprofile.html')


if __name__ == "__main__":
    app.run(debug=True)
