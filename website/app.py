from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/create_new")
def create_new():
    return render_template("create.html")

@app.route("/profile")
def open_profile():
    return render_template("profile.html")



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)