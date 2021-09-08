from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from apps.utils.colors import red, green, cyan


class Command(BaseCommand):
    help = 'Create Super User Automatically'

    def handle(self, *args, **kwargs):
        print(green(msg='\nCreating Django User ...'))
        username = 'admin'
        password = '123'
        try:
            User.objects.create(
                username=username,
                password=make_password(password),
                is_active=True,
                is_staff=True,
                is_superuser=True
            )
            print(green('User created successfully'))
            print(cyan('Username: {} \nPassword: {}'.format(
                green(msg=username),
                green(msg=password),
            )))
        except:
            print(red(msg='User cannot be created, check database connection or if the user already exists'))
        print(cyan(msg='User creation process done \n'))

