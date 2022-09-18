from django.db import models

from party_api.models import Partys

from jb_be import settings

# Create your models here.


class Loats(models.Model):
    userid = models.ForeignKey(
        settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='userid', related_name='loat_django_user')
    partyid = models.ForeignKey(
        Partys, models.DO_NOTHING, db_column='partyid', related_name='loat_party')
    l_cuttingtype = models.CharField(max_length=250)
    l_entrydate = models.DateField()
    l_price = models.DecimalField(max_digits=20, decimal_places=2)
    l_weight = models.DecimalField(max_digits=20, decimal_places=2)
    l_month = models.IntegerField()
    l_year = models.IntegerField()
    l_numofdimonds = models.IntegerField()
    l_multiwithdiamonds = models.BooleanField()
    isactive = models.BooleanField(default=True)
    isdelete = models.BooleanField(default=False)
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)
    # objid = models.CharField(max_length=250, blank=True, null=True)
    # old_userid = models.CharField(max_length=250, blank=True, null=True)
    # old_partyid = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'loats'

    def __str__(self):
        return self.l_cuttingtype
