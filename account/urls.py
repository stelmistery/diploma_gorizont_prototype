from django.urls import path, include
from django.conf.urls.static import static, settings
from django.conf import settings
from .views import RegisterUserView, RegisterDoneView

app_name = 'account'

urlpatterns = [
    path('register/done/', RegisterDoneView.as_view(), name='register_done'),
    path('register/', RegisterUserView.as_view(), name='register'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
