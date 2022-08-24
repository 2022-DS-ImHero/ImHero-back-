# Generated by Django 4.1 on 2022-08-24 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_is_mentor_alter_customuser_is_mentor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_mentor',
            field=models.CharField(choices=[('Y', 'Mentor'), ('N', 'Mentee')], max_length=3),
        ),
        migrations.DeleteModel(
            name='is_mentor',
        ),
    ]