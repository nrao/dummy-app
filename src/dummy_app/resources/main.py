import importlib
import os

from flask import Blueprint
import flask


main = Blueprint("main", __name__)

@main.route("/")
def root():
    version = importlib.metadata.version("dummy_app")
    sample_var = os.getenv("SAMPLE_VAR", "UNSET")
    return flask.render_template("main.html", version=version, sample_var=sample_var)
