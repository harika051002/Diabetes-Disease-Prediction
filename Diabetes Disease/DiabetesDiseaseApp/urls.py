from django.urls import path

from . import views
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordResetCompleteView, PasswordResetDoneView

urlpatterns = [
       
           path("",views.index,name="index"),
           path("index.html/", views.index, name="index"),
           path("About.html/", views.About, name="About"),
	       path("Login.html/", views.Login, name="Login"), 
           path('Yoga.html/', views.Yoga, name="Yoga"), 
	       path("Register.html/", views.Register, name="Register"),
           path('Food_index.html/',views.Food_index,name="Food_index"),
	       path('Signup/', views.Signup, name="Signup"),
           path('save/', views.save, name="save"),
             path('pridictAc/', views.pridictAc, name="pridictAc"),
              path('DPridict.html/', views.DPridict, name="DPridict"),
              path('Logs.html/', views.Logs, name="Logs"),
              path('log/', views.log, name="log"),
           path('result',views.result,name="result"),
           path('result_yoga',views.result_yoga,name="result_yoga"),
	       path('UserLogin', views.UserLogin, name="UserLogin"), 
           path('password_reset.html/',views.password_reset,name="password_reset"),
            path('password_reset_confirm/<str:uidb64>/<str:token>/', views.password_reset_confirm, name="password_reset_confirm"),
            path('password_reset_update/', views.password_reset_update, name='password_reset_update'),
            path('password_reset_done.html/',views.password_reset_done,name="password_reset_done"),
   
]
	       
