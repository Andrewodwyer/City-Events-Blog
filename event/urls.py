from . import views # Function-based view is imported
from .views import EventListByCategory
from django.urls import path
# from .views import add_event


urlpatterns = [
    path('', views.EventList.as_view(), name='home'), #This pattern tells Django to look in the event app URL file for any blog urlpatterns.
    path('calendar/', views.calendar_view, name='calendar'),  # Path for the calendar page
    path('api/events/', views.get_events, name='get_events'),  # API to fetch events from the database
    path('event/my_events/', views.my_events, name='my_events'), # The organisers events
    path('event/add/', views.add_event, name='add_event'),
    path('event/<slug:slug>/edit/', views.edit_event, name='edit_event'), # to edit the event in the add_event.html using the view edit_event
    path('event/<slug:slug>/', views.addevent_detail, name='addevent_detail'), # to see the selected event
    path('event/<slug:slug>/edit_comment/<int:comment_id>',views.comment_edit, name='comment_edit'), # to edit the comment in the addevent_detail.html using the view comment_edit
    path('event/<slug:slug>/delete_comment/<int:comment_id>',views.comment_delete, name='comment_delete'), # delete comments
    path('event/<slug:slug>/delete_event/<int:event_id>',views.delete_event, name='delete_event'), # delete event
    path('event/category/<int:category_id>/', EventListByCategory.as_view(), name='events_by_category'), #Users can filter events by category
    path('toggle-attendance/', views.toggle_attendance, name='toggle_attendance'), # attendance button
]