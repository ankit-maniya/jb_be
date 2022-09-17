from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class DjangoUserManager(BaseUserManager):
    def create_user(self, u_email, u_name, u_mobile, u_billingname=None, u_role=None, isactive=True, is_active=True, is_admin=False, isdelete=False, password=None, password2=None):
        """
        Creates and saves a User with the given email, name, mobile and password.
        """
        if not u_email:
            raise ValueError('Users must have an email address')

        user = self.model(
            u_email=self.normalize_email(u_email),
            u_name=u_name,
            u_mobile=u_mobile,
            u_billingname=u_billingname,
            u_role=u_role,
            isactive=isactive,
            is_active=is_active,
            isdelete=isdelete,
            is_admin=is_admin,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, u_email, u_name, u_mobile, u_billingname=None, u_role=None, isactive=True, is_admin=True, isdelete=False, password=None, password2=None):
        """
        Creates and saves a superuser with the given email, name, mobile and password.
        """
        user = self.create_user(
            u_email,
            password=password,
            u_name=u_name,
            u_mobile=u_mobile,
            u_billingname=u_billingname,
            u_role=u_role,
            isactive=isactive,
            isdelete=isdelete,
            is_admin=is_admin,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


#  Create User Model
class DjangoUser(AbstractBaseUser):
    u_email = models.EmailField(
        verbose_name='Email', max_length=255, unique=True)
    u_name = models.CharField(max_length=150, blank=True, null=True)
    u_billingname = models.CharField(max_length=200, blank=True, null=True)
    u_mobile = models.CharField(max_length=20, blank=True, null=True)
    u_address = models.CharField(max_length=500, blank=True, null=True)
    u_role = models.CharField(
        default="USER", max_length=100)
    u_timezone = models.CharField(max_length=100, blank=True, null=True)
    isactive = models.BooleanField(default=True, blank=True, null=True)
    isdelete = models.BooleanField(default=False, blank=True, null=True)
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)
    u_createdby = models.IntegerField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = DjangoUserManager()

    USERNAME_FIELD = 'u_email'
    REQUIRED_FIELDS = ['u_name', 'u_mobile', 'password']

    def __str__(self):
        return self.u_email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
