from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    return f"<h1>Thank you, {name}!</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
