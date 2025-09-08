from flask import Flask, render_template, request
import os
import click
from app import db





def get_random_settlement(data, selected_religions, selected_devoutness):
    clauses = []
    params = []

    if selected_religions:
        placeholders = ",".join(["?"] * len(selected_religions))
        clauses.append(f"religion IN ({placeholders})")
        params.extend(selected_religions)

    if selected_devoutness:
        placeholders = ",".join(["?"] * len(selected_devoutness))
        clauses.append(f"devout IN ({placeholders})")
        params.extend(selected_devoutness)

    where_clause = " AND ".join(clauses) if clauses else "1=1"


    query = f"""
        SELECT * FROM settelments
        WHERE {where_clause}
        ORDER BY RANDOM()
        LIMIT 1
    """
    print (query)
    print (params)

    row = data.execute(query, params).fetchone()
    return dict(row) if row else None


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
    def index():
        chosen = None
        message = None

        if request.method == 'POST':
            data = db.get_db()  # your db cursor/connection

            selected_religions = request.form.getlist("religion")
            selected_devoutness = request.form.getlist("devout")

            if not selected_religions and not selected_devoutness:
                message = "אנא בחר לפחות אפשרות אחת."
            elif not selected_religions:
                message = "אנא בחר לפחות אפשרות אחת עבור דת."
            elif not selected_devoutness:
                message = "אנא בחר לפחות אפשרות אחת עבור רמת דתיות."
            else:
                chosen = get_random_settlement(data, selected_religions, selected_devoutness)
                print (chosen)
                if not chosen:
                    message = "לא נמצאו יישובים מתאימים."
                    

        return render_template("index.html", settlement=chosen, message=message)


    return app


