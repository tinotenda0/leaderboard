from flask import Flask, render_template, request
import requests

app = Flask(__name__)
URL = "https://leaderboard-server-n4pf.onrender.com/submit"

@app.route("/", methods=["GET", "POST"])
def index():
    name = None
    score = None
    resp_text = None
    status = None

    if request.method == "POST":
        name = request.form.get("name")  # safe access
        score = request.form.get("score")
        if name and score:
            try:
                r = requests.post(URL, json={"name": name, "score": score}, timeout=10)
                resp_text = r.text
                status = r.status_code
            except requests.RequestException as e:
                resp_text = f"Request failed: {e}"
                status = 502

    return render_template("index.html", name=name, score=score, response=resp_text, status=status)

if __name__ == "__main__":
    app.run(debug=True)
