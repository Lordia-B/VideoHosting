from django.urls import path
from . import views
from .views import video_detail
from VideoHosting import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('video/<int:pk>/', video_detail, name='video_detail'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)