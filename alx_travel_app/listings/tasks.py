# alx_travel_app_0x03/listings/tasks.py
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_booking_confirmation_email(booking_id, customer_email):
    subject = f"Booking Confirmation #{booking_id}"
    message = f"Your booking with ID {booking_id} has been confirmed."
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [customer_email]

    send_mail(subject, message, from_email, recipient_list)
    return f"Booking confirmation email sent to {customer_email}"

