# Generated by Django 4.1.1 on 2022-09-16 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_name', models.CharField(blank=True, max_length=150, null=True)),
                ('u_billingname', models.CharField(blank=True, max_length=200, null=True)),
                ('u_mobile', models.CharField(blank=True, max_length=20, null=True)),
                ('u_address', models.CharField(blank=True, max_length=500, null=True)),
                ('u_email', models.CharField(blank=True, max_length=100, null=True)),
                ('u_role', models.CharField(blank=True, max_length=100, null=True)),
                ('u_timezone', models.CharField(blank=True, max_length=100, null=True)),
                ('isactive', models.BooleanField(blank=True, null=True)),
                ('isdelete', models.BooleanField(blank=True, null=True)),
                ('createdat', models.DateTimeField(blank=True, null=True)),
                ('updatedat', models.DateTimeField(blank=True, null=True)),
                ('u_createdby', models.IntegerField(blank=True, null=True)),
                ('password', models.CharField(blank=True, max_length=150, null=True)),
                ('oldpassword', models.CharField(blank=True, max_length=250, null=True)),
                ('objid', models.CharField(blank=True, max_length=300, null=True)),
            ],
            options={
                'db_table': 'users',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('u_email', models.EmailField(max_length=255, unique=True, verbose_name='Email')),
                ('u_name', models.CharField(blank=True, max_length=150, null=True)),
                ('u_billingname', models.CharField(blank=True, max_length=200, null=True)),
                ('u_mobile', models.CharField(blank=True, max_length=20, null=True)),
                ('u_address', models.CharField(blank=True, max_length=500, null=True)),
                ('u_role', models.CharField(blank=True, default='USER', max_length=100, null=True)),
                ('u_timezone', models.CharField(blank=True, max_length=100, null=True)),
                ('isactive', models.BooleanField(blank=True, default=True, null=True)),
                ('isdelete', models.BooleanField(blank=True, default=False, null=True)),
                ('createdat', models.DateTimeField(auto_now_add=True)),
                ('updatedat', models.DateTimeField(auto_now=True)),
                ('u_createdby', models.IntegerField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
