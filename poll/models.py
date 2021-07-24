from django.db import models
from django.contrib.auth.models import User


class Poll(models.Model):
    name = models.CharField(max_length=150)
    topic = models.CharField(max_length=150)
    data_created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    user = models.ForeignKey(User , on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.name} - {self.user.username}"