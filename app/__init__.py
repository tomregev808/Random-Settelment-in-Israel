from flask import Flask, render_template, request
import os
import click
from app import db







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

    @app.cli.command("init-db")
    def init_db_command():
        """Clear the existing data and create new tables."""
        db.init_db()
        click.echo("Initialized the database.")


    @app.route('/', methods=['GET', 'POST'])
    def index ():
            
            if request.method == 'POST':
                data = db.get_db()

                chosen = data.execute ("SELECT * FROM settelments ORDER BY RANDOM() LIMIT 1;").fetchall()


                print (chosen [0] ['name'])
                return render_template("index.html", settlement=chosen)
            return render_template("index.html")



    return app


