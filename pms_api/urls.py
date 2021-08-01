"""pms_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views
from main.views import (ChapterApiView, ChapterCreateApiView, ChapterUpdateApiView, ProfileApiView, 
    ProfileUpdateApiView, MeetingCreateApiView, MeetingUpdateApiView, StatusSerializerApiView,
    AssessChapterApiView, StatusApiView,
    )


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('api-token-auth/', views.obtain_auth_token),

    path('chapters/', ChapterApiView.as_view(), name="chapters"),
    path('create_chapter/', ChapterUpdateApiView.as_view(), name="create_chapter"),
    path('update_chapter/<int:pk>/update/', ChapterUpdateApiView.as_view(), name="update_chapter"),

    path('assess_chapter/<int:pk>/update/', AssessChapterApiView.as_view(), name="assess_chapter"),

    path('profile/', ProfileApiView.as_view(), name="profile"),
    path('update_profile/<int:pk>/update/', ProfileUpdateApiView.as_view(), name="update_profile"),

    path('create_meeting/', MeetingCreateApiView.as_view(), name="create_meeting"),
    path('update_meeting/<int:pk>/update/', MeetingUpdateApiView.as_view(), name="update_meeting"),

    path('status/', StatusApiView.as_view(), name="status"),
    path('update_status/<int:pk>/update/', StatusSerializerApiView.as_view(), name="update_status"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
