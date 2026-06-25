# Release Engineering Dummy App

A minimal app for testing and demoing GitOps processes.

## App
The app runs a simple webserver and has two endpoints:

- `/healthz` returns a json object containing the app version as a string
- `/` displays a very simple web page that also has the app version, as well as content that is set via environment variables

### Environment Variables

The following environment variables can be set in the built container image, or locally in a `.env` file:

| Variable | Default | Valid Values | Description |
| --- | --- | --- | --- |
| `SAMPLE_VAR` | `"UNSET"` | Any string | A text value that is displayed on the webpage |
| `COLOR` | `none` | `none`, `yellow`, `orange`, `red`, `magenta`, `violet`, `blue`, `cyan`, `green` | Sets the background color of the webpage. Valid values are the (non-`base`) [Solarized](https://ethanschoonover.com/solarized/) color names (e.g. `blue`, `red`, `cyan`, etc.) |

### Progress
-  CI/CD
    - [x] code updates
    - [x] unit testing
    - [x] containerized artifact
    - [x] GitHub action(s) to build & push container
- Environment definitions
    - [x] Environment variables
- GitOps Delivery
    - [x] helm chart
    - [ ] smoke tests

# Development
Install development dependencies
```bash
pip install -e '.[all]'
```

Run app in dev mode
```bash
gunicorn --reload 'dummy_app:init_app()'
```
