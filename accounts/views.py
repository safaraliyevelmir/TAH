from django.shortcuts import render, redirect
from .forms import UserRegisterForm, LoginForm
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView    
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()


class LoginPage(LoginView):
  
  template_name = 'login.html'
  authentication_form=LoginForm


class SignUpView(SuccessMessageMixin, CreateView):
  template_name = 'register.html'
  success_url = '/'
  form_class = UserRegisterForm
  success_message = "Your profile was created successfully"
  print(form_class.error_messages)
  
  def form_valid(self, form):
      if form.is_valid():
        user = form.save(commit=False)
        user.is_active = False
        user.save()
      email=form.cleaned_data.get('email')
      user = User.objects.filter(email=email).first()
      message = f"You can click this link http://127.0.0.1:8000/accounts/verify/{user.token} and confirmation your email"
      send_mail("Confirmation Email", message, settings.EMAIL_HOST_USER, [email])
      
      return super().form_valid(form)
    
  
def verify(request,token):
    user = User.objects.get(token=token)
    user.is_active = True
    user.save()
    return redirect('login')
