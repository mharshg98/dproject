# Generated by Django 2.2.6 on 2020-04-11 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('cust_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('mobile_no', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=100)),
                ('lat_long', models.CharField(max_length=30)),
            ],
        ),
    ]