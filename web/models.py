import datetime

from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class BasicModel(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AccountType(BasicModel):
    title = models.CharField(max_length=245, null=True)
    description = models.TextField(null=True, default='...')
    price = models.IntegerField(null=True, default=0)

    def __str__(self):
        return self.title


class Person(BasicModel):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profiles', null=True, default='/profiles/avatars.png')
    name = models.CharField(max_length=245, null=True, default='None')
    type = models.ForeignKey(AccountType, null=True, on_delete=models.CASCADE)
    key = models.CharField(null=True, default='Empty', max_length=100)
    due = models.IntegerField(null=True, default=0)

    def __str__(self):
        return self.user.username


class Actor(BasicModel):
    name = models.CharField(max_length=245, null=True, default='None')
    date_of_birth = models.DateField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='actors')

    def __str__(self):
        return self.name


class Tag(BasicModel):
    title = models.CharField(max_length=245, null=True)

    def __str__(self):
        return self.title


class Movie(BasicModel):
    image = models.ImageField(null=True, upload_to='movies')
    title = models.CharField(max_length=100, null=True, default='Unknown Movie')
    description = models.TextField(null=True, default='...')
    url = models.CharField(null=True, blank=True, max_length=245)
    year_released = models.CharField(max_length=10, default='0000', null=True)
    movie_added_by = models.ForeignKey(Person, null=True, on_delete=models.CASCADE)
    cast = models.ManyToManyField(Actor)
    watched_by = models.IntegerField(null=True, default=0)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


class BillReceipt(BasicModel):
    bill_of = models.ForeignKey(Person, null=True, on_delete=models.CASCADE)
    price = models.IntegerField(null=True, default=0)
    status_choices = [
        ('Paid', 'paid'),
        ('Pending', 'pending')
    ]
    status = models.CharField(max_length=20, null=True, default='Pending', choices=status_choices)

    def __str__(self):
        return self.bill_of.user.username


class MonthTimer(BasicModel):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)
    current = models.DateTimeField(default=datetime.datetime.now(), null=True)

    def __str__(self):
        return str(self.date_updated)
