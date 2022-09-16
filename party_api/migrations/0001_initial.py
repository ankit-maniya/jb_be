# Generated by Django 4.1.1 on 2022-09-16 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Partys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(blank=True, max_length=150, null=True)),
                ('p_billingname', models.CharField(blank=True, max_length=200, null=True)),
                ('p_mobile', models.CharField(blank=True, max_length=200, null=True)),
                ('p_address', models.CharField(blank=True, max_length=200, null=True)),
                ('p_email', models.CharField(blank=True, max_length=200, null=True)),
                ('p_openingbalance', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('isactive', models.BooleanField(blank=True, null=True)),
                ('isdelete', models.BooleanField(blank=True, null=True)),
                ('createdat', models.DateTimeField(blank=True, null=True)),
                ('updatedat', models.DateTimeField(blank=True, null=True)),
                ('old_userid', models.CharField(blank=True, max_length=250, null=True)),
                ('objid', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'db_table': 'partys',
                'managed': False,
            },
        ),
    ]
