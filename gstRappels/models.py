from django.db import models

# Gestion des rappels
from django.utils.text import slugify


class Rappel(models.Model):
    titre = models.CharField(max_length=255)
    description = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)
    date_rappel = models.DateTimeField()
    slug = models.SlugField(unique=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titre)
        super(Rappel, self).save(*args, **kwargs)

    def __str__(self):
        return self.titre

    class Meta:
        ordering = ['-titre']
        verbose_name = 'Rappel'
        verbose_name_plural = 'Rappels'
