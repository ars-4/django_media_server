from django.contrib import admin
from web.models import *

# Register your models here.

REGISTERED_MODELS = [
    Person, AccountType, Movie, Actor, BillReceipt, Tag
]

admin.site.register(REGISTERED_MODELS)
