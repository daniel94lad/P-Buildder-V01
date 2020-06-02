# Generated by Django 3.0.6 on 2020-06-02 00:25

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='B_User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=120)),
                ('last_name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
                ('photo', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=users.models.upload_location, width_field='width_field')),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
                ('joined', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['joined'],
            },
        ),
    ]