from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import get_user_model
# from django.contrib.auth import get_user_model
# User = get_user_model()
from .models import CustomUser
# User = get_user_model()


class SignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].errors = None

    first_name = forms.CharField(max_length=50, required=False)
    last_name = forms.CharField(max_length=50, required=False)
    username = forms.CharField(max_length=30, required=True)
    # email = forms.EmailField(max_length=254, help_text=' Enter a valid email address.')

    class Meta:
        model = CustomUser
        fields=('username','first_name','last_name','email','password1','password2',)
        

class UserLoginForm(forms.Form):
    email=forms.CharField(label="Email", widget=forms.EmailInput(attrs={'placeholder': 'email@domain.com'}),required=True)


    password=forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'placeholder': "Password"}),required=True)

    def aut(self,request):
        
        uname=self.cleaned_data.get('email')
        pword=self.cleaned_data.get('password')
        return authenticate(request, username=uname, password=pword)


class EditUserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50, required=False)
    last_name = forms.CharField(max_length=50, required=False)
     
    class Meta:
        model = CustomUser
        fields=('first_name','last_name')




# class UpdateUserForm(ModelForm):
#     email=forms.CharField(label="Email", widget=forms.EmailInput(attrs={'placeholder':'email@domain.com'}),required=True)})
#     firstname = forms.CharField(label="First Name", widget=forms.TextInput(attrs={'placeholder':'First Name'}), max_length=200)
#     lastname = forms.CharField(label="Last Name", widget=forms.TextInput(attrs={'placeholder':'Last Name'}), max_length=200)


#     class Meta:
#         model = CustomUser
#         fields=['email','firstname','lastname','about_me']

# class UserRegForm(ModelForm):
#     email = forms.Charfield(label="Email", widget=forms.EmailInput(attrs={'placeholder': 'email@domain.com'})required=True)
#     password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), required=True)
#     password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password'}))

#     class Meta:
#         model = CustomUser
#         fields={'email', 'password'}

#     def clean_email(self):
#         email=self.cleaned_data.get('email')
    

