# ocr/urls.py

from django.urls import path
from ocr import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('upload/', views.upload_image, name='upload_image'),
    path('process/', views.upload_image, name='process_image'),
    path('', LoginView.as_view(template_name='ocr/login.html'), name='login'),
    path('signup/', views.signup, name='signup'),
    path('home/', auth_views.LoginView.as_view(template_name='ocr/login.html'), name='home'),
    path('logout/', LogoutView.as_view(template_name='ocr/logged_out.html'), name='logout'),
]

# Static and media files settings for development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
