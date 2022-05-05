from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from web.models import Person, AccountType
from django.contrib.auth import authenticate, login, logout


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("HomePage")
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


@unauthenticated_user
def register(request):
    form = UserForm()
    account_type = AccountType.objects.get(id=2)
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            person = Person.objects.create(
                user=user,
                name=form.cleaned_data['first_name'] + form.cleaned_data['last_name'],
                type=account_type,
            )
            person.save()
            return redirect("LoginPage")
        else:
            return HttpResponse("An Error Occurred")
    context = {
        'form': form
    }
    return render(request, 'register.html', context)


@unauthenticated_user
def login_r(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            upass = form.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                return redirect('HomePage')
        else:
            return HttpResponse("Wrong Username and/or Password")
    else:
        form = AuthenticationForm()

    context = {
        'form': form,
    }
    return render(request, 'login.html', context)


def logout_r(request):
    logout(request)
    return redirect('HomePage')

