from django.db import models

# Create your models here.


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

    def __str__(self):
        return self.u_name
