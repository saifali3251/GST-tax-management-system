from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


# Create your models  here.
# class CustomUser(AbstractUser):
  # pass

  # def __str__(self):
    # return self.username

    # is_tax_payer = models.BooleanField(default=True)
    # is_tax_accountant = models.BooleanField(default=False)
    # middleName = models.CharField(max_length=20,null=True,blank=True)
    # mailing_address = models.CharField(max_length=200, blank=True)
    # role = models.CharField(max_length=10,default='Tax-Payer',null=True)



class Profile(models.Model):
  CHOICES = (
    ('TP','taxPayer'),('TA','taxAccountant')
  )
  user = models.OneToOneField(User,on_delete=models.CASCADE)
  name = models.CharField(max_length=200,null=True)
  middleName = models.CharField(max_length=20,null=True,blank=True)
  role = models.CharField(max_length=20,default='Tax-Payer')
  # role = models.CharField(max_length=20,choices=CHOICES,default=CHOICES[0][0])
  created = models.DateTimeField(blank=True,auto_now_add=True)
  updated = models.DateTimeField(blank=True,auto_now=True)

  def __str__(self):
    return f'{self.user}'

  def get_absolute_url(self):
    # return reverse('tax_app:user_detail',pk = self.id)
    # print(self.user.id)
    return reverse('tax_app:user_detail',args=[self.user.id])

  # @receiver(post_save, sender=User)
  # def create_user_profile(sender, instance, created, **kwargs):
  #   if created:
  #       Profile.objects.create(user=instance)

  # @receiver(post_save, sender=User)
  # def save_user_profile(sender, instance, **kwargs):
  #   instance.profile.save()




