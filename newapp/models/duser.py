from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class DUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_login = models.BooleanField(default=False)
    is_sec = models.BooleanField(default=False)
    que1 = models.CharField(max_length=255, blank=True)
    ans1 = models.CharField(max_length=255, blank=True)
    que2 = models.CharField(max_length=255, blank=True)
    ans2 = models.CharField(max_length=255, blank=True)
    def __str__(self):
        return str(self.user)

