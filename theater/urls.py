from django.urls import path
from theater.views import TheaterView


urlpatterns = [
    path('', TheaterView.as_view(),name="list_theaters"),
]