from django.db import models
from django.db.models.base import ModelState
from poll.models import Poll


class Question(models.Model):
    poll = models.ForeignKey(Poll , on_delete=models.CASCADE)
    text = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.poll.name


class Answer(models.Model):
    question = models.ForeignKey(Question , on_delete=models.CASCADE)
    text = models.CharField(max_length=150)
    score = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.text
