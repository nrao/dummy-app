FROM python:3.12-slim

LABEL org.opencontainers.image.title="NRAO Release Engineering Dummy App"
LABEL org.opencontainers.image.description="A minimal app for testing and demoing GitOps processes"
LABEL org.opencontainers.image.vendor="Associated Universities, Inc. Washington DC, USA"
LABEL org.opencontainers.image.url="https://public.nrao.edu/"
LABEL org.opencontainers.image.licenses="BSD-3-Clause"
LABEL org.opencontainers.image.source="https://github.com/nrao/dummy-app" 

WORKDIR /app

COPY pyproject.toml README.md src/ container/ ./
RUN chmod +x runApp.sh

RUN pip install --upgrade pip && \
    pip install -e '.[all]'

# https://github.com/docker/buildx/issues/2751
ENV PYTHONPATH="${PYTHONPATH}:/app"

ENV SAMPLE_VAR=docker_default
ENV COLOR=green

EXPOSE 5000

CMD ["./runApp.sh"]
