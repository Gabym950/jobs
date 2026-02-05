# Jobs API

Minimal Django REST API for managing job offers.

The project focuses on clear backend structure, business logic separation and
testable behavior using Django and Django REST Framework.

---

## Features

- Create job offers
- Search jobs by keyword in the job title
- Basic listing and detail endpoints

---

## API

### Create job

POST /jobs/

Example:

```json
{
  "title": "Software Engineer",
  "description": "Develop and maintain software applications",
  "salary": 90000,
  "country": "US",
  "status": "OPEN"
}
```

---

### Search jobs

GET /jobs/search/?q=engineer

The search is case-insensitive and matches job titles.

---

## Project structure

```text
apps/jobs/
    models.py
    serializer.py
    views.py
    services.py
    tests.py
```

- models.py contains persistence models.
- serializer.py handles request/response validation.
- views.py exposes the HTTP API.
- services.py contains application and business rules.
- tests.py contains API and behavior tests.

---

## Tests

The project includes API tests using pytest and Django REST Framework’s test tools.

Main scenarios covered:

- job creation
- validation errors
- listing and detail endpoints
- update and delete operations

---

## Installation

```bash
python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt -r requirements-dev.txt
```

```bash
python manage.py migrate
python manage.py runserver
```

---

## Running tests

```bash
pytest
```

---

## Example usage

Create a job:

```bash
curl -X POST http://localhost:8000/jobs/   -H "Content-Type: application/json"   -d '{
    "title": "Backend Engineer",
    "description": "Build APIs",
    "salary": 80000,
    "country": "AR",
    "status": "OPEN"
  }'
```

Search jobs:

```bash
curl "http://localhost:8000/jobs/search/?q=backend"
```
