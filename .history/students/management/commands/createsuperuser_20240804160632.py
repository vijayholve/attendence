from django.contrib.auth.management.commands.createsuperuser import Command as SuperUserCommand
from django.core.management import CommandError
from django.contrib.auth import get_user_model

class Command(SuperUserCommand):
    def add_arguments(self, parser):
        super().add_arguments(parser)
        parser.add_argument(
            '--user_type', 
            dest='user_type', 
            default=None,
            help='Specifies the user type for the superuser.'
        )

    def handle(self, *args, **options):
        user_type = options.get('user_type')

        if not user_type:
            raise CommandError('You must provide a user type.')

        options['user_type'] = user_type

        super().handle(*args, **options)

    def get_input_data(self, field, value):
        if field.name == 'user_type':
            if not value:
                raise CommandError(f"You must provide a {field.name}.")
        return super().get_input_data(field, value)
