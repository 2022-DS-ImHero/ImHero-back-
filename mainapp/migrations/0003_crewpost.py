# Generated by Django 3.2.9 on 2022-08-24 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='CrewPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('tags', models.ManyToManyField(blank=True, to='mainapp.Tag')),
            ],
        ),
    ]
