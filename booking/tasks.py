from celery import shared_task

@shared_task
def send_email(user_obj, movie, seats):
    email = f"""
    hello {user_obj.email},
    {seats}tickets confirmed for {movie}."""
    # send email
    return True