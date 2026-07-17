#!/bin/bash -e

SCRIPT_NAME=/subdir gunicorn --config gunicorn_dev_config.py 'dummy_app:init_app()'
