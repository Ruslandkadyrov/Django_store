from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create(self, contact_number, password=None, **extra_fields):
        if not contact_number:
            raise ValueError('Phone number is required')
        user = self.model(username=contact_number, contact_number=contact_number, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, contact_number, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        return self.create(contact_number, password, **extra_fields)
