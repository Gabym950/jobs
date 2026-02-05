import pytest
from rest_framework.test import APIClient
from .models import Job


@pytest.fixture
def client():
    return APIClient()

@pytest.mark.django_db
def test_create_job_success(client):
    payload = {
        "title": "Software Engineer",
        "description": "Develop and maintain software applications.",
        "salary": 90000,
        "country": "US",
        "status": "OPEN"
    }
    response = client.post("/jobs/", data=payload, format="json")
    assert response.status_code == 201
    assert response.data["title"] == payload["title"]
    assert response.data["description"] == payload["description"]
    assert response.data["salary"] == '90000.00'
    assert response.data["country"] == payload["country"]
    assert response.data["status"] == payload["status"]

@pytest.mark.django_db
def test_create_job_invalid_country_choice(client):
    payload = {
        "title": "Software Engineer",
        "description": "Develop and maintain software applications.",
        "salary": 90000,
        "country": "XX",  # Invalid country code
        "status": "OPEN"
    }
    response = client.post("/jobs/", data=payload, format="json")
    assert response.status_code == 400
    assert "country" in response.data


	# 3.	GET list (200 + devuelve items)
	# 4.	GET detail (200)
	# 5.	PATCH update OK (200 + cambia en DB)
	# 6.	PATCH con choice inválida (400)
	# 7.	DELETE (204)


@pytest.mark.django_db
def test_get_jobs_list_returns_items(client):
    Job.objects.create(title="Dev A", description="A", salary=50000, country="US", status="OPEN")
    Job.objects.create(title="Dev B", description="B", salary=60000, country="CA", status="OPEN")
    response = client.get("/jobs/")
    assert response.status_code == 200
    assert len(response.data) >= 2
    titles = [j["title"] for j in response.data]
    assert "Dev A" in titles
    assert "Dev B" in titles


@pytest.mark.django_db
def test_get_job_detail(client):
    job = Job.objects.create(title="Detail Job", description="Desc", salary=70000, country="GB", status="OPEN")
    response = client.get(f"/jobs/{job.id}/")
    assert response.status_code == 200
    assert response.data["id"] == job.id
    assert response.data["title"] == job.title


@pytest.mark.django_db
def test_patch_update_job_success(client):
    job = Job.objects.create(title="Old Title", description="Old", salary=80000, country="US", status="OPEN")
    payload = {"title": "New Title", "salary": 85000}
    response = client.patch(f"/jobs/{job.id}/", data=payload, format="json")
    assert response.status_code == 200
    job.refresh_from_db()
    assert job.title == "New Title"
    assert str(job.salary) == '85000.00'


@pytest.mark.django_db
def test_patch_invalid_choice_returns_400(client):
    job = Job.objects.create(title="Test", description="Test", salary=50000, country="US", status="OPEN")
    payload = {"country": "XX"}  # invalid country
    response = client.patch(f"/jobs/{job.id}/", data=payload, format="json")
    assert response.status_code == 400
    assert "country" in response.data


@pytest.mark.django_db
def test_delete_job_returns_204(client):
    job = Job.objects.create(title="To Delete", description="Delete me", salary=40000, country="AR", status="OPEN")
    response = client.delete(f"/jobs/{job.id}/")
    assert response.status_code == 204
    assert not Job.objects.filter(pk=job.id).exists()
