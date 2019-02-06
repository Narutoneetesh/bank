# Generated by Django 2.0.6 on 2018-08-09 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User_bal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=100, unique=True)),
                ('Email', models.EmailField(max_length=254)),
                ('Password', models.CharField(max_length=50)),
                ('Balance', models.CharField(max_length=10)),
            ],
        ),
    ]
