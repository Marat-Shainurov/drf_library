from celery import shared_task

from users.service import send_greeting_email


@shared_task
def greet_new_user(user_email: str, username: str) -> None:
    """
    Celery task for sending the greeting email for new users.

    :param user_email: a string representing the new user's email
    :param username: a string representing the new user's username
    """
    send_greeting_email(user_email=user_email, username=username)
