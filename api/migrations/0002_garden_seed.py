# Generated by Django 3.0 on 2021-09-15 15:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Garden',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('location', models.CharField(max_length=250)),
                ('notes', models.TextField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Seed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('season', models.CharField(max_length=100)),
                ('light', models.CharField(max_length=100)),
                ('favorite', models.BooleanField()),
                ('number', models.IntegerField()),
                ('notes', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('garden', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Garden')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]