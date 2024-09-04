from . import views
from django.urls import path

urlpatterns = [
    path('event/', views.EventList.as_view(), name='home'), #This pattern tells Django to look in the event app URL file for any blog urlpatterns.
    path('calendar/', views.calendar_view, name='calendar'),  # Path for the calendar page
    path('api/events/', views.get_events, name='get_events'),  # API to fetch events from the database
    path('event/<slug:slug>/', views.addevent_detail, name='addevent_detail'),
]