from django.db import models
from django.utils.text import slugify

from accounts.models import Customer
from toutchycloud_settings.settings import AUTH_USER_MODEL


# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    due_date = models.DateField(auto_now_add=False)
    # priority = models.IntegerField()
    status = models.CharField(max_length=20)
    assigned_to = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField('créé le', auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField('modifier le', auto_now_add=False, blank=True, null=True)
    slug = models.SlugField(unique=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Task, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Tasks'
