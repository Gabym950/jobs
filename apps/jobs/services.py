from .models import Job

def create_job(title, description, salary, country, status) -> Job:
    title = title.strip()

    return Job.objects.create(
        title=title,
        description=description,
        salary=salary,
        country=country,
        status=status
    )