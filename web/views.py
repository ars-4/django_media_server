from django.contrib.auth.decorators import login_required
from web.forms import *
from web.models import *
from guardian.views import *
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def categories(request):
    if request.user is None:
        person = Person.objects.get(user_id=request.user.id)
    else:
        person = Person.objects.get(id=1)
    context = {
        'categories': Tag.objects.all(),
        'person': person
    }
    return context


@login_required(login_url='LoginPage')
def homepage(request):
    person = Person.objects.get(user_id=request.user.id)
    if person.type.id == 4:
        return HttpResponse("Your Account Expired")
    else:
        movies = Movie.objects.all()
        movies_filter = TagFilter(request.GET, queryset=movies)
        movies = movies_filter.qs
        person = Person.objects.get(user_id=request.user.id)
        context = {
            'person': person,
            'movies': movies,
            'filter': movies_filter
        }
        return render(request, 'movies.html', context)


@login_required(login_url='LoginPage')
def usertypemanagement(request):
    person = Person.objects.get(user_id=request.user.id)
    if person.type.id == 1:
        persons = Person.objects.all()
        context = {
            'persons': persons
        }
        return render(request, 'user/useraccounts.html', context)
    else:
        return HttpResponse("Error")


@login_required(login_url='LoginPage')
def usertypemanagementform(request, pk):
    prsn = Person.objects.get(id=pk)
    form = PersonAccountForm(instance=prsn)
    if request.method == 'POST':
        form = PersonAccountForm(request.POST, instance=prsn)
        if form.is_valid():
            form.save()
    return render(request, 'user/form.html', context={'form': form})


@login_required(login_url='LoginPage')
def moviepage(request, pk):
    person = Person.objects.get(user_id=request.user.id)
    if person.type.id == 4:
        return HttpResponse("Your Account Expired")
    else:
        movie = Movie.objects.get(id=pk)
        context = {
            'movie': movie
        }
        return render(request, 'movie.html', context)


@login_required(login_url='LoginPage')
def moviepagewatchers(request, pk):
    movie = Movie.objects.get(id=pk)
    movie.watched_by = int(movie.watched_by) + 1
    movie.save()
    return moviepage(request, movie.id)


# User / Person
def usercreatepage(request):
    return HttpResponse("User Create Page")


@login_required(login_url='LoginPage')
def userreadpage(request, pk):
    user = User.objects.get(id=pk)
    person = Person.objects.get(user=user)
    context = {
        'person': person
    }
    return render(request, 'user.html', context)


@login_required(login_url='LoginPage')
def userupdatepage(request, pk):
    if request.user.id == pk:
        person = Person.objects.get(user=request.user)
        form = PersonForm(instance=person)
        if request.method == 'POST':
            form = PersonForm(request.POST, request.FILES, instance=person)
            if form.is_valid():
                form.save()
                return redirect('HomePage')
        context = {
            'form': form,
            'person': person
        }
        return render(request, 'userupd.html', context)
    else:
        return redirect('HomePage')


# Account Type
def typecreatepage(request):
    form = AccountTypeForm()
    if request.method == 'POST':
        form = AccountTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ReadPackages')
    return render(request, 'account_type/create.html', context={"form": form})


def typereadpage(request):
    account_types = AccountType.objects.all()
    return render(request, 'account_type/read.html', context={"account_types": account_types})


def typeupdatepage(request, pk):
    account_type = AccountType.objects.get(id=pk)
    form = AccountTypeForm(instance=account_type)
    if request.method == 'POST':
        form = AccountTypeForm(request.POST, instance=account_type)
        if form.is_valid():
            form.save()
            return redirect('ReadPackages')
    return render(request, 'account_type/update.html', context={"form": form})


def typedeletepage(request, pk):
    account_type = AccountType.objects.get(id=pk)
    account_type.delete()
    return redirect('ReadPackages')


# Movie
def moviecreatepage(request):
    form = MovieForm()
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('HomePage')
    context = {
        'form': form,
    }
    return render(request, 'movie/create.html', context)


def tagcreatepage(request):
    form = TagForm()
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
    context = {
        'form': form,
    }
    return render(request, 'tag/create.html', context)


# Actor
def actorcreatepage(request):
    form = ActorForm()
    if request.method == 'POST':
        form = ActorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    context = {
        'form': form,
    }
    return render(request, 'actor/create.html', context)


def actorreadpage(request, pk):
    actor = Actor.objects.get(id=pk)
    movies = Movie.objects.filter(cast=actor)
    context = {
        'movies': movies,
        'actor': actor
    }
    return render(request, 'actor/read.html', context)
