# Generated by Django 3.1.4 on 2020-12-04 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=25)),
                ('title', models.CharField(max_length=25)),
                ('description', models.CharField(max_length=150)),
                ('no_of_likes', models.IntegerField()),
            ],
        ),
    ]
