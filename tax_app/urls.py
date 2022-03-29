import django
from django.urls import path
from django.contrib.sitemaps.views import sitemap
from . import views
from account import views as account_view

app_name = 'tax_app'

urlpatterns = [
  path('',views.homepage,name='homepage'),
  path('bill-list/',views.view_bills,name='bill_list'),
  path('add-bill/',views.billCreate,name='add_bill'),
  path('bill-detail/<int:pk>',views.bill_detail,name='bill_detail'),
  path('bill/<int:pk>/edit',views.BillUpdateView,name='bill_update'),
  path('bill/<int:pk>/pay',views.BillPayView,name='bill_pay'),
  path('bill/<int:pk>/delete',views.BillDeleteView,name='bill_delete'),
  path('bill-staus/<str:pk>',views.bill_status,name='bill_status'),
  path('payment-staus/<str:pk>',views.payment_status,name='payment_status'),
  path('bill-stats/',views.bill_stats,name='bill_stats'),


  path('user-list/',account_view.user_list,name='user_list'),
  path('user-detail/<int:pk>',account_view.user_detail,name='user_detail'),
]

