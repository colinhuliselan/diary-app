FROM python:3.12-slim AS builder

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip wheel --no-cache-dir --no-deps --wheel-dir wheels -r requirements.txt

COPY src src
COPY pyproject.toml pyproject.toml
RUN pip wheel --no-cache-dir --no-deps --wheel-dir wheels .


FROM python:3.12-slim AS runner

WORKDIR /app

COPY --from=builder /app/wheels /wheels
RUN pip install --no-cache /wheels/* && rm -rf /wheels
# Just for reference
EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]