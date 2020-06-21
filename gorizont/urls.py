
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static, settings
from django.conf import settings
from main.views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/', include('book.urls')),
    path('event/', include('event.urls')),
    path('', index, name='main'),
    path('panel/', include('panel.urls')),
    path('account/', include('account.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
