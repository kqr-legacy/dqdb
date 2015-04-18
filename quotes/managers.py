from django.db import models


class LatestQuotesManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('-timestamp')

class TopQuotesManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('-score')


