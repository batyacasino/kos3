# Generated by Django 3.0.6 on 2020-07-16 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kosapp', '0006_client_case_number'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'ordering': ['-date_creat']},
        ),
        migrations.CreateModel(
            name='StateMovement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('condition', models.CharField(max_length=200)),
                ('document_base', models.CharField(blank=True, max_length=200, null=True)),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kosapp.Client')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='LocationCaseMovement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('location', models.CharField(max_length=200)),
                ('comment', models.CharField(blank=True, max_length=200, null=True)),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kosapp.Client')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='JudicialActs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('type_of_document', models.CharField(max_length=200)),
                ('document_text', models.CharField(blank=True, max_length=200, null=True)),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kosapp.Client')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='CourtSessions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('hall', models.IntegerField()),
                ('stage', models.CharField(max_length=200)),
                ('result', models.CharField(max_length=200)),
                ('base', models.CharField(blank=True, max_length=200, null=True)),
                ('video_was_recorded', models.CharField(blank=True, max_length=200, null=True)),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kosapp.Client')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
    ]