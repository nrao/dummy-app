FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml README.md src/ container/ ./
RUN chmod +x runApp.sh

RUN pip install --upgrade pip && \
    pip install -e '.[all]'

ENV PYTHONPATH="${PYTHONPATH}:/app"

ENV SAMPLE_VAR=docker_default

EXPOSE 5000

CMD ["./runApp.sh"]
