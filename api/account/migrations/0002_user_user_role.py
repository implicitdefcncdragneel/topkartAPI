# Generated by Django 4.2.1 on 2023-05-20 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_role',
            field=models.CharField(choices=[('Customer', 'Customer'), ('TAdmin', 'TAdmin'), ('Unknown', 'Unknown')], default='Unknown', max_length=10),
        ),
    ]
