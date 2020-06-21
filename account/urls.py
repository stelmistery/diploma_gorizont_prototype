from django.urls import path, include
from django.conf.urls.static import static, settings
from django.conf import settings
from django.contrib.auth.views import LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView
from .views import CustomPasswordResetView, CustomPasswordResetDoneView, CustomPasswordResetConfirmView, reset_done

from .views import RegisterDoneView, LoginUserView, register_user, phone_activate, LogoutUserView

# app_name = 'account'

urlpatterns = [
    path('register/done/', RegisterDoneView.as_view(), name='register_done'),
    path('register/', register_user, name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='main'), name='login'),
    path('phone_activate/', phone_activate, name='phone_activate'),
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', reset_done, name='password_reset_complete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
