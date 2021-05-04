"""djngoblog URL Configuration

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
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from posts.views import CreatedArticleView
from users.views import IndexView



urlpatterns = [
    path('admin/', admin.site.urls),
   
    # path('accounts/', include('django.csontrib.auth.urls')),
    
    path('dashboard', CreatedArticleView.as_view(template_name='dashboard.html'), name='dashboard'),
    path('home/', IndexView.as_view(template_name='home.html'), name='home'),
    path('accounts/',include(('users.urls'),namespace='users')), 
    path('posts/',include(('posts.urls'), namespace='posts')),

    
    
    
    


 

]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
