import os
from flask import Flask, render_template, request

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024  # small form-only requests

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("student_name", "").strip()
        roll_no = request.form.get("roll_no", "").strip()
        if not name or not roll_no:
            return render_template("index.html", error="Please enter both name and roll number."), 400
        if len(name) > 80 or len(roll_no) > 40:
            return render_template("index.html", error="Name must be 80 characters or fewer and roll number 40 characters or fewer."), 400
        return render_template("invitation.html", name=name, roll_no=roll_no)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=False)
