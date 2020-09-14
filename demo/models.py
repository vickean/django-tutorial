import uuid
from django.db import models

# Create your models here.


class Folder(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    create_date = models.DateTimeField(auto_now_add=True)


class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    demo = models.ForeignKey(Folder, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=500)
