from django.db import models
from django.contrib.auth.models import User

from .managers import LatestQuotesManager, TopQuotesManager

class Quote(models.Model):
    text = models.TextField(unique=True)
    score = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    submitter = models.ForeignKey(User)
    legacy_hash = models.CharField(max_length=42, blank=True)

    objects = LatestQuotesManager()
    top = TopQuotesManager()

    def __str__(self):
        return self.text[:41] + '…' if len(self.text) > 42 else self.text

