from django.contrib import admin

from . models import Member, RoleType, MemberRole

admin.site.register(Member)
admin.site.register(RoleType)
admin.site.register(MemberRole)

