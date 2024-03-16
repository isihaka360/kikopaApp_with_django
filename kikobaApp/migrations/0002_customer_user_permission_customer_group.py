# Generated by Django 5.0.2 on 2024-03-14 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('kikobaApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='User_permission',
            field=models.ManyToManyField(related_name='User_Customer_permission', to='auth.permission'),
        ),
        migrations.AddField(
            model_name='customer',
            name='group',
            field=models.ManyToManyField(related_name='Customer_group', to='auth.group'),
        ),
    ]