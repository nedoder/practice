# Generated by Django 3.2.7 on 2021-10-05 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motivo', '0003_alter_collectedawards_user_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='uploads/challenge_files/'),
        ),
    ]