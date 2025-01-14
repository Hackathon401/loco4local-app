# Generated by Django 3.1.5 on 2021-01-24 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendorpost',
            name='vendorPost_text',
        ),
        migrations.AddField(
            model_name='vendorpost',
            name='business_address',
            field=models.CharField(default='PLEASE CONTACT', max_length=100),
        ),
        migrations.AddField(
            model_name='vendorpost',
            name='business_name',
            field=models.CharField(default=' ', max_length=100),
        ),
        migrations.AddField(
            model_name='vendorpost',
            name='owner_name',
            field=models.CharField(default=' ', max_length=100),
        ),
        migrations.AddField(
            model_name='vendorpost',
            name='phone_number',
            field=models.CharField(default=' ', max_length=100),
        ),
        migrations.AddField(
            model_name='vendorpost',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
