from django.contrib.auth.backends import ModelBackend

from .models import CustomUser


class PhoneModelBackend(ModelBackend):
    def authenticate(self, request, contact_number=None, password=None):
        try:
            user = CustomUser.objects.get(contact_number=contact_number)
            if user.check_password(password):
                return user
        except CustomUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None

