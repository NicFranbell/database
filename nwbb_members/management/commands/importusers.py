import csv

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand

from nwbb_members.models import Member


class Command(BaseCommand):
    help = 'Imports the users from users.csv into the Database'

    def handle(self, *args, **options):
        membershipList = csv.reader(open('users.csv', 'rb'), delimiter=',', quotechar='"')
        for row in membershipList:
            id_number = row[0]
            full_name = row[1].strip().title()
            first_name = full_name.split(' ', 1)[0]
            last_name = full_name.split(' ', 1)[1]
            user_name = first_name + '.' + last_name.replace(' ', '_')
            address = row[2]
            address_one = address.split(',')[0]
            town = address.split(',', 1)[1] if len(address.split(',', 1)) > 1 else ""
            post_code = row[3].strip()
            home_tel = row[4].strip()
            mobile_tel = row[5].strip()
            email = row[6].strip()

            user = None
            try:
                user = User.objects.get(username=user_name)
                if (not user):
                    user = User.objects.get(email=email)
            except ObjectDoesNotExist:
                pass
            if not user:
                user = User()
            user.first_name = first_name
            user.last_name = last_name
            user.username = user_name
            user.email = email
            user.save()

            member = None
            try:
                member = Member.objects.get(user=user)
            except ObjectDoesNotExist:
                pass
            if not member:
                member = Member()
            member.user = user
            member.id_number = id_number
            member.address_one = address_one
            member.town = town
            member.post_code = post_code
            member.home_tel = home_tel
            member.mobile_tel = mobile_tel
            member.save()
