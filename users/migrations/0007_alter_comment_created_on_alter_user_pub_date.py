# Generated by Django 4.1.1 on 2022-09-27 08:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_comment_created_on_alter_user_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2022, 9, 27, 8, 18, 58, 334650, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2022, 9, 27, 8, 18, 58, 334650, tzinfo=datetime.timezone.utc)),
        ),
    ]
