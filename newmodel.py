# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Cuttingtypes(models.Model):
    c_id = models.AutoField(primary_key=True)
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userid')
    partyid = models.ForeignKey(
        'Partys', models.DO_NOTHING, db_column='partyid', blank=True, null=True)
    c_name = models.CharField(max_length=150, blank=True, null=True)
    c_colorcode = models.CharField(max_length=200, blank=True, null=True)
    c_multiwithdiamonds = models.BooleanField(blank=True, null=True)
    c_price = models.DecimalField(
        max_digits=20, decimal_places=2, blank=True, null=True)
    isactive = models.BooleanField(blank=True, null=True)
    isdelete = models.BooleanField(blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)
    updatedat = models.DateTimeField(blank=True, null=True)
    objid = models.CharField(max_length=250, blank=True, null=True)
    old_userid = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cuttingtypes'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey(
        'DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Loats(models.Model):
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userid')
    partyid = models.ForeignKey(
        'Partys', models.DO_NOTHING, db_column='partyid')
    l_cuttingtype = models.CharField(max_length=250, blank=True, null=True)
    l_entrydate = models.DateField(blank=True, null=True)
    l_price = models.DecimalField(
        max_digits=20, decimal_places=2, blank=True, null=True)
    l_weight = models.DecimalField(
        max_digits=20, decimal_places=2, blank=True, null=True)
    l_month = models.IntegerField(blank=True, null=True)
    l_year = models.IntegerField(blank=True, null=True)
    l_numofdimonds = models.IntegerField(blank=True, null=True)
    l_multiwithdiamonds = models.BooleanField(blank=True, null=True)
    isactive = models.BooleanField(blank=True, null=True)
    isdelete = models.BooleanField(blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)
    updatedat = models.DateTimeField(blank=True, null=True)
    objid = models.CharField(max_length=250, blank=True, null=True)
    old_userid = models.CharField(max_length=250, blank=True, null=True)
    old_partyid = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'loats'


class Partys(models.Model):
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userid')
    p_name = models.CharField(max_length=150, blank=True, null=True)
    p_billingname = models.CharField(max_length=200, blank=True, null=True)
    p_mobile = models.CharField(max_length=200, blank=True, null=True)
    p_address = models.CharField(max_length=200, blank=True, null=True)
    p_email = models.CharField(max_length=200, blank=True, null=True)
    p_openingbalance = models.DecimalField(
        max_digits=20, decimal_places=2, blank=True, null=True)
    isactive = models.BooleanField(blank=True, null=True)
    isdelete = models.BooleanField(blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)
    updatedat = models.DateTimeField(blank=True, null=True)
    c_cuttingtype = models.ForeignKey(
        Cuttingtypes, models.DO_NOTHING, db_column='c_cuttingtype', blank=True, null=True)
    old_userid = models.CharField(max_length=250, blank=True, null=True)
    objid = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'partys'


class Users(models.Model):
    u_name = models.CharField(max_length=150, blank=True, null=True)
    u_billingname = models.CharField(max_length=200, blank=True, null=True)
    u_mobile = models.CharField(max_length=20, blank=True, null=True)
    u_address = models.CharField(max_length=500, blank=True, null=True)
    u_email = models.CharField(max_length=100, blank=True, null=True)
    u_role = models.CharField(max_length=100, blank=True, null=True)
    u_timezone = models.CharField(max_length=100, blank=True, null=True)
    isactive = models.BooleanField(blank=True, null=True)
    isdelete = models.BooleanField(blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)
    updatedat = models.DateTimeField(blank=True, null=True)
    u_createdby = models.IntegerField(blank=True, null=True)
    password = models.CharField(max_length=150, blank=True, null=True)
    oldpassword = models.CharField(max_length=250, blank=True, null=True)
    objid = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
