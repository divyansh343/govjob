# Generated by Django 3.2.6 on 2021-08-14 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_alter_applyform_aadhar'),
    ]

    operations = [
        migrations.AddField(
            model_name='applyform',
            name='resume',
            field=models.FileField(default='', upload_to='uploads/resumes/ %y / %m / % d'),
        ),
    ]
