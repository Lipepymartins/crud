# Generated by Django 4.2.7 on 2023-11-05 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CLiente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.IntegerField(max_length=11)),
                ('email', models.EmailField(max_length=254)),
                ('data_nasc', models.DateField()),
                ('profissao', models.CharField(max_length=100)),
            ],
        ),
    ]
