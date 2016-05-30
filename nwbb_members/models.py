from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


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

class DrivingOffence(models.Model):
    code = models.CharField(max_length=10, blank=False)
    name= models.CharField(max_length=200, blank=False)
    min_points = models.IntegerField(blank=True)
    max_points = models.IntegerField(blank=True)
    duration = models.IntegerField()
    DURATION_DETAILS = (
        ('DOO','Depending on Offence'),
        ('DOC','Depending on Conviction'),                     )
    duration_details = models.CharField(max_length=3, choices = DURATION_DETAILS, blank=True)
    
    def __unicode__(self):
        return self.code   + " " + self.name + " (" + str(self.min_points) + "-" + str(self.max_points) + " points)"  
                             
class MemberDrivingOffence(models.Model):
    member = models.ForeignKey(User, related_name="member_offence")
    code = models.ForeignKey(DrivingOffence, related_name="offences", blank=False, null=False)
    date = models.DateField()
    points = models.IntegerField()
    
    def __unicode__(self):
        return self.code.code + " - " + self.code.name + " - " + str(self.points) + " point(s)"
    
    def clean(self): 
        if self.date :
            if self.date > date.today():
                raise ValidationError({'date': _('The date cannot be in the future.')})
        
        if self.points and self.code_id is not None:
            if self.points < self.code.min_points:
                raise ValidationError({'points': _('Points cannot be less than the minimum for the offence.')})
        
            if self.points > self.code.max_points:
                raise ValidationError({'points': _('Points cannot be more than the maximum for the offence.')})

class Training(models.Model):   
    name = models.CharField(max_length=200, blank=False)
    description = models.TextField(blank=True, null=True)
    
    def __unicode__(self):
        return self.name
        
class MemberTraining(models.Model):
    member = models.ForeignKey(User, related_name="member_training")
    training = models.ForeignKey(Training, related_name="member_training", blank=False, null=False)
    date_completed = models.DateField(blank=True, null=True)
    expiry_date = models.DateField(blank=True, null=True)
    awarded_by = models.CharField(max_length=200, blank=True, null=True)
    
    def __unicode__(self):
        return self.training.name
        
    def clean(self): 
        if self.date_completed :
            if self.date_completed > date.today():
                raise ValidationError({'date_completed': _('The date cannot be in the future.')})