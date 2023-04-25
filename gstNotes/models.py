from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=50)
    image_note_cat = models.ImageField(upload_to='notes/', default='notes/note.png', blank=True, null=True)
    slug = models.SlugField(unique=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Note(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, editable=False)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Note, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-title']
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'


