from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from BaseApp.models import UserDetails

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('email')
        parser.add_argument('password')
        parser.add_argument('role')

    def handle(self, *args, **options):
        try:
            user = User.objects.get(email=str(options['email']))
            self.stdout.write('user already created')
            user_details = UserDetails.objects.get(userKey = user)
            print '--------------user is deleted-----------'
            user.delete()
            user_details.delete()
            print '---------------re creating user-------- '
            user = User.objects.create_user(str(options['email']), str(options['email']), str(options['password']))
            userobj = UserDetails()
            userobj.userKey = user
            userobj.role = str(options['role'])
            userobj.save()
            user.save()
            self.stdout.write('Successfully closed poll ')



        except Exception, e:
            print '---------------creating new user-------- '
            user = User.objects.create_user(str(options['email']), str(options['email']), str(options['password']))
            userobj = UserDetails()
            userobj.userKey = user
            userobj.role = str(options['role'])
            userobj.save()
            user.save()
            self.stdout.write('Successfully created')