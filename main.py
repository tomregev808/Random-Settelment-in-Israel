import requests


import random
from flask import Flask
import os

def get_name ():


    d = requests.get ("https://data.gov.il/api/3/action/datastore_search?resource_id=5c78e9fa-c2e2-4771-93ff-7f400a12f7ba")

    dict = d.json()

    list = dict["result"]["records"]
    list.pop(0)

    names = []
    for record in list:
        names.append (record ["שם_ישוב"])

    name = random.choice(names)

    return name




def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'db.sqlite'),
    )
    if test_config is None:
        app.config.from_pyfile('config.py', silent = True)
    else:
        app.config.from_mapping (test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/', methods=['get', 'post'])
    def index ():
        return (get_name())

    return app


