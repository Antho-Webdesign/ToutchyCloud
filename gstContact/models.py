from django.db import models
from django.utils.text import slugify


class Contact(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    image_prfl = models.ImageField(upload_to='profiles/', default='profiles/default.png', blank=True, null=True)
    email = models.EmailField(blank=True)
    telephone = models.CharField(max_length=20, blank=True)
    adresse = models.TextField(blank=True)
    ville = models.CharField(max_length=50, blank=True)
    pays = models.CharField(max_length=50, blank=True)
    date_de_naissance = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True)
    date_de_creation = models.DateTimeField(auto_now_add=True)
    date_de_modification = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nom)
        super(Contact, self).save(*args, **kwargs)

    def __str__(self):
        return self.nom

    class Meta:
        ordering = ['-nom']
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

