from rest_framework.views import APIView
from rest_framework.response import Response
from booking.models import Booking, User
from theater.models import ShowTiming, Seat
from booking.tasks import send_email

class BookingView(APIView):

    def post(self, request):
        data = request.data
        seat_ids = data['seat_ids']

        for seat in seat_ids:

            booking = Booking.objects.create(
                booked_by_id=data['user_id'],
                show_timing_id=data['show_timing_id'],
                seat_id=seat
            )
        data['status'] = "confirmed"
        movie = ShowTiming.objects.get(id=data['show_timing_id']).movie.name
        data['movie'] = movie
        seats = Seat.objects.filter(id__in=seat_ids).values('seat_number')
        user = User.objects.get(id=data['user_id'])

        send_email(user, movie, seats)

        return Response(data=data)