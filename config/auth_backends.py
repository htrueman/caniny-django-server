from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

UserModel = get_user_model()


class EmailOrSocialBackend:
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserModel.objects.get(Q(id=username)
                                         | Q(email=username)
                                         | Q(google_key=username)
                                         | Q(instagram_key=username)
                                         | Q(facebook_key=username))
        # except UserModel.DoesNotExist:
        #     # Run the default password hasher once to reduce the timing
        #     # difference between an existing and a nonexistent user (#20760).
        #     UserModel().set_password(password)
        # else:
        #     if user.check_password(password) and self.user_can_authenticate(user):
        #         return user
