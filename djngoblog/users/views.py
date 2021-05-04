from django.contrib.auth import login,logout,authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import EditUserForm, UserLoginForm,SignupForm
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from users.models import CustomUser
from posts.models import Articles

# from django.contrib.auth import get_user_model
# User = get_user_model()



# Create your views here.
# class IndexView(TemplateView):
class IndexView(TemplateView):
    template_name="home"    
    def get(self, request):        
        
            
            return render(request, 'home.html')
    # class SignupView(TemplateView):
    #     template_name=""

class SignupView(TemplateView): 
    template_name = 'signup.html'
    def get(self, request):                   
        form = SignupForm()
        return render(request, self.template_name,{'form':form})

    def post(self, request):            
            form = SignupForm(request.POST)
            if form.is_valid():            
                form.save()
                username = form.cleaned_data.get('email')
                raw_password = form.cleaned_data.get('password1')                
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('dashboard')
            else:
                form = SignupForm()
                return render(request, 'signup.html', {'form': form})

# import pdb;pdb.set_trace()   
class LoginView(TemplateView):
    template_name='registration/login.html'
    def get(self, request):      
        form = UserLoginForm()
        return render(request, self.template_name,{'form':form})

   
    def post(self, request):       
        form = UserLoginForm(request.POST)        
        if form.is_valid():             
            user = form.aut(request)                
            if user:
                login(request, user)
                return redirect('dashboard')

        else:
            return render(request, self.template_name, {'form':form})

        
class LogoutView(TemplateView):
    
    def get(self, request):
        logout(request)
        return redirect('users:login')


# class ProfileView(TemplateView):


    
#     def get(self, request, pk):
#          import pdb;pdb.set_trace() 
#          if request.user.is_authenticated:
#         # import pdb;pdb.set_trace()         
#             user=get_object_or_404(CustomUser, pk=pk)
#             user_posts=Articles.objects.filter(owner=user)            
#             return render(request,'view_profile.html', {'user':user,'user_posts':user_posts})


#     def put(request, pk): 
           
#         userid = get_object_or_404(CustomUser, pk=pk)
#         form = SignupForm(request.POST,instance=userid)
                    
#         if form.is_valid():               
#             user = form.save(commit=False)
#             user.owner = request.user               
#             user.save()
           
#             return redirect('users:view_profile', pk=user.pk)

#         else:

#             form = SignupForm(instance=userid)
#             return render(request, 'edit_profile.html', {'form':form})


class ProfileView(TemplateView):
    
    template_name = 'view_profile.html'
    
    def get(self, request, *args, **kwargs):
        id_ = self.kwargs.get('pk')
        if request.user.is_authenticated:             
            user = get_object_or_404(CustomUser, pk=id_)
            user_posts = Articles.objects.filter(owner=user)
            return render(request, self.template_name, {'user': user, 'user_posts': user_posts })
        return redirect('users:login')
    
    
  

class EditProfileView(TemplateView):
    
    template_name = 'edit_profile.html'
    
    def get(self, request, *args, **kwargs):
        id_ = self.kwargs.get('pk')
        if request.user.is_authenticated:             
            user = get_object_or_404(CustomUser, pk=id_)
            form = EditUserForm(instance=user)           
            return render(request, self.template_name, {'user': user,  'form':form })
        return redirect('users:login')
    
    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')        
        userid = get_object_or_404(CustomUser, pk=pk)
        form = EditUserForm(request.POST, instance=userid)        
        if form.is_valid():
          user = form.save(commit=False)
          user.owner = request.user
          user.save()
          return redirect('users:view_profile', pk=user.pk)
        return render(request, 'edit_profile.html', {'form': form })
        
        









