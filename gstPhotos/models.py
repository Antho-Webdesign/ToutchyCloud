from django.db import models
from django.utils.text import slugify


class Photos(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)
    images = models.ImageField(upload_to='photos/')
    extension = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nom)
        super(Photos, self).save(*args, **kwargs)

    def __str__(self):
        return self.nom

    class Meta:
        ordering = ['-nom']
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'
