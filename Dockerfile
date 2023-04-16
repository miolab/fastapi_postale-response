FROM --platform=linux/x86_64 python:3.11-slim

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

COPY ./app /app
COPY pyproject.toml poetry.lock ./

RUN pip install poetry==1.4.2
RUN poetry config virtualenvs.create false \
  && poetry install

EXPOSE 80

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
