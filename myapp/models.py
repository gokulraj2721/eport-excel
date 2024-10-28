from django.db import models
from django.utils import timezone

class Details(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)  # Adjust max_length as necessary
    address = models.CharField(max_length=255, blank=True)
    message = models.TextField(blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
