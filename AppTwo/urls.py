from django.urls import path
from AppTwo import views

app_name = 'app_two'

urlpatterns = [
    path('', views.myView, name="myview"),
    path('help/', views.myhelp, name='help'),
    path('users/', views.myUsers, name='users'),
    path('form/', views.myForm, name='myform')
]
