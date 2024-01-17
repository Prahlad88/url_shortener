from django.db import models
from datetime import datetime, timedelta
from django.utils import timezone


class ShortenerTable(models.Model):
    visit_count = models.PositiveIntegerField(default=0)
    short_url = models.CharField(max_length=100, default="", primary_key=True)
    original_url = models.CharField(max_length=1000, default="")
    created_by = models.CharField(max_length=255, default="Anonymous")
    creation_date = models.DateTimeField(auto_now_add=True)
    expiry_date = models.DateTimeField(default=timezone.now() + timedelta(days=3))
    qr_code = models.CharField(max_length=10000, default="")

    def increment_visit_count(self):
        self.visit_count += 1
        self.save()


