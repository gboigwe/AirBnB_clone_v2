#!/usr/bin/python3
"""
Starting web application
With routings
"""

from models import storage
from models.state import State
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/cities_by_states')
def states_list():
    """Render template with states
    """
    path = '8-cities_by_states.html'
    states = storage.all(State)

    # sort State object alphabetically by name
    return render_template(path, states=states)


@app.teardown_appcontext
def the_app_tearown_db(arg=None):
    """Cleaning-up session
    """
    storage.close()


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
