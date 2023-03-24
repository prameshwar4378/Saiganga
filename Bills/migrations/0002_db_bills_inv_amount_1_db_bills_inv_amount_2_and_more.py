# Generated by Django 4.0.3 on 2022-03-05 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bills', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='db_bills',
            name='inv_amount_1',
            field=models.FloatField(default='0'),
        ),
        migrations.AddField(
            model_name='db_bills',
            name='inv_amount_2',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='db_bills',
            name='inv_amount_3',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='db_bills',
            name='inv_amount_4',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='db_bills',
            name='inv_amount_5',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='db_bills',
            name='inv_amount_6',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='db_bills',
            name='inv_cgst',
            field=models.FloatField(default='0'),
        ),
        migrations.AddField(
            model_name='db_bills',
            name='inv_chessis_1',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='db_bills',
            name='inv_chessis_2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='db_bills',
            name='inv_chessis_3',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='db_bills',
            name='inv_chessis_4',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='db_bills',
            name='inv_chessis_5',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='db_bills',
            name='inv_chessis_6',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='db_bills',
            name='inv_date',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='db_bills',
            name='inv_description_1',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='db_bills',
            name='inv_description_2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='db_bills',
            name='inv_description_3',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='db_bills',
            name='inv_description_4',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='db_bills',
            name='inv_description_5',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='db_bills',
            name='inv_description_6',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='db_bills',
            name='inv_engine_1',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='db_bills',
            name='inv_engine_2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='db_bills',
            name='inv_engine_3',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='db_bills',
            name='inv_engine_4',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='db_bills',
            name='inv_engine_5',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='db_bills',
            name='inv_engine_6',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='db_bills',
            name='inv_grand_total',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='db_bills',
            name='inv_no',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='db_bills',
            name='inv_qty_1',
            field=models.IntegerField(default='1'),
        ),
        migrations.AddField(
            model_name='db_bills',
            name='inv_qty_2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='db_bills',
            name='inv_qty_3',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='db_bills',
            name='inv_qty_4',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='db_bills',
            name='inv_qty_5',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='db_bills',
            name='inv_qty_6',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='db_bills',
            name='inv_rate_1',
            field=models.FloatField(default='0'),
        ),
        migrations.AddField(
            model_name='db_bills',
            name='inv_rate_2',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='db_bills',
            name='inv_rate_3',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='db_bills',
            name='inv_rate_4',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='db_bills',
            name='inv_rate_5',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='db_bills',
            name='inv_rate_6',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='db_bills',
            name='inv_rto',
            field=models.FloatField(default='0'),
        ),
        migrations.AddField(
            model_name='db_bills',
            name='inv_sgst',
            field=models.FloatField(default='0'),
        ),
        migrations.AddField(
            model_name='db_bills',
            name='inv_sub_total',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='db_bills',
            name='other_reference',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
