FROM python:3.12-alpine as builder

WORKDIR /app

COPY pyproject.toml uv.lock ./

COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

RUN uv sync


FROM python:3.12-alpine as runner

COPY --from=builder /app /app

COPY . /app

EXPOSE 5000

CMD ["uv", "run", "your_app.py"]