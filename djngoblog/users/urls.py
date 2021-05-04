from django.urls import path
from django.views.generic.base import TemplateView
from users.views import IndexView, UserView, ProfileView
from .import views
from posts.views import CreatedArticleView



app_name = 'users'
urlpatterns = [
    # path('dashboard/',CreatedArticleView.as_view(), name='dashboard'),
    path('signup/',UserView.signup, name='signup'),
    path('login/',UserView.login_user, name='login'),
    path('logout/',UserView.logout_user, name='logout'),
    path('view_profile/<int:pk>',ProfileView.as_view(),name='view_profile'),
    path('edit_profile/<int:pk>',ProfileView.put,name='edit_profile'),

    
]

