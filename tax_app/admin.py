from django.contrib import admin
from .models import Tax
# Register your models here.

# admin.site.register(Tax)

@admin.register(Tax)
class TaxAdmin(admin.ModelAdmin):
  list_display = ('userId','total_tax','created','dueDate')
  list_filter = ('userId','created')