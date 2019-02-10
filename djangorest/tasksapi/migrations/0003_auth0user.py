# Generated by Django 2.1.4 on 2019-02-10 20:34

from django.db import migrations
from django.conf import settings

def create_data(apps, schema_editor):
    User = apps.get_model(settings.AUTH_USER_MODEL)
    user = User(pk=1, username="auth0user", is_active=True, email="okongo.odhiambo@outlook.com")
    user.save()

class Migration(migrations.Migration):

    dependencies = [
        ('tasksapi', '0002_dummy_tasks'),
    ]

    operations = [
        migrations.RunPython(create_data),
    ]
