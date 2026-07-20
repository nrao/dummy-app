#!/bin/bash -e

pip install -e '.[all]'

gunicorn --config gunicorn_dev_config.py 'dummy_app:init_app()'
