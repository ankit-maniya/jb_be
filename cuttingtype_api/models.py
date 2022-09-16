from django.conf import settings
from django.db import models

from party_api.models import Partys

# Create your models here.


class Cuttingtypes(models.Model):
    c_id = models.AutoField(primary_key=True)
    userid = models.ForeignKey(
        settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='userid', related_name='django_user')
    partyid = models.ForeignKey(
        Partys, models.DO_NOTHING, db_column='partyid', blank=True, null=True)
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

    def __str__(self):
        return self.c_name
