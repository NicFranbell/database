import operator
from django.contrib.auth.models import AnonymousUser
from nwbb_members.models import MemberRole
from django.db.models.query_utils import Q

def check_member_roles(user, roles):
    return MemberRole.objects.filter(Q(member=user)&(reduce(operator.or_, [Q(role_type__name=x) for x in roles]))).exists()

def can_view_member(user):
    if user is AnonymousUser:
        return False
    else:
        return check_member_roles(user, ['Membership Secretary','Recruitment Manager','Events Manager','Committee Member','Trustee','Rider','Examiner','Controller','Fundraiser','Member','Deputy Area Manager','Area Manager','Controller Manager'])
    

def can_add_member(user):
    return check_member_roles(user, ['Membership Secretary','Recruitment Manager'])
 
def can_delete_member(user):
    return MemberRole.objects.filter(member__user=user, role_type='Membership Secretary').count() > 0
