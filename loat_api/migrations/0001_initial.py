# Generated by Django 4.1.1 on 2022-09-17 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Loats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('l_cuttingtype', models.CharField(blank=True, max_length=250, null=True)),
                ('l_entrydate', models.DateField(blank=True, null=True)),
                ('l_price', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('l_weight', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('l_month', models.IntegerField(blank=True, null=True)),
                ('l_year', models.IntegerField(blank=True, null=True)),
                ('l_numofdimonds', models.IntegerField(blank=True, null=True)),
                ('l_multiwithdiamonds', models.BooleanField(blank=True, null=True)),
                ('isactive', models.BooleanField(blank=True, null=True)),
                ('isdelete', models.BooleanField(blank=True, null=True)),
                ('createdat', models.DateTimeField(auto_now_add=True)),
                ('updatedat', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'loats',
                'managed': False,
            },
        ),
    ]