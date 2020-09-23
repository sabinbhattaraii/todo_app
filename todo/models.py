from django.db import models
from django.urls import reverse

# Create your models here.
class Todo(models.Model):
    content = models.TextField()

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse('detail',args=[str(self.id)])