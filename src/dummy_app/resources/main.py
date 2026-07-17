import importlib
import os

from flask import Blueprint, request
import flask


main = Blueprint("main", __name__)

@main.route("/")
def root():
    version = importlib.metadata.version("dummy_app")
    sample_var = os.getenv("SAMPLE_VAR", "UNSET")
    color_var = os.getenv("COLOR", "none").lower()
    if color_var in ("none", "yellow", "orange", "red", "magenta", "violet", "blue", "cyan", "green"):
        color = color_var
    else:
        color = "invalid"
    
    base_url = request.base_url
    return flask.render_template("main.html", version=version, base_url=base_url, sample_var=sample_var, color=color)
