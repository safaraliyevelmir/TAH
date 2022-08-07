from django import forms
from django.contrib.auth import get_user_model 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm



User = get_user_model()

class UserRegisterForm(UserCreationForm):

  class Meta:
      model = User
      fields = ['email','password1']
      
      
      widgets = {
        'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
      }
      
  def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'})


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username','password']
        
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'class':'form-control','placeholder': 'Username'})
        self.fields['password'].widget = forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}) 