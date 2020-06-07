from django.urls import path, include
from django.conf.urls.static import static, settings
from django.conf import settings
from .views import RegisterDoneView, LoginUserView, register_user, phone_activate

app_name = 'account'

urlpatterns = [
    path('register/done/', RegisterDoneView.as_view(), name='register_done'),
    path('register/', register_user, name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('phone_activate/', phone_activate, name='phone_activate')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
