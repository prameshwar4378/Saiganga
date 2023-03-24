# Generated by Django 4.0 on 2022-03-06 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bills', '0006_db_bills_del_amount1_db_bills_del_amount2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='db_bills',
            name='del_num',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='db_bills',
            name='del_amount2',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='db_bills',
            name='del_amount3',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='db_bills',
            name='del_amount4',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='db_bills',
            name='del_amount5',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='db_bills',
            name='del_chessis2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='db_bills',
            name='del_chessis3',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='db_bills',
            name='del_chessis4',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='db_bills',
            name='del_chessis5',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='db_bills',
            name='del_descrtiption2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='db_bills',
            name='del_descrtiption3',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='db_bills',
            name='del_descrtiption4',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='db_bills',
            name='del_descrtiption5',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='db_bills',
            name='del_engine2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='db_bills',
            name='del_engine3',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='db_bills',
            name='del_engine4',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='db_bills',
            name='del_engine5',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='db_bills',
            name='del_qty2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='db_bills',
            name='del_qty3',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='db_bills',
            name='del_qty4',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='db_bills',
            name='del_qty5',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
