from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from datetime import date
import requests
import environ

env = environ.Env()
environ.Env.read_env()


class HomepageView(View):
    def get(self, request):
        API_KEY = env('API_KEY')
        BASE_URL = ''

        category = request.GET.get('category')
        
        if category:
            BASE_URL = f'https://newsapi.org/v2/everything?q=category={category}&apiKey={API_KEY}'
        
        else:
            BASE_URL = f'https://newsapi.org/v2/everything?q=country&apiKey={API_KEY}'

        response = requests.get(BASE_URL)
        data = response.json()
        news_articles = data['articles']

        # pagination
        p = Paginator(list(news_articles), 10) 
        page_number = request.GET.get('page')

        try:
            page_obj = p.get_page(page_number)
        except PageNotAnInteger:
            page_obj = p.page(1)    # if page_number is not an integer then assign the first page
        except EmptyPage:
            page_obj = p.page(p.num_pages)   # if page is empty then return last page

        # recent news articles -> footer section
        current_date = date.today().strftime('%Y-%m-%d')
        RECENT_ARTICLES_URL = f'https://newsapi.org/v2/everything?q=from={current_date}&apiKey={API_KEY}'
        response = requests.get(RECENT_ARTICLES_URL)
        data = response.json()

        print(f'Recent: {data}')
        recent_articles = data["articles"][:5]      # get the first 5 recent news articles


        
        context = {
            'news_articles': page_obj, 'page': page_obj,
            'category': category, 'recent_articles': recent_articles,
        }
        return render(request, 'news/index.html', context)
