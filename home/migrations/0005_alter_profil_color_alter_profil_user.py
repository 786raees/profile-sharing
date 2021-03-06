# Generated by Django 4.0.4 on 2022-05-18 19:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0004_alter_profil_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profil',
            name='color',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='profil',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
