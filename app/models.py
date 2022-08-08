from django.db import models
from django.contrib.auth.models import User


class Lead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    details = models.CharField(max_length=500, blank=False)
    lead_owner = models.ForeignKey(
        User, related_name="lead", on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)