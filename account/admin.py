from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Profile
# from TaxSystemAPI.gstProject.account.models import Profile
# from .models import CustomUser

# Register your models here.
# class CustomUserAdmin(UserAdmin):
  # pass
  # list_display = (
  #       'username', 'email', 'first_name', 'last_name', 'is_staff',
  #       'is_tax_payer', 'is_tax_accountant', 'role'
  #       )

  # add_fieldsets = (
  #       (None, {
  #           'fields': ('username', 'password1', 'password2')
  #       }),
  #       ('Personal info', {
  #           'fields': ('first_name', 'last_name', 'email')
  #       }),
  #       ('Important dates', {
  #           'fields': ('last_login', 'date_joined')
  #       }),
  #       ('Additional info', {
  #           'fields': ('is_tax_payer', 'is_tax_accountant', 'role')
  #       })
  #   )


# admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile)


# @admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
  list_display= ('user','role')