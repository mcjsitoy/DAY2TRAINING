from django.urls import path
from posts.views import CreateArticleView
from posts.views import CreatedArticleView, ArticleDetailView
# from posts.views import TestArticleView

from . import views

app_name = 'posts'
urlpatterns = [
    
    path('create_article/',CreateArticleView.as_view(), name='create_article'),
    # path('dashboard/',CreatedArticleView.as_view(),name='created_article'),
    # path('test_article/',TestArticleView.as_view(), name='test_article'),
    path('article_details/<int:pk>',ArticleDetailView.as_view(), name ='article_details'),
    path('update_article/<int:pk>',CreateArticleView.put, name ='update_article'),
    path('delete_article/<int:pk>',CreateArticleView.delete_article, name='delete_article'),
    # path('posts/<int:pk>/comment/',CreateArticleView.add_comment, name='add_comment'),
    # path('delete_view/',DeleteView.deleteview, name='delete_view'),

]