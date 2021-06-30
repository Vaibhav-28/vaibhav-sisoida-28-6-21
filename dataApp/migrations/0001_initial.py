# Generated by Django 3.2.4 on 2021-06-29 09:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataEntity',
            fields=[
                ('entity', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('date', models.DateField(default=datetime.date.today)),
                ('open_val', models.DecimalField(decimal_places=2, max_digits=100)),
                ('high_val', models.DecimalField(decimal_places=2, max_digits=100)),
                ('low_val', models.DecimalField(decimal_places=2, max_digits=100)),
                ('close_val', models.DecimalField(decimal_places=2, max_digits=100)),
            ],
        ),
    ]
