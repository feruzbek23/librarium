# Generated by Django 5.0.4 on 2024-10-01 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='books_count',
            field=models.IntegerField(null=True),
        ),
    ]
