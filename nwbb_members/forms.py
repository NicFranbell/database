from django.forms import ModelForm
from nwbb_members.models import Member
from django.contrib.auth.models import User


class MemberForm(ModelForm):
    class Meta:
        model = Member
        fields = ['id_number', 'address_one','address_two','town','county','post_code','home_tel','mobile_tel','email_shared']
    

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')