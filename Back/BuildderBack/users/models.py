from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
# Create your models here.

def upload_location(instance, filename):
    return "%s/%s" %(instance.user_id,filename)

class B_User(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length= 120)
    last_name = models.CharField(max_length=120)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50,null=False)
    photo = models.ImageField(upload_to=upload_location ,null=True, blank=True, width_field="width_field" ,height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    joined = models.DateTimeField(auto_now=False, auto_now_add=True)
    # facebook_link = models.URLField(max_length=200)
    # twitter_link = models.URLField(max_length=200)
    # linkedin_link = models.URLField(max_length=200)
    # Projects_active = pending
    # Posts= pending
    # Comments = pending
    # P_Creator = models.BooleanField(default=False)
    # P_Collaborator = models.BooleanField(default=False)
    # P_Investor = models.BooleanField(default=False)

    def __unicode__(self):
        return self.first_name
    
    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse("users:detail",kwargs={"user_id":self.user_id})
    
    class Meta:
        ordering=["joined"]

