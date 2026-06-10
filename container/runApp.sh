#!/bin/bash -e

gunicorn --config gunicorn_config.py 'dummy_app:init_app()'
