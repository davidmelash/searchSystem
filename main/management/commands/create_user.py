from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from main.models import CustomUser


class Command(BaseCommand):
    help = 'Create a user'

    def handle(self, *args, **options):
        User = get_user_model()
        email = "admin@example.com"
        first_name = "Admin"
        last_name = "User"
        password = "password"
        is_superuser = True

        try:
            if is_superuser:
                user = User.objects.create_superuser(
                    email=email,
                    username="admin",
                    first_name=first_name,
                    last_name=last_name,
                    password=password,
                )
                self.stdout.write(self.style.SUCCESS(f'Successfully created superuser {user}'))
            else:
                user = User.objects.create_user(
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                    password=password,
                )
                self.stdout.write(self.style.SUCCESS(f'Successfully created user {user}'))
        except Exception as e:  # Catching specific exceptions is better
            self.stdout.write(self.style.ERROR(f'Error creating user: {e}'))