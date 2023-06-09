# FastAPI Postale Response

HTTP Request Endpoint mock. (for personal use)

- Versions
  ```sh
  docker run --rm -it fastapi-postale-response python -V
  ```
  > `Python 3.11.3`

  ```sh
  docker run --rm -it fastapi-postale-response uvicorn --version
  ```
  > `Running uvicorn 0.21.1 with CPython 3.11.3 on Linux`

## Example use

```sh
docker build -t fastapi-postale-response .
```

```sh
docker run --rm -p 8080:8080 -it fastapi-postale-response

INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8080 (Press CTRL+C to quit)
```

```sh
curl "http://0.0.0.0:8080" -X POST \
  -H 'Content-Type: application/json' \
  -d '{
    "status": "ping"
  }' | jq

  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100    43  100    17  100    26    141    216 --:--:-- --:--:-- --:--:--   358
{
  "status": "pong"
}
```

### Execute test

```sh
docker run --rm -it fastapi-postale-response pytest --pyargs app
```
