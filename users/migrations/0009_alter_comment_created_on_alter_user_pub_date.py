# Generated by Django 4.1.1 on 2022-10-12 03:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_comment_created_on_alter_user_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 12, 3, 30, 29, 388796, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2022, 10, 12, 3, 30, 29, 388796, tzinfo=datetime.timezone.utc)),
        ),
    ]
