# Jobs API – Simple backend design with Django REST Framework

Small REST API for managing job offers, designed as a minimal and pragmatic backend
example focused on clarity, testability and long-term maintainability.

---

## ✨ Scope

The API currently exposes two main use cases:

- Create a job offer
- Search jobs by a keyword in the job title

CRUD endpoints are intentionally kept minimal.

---

## 🧠 Design goals

This project focuses on:

- keeping the Django + DRF stack simple and idiomatic
- isolating business behavior from HTTP concerns
- making the code easy to evolve without introducing unnecessary layers

It intentionally avoids:

- dependency injection frameworks
- complex Clean Architecture templates
- abstract repositories for a single persistence backend

---

## 🏗 Project structure

apps/jobs/
    models.py       # Django models and choices
    serializer.py   # DRF serializers
    views.py        # API layer (ViewSet)
    services.py     # application / business logic (entry point for use cases)
    tests.py        # API and behavior tests

### Responsibilities

- models.py  
  - persistence model  
  - domain constraints through Django fields and choices

- serializer.py  
  - input/output validation and representation

- views.py  
  - HTTP layer only  
  - delegates behavior to the application layer (services)

- services.py  
  - application logic and business rules  
  - intended place for future rules (validation, invariants, workflows)

---

## 🚀 Features

### Create job

POST /jobs/

Example:

{
  "title": "Software Engineer",
  "description": "Develop and maintain software applications",
  "salary": 90000,
  "country": "US",
  "status": "OPEN"
}

---

### Search jobs by title keyword

GET /jobs/search/?q=engineer

Search is case-insensitive and matches job titles.

---

## 📌 Other available endpoints

For completeness, the API also exposes:

- list jobs
- retrieve job by id
- partial update
- delete

Those endpoints exist to support testing and basic usage, but are not the main focus of the exercise.

---

## 🧪 Tests

The project includes API-level tests using pytest and DRF’s test client.

Main scenarios covered:

- successful job creation
- invalid country choice
- list jobs
- retrieve job detail
- partial update
- invalid update
- delete job

Example file:

apps/jobs/tests.py

The tests focus on observable behavior instead of internal implementation.

---

## ⚙️ Installation

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
pip install -r requirements-dev.txt

Run migrations:

python manage.py migrate

Run the server:

python manage.py runserver

---

## ▶️ Running tests

pytest

---

## 🛠 Example usage

Create a job:

curl -X POST http://localhost:8000/jobs/ \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Backend Engineer",
    "description": "Build APIs",
    "salary": 80000,
    "country": "AR",
    "status": "OPEN"
  }'

Search jobs:

curl "http://localhost:8000/jobs/search/?q=backend"

---

## 🧩 Design notes

This project originally explored a stricter Clean Architecture structure.
For this version, the design was intentionally simplified.

The current approach follows a pragmatic separation:

- Django models and serializers handle data and validation
- the API layer is kept thin
- business logic is intended to live in a dedicated application layer (services.py)

This keeps the project:

- easy to understand
- easy to test
- easy to evolve

without introducing abstractions that are not justified by the current size of the system.

---

## 🧭 Possible next steps

Some natural extensions for this project would be:

- move creation and update logic into services.py
- introduce a small business rule (for example, default status handling or invariants)
- extract query logic (search, filters) into a dedicated query layer
- add pagination and filtering explicitly at the API boundary

These are intentionally left out to keep the current scope small and focused.
