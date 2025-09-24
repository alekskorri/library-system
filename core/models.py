
from django.db import models
import uuid
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Genre(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    genre = models.CharField(max_length=50)
    created = models.DateField(auto_created=timezone.now())

    def __str__(self):
        return self.genre

class Books(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    gener = models.ForeignKey(Genre, on_delete=models.CASCADE, null=True, blank=True)
    edition = models.DateField()
    publication = models.DateField(blank=True, null=True)
    publisher = models.CharField(max_length=100, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)

    create_by = models.CharField(max_length=100, blank=True, null=True)
    created_date = models.DateField(blank=True, null=True)

    update_by = models.CharField(max_length=100, blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)


    def __str__(self):
        return self.title