from django.contrib import admin
from django.urls import path, include
# include allows us to import and use another urls.py file

urlpatterns = [
    path('admin/', admin.site.urls),  # admins url
    path("accounts/", include("allauth.urls")),
    path('summernote/', include('django_summernote.urls')),
    path("", include("event.urls"), name="event-urls"),
    # events page url including, paginated events and calender page
]
