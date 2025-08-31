# بعد إنشاء الحجز، استدعي task
from .tasks import send_booking_confirmation_email

def create(self, request, *args, **kwargs):
    response = super().create(request, *args, **kwargs)
    booking = self.get_object()  # افتراضاً بيجيب الحجز الجديد
    send_booking_confirmation_email.delay(booking.id, booking.customer.email)
    return response

