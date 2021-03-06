# Generated by Django 4.0.4 on 2022-05-21 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_profil_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profil',
            name='Name',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='profil',
            name='emiall',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='profil',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='profil',
            name='number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profil',
            name='profession',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
