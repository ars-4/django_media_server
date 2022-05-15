[![License: Unlicense](https://img.shields.io/badge/license-Unlicense-blue.svg)](http://unlicense.org/)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![Flutter](https://img.shields.io/badge/Flutter-%2302569B.svg?style=for-the-badge&logo=Flutter&logoColor=white)

# Django Media Server
Super cool easy to use media server made on Django

Live Demo: https://django-media-server.herokuapp.com/web/
SignUp To Check it out!

### Install Instructions
* Clone the projects `git clone https://github.com/ars-4/django_media_server.git`
* Create virtualenv and activate it
* Open web\views.py and find this:

```def categories(request):
    if request.user is not None:
        person = Person.objects.get(id=2)

    else:
        person = Person.objects.get(user_id=request.user.id)
    context = {
        'categories': Tag.objects.all(),
        'person': person
    }
    return context
 ``` 
 
 * Change it to:
 ```
 def categories(request):
    context = {
        'categories': Tag.objects.all()
    }
    return context
 ```
 
 * Install requirements.txt: `pip install -r requirements.txt`
 * Make migrations and migrate to db: `py manage.py makemigrations & py manage.py migrate`
 * Create super user: `py manage.py createsuperuser`
 * Run the server: `py manage.py runserver`
 * Open this url: `http://127.0.0.1:8000/admin/` and login with superuser credentials
 * Create 4 Account Types with the following order:
    * Management (Admin Account Type) -> You can name it whatever you want
    * Trial (Default Account When User First SignUP)
    * Standard (Standard account type)
    * Expired (User who is expired)
 * Create a person with user as the previous made superuser
 * Create one more account with No staff login and create this user's person account with Standard Account Type
 * Change back web\views.py Categories Function in the file
 * Congrats your server is accessible at `http://127.0.0.1:8000/web/`

#### If you want to run the server on your current system IP run it via: `py manage.py runserver 0.0.0.0:80` -> ( 80 is the default port for windows OS so if your IP is 192.168.0.7 server will be accessible to it without writing any port number in the end )

#### Other useful Info:
* Bill Receipts and Month Timers are auto and will be added automatically when user signs up.
* After the month of user first signed up a bill will be generated according to his account type's price
* If bill is more than 3000 his account will auto expire. More than 3000 means 3001 and .... so on not 3000


#### Please help me contribute in making of Desktop and Mobile apps
