# Generated by Django 3.1.2 on 2020-11-01 00:51

import apps.candidato.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('numero', models.PositiveIntegerField()),
                ('foto', models.ImageField(blank=True, null=True, upload_to=apps.candidato.models.upload_foto)),
            ],
        ),
    ]
