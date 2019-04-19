import re
from uuid import UUID

from django.contrib.auth import get_user_model
from django.db.models import Q

UserModel = get_user_model()


class EmailOrSocialBackend:
    def get_user(self, user_id):
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None

    def authenticate(self, request, username=None, password=None, **kwargs):
        api_auth = False

        try:
            username = UUID(username, version=4)
            query = Q(id=username)
        except ValueError:
            if re.match(r"[^@]+@[^@]+\.[^@]+", username):
                query = Q(email=username)
            else:
                query = Q(google_key=username) \
                        | Q(instagram_key=username) \
                        | Q(facebook_key=username)
                api_auth = True
        try:
            user = UserModel.objects.get(query)
        except UserModel.DoesNotExist:
            UserModel().set_password(password)
        else:
            if (not api_auth and user.check_password(password)) or api_auth:
                return user
