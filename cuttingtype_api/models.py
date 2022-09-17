from django.conf import settings
from django.db import models

from party_api.models import Partys

# Create your models here.


class Cuttingtypes(models.Model):
    c_id = models.AutoField(primary_key=True)
    userid = models.ForeignKey(
        settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='userid', related_name='django_user')
    partyid = models.ForeignKey(
        Partys, models.DO_NOTHING, db_column='partyid', related_name='party')
    c_name = models.CharField(max_length=150)
    c_colorcode = models.CharField(max_length=200)
    c_multiwithdiamonds = models.BooleanField(default=False)
    c_price = models.DecimalField(
        max_digits=20, decimal_places=2)
    isactive = models.BooleanField(default=True)
    isdelete = models.BooleanField(default=False)
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)
    objid = models.CharField(max_length=250, blank=True, null=True)
    old_userid = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cuttingtypes'

    def __str__(self):
        return self.c_name
