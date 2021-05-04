from django.urls import path
from django.views.generic.base import TemplateView
from users.views import IndexView,SignupView,ProfileView,EditProfileView,LoginView,LogoutView
from .import views




app_name = 'users'
urlpatterns = [
    # path('dashboard/',CreatedArticleView.as_view(), name='dashboard'),
    path('signup/',SignupView.as_view(), name='signup'),
    path('login/',LoginView.as_view(), name='login'),
    path('logout/',LogoutView.as_view(), name='logout'),
    path('view_profile/<int:pk>',ProfileView.as_view(),name='view_profile'),
    path('edit_profile/<int:pk>',EditProfileView.as_view(),name='edit_profile'),

    
]

