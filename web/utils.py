import requests
from django import template

register = template.Library()

# 
@register.filter(name='find_movie')
def find_movie(movie_name):
    url = "https://online-movie-database.p.rapidapi.com/auto-complete?q="
    headers = {
        'X-RapidAPI-Key': '941f406cf1msh25d5e4addbb8f7dp1dda02jsnc59c17972b62',
		'X-RapidAPI-Host': 'online-movie-database.p.rapidapi.com'
    }
    req = requests.get(url + movie_name, headers=headers)
    return req.text
