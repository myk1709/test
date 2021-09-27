from django import forms
from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import AccessRecord, UserNames
from AppTwo import forms

# Create your views here.


def myView(request):
    return render(request,'index.html')


def myhelp(request):
    webpage_list = AccessRecord.objects.order_by('date')
    date_dict = {
        'acc_rec': webpage_list
    }

    return render(request, 'help.html', context=date_dict)


def myUsers(request):
    users = UserNames.objects.all()
    user = {
        'user': users
    }
    return render(request, 'user.html', user)


def myForm(request):
    form = forms.MyFormSignIn()
    if request.method == 'POST':
        form = forms.MyFormSignIn(request.POST)
        if form.is_valid():
            form.save()
            form = forms.MyFormSignIn()
        else: 
            print('error')
    return render(request, 'myform.html', {'form': form})
