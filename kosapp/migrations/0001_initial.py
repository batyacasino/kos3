# Generated by Django 3.0.6 on 2020-06-05 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_creat', models.DateField(auto_now_add=True)),
                ('claimant', models.CharField(max_length=200)),
                ('defendant', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('email_password', models.CharField(max_length=200)),
                ('date_of_inspection', models.DateField()),
            ],
        ),
    ]
