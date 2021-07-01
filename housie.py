import random
from flask import Flask, request, session, render_template 

app = Flask(__name__)
app.secret_key = b"\xdb\xd8\xcb)@\xbbi\xcc\xd4\xb8\xbcz+5]g\xb6\x1d\xf3\xf4'\xf7\x82["

@app.route('/')
def index():
    session['numbers'] = random.sample(range(1,91),90)
    session['count'] = 0
    return render_template('index.html', nums=['0'])

@app.route('/startnew')
def startnew():
    global numbers, count
    session['count'] = 0
    session['numbers'] = random.sample(range(1,91),90)
    return render_template('index.html', nums=['0'])

@app.route('/next', methods=['POST'])
def next():
    global count
    session['count'] = session['count'] + 1
    return render_template('index.html', nums=session['numbers'][:session['count']])

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81)
