import datetime

from django.db import models
from django.utils.text import slugify

from accounts.models import Customer


# Create your models here.

class Event(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, editable=False)
    description = models.TextField()
    start_time = models.DateTimeField(default=datetime.date, null=True)
    end_time = models.DateTimeField(null=True)
    location = models.CharField(max_length=100, null=True)
    participants = models.ManyToManyField(Customer, related_name='events')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Event, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['start_time']
