import requests
from requests.compat import quote_plus
from django.shortcuts import render
from . import models
from bs4 import BeautifulSoup

# BASE_CRAIGSLIST_URL = 'https://losangeles.craigslist.org/search/?query={}'
BASE_CRAIGSLIST_URL = 'https://web.archive.org/web/20200407025058/https://losangeles.craigslist.org/search/sss'
BASE_IMAGE_URL = 'https://images.craigslist.org/{}_300x300.jpg'

# Create your views here.
def home(request):
    return render(request, 'base.html')

def new_search(request):
    # search = request.POST.get('search')
    # models.Search.objects.create(search=search)
    # final_url = BASE_CRAIGSLIST_URL.format(quote_plus(search))
    final_url = BASE_CRAIGSLIST_URL
    # print(final_url)
    response = requests.get(final_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    post_listings = soup.find_all('li', {'class': 'result-row'})

    final_postings = []
    for post in post_listings:
        post_title = post.find(class_='result-title').text
        post_url = post.find('a').get('href')
        if post.find(class_='result-price').text:
            post_price = post.find(class_='result-price').text
        else:
            post_price = 'N/A'

        if post.find(class_='result-image').get('data-ids'):
            post_image_id = post.find(class_='result-image').get('data-ids').split(',')[0].split(':')[1]
            post_image_url = BASE_IMAGE_URL.format(post_image_id)

        else:
            post_image_url = 'https://craigslist.org/images/peace.jpg'
        
        final_postings.append((post_title, post_url, post_price, post_image_url))


    # post_title = post.find('a', {'class': 'titlestring'})

    # print(data)
    stuff_for_frontend = {
        'search': 'sale',
        'final_postings': final_postings,
    }
    return render(request, 'my_app/new_search.html', stuff_for_frontend)
