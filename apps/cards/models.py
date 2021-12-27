from django.db import models
from django.utils import timezone

from apps.decks.models import Deck
from apps.utils.models import Timestamps


class Card(Timestamps):
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    question = models.TextField()
    answer = models.TextField()
    buckets = (
        (1, "1 Day"),
        (2, "3 Day"),
        (3, "7 Day"),
        (4, "16 Day"),
        (5, "30 Day"),
    )
    bucket = models.IntegerField(choices=buckets, default=1)
    next_review_at = models.DateTimeField(default=timezone.now())
    last_review_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.question
