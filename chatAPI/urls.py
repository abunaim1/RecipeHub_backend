from django.urls import path, include
from .views import SearchUser

urlpatterns = [
    path('search/<username>', SearchUser.as_view())
]
