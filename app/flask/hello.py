import os

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def route():
    name = "HOGE"
    # return name
    return render_template('hello.html', title='flask test', name=name)


@app.route('/<id>')
def route_id(id):
    name = id
    # return name
    return render_template('hello.html', title='flask test', name=name)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
