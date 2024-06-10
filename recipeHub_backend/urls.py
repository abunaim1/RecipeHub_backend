from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    path('auth/', include('authentication.api.urls')),
    path('user/', include('user.urls')),

    path('kitchen/', include('kitchen.urls')),
    path('banner/', include('banner.urls')),
    path('support/', include('support.urls')),
    path('promotions/', include('promotions.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
