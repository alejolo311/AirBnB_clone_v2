#!/usr/bin/python3
"""start flask and set a route"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """main route return"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """return in other route"""
    return 'HBNB'


@app.route('/c/<var>', strict_slashes=False)
def c(var):
    """Returns  in c"""
    return 'C %s' % var.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """Returns in python"""
    return 'Python %s' % text.replace('_', ' ')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
