# Generated by Django 3.2.8 on 2021-10-26 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('z_awwards', '0012_alter_userproject_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userproject',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/user_post/'),
        ),
    ]
