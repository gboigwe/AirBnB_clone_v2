#!/usr/bin/python3
"""
Code to run web templateon flask with port 0.0.0.0:5000
"""
from flask import Flask, render_template
from models import storage
from models.state import State
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
    path = '7-states_list.html'
    states = storage.all(State)
    # sort State object alphabetically by name
    sorted_states = sorted(states.values(), key=lambda state: state.name)
    return render_template(path, sorted_states=sorted_states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
