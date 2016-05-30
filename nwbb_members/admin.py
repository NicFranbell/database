from django.contrib import admin

from . models import Member, RoleType, DrivingOffence, MemberDrivingOffence, Training, MemberTraining

admin.site.register(Member)
admin.site.register(RoleType)
admin.site.register(DrivingOffence)
admin.site.register(MemberDrivingOffence)
admin.site.register(Training)
admin.site.register(MemberTraining)
