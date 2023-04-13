FROM python:3.11-slim

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

COPY ./app /app

RUN pip install \
  fastapi==0.95.0 \
  uvicorn \
  pydantic \
  pytest \
  httpx

EXPOSE 80

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
