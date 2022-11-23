from django.shortcuts import render
from . import forms

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('temp:main'))
            else:
                return HttpResponse('ACCOUNT NOT ACTIVE')
        else:
            print('Someone tried to login and fail')
            print('Username: {} and password {}'.format(username, password))
            return HttpResponse('invalid login of password')
    else:
        return render(request, 'temp/login.html', {})


def inh_temp_main(request):

    context = {

    }
    return render(request, 'temp/main.html', context=context)

@login_required
def special(request):
    return HttpResponse("You are logged in, Nice!")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('temp:main'))


def inh_temp_new_page(request):
    text = 'hello world'

    context = {
        'text': text,
    }
    return render(request, 'temp/newpage.html', context=context)

def register(request):
    reg = False
    if request.method == "POST":
        user_form = forms.UserForm(data=request.POST)
        profile_form = forms.UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            # saving hashed password to database
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            reg = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = forms.UserForm()
        profile_form = forms.UserProfileInfoForm()

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'temp/registration.html', context=context)

