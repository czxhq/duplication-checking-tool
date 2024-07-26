from django.contrib import admin
from newapp.models.duser import DUser
from newapp.models.record import Record

# Register your models here.
admin.site.register(DUser)
admin.site.register(Record)
