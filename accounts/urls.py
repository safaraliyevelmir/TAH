from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.SignUpView.as_view(),name='register'),
    path("login/",views.LoginPage.as_view(),name='login'),
    path('verify/<str:token>',views.verify,name='verify')
]