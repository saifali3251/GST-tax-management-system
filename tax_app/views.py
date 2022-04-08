from django.shortcuts import render,get_object_or_404
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .models import Tax
from django.contrib.auth.models import User
from django.http import HttpResponse
from .forms import BillForm,BillForm2
from django.views.generic import (TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from datetime import timedelta,datetime,date
from django.db.models import Sum,Count

# from datetime import datetime

STATE = ['Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chhattisgarh','Goa','Gujarat','Haryana','Himachal Pradesh','Jammu Kashmir','Jharkhand','Karnataka','Kerala','Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Odisha','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura','Uttar Pradesh','Uttarakhand','West Bengal']

U_T = ['Andaman And Nicobar Islands','Chandigarh','Dadra And Nagar Haveli','Daman','Delhi','Lakshadweep','Pondicherry']

# Create your views here.


@login_required
def homepage(request):
  context = {}
  context['user'] = User.objects.all().count() - 1
  # print(context['user'])
  if str(request.user) == 'admin' or str(request.user.profile.role) == 'Tax-Accountant':
    bills = Tax.objects.all().exclude(userId=1).order_by('id')
  else:
    print('Else..')
    bills = Tax.objects.all().filter(userId=request.user).order_by('-created')

  context['count'] = bills.count()
  # print('Total count : ',context['count'])
  # print('Total count : ',type(context['count']))
  if context['count'] == 0:
    print('Total count : ',context['count'])
    context['unpaid_tax'] = 0
    context['paid_tax'] = 0
    context['partial_bills'] = None
    print(context['partial_bills'])
    context['paid_share'] = 0
    context['unpaid_share'] = 0
    context['net_tax'] = 0
  else:
    context['partial_bills'] = bills[:3]
    # print(context['partial_bills'])
    # unpaid_bill = Tax.objects.all().filter(userId=request.user,paymentStatus='Unpaid')
    # context['net_tax'] = Tax.objects.all().aggregate(Sum('total_tax'))
    # context['net_tax'] = context['net_tax']['total_tax__sum']
    # print(context['net_tax'])
    # if str(request.user) == 'admin':
    if str(request.user) == 'admin' or str(request.user.profile.role) == 'Tax-Accountant':
      unpaid_bill = Tax.objects.all().filter(paymentStatus='Unpaid')
      paid_bill = Tax.objects.all().filter(paymentStatus='Paid')
      context['net_tax'] = Tax.objects.all().aggregate(Sum('total_tax'))
      context['net_tax'] = context['net_tax']['total_tax__sum']
    else:
      unpaid_bill = Tax.objects.all().filter(userId=request.user,paymentStatus='Unpaid')
      paid_bill = Tax.objects.all().filter(userId=request.user,paymentStatus='Paid')
      context['net_tax'] = Tax.objects.all().filter(userId=request.user).aggregate(Sum('total_tax'))
      context['net_tax'] = context['net_tax']['total_tax__sum']

    # unpaid_bill = Tax.objects.all().filter(paymentStatus='Unpaid')
    # unpaid_bill = Tax.objects.all().filter(userId=request.user,paymentStatus='Unpaid')
    # paid_bill = Tax.objects.all().filter(paymentStatus='Paid')
    # paid_bill = Tax.objects.all().filter(userId=request.user,paymentStatus='Paid')
    # paid_bill = Tax.objects.all().filter(userId=request.user,paymentStatus='Paid')
    context['unpaid_tax'] = unpaid_bill.aggregate(Sum('total_tax'))
    context['paid_tax'] = paid_bill.aggregate(Sum('total_tax'))
    # context['net_tax'] = context['paid_tax']+context['unpaid_tax']
    if context['paid_tax']['total_tax__sum'] == None:
      context['paid_tax'] = 0
      context['paid_share'] = 0
    else:
      context['paid_tax'] = round(context['paid_tax']['total_tax__sum'],2)
      context['paid_share'] = round((context['paid_tax']/context['net_tax'])*100,2)

    if context['unpaid_tax']['total_tax__sum'] == None:
      context['unpaid_tax'] = 0
      context['unpaid_share'] = 0
    else:
      context['unpaid_tax'] = round(context['unpaid_tax']['total_tax__sum'],2)
      context['unpaid_share'] = round((context['unpaid_tax']/context['net_tax'])*100,2)

    # context['paid_share'] = round((context['paid_tax']/context['net_tax'])*100,2)
    # context['unpaid_share'] = round((context['unpaid_tax']/context['net_tax'])*100,2)

    # context['paid_tax'] = round(context['paid_tax']['total_tax__sum'],2)
    # context['net_tax'] = context['paid_tax']+context['unpaid_tax']
    # if context['paid_tax'] != 0:
      # context['paid_share'] = round((context['paid_tax']/context['net_tax'])*100,2)
    # if context['unpaid_tax'] != 0:
      # context['unpaid_share'] = round((context['unpaid_tax']/context['net_tax'])*100,2)

  # context['unpaid_share'] = round((context['unpaid_tax']/context['net_tax'])*100,2)
  # context['paid_share'] = round((context['paid_tax']/context['net_tax'])*100,2)

  # context['paid_share'] = round((context['paid_tax']/context['net_tax'])*100,2)
  # context['unpaid_share'] = round((context['unpaid_tax']/context['net_tax'])*100,2)
  # context['paid_tax'] = round(context['paid_tax']['total_tax__sum'],2)
  # context['unpaid_tax'] = round(context['unpaid_tax']['total_tax__sum'],2)
  print(context['paid_tax'])
  print(context['unpaid_tax'])
  return render(request,'homepage.html',{'bills':bills,'context':context})



@login_required
def admin_dashboard(request):
  context = {}
  context['user'] = User.objects.all().count() - 1
  # print(context['user'])
  if str(request.user) == 'admin' or str(request.user.profile.role) == 'Tax-Accountant':
    bills = Tax.objects.all().exclude(userId=1).order_by('id')
  else:
    print('Else..')
    bills = Tax.objects.all().filter(userId=request.user).order_by('-created')

  context['count'] = bills.count()
  # print('Total count : ',context['count'])
  # print('Total count : ',type(context['count']))
  if context['count'] == 0:
    print('Total count : ',context['count'])
    context['unpaid_tax'] = 0
    context['paid_tax'] = 0
    context['partial_bills'] = None
    print(context['partial_bills'])
    context['paid_share'] = 0
    context['unpaid_share'] = 0
    context['net_tax'] = 0
  else:
    context['partial_bills'] = bills[:3]
    # print(context['partial_bills'])
    # unpaid_bill = Tax.objects.all().filter(userId=request.user,paymentStatus='Unpaid')
    context['net_tax'] = Tax.objects.all().aggregate(Sum('total_tax'))
    context['net_tax'] = context['net_tax']['total_tax__sum']
    print(context['net_tax'])
    unpaid_bill = Tax.objects.all().filter(paymentStatus='Unpaid')
    # unpaid_bill = Tax.objects.all().filter(userId=request.user,paymentStatus='Unpaid')
    paid_bill = Tax.objects.all().filter(paymentStatus='Paid')
    # paid_bill = Tax.objects.all().filter(userId=request.user,paymentStatus='Paid')
    # paid_bill = Tax.objects.all().filter(userId=request.user,paymentStatus='Paid')
    context['unpaid_tax'] = unpaid_bill.aggregate(Sum('total_tax'))
    context['paid_tax'] = paid_bill.aggregate(Sum('total_tax'))
    # context['net_tax'] = context['paid_tax']+context['unpaid_tax']
    if context['paid_tax']['total_tax__sum'] == None:
      context['paid_tax'] = 0
      context['paid_share'] = 0
    else:
      context['paid_tax'] = round(context['paid_tax']['total_tax__sum'],2)
      context['paid_share'] = round((context['paid_tax']/context['net_tax'])*100,2)

    if context['unpaid_tax']['total_tax__sum'] == None:
      context['unpaid_tax'] = 0
      context['unpaid_share'] = 0
    else:
      context['unpaid_tax'] = round(context['unpaid_tax']['total_tax__sum'],2)
      context['unpaid_share'] = round((context['unpaid_tax']/context['net_tax'])*100,2)

    # context['paid_share'] = round((context['paid_tax']/context['net_tax'])*100,2)
    # context['unpaid_share'] = round((context['unpaid_tax']/context['net_tax'])*100,2)

    # context['paid_tax'] = round(context['paid_tax']['total_tax__sum'],2)
    # context['net_tax'] = context['paid_tax']+context['unpaid_tax']
    # if context['paid_tax'] != 0:
      # context['paid_share'] = round((context['paid_tax']/context['net_tax'])*100,2)
    # if context['unpaid_tax'] != 0:
      # context['unpaid_share'] = round((context['unpaid_tax']/context['net_tax'])*100,2)

  # context['unpaid_share'] = round((context['unpaid_tax']/context['net_tax'])*100,2)
  # context['paid_share'] = round((context['paid_tax']/context['net_tax'])*100,2)

  # context['paid_share'] = round((context['paid_tax']/context['net_tax'])*100,2)
  # context['unpaid_share'] = round((context['unpaid_tax']/context['net_tax'])*100,2)
  # context['paid_tax'] = round(context['paid_tax']['total_tax__sum'],2)
  # context['unpaid_tax'] = round(context['unpaid_tax']['total_tax__sum'],2)
  print(context['paid_tax'])
  print(context['unpaid_tax'])
  return render(request,'homepage.html',{'bills':bills,'context':context})


@login_required
def view_bills(request):
  if str(request.user) == 'admin' or str(request.user.profile.role) == 'Tax-Accountant':
    bills = Tax.objects.all().exclude(userId=1).order_by('id')
  else:
    # print('Else..')
    bills = Tax.objects.all().filter(userId=request.user).order_by('id')
  for bill in bills:
    if bill.dueDate <= date.today() and bill.paymentStatus == 'Unpaid':
      nod = (date.today()-bill.dueDate).days
      bill.STATUS = 'DELAYED'
      bill.fines = -10*max(1,int(nod))
    bill.save()
  bill_length = bills.count()
  return render(request,'bill_list.html',{'bills':bills,'bill_length':bill_length})


@login_required
def bill_detail(request,pk):
  bill = get_object_or_404(Tax,id=pk)
  print(request.user,bill.userId)
  if request.user == bill.userId or str(request.user) == 'admin' or str(request.user.profile.role) == 'Tax-Accountant':
    print(bill.STATUS)
    # d1 = bill.dueDate
    # # d1 = datetime.date.strptime(str(bill.dueDate),'%Y-%m-%d')
    # d2 = bill.created
    # d3 = date.today()
    # print(d1,type(d1),d2,type(d2),d3,type(d3))
    # if d1 <= d3 and bill.paymentStatus == 'Unpaid':
    #   # status = "Delayed"
    #   # fine = -10
    #   bill.STATUS = 'DELAYED'
    #   bill.fines = -10
    # elif d1 <= d3 and bill.paymentStatus == 'Paid':
    #   # status = "Delayed"
    #   # fine = -10
    #   bill.STATUS = 'New'
    #   bill.fines = 0
    # else:
    #   bill.STATUS = 'New'
    # bill.save()
  else:
    return HttpResponse('Unauthorised!')
  # context = {'status':status,'fine':fine}
  return render(request,'bill_detail.html',{'bill':bill})

# CREATE
@login_required
def billCreate(request):
  print(request.user)
  # print(request.cleaned_data)
  if str(request.user) == 'admin' or str(request.user.profile.role) == 'Tax-Accountant':
    form = BillForm2
  else:
    form = BillForm()
  if request.method == 'POST':
    form = BillForm(request.POST)
    web1 = form.save(commit=False)
    print('Inside form')
    web1.userId = request.user
    print(web1.state)
    if web1.state.title() in STATE or web1.state.title() in U_T:
      if web1.state.title() in U_T:
        web1.total_tax = round((web1.salaryIncome + web1.stockIncome)*(web1.CGST)*0.01,2)
      else:
        web1.total_tax = round((web1.salaryIncome + web1.stockIncome)*(web1.SGST + web1.CGST)*0.01,2)
      web1.fine = 0
      print(web1.userId)
    else:
      errors ='Invalid State'
      val = 'Invalid'
      print(val)
      return render(request,'tax_app/add_bill.html',{'form':form,'errors':errors,'val':val})
    # print(form.cleaned_data)
    if form.is_valid():
      web1.save()
      return render(request,'tax_app/bill_list.html')
    else:
      return HttpResponse('Not a valid field!')
  else:
    print('Else...')
  # return render(request,'tax_app/bill_list.html',{'form':form})
  return render(request,'tax_app/add_bill.html',{'form':form})


@login_required
def BillUpdateView(request,pk):
  print(request.user)
  bill = get_object_or_404(Tax,pk=pk)
  if str(request.user) == 'admin' or str(request.user.profile.role) == 'Tax-Accountant':
    form = BillForm2(request.POST or None, instance=bill)
  else:
    form = BillForm(request.POST or None, instance=bill)

  print('Check1')
  f = form.save(commit=False)
  state_field = f.state
  # print(bill.state.title())
  f = False
  val = 'Invalid'
  if state_field.title() in STATE or state_field.title() in U_T:
    print('Check')
    f = True
    val = 'Valid'
  else:
    return render(request,'tax_form.html',{'form':form,'val':val})

  if form.is_valid() and f==True:
    print('Bills details :')
    # print(bill.salaryIncome,bill.stockIncome,bill.SGST,bill.CGST)
    bill.total_tax = round((bill.salaryIncome + bill.stockIncome)*(bill.SGST + bill.CGST)*0.01,2)
    form.save()
    return redirect('tax_app:bill_detail',pk=pk)
    # return redirect('practice:website_list')

  return render(request,'tax_form.html',{'form':form})

@login_required
def BillPayView(request,pk):
  bill = Tax.objects.get(id=pk)
  bill.STATUS = 'New'
  # bill.total_tax = 0
  # bill.fines = 0
  bill.paymentStatus = 'Paid'
  bill.save()
  return render(request,'tax_pay.html',{'bill':bill})

@login_required
def BillDeleteView(request,pk):
  website = get_object_or_404(Tax,pk=pk)
  if request.method == 'POST':
    if request.POST.get('confirm'):
      website.delete()
      return redirect('tax_app:bill_list')
    if request.POST.get('cancel'):
      return redirect('tax_app:bill_detail',pk=pk)
      # return redirect('practice:website_list')
  context = {'website':website}
  return render(request,'website_confirm_delete.html',context)


@login_required
def payment_status(request,pk):
  if str(request.user) == 'admin' or str(request.user.profile.role) == 'Tax-Accountant':
    bills = Tax.objects.all().filter(paymentStatus=pk).order_by('id').exclude(userId=1)
  else:
    print('Else..')
    bills = Tax.objects.all().filter(paymentStatus=pk,userId=request.user).order_by('id').exclude(userId=1)
  bill_length = bills.count()
  print(bill_length)
  return render(request,'bill_list.html',{'bills':bills,'bill_length':bill_length})


@login_required
def bill_status(request,pk):
  if str(request.user) == 'admin' or str(request.user.profile.role) == 'Tax-Accountant':
    bills = Tax.objects.all().filter(STATUS=pk).order_by('id').exclude(userId=1)
  else:
    print('Else..')
    bills = Tax.objects.all().filter(STATUS=pk,userId=request.user).order_by('id').exclude(userId=1)
  bill_length = bills.count()
  bill_length = bills.count()
  return render(request,'bill_list.html',{'bills':bills,'bill_length':bill_length})

prev_tax = 0


@login_required
def bill_stats(request):
  bills = Tax.objects.all()
  # net tax,total tax,total fine,total paid,total due
  total_due,total_fine,total_paid,total_tax = 0,0,0,0
  for bill in bills:
    total_tax += bill.total_tax
    total_fine += bill.fines
    if bill.paymentStatus == 'Paid':
      total_paid += bill.total_tax + abs(bill.fines)
    else:
      total_due += bill.total_tax + abs(bill.fines)

  diff = 0
  if total_tax > prev_tax and prev_tax!=0:
    diff = round((((total_tax-prev_tax)/prev_tax)*0.01),2)
  else:
    pass
    # prev_tax = total_tax

  context = {'total_tax':round(total_tax,2),'total_fine':round(total_fine,2),
              'total_paid':round(total_paid,2),'total_due':round(total_due,2),
              'net_tax':round(total_tax+abs(total_fine),2),'diff':diff}
  return render(request,'bill_stats.html',{'context':context})


