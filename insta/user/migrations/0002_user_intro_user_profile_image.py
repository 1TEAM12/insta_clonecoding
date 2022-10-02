# Generated by Django 4.1.1 on 2022-10-02 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='intro',
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.AddField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(default='default_profile_pic.jpg', upload_to='profile_pics'),
        ),
    ]
