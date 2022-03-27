from cProfile import label
from email.policy import default
import imp
from tkinter import HIDDEN
from django.db import models
from django.utils import timezone
from datetime import timedelta,datetime
from django.contrib.auth.models import User
from django.urls import reverse
from django import forms

def given_date():
    now = timezone.now()
    return now + timedelta(days=1)

STATES = (
    ('DLH','DELHI'),('BR','BIHAR'),('WB','WEST BENGAL')
  )
TAX_STATUS = (
    ('N','New'),('D','Delayed'),('P','Paid')
  )

class Tax(models.Model):
  userId = models.ForeignKey(User,on_delete=models.CASCADE,related_name='tax')
  state = models.CharField(max_length=20,null=False,blank=False)
  SGST = models.FloatField(max_length=20,null=False,default=9.0)
  CGST = models.FloatField(max_length=20,null=False,default=9.0)
  PanCard = models.CharField(max_length=12,null=False)
  salaryIncome = models.IntegerField(null=False,blank=False,default=0)
  stockIncome = models.IntegerField(null=False,default=0)
  dueDate = models.DateField(blank=True,default=given_date)
  created = models.DateField(blank=True,auto_now_add=True)
  updated = models.DateTimeField(blank=True,auto_now=True)
  STATUS = models.CharField(max_length=10,default='New')
  total_tax = models.FloatField(max_length=10,null=True,blank=True,default=0)
  fines = models.IntegerField(null=True,blank=True,default=0)
  paymentStatus = models.CharField(max_length=10,default='Unpaid')

  def __str__(self):
    return f'{self.userId} : Bill_ID {self.id}'

  def get_absolute_url(self):
    return reverse('tax_app:bill_detail',args=[self.id])




