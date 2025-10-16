from flask import Flask, render_template, request
import requests
app = Flask(__name__)
url = 'https://leaderboard-server-n4pf.onrender.com/submit'

@app.route('/', methods=['GET', 'POST'])
def index():
    status = None
    if request.method == 'POST':
        name = request.form['name']
        score = request.form['score']
        data = {'name': name, 'score': score}
        response = requests.post(url, json=data)
        status = response.status_code
    return render_template('index.html', name=name, score=score, response=response.text, status=status)

if __name__ == '__main__':
    app.run()


if __name__ == '__main__':
    app.run()
