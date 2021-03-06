# Generated by Django 4.0.4 on 2022-05-21 14:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0008_alter_profil_name_alter_profil_emiall_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='links',
            name='icon',
        ),
        migrations.AddField(
            model_name='links',
            name='link',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='links',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='UserLinks',
        ),
    ]
