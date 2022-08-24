"""mainproj URL Configuration

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
import mainapp.views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/',include('account.urls')),
    path('', views.home, name='home'),
    path('ideanote/', views.ideaNote, name='ideaNote'),
    path('upload_idea/', views.uploadIdea, name='uploadIdea'),
    path('makecrew/', views.makecrew, name='makecrew'),
    path('makecrew/tag/<str:slug>', views.tag_page),
    path('upload_crew/', views.uploadCrew, name='uploadCrew'),
    path('info/', views.info, name='info'),
    path('mypage/', views.mypage, name='mypage')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
