from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/jackets/")
def jackets():
    return render_template("jackets.html")


@app.route("/shoes/")
def shoes():
    return render_template("shoes.html")


@app.route("/cloath/")
def cloath():
    return render_template("cloath.html")


if __name__ == "__main__":
    app.run(debug=True)
