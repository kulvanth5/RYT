# Generated by Django 4.1.5 on 2023-01-26 12:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('userID', models.CharField(default='000000', max_length=6, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(default='Enter user name here', max_length=20)),
                ('dept_name', models.CharField(choices=[('stores', 'Stores'), ('kitchen', 'Kitchen'), ('h2', 'Holistic Health'), ('aura', 'Aura'), ('hr', 'Maintenance'), ('altar', 'Altar'), ('ankur', 'ankur'), ('he', 'Hostel Essentials')], max_length=15)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'Users',
            },
        ),
    ]
