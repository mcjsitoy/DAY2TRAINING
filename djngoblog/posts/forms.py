from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Articles, ArticleComment;


class CreateArticleForm(forms.ModelForm):
    title = forms.CharField(max_length=50,required=True)
    description = forms.CharField(max_length=50,required=False)
    content = forms.Textarea()
    
    


    class Meta:
        model = Articles
        fields = ('title','description','content')
        exclude = ['owner']

class CommentForm(forms.ModelForm):
        

    class Meta:
        model = ArticleComment
        fields = ('user', 'comment',)