# Generated by Django 3.0 on 2021-09-15 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_garden_seed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seed',
            name='garden',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='api.Garden'),
        ),
    ]
