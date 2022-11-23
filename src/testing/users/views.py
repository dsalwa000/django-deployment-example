from django.shortcuts import render
from .models import User
from .forms import UserForm, UserModelForm

# Create your views here.
def users_list(request):
    users = User.objects.all()
    context = {
        'users': users,
    }
    return render(request, 'users_list.html', context=context)

def fill_form(request):
    form = UserForm
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            newUser = User(name=form.cleaned_data['name'],
                           second_name=form.cleaned_data['second_name'],
                           email=form.cleaned_data['email'])
            newUser.save()
    return render(request, 'form.html', context={'form': form})

def fill_form_model(request):
    form = UserModelForm
    if request.method == 'POST':
        form = UserModelForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'form_model.html', context={'form': form})