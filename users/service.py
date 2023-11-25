from django.core.mail import send_mail

from config import settings


def send_greeting_email(user_email: str, username: str) -> None:
    """
    Sends a greeting email to a user with <user_email> and <username>.

    :param user_email: a string representing user's email
    :param username: a string representing user's username
    """
    send_mail(
        subject="Hello and Welcome!",
        message=f'Dear {username}, \nThanks for joining to our library! ;)',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user_email],
    )
