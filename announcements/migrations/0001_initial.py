# Generated by Django 4.1.6 on 2023-04-18 15:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='announcements_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=10)),
                ('Announcement', models.TextField()),
                ('Created_At', models.DateTimeField(auto_now_add=True)),
                ('Department_Name', models.CharField(default=None, max_length=20)),
                ('Validity', models.DateTimeField()),
                ('made_by', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Announcments',
            },
        ),
    ]
