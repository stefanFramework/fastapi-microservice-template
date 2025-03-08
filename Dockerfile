FROM python:3.10-slim

WORKDIR /app

# Poetry
ENV POETRY_VERSION=2.1.1
ENV POETRY_VIRTUALENVS_IN_PROJECT=true
RUN pip install "poetry==$POETRY_VERSION"

ENV PYTHONPATH=/app

# Install psycopg2 dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    libpq-dev \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*


COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root

COPY . .

EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

