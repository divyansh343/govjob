# Generated by Django 3.2.6 on 2021-08-14 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_auto_20210814_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='image',
            field=models.ImageField(upload_to='jobs/image/'),
        ),
    ]