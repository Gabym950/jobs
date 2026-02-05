from django.db import models


class CountryChoices(models.TextChoices):
    US = "US", "United States"
    CA = "CA", "Canada"
    GB = "GB", "United Kingdom"
    AR = "AR", "Argentina"


class StatusChoices(models.TextChoices):
    OPEN = "OPEN", "Open"
    CLOSED = "CLOSED", "Closed"
    PAUSED = "PAUSED", "Paused"


class Job(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    salary = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    country = models.CharField(choices=CountryChoices.choices, default=CountryChoices.US)
    status = models.CharField(choices=StatusChoices.choices, default="OPEN")

    def __str__(self):
        return self.title + " - " + self.country
