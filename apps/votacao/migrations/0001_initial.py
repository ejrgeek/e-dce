# Generated by Django 3.1.2 on 2020-11-01 02:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('chapa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Votacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('votos', models.IntegerField(default=0)),
                ('chapa', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='chapa.chapa')),
            ],
            options={
                'verbose_name_plural': 'Votações',
            },
        ),
    ]
