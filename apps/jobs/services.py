from .models import Job


def create_job(title, description, salary, country, status, external_id=None) -> Job:
    external_id = external_id.strip() if external_id else None
    if external_id:
        existing_job = Job.objects.filter(external_id=external_id).first()
        if existing_job:
            return existing_job

    return Job.objects.create(
        title=title,
        description=description,
        salary=salary,
        country=country,
        status=status,
        external_id=external_id,
    )
