from django.db import models

# Create your models here.
"""
from django.db import models
from django.contrib.auth.models import User

class Rdv(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, editable=False)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    location = models.CharField(max_length=100)
    participants = models.ManyToManyField(User, related_name='appointments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
    self.slug = slugify(self.title)
    super(Rdv, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['start_time']

"""