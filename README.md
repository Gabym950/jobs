# Job Management API

Backend API to manage job postings and applications, designed with a focus on clean architecture, scalability, and real-world backend practices.

---

## 🚀 Overview

This project simulates a real-world backend system where companies can publish job offers and candidates can interact with them.

It focuses on building a maintainable API structure, handling business logic clearly, and preparing the system to scale with new features.

---

## 🧩 Features

- Create, update, and delete job postings
- List and retrieve jobs
- Search jobs by title (`?q=python`)
- Filter jobs by status and other fields
- Pagination support
- Authentication with JWT
- Structured error handling
- API documentation with Swagger/OpenAPI

---

## 🛠️ Tech Stack

- Python
- Django
- Django REST Framework
- PostgreSQL
- Docker
- drf-spectacular (Swagger/OpenAPI)
- SimpleJWT (authentication)
- django-filter

---

## 🏗️ Architecture

The project is structured to separate concerns and keep business logic independent:

- **Views** → Handle HTTP layer
- **Services** → Business logic
- **Models** → Data layer
- **Serializers** → Data validation and transformation

This approach makes the code easier to maintain, test, and extend.

---

## 🔍 API Examples

### Get all jobs

```
GET /jobs/
```

---

### Search jobs

```
GET /jobs/?q=python
```

Returns jobs filtered by title using case-insensitive search.

---

### Filter jobs

```
GET /jobs/?status=OPEN
```

---

### Pagination

```
GET /jobs/?page=2&page_size=10
```

---

## 🔐 Authentication

This API uses JWT authentication.

Example:

```
Authorization: Bearer <your_token>
```

---

## 📄 API Documentation

Swagger UI available at:

```
/api/schema/swagger-ui/
```

---

## 🧪 Testing

Run tests with:

```bash
pytest
```

---

## 🐳 Run with Docker

```bash
docker-compose up --build
```

---

## 🎯 What I focused on

- Designing clean and maintainable backend architecture
- Separating business logic from framework logic
- Building scalable and extensible APIs
- Handling real-world backend scenarios (search, filtering, pagination)
- Keeping the system ready for future growth

---

## 🚧 Possible Improvements

- Add background jobs for async processing
- Introduce event-driven patterns
- Improve observability (logging, tracing)
- Add role-based permissions
- CI/CD pipeline improvements

---

## 📌 Notes

This project is intended as a portfolio piece to demonstrate backend engineering skills and architectural thinking rather than a fully production-ready system.
