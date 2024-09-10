from . import views
from django.urls import path
from .views import add_event, EventListByCategoryView

urlpatterns = [
    path('', views.EventList.as_view(), name='home'), #This pattern tells Django to look in the event app URL file for any blog urlpatterns.
    path('calendar/', views.calendar_view, name='calendar'),  # Path for the calendar page
    path('api/events/', views.get_events, name='get_events'),  # API to fetch events from the database
    path('event/<slug:slug>/', views.addevent_detail, name='addevent_detail'),
    path('add-event/', add_event, name='add_event'),
    path('category/<int:category_id>/', views.event_list_by_category, name='events_by_category'), #Users can filter events by category id int number
]