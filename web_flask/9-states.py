#!/usr/bin/python3
"""
Starting web application 
With two routes process
"""

from models import storage
from models.state import State
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/states')
@app.route('/states/<id>')
def states_list(id=None):
    """
    Rendering the states template
    """
    path = '9-states.html'
    states = storage.all(State)
    return render_template(path, states=states, id=id)


@app.teardown_appcontext
def the_app_tearown_db(arg=None):
    """
    Cleaning-up session
    """
    storage.close()


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
