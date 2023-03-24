# Generated by Django 4.0 on 2022-03-06 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bills', '0007_db_bills_del_num_alter_db_bills_del_amount2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='db_bills',
            name='mrm_amount',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='db_bills',
            name='mrm_amt_in_word',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='db_bills',
            name='mrm_date',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='db_bills',
            name='mrm_hyp',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='db_bills',
            name='mrm_no',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='db_bills',
            name='mrm_payment_mode',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='db_bills',
            name='mrm_region',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='db_bills',
            name='mrm_remark',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
