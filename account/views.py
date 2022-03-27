from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import UserCreationForm
from .forms import UserCreateForm, ProfileForm,ProfileUpdateForm
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.shortcuts import render,get_object_or_404


# Create your views here.
def register(request):
  if request.method == 'POST':
    form = UserCreateForm(request.POST)
    profile_form = ProfileForm(request.POST)
    # profile_form = ProfileForm(request.POST)
    # print(profile_form.user_id)
    # form.fields['username'].widget.attrs.update({
    #         'placeholder': 'Username'
    #     })
    # form.fields['first_name'].widget.attrs.update({
    #         'placeholder': 'First Name'
    #     })
    # form.fields['last_name'].widget.attrs.update({
    #         'placeholder': 'Last Name'
    #     })
    # profile_form.fields['role'].widget.attrs.update({
            # 'placeholder': 'Enter Role(Tax-Payer/Tax-accountant)'
        # })
    # form.fields['email'].widget.attrs.update({
    #         'placeholder': 'Enter Email'
    #     })
    # form.fields['password1'].widget.attrs.update({
    #         'placeholder': 'Password'
    #     })
    # form.fields['password2'].widget.attrs.update({
    #         'placeholder': 'Confirm Password'
    #     })
    # profile_form.fields['role'].widget.attrs.update({
    #         'placeholder': 'Enter Role'
    #     })
    if form.is_valid() and profile_form.is_valid():
      user = form.save()
      profile = profile_form.save(commit=False)
      profile.user = user
      profile.save()
    #   user_info = request.user.get_profile()
    #   user_info.role = form.cleaned_data['role']
    #   user_info.middleName = form.cleaned_data['middleName']
    #   user_info.save()

    #   profile_form.save()

      username = form.cleaned_data.get('username')
      messages.success(request,f"Welcome {username}, Please login to continue!")
      return redirect("login")
      # return redirect("practice:index")
    # else:
      # messages.error(request,'Something went wrong!')
      # return redirect("register")
  else:
    form = UserCreateForm()
    profile_form = ProfileForm()
    # form.fields['username'].widget.attrs.update({
    #         'placeholder': 'Username'
    #     })
    # form.fields['first_name'].widget.attrs.update({
    #         'placeholder': 'First Name'
    #     })
    # form.fields['last_name'].widget.attrs.update({
    #         'placeholder': 'Last Name'
    #     })
    # # profile_form.fields['role'].widget.attrs.update({
    # #         'placeholder': 'Enter Role'
    # #     })
    # form.fields['email'].widget.attrs.update({
    #         'placeholder': 'Enter Email'
    #     })
    # form.fields['password1'].widget.attrs.update({
    #         'placeholder': 'Password'
    #     })
    # form.fields['password2'].widget.attrs.update({
    #         'placeholder': 'Confirm Password'
    #     })
  return render(request,'account/register.html',{'form':form,'profile_form':profile_form})


@login_required
def userProfile(request):
  return render(request,'account/profile.html')

@login_required
def update_profile(request,pk):
  if request.method == 'POST':
    # form = UserCreateForm(request.POST)
    profile_form = ProfileForm(request.POST)
    if profile_form.is_valid():
      # user = form.save()
      profile = profile_form.save(commit=False)
      # profile.user = user
      profile.save()
    #   user_info = request.user.get_profile()
    #   user_info.role = form.cleaned_data['role']
    #   user_info.middleName = form.cleaned_data['middleName']
    #   user_info.save()

    #   profile_form.save()

      # username = form.cleaned_data.get('username')
      # messages.success(request,f"Welcome {username}, Please login to continue!")
      return redirect("profile")
      # return redirect("practice:index")
    # else:
      # messages.error(request,'Something went wrong!')
      # return redirect("register")
  else:
    # form = UserCreateForm()
    profile_form = ProfileForm()
  return render(request,'account/update_profile.html',{'profile_form':profile_form})


# @login_required
# def userProfile(request):
#     if request.method == 'POST':
#         user_form = UserCreateForm(request.POST, instance=request.user)
#         profile_form = ProfileForm(request.POST, instance=request.user.profile)
#         print(profile_form)
#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             messages.success(request, _('Your profile was successfully updated!'))
#             return redirect('settings:profile')
#         else:
#             messages.error(request, _('Please correct the error below.'))
#     else:
#         user_form = UserCreateForm(instance=request.user)
#         profile_form = ProfileForm(instance=request.user.profile)
#     return render(request, 'account/profile.html', {
#         'user_form': user_form,
#         'profile_form': profile_form
#     })


# def user_type(request,pk):
#   users = User.objects.all().filter(userId.role_contains=pk).order_by('id')
#   return render(request,'user_list.html',{'users':users})

def user_list(request):
  users = User.objects.all().order_by('id').exclude(id=1)
  return render(request,'user_list.html',{'users':users})

def user_detail(request,pk):
  # user = get_object_or_404(User,pk=pk)
  print(pk)
  user1 = User.objects.get(id=pk)
  print('Staff user is : ',user1)
  return render(request,'user_detail.html',{'user1':user1})


def update_profile(request,pk):
  staff = get_object_or_404(User,pk=pk)
  form = ProfileUpdateForm(request.POST or None, instance=staff)
  if form.is_valid():
    print('Staff details :')
    # print(staff,staff.profile.role)
    # print(form.cleaned_data)
    staff.profile.role = form.cleaned_data['role']
    staff.profile.save()
    # form.save()
    return redirect('tax_app:user_detail',pk=pk)
  else:
    print('Inside Else..')
    form = ProfileUpdateForm()

  return render(request,'account/update_profile.html',{'form':form})
