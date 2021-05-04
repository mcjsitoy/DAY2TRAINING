from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView,UpdateView
from .forms import CreateArticleForm
from django.views.generic import TemplateView
from django.contrib.auth import authenticate
from posts.models import Articles
from django.http import HttpResponse
from django.urls import reverse
from users.forms import SignupForm, UserLoginForm
from posts.forms import CommentForm
from django.shortcuts import get_object_or_404
from django.utils import timezone


# Create your views here.


class CreateArticleView(TemplateView):
    model = Articles
    template_name='posts/create_article.html'

    def get(self, request, *args, **kwargs):
        # Current user is authenticated 
        if request.user.is_authenticated:
            form = CreateArticleForm()
            
            return self.render_to_response({
                'form':form,

            })

        else:
            return redirect('users:login')
    # import pdb; pdb.set_trace()
    def post(self, request, *args, **kwargs):
        
        form = CreateArticleForm(request.POST)
        if form.is_valid():                
            create_article = form.save(commit=False)            
            create_article.owner = request.user
            form.save()
                
            return redirect('dashboard')
        else:            
            return render(request, self.template_name, {'form':form})



    def put(request, pk):       
      
        article = get_object_or_404(Articles, pk=pk)

        form = CreateArticleForm(request.POST,instance=article)
                      
        if form.is_valid():               
            article = form.save(commit=False)
            article.owner = request.user
            article.published_date = timezone.now()
            article.save()
            return redirect('posts:article_details', pk=article.pk)

        else:

            form = CreateArticleForm(instance=article)
        return render(request, 'posts/update_article.html', {'form':form})



    def delete_article(request, pk):
        template_name='delete_article.html'
        if request.user.is_authenticated:
            query = get_object_or_404(Articles, pk=pk)                        
            query.delete()
            return redirect('dashboard')
           
        else:
            return render('registration/login.html', {'form': form})

    def add_comment(request, pk):
        
        if request.method == "POST":
            form = CommentForm(request.POST)
            if form.is_valid():
                article = get_object_or_404(Articles, pk=pk)
                comment=form.save(commit=False)
                comment.article = article
                comment.save()
                return redirect('article_details', pk=article.pk)
        
        else:
            form=CommentForm()
        return render(request, 'posts:add_comment',{'form': form})
        
# class DeleteView(TemplateView):
#     def deleteview(self, request, *args, **kwargs):
#         if request.user.is_authenticated:   

#             if request.user.id == article.owner.id:
#                 article.delete()
#                 return HttpResponseRedirect('dashboard')
#             else:
#                 raise Http404("Not allowed")
#         else:
#             return render('users:login')
        # def details(request, articles_id):
        #     if request.user.is_authenticated:
        #         articles = Articles.objects.all()
        #         context={'articles':articles,}
        
class ArticleDetailView(DetailView):
    model = Articles
    template_name ='article_details.html'      


# class UpdateArticleView(UpdateView):
#     model = Articles
#     form = CreateArticle
#     template_name = 'update_articles.html'
#     fields = ['title','description','content']
    


        
       
        

        



class CreatedArticleView(TemplateView):

    template_name='dashboard'
   

    def get(self, request):
        if request.user.is_authenticated:
            try:
                articlet = Articles.objects.all()
                context ={
                'articlet': articlet,
            }
           
            except Articles.DoesNotExist:
                raise Http404("No Articles Found")
               
            
              
            return render(request, self.template_name, context)
        else:
            form = UserLoginForm()
            return render(request,'users/login.html', {'form':form})
    












# class TestArticleView(TemplateView):
#     template_name='test_article.html'
#     def get(self, request):
#         if request.user.is_authenticated:
           
#             try:
#                 articletest = Articles.objects.all()
                
#             except Articles.DoesNotExist:
#                 raise Http404("No Articles Found")
                
            
#                 # context ={
#                 #     'articletest': articletest,
#                 # }

#             return render(request, 'test_article.html', {'articletest': articletest})
#         else:
#             form = UserLoginForm()
#             return render(request,'users/login.html', {'form':form})
        


    # def create_article(request):
    
    #     if request.user.is_authenticated:
            
    #         # import pdb; pdb.set_trace()   
    #         if request.method =='POST':
                
    #             get_data = {'owner':request.user}
                
    #             form = CreateArticle(request.POST)
            
    #             if form.is_valid():
                    
    #                 create_article = form.save(commit=False)
    #                 create_article.author = request.user
    #                 form.save()
                    
    #                 return redirect('dashboard')
    #             else:
    #                 form = CreateArticle(request.POST)
    #                 return render(request, 'create_article.html', {'form':form})
    #         else:
    #             return redirect("dashboard")