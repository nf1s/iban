FROM python:3.10.5-slim AS builder
COPY Pipfile .
COPY Pipfile.lock .
RUN pip install pipenv
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --dev


FROM python:3.10.5-slim
ENV PYTHONUNBUFFERED=1
COPY --from=builder /.venv /.venv
ENV PATH="/.venv/bin:$PATH"
RUN useradd -d /app --create-home app
COPY --chown=app:app . /app
USER app
WORKDIR /app

CMD ["uvicorn", "main:app"]
