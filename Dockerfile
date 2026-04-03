FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends build-essential && rm -rf /var/lib/apt/lists/*

# Ensure setuptools/pkg_resources is available (needed by rest_framework_simplejwt imports)
RUN pip install --upgrade pip setuptools==80.0.0 wheel

COPY requirements.txt requirements-dev.txt ./
RUN pip install --no-cache-dir -r requirements.txt -r requirements-dev.txt

COPY . .

CMD [ "python"]
