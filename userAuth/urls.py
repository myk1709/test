from django.urls import path
from userAuth import views

app_name = 'userAuth'

urlpatterns = [
    path('signin/', views.register, name='register')
]
