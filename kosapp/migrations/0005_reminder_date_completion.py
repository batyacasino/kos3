# Generated by Django 3.0.6 on 2020-07-02 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kosapp', '0004_reminder'),
    ]

    operations = [
        migrations.AddField(
            model_name='reminder',
            name='date_completion',
            field=models.DateField(default='2000-01-01'),
            preserve_default=False,
        ),
    ]