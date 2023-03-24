# Generated by Django 4.0.3 on 2022-03-05 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DB_Bills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_name', models.CharField(max_length=50)),
                ('cust_village', models.CharField(max_length=50)),
                ('cust_taluka', models.CharField(max_length=50)),
                ('cust_dist', models.CharField(max_length=50)),
                ('cust_mobile', models.BigIntegerField()),
            ],
        ),
    ]
