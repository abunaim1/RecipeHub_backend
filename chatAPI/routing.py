from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/ac/<str:group_name>/', consumers.MyAsyncConsumer.as_asgi()),
]
