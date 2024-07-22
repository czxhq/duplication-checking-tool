from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class DUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_login = models.BooleanField(default=False)
    def __str__(self):
        return str(self.user)

