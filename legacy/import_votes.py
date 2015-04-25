from quotes.models import Quote, Vote
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from urllib.request import urlopen
from datetime import datetime

def download_votes(url):
    with urlopen(url) as f:
        for line in f:
            line = line.strip().decode('utf-8')
            if not line:
                continue
            hash, ip = line.split(',')
            try:
                quote = Quote.objects.get(legacy_hash=hash)
            except ObjectDoesNotExist:
                continue
            yield Vote(voter=ip, quote=quote)


def save_votes(votes):
    for vote in votes:
        try:
            vote.save()
        except IntegrityError:
            continue


