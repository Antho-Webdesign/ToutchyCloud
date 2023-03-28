from django.db import models
from django.utils.text import slugify


class MotsCles(models.Model):
    mot = models.CharField(max_length=255)
    small_preview = models.ImageField(upload_to='Documents/', blank=True, null=True)

    def __str__(self):
        return self.mot

    class Meta:
        ordering = ['mot']
        verbose_name = 'MotCles'
        verbose_name_plural = 'MotsCles'


class Tags(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Tags, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-name']
        verbose_name = 'tag'
        verbose_name_plural = 'tags'

    def __str__(self):
        return self.name


class Documents(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, editable=False)
    type = models.CharField(max_length=50)
    mots_cles = models.ManyToManyField(MotsCles)
    tag = models.ForeignKey(Tags, on_delete=models.CASCADE)
    file_upload = models.FileField(upload_to='documents/%Y/%m/%d/', blank=True)
    preview = models.ForeignKey(MotsCles, on_delete=models.CASCADE, related_name="preview", null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nom)
        super(Documents, self).save(*args, **kwargs)

    def __str__(self):
        return self.nom

    class Meta:
        ordering = ['-nom']
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'
