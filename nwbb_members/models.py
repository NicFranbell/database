from django.db import models
from django.contrib.auth.models import User



class Member(models.Model):
    user = models.OneToOneField(User, related_name="profile")
    id_number = models.CharField(max_length=50, blank=False)
    address_one = models.CharField(max_length=50, blank=True)
    address_two = models.CharField(max_length=50, blank=True)
    town = models.CharField(max_length=20, blank=True)
    county = models.CharField(max_length=20, blank=True)
    post_code = models.CharField(max_length=9, blank=False)
    home_tel = models.CharField(max_length=25, blank=True)
    mobile_tel = models.CharField(max_length=25, blank=True)
    email_shared = models.BooleanField(default=True)
    
       
    def __unicode__(self):
        return self.user.get_full_name()


class RoleType(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    
    def __unicode__(self):
        return self.name
    

class MemberRole(models.Model):
    member = models.ForeignKey(User, related_name="member_role")
    role_type = models.ForeignKey(RoleType)
    
    def __unicode__(self):
        return self.role_type.name 
    
    