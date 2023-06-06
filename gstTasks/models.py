from django.db import models
from django.utils.text import slugify


# Tasks models
class CategoryTasks(models.Model):
    name = models.CharField(max_length=50)
    # image_task_cat = models.ImageField(upload_to='tasks/', default='tasks/task.png', blank=True, null=True)
    slug = models.SlugField(unique=True, editable=False)
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('accounts.Customer', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(CategoryTasks, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Categorie Tache'
        verbose_name_plural = 'Categories aches'


class Tasks(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, editable=False)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    date_butoir = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    category = models.ForeignKey(CategoryTasks, on_delete=models.CASCADE)
    author = models.ForeignKey('accounts.Customer', on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Tasks, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-title']
        verbose_name = 'Tache'
        verbose_name_plural = 'Taches'





