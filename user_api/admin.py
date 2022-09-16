from django import forms
from django.contrib import admin as AdminNew
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from .models import DjangoUser

from .user_model import Users

# Register your models here.


class UserAdmin(AdminNew.ModelAdmin):
    # list_display = ['id', 'u_name']
    list_display = ['id', 'u_name', 'u_billingname', 'u_mobile']


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = DjangoUser
        fields = ('u_name', 'u_email', 'u_mobile', 'u_billingname')
        # fields = ('u_name', 'u_email')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = DjangoUser
        fields = ('u_name', 'u_email', 'u_mobile',
                  'u_billingname', 'is_active', 'is_admin')
        # fields = ('u_name', 'u_email', 'is_active', 'is_admin')


class DjangoUserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('id', 'u_name', 'u_email', 'u_mobile',
                    'u_billingname', 'is_admin')
    # list_display = ('id', 'u_name', 'u_email', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('u_email', 'password')}),
        ('Personal Name', {'fields': ('u_name',)}),
        ('Personal Mobile', {'fields': ('u_mobile',)}),
        ('Personal Billing name', {'fields': ('u_billingname',)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('u_name', 'u_email', 'u_mobile', 'u_billingname', 'password1', 'password2'),
        }),
    )
    search_fields = ('u_email',)
    ordering = ('u_email',)
    filter_horizontal = ()


AdminNew.site.register(Users, UserAdmin)
AdminNew.site.register(DjangoUser, DjangoUserAdmin)
