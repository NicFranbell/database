from django.db import models
from django.contrib.auth.models import User

class RoleType(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    
    def __unicode__(self):
        return self.name
    
class Member(models.Model):
    user = models.OneToOneField(User, related_name="profile")
    id_number = models.CharField(max_length=50, blank=False)
    address_one = models.CharField(max_length=100, blank=True)
    address_two = models.CharField(max_length=50, blank=True)
    town = models.CharField(max_length=100, blank=True)
    county = models.CharField(max_length=50, blank=True)
    post_code = models.CharField(max_length=9, blank=False)
    home_tel = models.CharField(max_length=25, blank=True)
    mobile_tel = models.CharField(max_length=25, blank=True)
    email_shared = models.BooleanField(default=True)
    roles = models.ManyToManyField(RoleType, related_name="member_roles", blank=True)
    comments = models.CharField(max_length=200, blank=True)
    driver_license_number = models.CharField(max_length=100, blank=True)
    driver_license_expiry_date = models.DateField(null=True, blank=True)
    bike_registration = models.CharField(max_length=100, blank=True)

    def __unicode__(self):
        return self.user.get_full_name()