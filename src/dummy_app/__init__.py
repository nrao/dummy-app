import logging
import os
import sys

from dotenv import load_dotenv
from flask import Flask

log = logging.getLogger(__name__)

def init_app(app_config=None):
    load_dotenv()

    app = Flask(__name__, instance_relative_config=False)

    app.config["LOG_LEVEL"] = os.getenv("LOG_LEVEL", "ERROR")

    if app_config:
        app.config.update(app_config)

    ## Setup logging
    match app.config["LOG_LEVEL"]:
        case _:
            level = logging.ERROR

    root = logging.getLogger("dummy_app")
    root.setLevel(level)

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(level)

    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")
    handler.setFormatter(formatter)
    root.addHandler(handler)

    with app.app_context():
        from .resources.main import main
        app.register_blueprint(main)

        from .resources.healthz import healthz
        app.register_blueprint(healthz)

        return app
