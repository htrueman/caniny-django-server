from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils import six
from django.contrib.auth.tokens import PasswordResetTokenGenerator


class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp) +
            six.text_type(user.is_active)
        )


account_activation_token = TokenGenerator()


def send_activation_token(mail_subject, template_name, user, email):
    message = render_to_string(template_name, {
        'domain': settings.HOST_NAME,
        'uid': user.pk,
        'token': account_activation_token.make_token(user),
    })
    send_mail(mail_subject, message, settings.DEFAULT_FROM_EMAIL, (email,))
