from django import forms
from django.forms import ModelForm
from nwbb_members.models import Member, MemberDrivingOffence, DrivingOffence,\
    Training, MemberTraining
from django.contrib.auth.models import User

    
class MemberForm(ModelForm):   
    class Meta:      
        model = Member
        fields = ['id_number', 'address_one','address_two','town','county','post_code','home_tel','mobile_tel','email_shared', 'driver_license_number','driver_license_expiry_date','comments', 'roles']
    
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')

class OffenceForm(ModelForm):
    code = forms.ModelChoiceField(queryset=DrivingOffence.objects.order_by('code'), label="Driving Offence", to_field_name="code")
    date = forms.DateField(widget=forms.SelectDateWidget())
    
    class Meta:
        model = MemberDrivingOffence        
        fields =('date','code', 'points')

class TrainingForm(ModelForm):
    training = forms.ModelChoiceField(queryset=Training.objects.order_by('name'), label="Training/Qualification")
    date_completed = forms.DateField(widget=forms.SelectDateWidget())
        
    class Meta:
        model = MemberTraining        
        fields =('training', 'date_completed', 'expiry_date','awarded_by')