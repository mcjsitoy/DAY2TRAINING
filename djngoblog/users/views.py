from django.contrib.auth import login,logout,authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SignupForm, UserLoginForm
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
    def index(request):
        return render(request, 'home.html')
    # class SignupView(TemplateView):
    #     template_name=""

class UserView(TemplateView):
    
    def signup(request):
            if request.method == 'POST':
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

# class LoginView(TemplateView):

    def login_user(request):
        if request.method == 'POST':
            form = UserLoginForm(request.POST)
            if form.is_valid():
                # import pdb;pdb.set_trace()    
                user = form.aut(request)                
                if user:
                    login(request, user)


                    return redirect('dashboard')
            else:
                return render(request, 'registration/login.html', {'form':form})

        else:
            form = UserLoginForm()
        return render(request, 'registration/login.html', {'form': form}) 


# def make_post(request):
# class LogoutView(TemplateView):
    def logout_user(request):
        logout(request,)
        return redirect("home")


class ProfileView(TemplateView):


    
    def get(self, request, pk):
        # import pdb;pdb.set_trace()   
        user=get_object_or_404(CustomUser, pk=pk)
        user_posts=Articles.objects.filter(owner=user)            
        return render(request,'view_profile.html', {'user':user,'user_posts':user_posts})


    def put(request, pk): 
           
        userid = get_object_or_404(CustomUser, pk=pk)
        form = SignupForm(request.POST,instance=userid)
                    
        if form.is_valid():               
            user = form.save(commit=False)
            user.owner = request.user               
            user.save()
            return redirect('users:view_profile', pk=user.pk)

        else:

            form = SignupForm(instance=userid)
            return render(request, 'edit_profile.html', {'form':form})
        
        









