# Release Engineering Dummy App

A minimal app for testing and demoing GitOps processes.

## App
The app runs a simple webserver and has two endpoints:

- `/healthz` returns a json object containing the app version as a string
- `/` displays a very simple web page that also has the app version, as well as content that is set via an env variable `SAMPLE_VAR`

### Progress
-  CI/CD
    - [x] code updates
    - [x] unit testing
    - [x] containerized artifact
- GitOps Delivery
    - [ ] helm chart
    - [ ] smoke tests
- Environment definitions
    - [x] Environment variables

# Development
Install development dependencies
```bash
pip install -e '.[all]'
```

Run app in dev mode
```bash
gunicorn --reload 'dummy_app:init_app()'
```
