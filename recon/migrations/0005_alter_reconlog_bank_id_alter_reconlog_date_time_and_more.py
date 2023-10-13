# Generated by Django 4.2.5 on 2023-10-13 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recon', '0004_reconlog_user_id_alter_reconlog_bank_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reconlog',
            name='bank_id',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='reconlog',
            name='date_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='reconlog',
            name='excep_rws',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='reconlog',
            name='feedback',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='reconlog',
            name='recon_id',
            field=models.CharField(blank=True, max_length=35, null=True),
        ),
        migrations.AlterField(
            model_name='reconlog',
            name='recon_rws',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='reconlog',
            name='rq_date_range',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='reconlog',
            name='rq_rws',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='reconlog',
            name='unrecon_rws',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='reconlog',
            name='upld_rws',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
