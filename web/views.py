from django.contrib.auth.decorators import login_required
from web.forms import *
from web.models import *
from django.shortcuts import render, redirect
from django.http import HttpResponse
from web.utils import find_movie


# Create your views here.


def categories(request):
    if request.user is None:
        person = Person.objects.get(user_id=request.user.id)
    else:
        person = Person.objects.get(id=2)
    context = {
        'categories': Tag.objects.all(),
        'person': person
    }
    return context


@login_required(login_url='LoginPage')
def homepage(request):
    person = Person.objects.get(user_id=request.user.id)
    if person.type.id == 4:
        return render(request, 'expired.html')
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
        return HttpResponse("Error Code 403")


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
#    month_timer(person.id)
    if person.type.id == 4:
        return render(request, 'expired.html')
    else:
        movie = Movie.objects.get(id=pk)
        context = {
            'movie': movie
        }
        return render(request, 'movie.html', context)


@login_required(login_url='LoginPage')
def moviepagewatchers(request, pk):
    person = Person.objects.get(user_id=request.user.id)
#    month_timer(person.id)
    if person.type.id == 4:
        return render(request, 'expired.html')
    else:
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
    person = Person.objects.get(user_id=request.user.id)
    if person.type.id == 1:
        form = AccountTypeForm()
        if request.method == 'POST':
            form = AccountTypeForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('ReadPackages')
        return render(request, 'account_type/create.html', context={"form": form})
    else:
        return HttpResponse("Error Code 403")


def typereadpage(request):
    account_types = AccountType.objects.all()
    return render(request, 'account_type/read.html', context={"account_types": account_types})


def typeupdatepage(request, pk):
    person = Person.objects.get(user_id=request.user.id)
    if person.type.id == 1:
        account_type = AccountType.objects.get(id=pk)
        form = AccountTypeForm(instance=account_type)
        if request.method == 'POST':
            form = AccountTypeForm(request.POST, instance=account_type)
            if form.is_valid():
                form.save()
                return redirect('ReadPackages')
        return render(request, 'account_type/update.html', context={"form": form})
    else:
        return HttpResponse("Error Code 403")


def typedeletepage(request, pk):
    person = Person.objects.get(user_id=request.user.id)
    if person.type.id == 1:
        account_type = AccountType.objects.get(id=pk)
        account_type.delete()
        return redirect('ReadPackages')
    else:
        return HttpResponse("Error Code 403")


# Movie
def moviecreatepage(request):
    person = Person.objects.get(user_id=request.user.id)
    if person.type.id == 1:
        form = MovieForm()
        if request.method == 'POST':
            form = MovieForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('HomePage')
        context = {
            'form': form,
            'find_movie': find_movie
        }
        return render(request, 'movie/create.html', context)
    else:
        return HttpResponse("Error Code 403")


def find_movie(request):
    return render(request, 'movie/find_movie.html', {'find_movie':find_movie})

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


def bill_receipt_creation(pk):
    person = Person.objects.get(id=pk)
    bill_receipt = BillReceipt.objects.create(
        bill_of=person,
        price=person.type.price
    )
    bill_receipt.save()
    due_bill_creation(pk)


def due_bill_creation(pk):
    person = Person.objects.get(id=pk)
    receipts = BillReceipt.objects.filter(bill_of=person, status='Pending')
    due = 0
    for receipt in receipts:
        due = int(receipt.price) + due
    person.due = due
    person.save()
    if due > 3000:
        person.type = AccountType.objects.get(id=3)
        person.save()
    else:
        person.save()


def month_timer(pk):
    person = Person.objects.get(id=pk)
    timer = MonthTimer.objects.get(person=person)
    month_span = timer.current.date().day + 30
    if timer.date_updated.date().day.__gt__(month_span):
        timer.current = datetime.datetime.now()
        timer.save()
        bill_receipt_creation(pk)
    else:
        timer.save()
