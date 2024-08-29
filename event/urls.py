from . import views
from django.urls import path

urlpatterns = [
    path('event/', views.EventList.as_view(), name='home'), #This pattern tells Django to look in the event app URL file for any blog urlpatterns.
]