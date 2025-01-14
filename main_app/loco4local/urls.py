
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('home/', include('home.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls'))

]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)