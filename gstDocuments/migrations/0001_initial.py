# Generated by Django 4.1.7 on 2023-03-28 00:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MotsCles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mot', models.CharField(max_length=255)),
                ('small_preview', models.ImageField(blank=True, null=True, upload_to='Documents/')),
            ],
            options={
                'verbose_name': 'MotCles',
                'verbose_name_plural': 'MotsCles',
                'ordering': ['mot'],
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('slug', models.SlugField(editable=False, unique=True)),
            ],
            options={
                'verbose_name': 'tag',
                'verbose_name_plural': 'tags',
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_modification', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(editable=False, unique=True)),
                ('type', models.CharField(max_length=50)),
                ('file_upload', models.FileField(blank=True, upload_to='documents/%Y/%m/%d/')),
                ('mots_cles', models.ManyToManyField(to='gstDocuments.motscles')),
                ('preview', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='preview', to='gstDocuments.motscles')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gstDocuments.tags')),
            ],
            options={
                'verbose_name': 'Document',
                'verbose_name_plural': 'Documents',
                'ordering': ['-nom'],
            },
        ),
    ]
