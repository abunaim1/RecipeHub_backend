from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import PromotionViewset

router = DefaultRouter()
router.register('list', PromotionViewset)

urlpatterns = [
    path('', include(router.urls))
]
