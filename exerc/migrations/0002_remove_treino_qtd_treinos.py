# Generated by Django 4.1.2 on 2022-10-06 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exerc', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='treino',
            name='qtd_treinos',
        ),
    ]
