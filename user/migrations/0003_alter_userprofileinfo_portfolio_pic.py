# Generated by Django 3.2.6 on 2021-08-18 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_remove_userprofileinfo_portfolio_site'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='portfolio_pic',
            field=models.ImageField(blank=True, default='profile_pics/default.png', upload_to='profile_pics'),
        ),
    ]