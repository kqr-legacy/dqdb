from django.db import models


class BaseQuotesManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset() \
                      .filter(removed=False) \
                      .annotate(score=models.Count('votes'))

class LatestQuotesManager(BaseQuotesManager):
    def get_queryset(self):
        return super().get_queryset().order_by('-timestamp')

class TopQuotesManager(BaseQuotesManager):
    def get_queryset(self):
        return super().get_queryset().order_by('-score')


