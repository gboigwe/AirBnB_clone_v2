#!/usr/bin/python3
"""
Code to run web templateon flask with port 0.0.0.0:5000
"""
from flask import Flask, render_template
from models import storage
from os import environ


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def tearown_db(exception):
    """Removig current session of SQLAlchemy
    """
    storage.close()


@app.route('/states_list')
def states_list():
    """Displaying the list of an HTML page in State objects"""
    states = sorted(storage.all('State').values(), key=lambda x: x.name)
    return render_template('states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
