from contextlib import nullcontext
from dataclasses import fields
from email.policy import default
from tkinter.tix import Form, Select
from django import forms
from .models import Tax
from django.forms import ModelForm


class BillForm2(ModelForm):
  class Meta:
    model = Tax
    fields = ('state','PanCard','salaryIncome','stockIncome','fines','total_tax','STATUS','SGST','CGST')


class BillForm(ModelForm):
  class Meta:
    model = Tax
    fields = ('state','PanCard','salaryIncome','stockIncome')
