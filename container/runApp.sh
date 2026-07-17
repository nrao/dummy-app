#!/bin/bash -e

export SCRIPT_NAME="${CONTEXT_PATH:-/}"
gunicorn --config gunicorn_config.py 'dummy_app:init_app()'
