# Generated by Django 5.0 on 2024-01-01 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='band',
            name='title',
            field=models.CharField(default='none', max_length=100),
        ),
    ]
