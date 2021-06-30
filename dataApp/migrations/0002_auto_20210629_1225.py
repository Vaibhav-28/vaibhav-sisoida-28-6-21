# Generated by Django 3.2.4 on 2021-06-29 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticker',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('open_val', models.DecimalField(decimal_places=2, max_digits=100)),
                ('high_val', models.DecimalField(decimal_places=2, max_digits=100)),
                ('low_val', models.DecimalField(decimal_places=2, max_digits=100)),
                ('close_val', models.DecimalField(decimal_places=2, max_digits=100)),
            ],
        ),
        migrations.DeleteModel(
            name='DataEntity',
        ),
    ]
