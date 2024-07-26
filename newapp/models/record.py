from django.db import models
import os
import hashlib
import time
def createPath(instance, filename):
    data = f"{filename}_{int(time.time())}"
    file_hash = hashlib.sha1(data.encode('utf-8')).hexdigest()
    return f"uploads/{file_hash}/{filename}"

class Record(models.Model):
    username = models.CharField(max_length=100, blank=True)
    date = models.CharField(max_length=100, blank=True)
    pre = models.FileField(upload_to=createPath)
    res_path = models.CharField(max_length=150, blank=True)
