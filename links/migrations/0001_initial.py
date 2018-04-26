# Generated by Django 2.0.4 on 2018-04-22 01:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tags', '0001_initial'),
        ('folders', '0001_initial'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(blank=True, null=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
                ('comment', models.TextField(blank=True, max_length=1000, null=True)),
                ('folder', models.ManyToManyField(to='folders.Folder')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='links', to='profiles.Profile')),
                ('tags', models.ManyToManyField(blank=True, null=True, to='tags.Tag')),
            ],
        ),
    ]
