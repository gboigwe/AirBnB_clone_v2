#!/usr/bin/python3
"""
Code to run web templateon flask with port 0.0.0.0:5000
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Display somthing in the page"""
    return 'Hello HBNB!'


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Display somthing HBNB in page"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def the_c_text(text):
    """Displays 'C' followed by the text variable"""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def the_python_text(text='is cool'):
    """Displays Python followed by the text variable"""
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def the_display_number(n):
    """Displays 'n is a number'
    if n is an integer"""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def the_number_template(n):
    """Displays an HTML page if n is an integer"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def the_number_odd_or_even(n):
    """Displaying an HTML page if n is an integer"""
    if n % 2 == 0:
        od_ev = 'even'
    else:
        od_ev = 'odd'
    return render_template('6-number_odd_or_even.html', n=n,
            od_ev=od_ev)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
