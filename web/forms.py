from django_filters import FilterSet
from web.models import *
from django.forms import ModelForm
from pyuploadcare.dj.forms import ImageField as fmif


class TagFilter(FilterSet):
    class Meta:
        model = Movie
        fields = ['tags', 'title', 'cast']


class PersonForm(ModelForm):
    profile_picture = fmif(label='')

    class Meta:
        model = Person
        fields = ['name', 'profile_picture']


class PersonAccountForm(ModelForm):
    class Meta:
        model = Person
        fields = ['type']


class AccountTypeForm(ModelForm):
    class Meta:
        model = AccountType
        fields = '__all__'


class MovieForm(ModelForm):
    image = fmif(label='')

    class Meta:
        model = Movie
        fields = ['title', 'description', 'url', 'image', 'movie_added_by', 'cast', 'tags', 'year_released']


class ActorForm(ModelForm):
    image = fmif(label='')

    class Meta:
        model = Actor
        fields = '__all__'


class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'
