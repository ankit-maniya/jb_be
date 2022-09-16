from django.conf import settings
from django.db import models

# This Cuttingtypes model import not require anymore as we are now saving each party data into cuttingtype table
# from cuttingtype_api.models import Cuttingtypes

# Create your models here.


class Partys(models.Model):
    userid = models.ForeignKey(
        settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='userid')
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
    # This c_cuttingtype not require anymore as we are now saving each party data into cuttingtype table
    # c_cuttingtype = models.ForeignKey(
    #     Cuttingtypes, models.DO_NOTHING, db_column='c_cuttingtype', blank=True, null=True, verbose_name="cutting_type_data")
    old_userid = models.CharField(max_length=250, blank=True, null=True)
    objid = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'partys'

    def __str__(self):
        return self.p_name
