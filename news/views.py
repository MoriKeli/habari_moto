from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from datetime import date, datetime
import requests
import environ

env = environ.Env()
environ.Env.read_env()


class HomepageView(View):
    def get(self, request):
        API_KEY = env('API_KEY')
        BASE_URL = ''

        # category = request.GET.get('category')
        
        # if category:
        #     BASE_URL = f'https://newsapi.org/v2/everything?q={category}&sortBy=relevancy&apiKey={API_KEY}'

        #     # sidebar nav news
        #     current_date = date.today().strftime('%Y-%m-%d')

        #     # this code is used to provide time period from first day of the month to the current day of the month.
        #     # popular news need to be fetched from day one of the month, e.g. from 1st Apr to 28th Apr. or from 1st June to 30th June.
        #     strip_time = datetime.strptime(current_date, '%Y-%m-%d')
        #     first_day = (strip_time.day - strip_time.day) + 1     # get the first day of the month
        #     first_date = date.today().strftime('%Y-%m-0') + str(first_day)

        #     # latest news articles
        #     LATEST_NEWS_ARTICLES_URL = f'https://newsapi.org/v2/everything?q=category={category}&from={current_date}&to={current_date}&sortBy=publishedAt&apiKey={API_KEY}'
        #     response = requests.get(LATEST_NEWS_ARTICLES_URL)
        #     data = response.json()
        #     latest_articles = data["articles"][:17]      # get the first 5 recent news articles

        #     # popular news articles
        #     POPULAR_NEWS_ARTICLES_URL = f'https://newsapi.org/v2/everything?q=category={category}&from={first_date}&to={current_date}&sortBy=popularity&apiKey={API_KEY}'
        #     response = requests.get(POPULAR_NEWS_ARTICLES_URL)
        #     data = response.json()
        #     popular_articles = data["articles"][:17]      # get the first 5 popular news articles

        #     # trending news articles
        #     TRENDING_NEWS_ARTICLES_URL = f'https://newsapi.org/v2/everything?q=category={category}&from={current_date}&sortBy=relevancy&apiKey={API_KEY}'
        #     response = requests.get(TRENDING_NEWS_ARTICLES_URL)
        #     data = response.json()
        #     trending_articles = data["articles"][:20]      # get the first 5 trending news articles

        # else:
        #     BASE_URL = f'https://newsapi.org/v2/everything?q=country&sortBy=publishedAt&apiKey={API_KEY}'

        #     # sidebar nav news
        #     current_date = date.today().strftime('%Y-%m-%d')

        #     # this code is used to provide time period from first day of the month to the current day of the month.
        #     # popular news need to be fetched from day one of the month, e.g. from 1st Apr to 28th Apr. or from 1st June to 30th June.
        #     strip_time = datetime.strptime(current_date, '%Y-%m-%d')
        #     first_day = (strip_time.day - strip_time.day) + 1     # get the first day of the month
        #     first_date = date.today().strftime('%Y-%m-0') + str(first_day)
            
        #     # latest news articles
        #     LATEST_NEWS_ARTICLES_URL = f'https://newsapi.org/v2/everything?q=from={current_date}&to={current_date}&sortBy=publishedAt&apiKey={API_KEY}'
        #     response = requests.get(LATEST_NEWS_ARTICLES_URL)
        #     data = response.json()
        #     latest_articles = data["articles"][:15]      # get the first 5 recent news articles

        #     # popular news articles
        #     POPULAR_NEWS_ARTICLES_URL = f'https://newsapi.org/v2/everything?q=from={first_date}&to={current_date}&sortBy=popularity&apiKey={API_KEY}'
        #     response = requests.get(POPULAR_NEWS_ARTICLES_URL)
        #     data = response.json()
        #     popular_articles = data["articles"][:15]      # get the first 5 popular news articles

        #     # trending news articles
        #     TRENDING_NEWS_ARTICLES_URL = f'https://newsapi.org/v2/everything?q=from={current_date}&sortBy=relevancy&apiKey={API_KEY}'
        #     response = requests.get(TRENDING_NEWS_ARTICLES_URL)
        #     data = response.json()
        #     trending_articles = data["articles"][:15]      # get the first 5 trending news articles

        # response = requests.get(BASE_URL)
        # data = response.json()
        # news_articles = data['articles']

        # # pagination
        # p = Paginator(list(news_articles), 10) 
        # page_number = request.GET.get('page')

        # try:
        #     page_obj = p.get_page(page_number)
        # except PageNotAnInteger:
        #     page_obj = p.page(1)    # if page_number is not an integer then assign the first page
        # except EmptyPage:
        #     page_obj = p.page(p.num_pages)   # if page is empty then return last page

        # # recent news articles -> footer section
        # current_date = date.today().strftime('%Y-%m-%d')
        # RECENT_ARTICLES_URL = f'https://newsapi.org/v2/everything?q=from={current_date}&apiKey={API_KEY}'
        # response = requests.get(RECENT_ARTICLES_URL)
        # data = response.json()
        # recent_articles = data["articles"][:5]      # get the first 5 recent news articles

        # context = {
        #     'news_articles': page_obj, 'page': page_obj,
        #     'category': category, 'recent_articles': recent_articles,
        #     'latest_news': latest_articles, 'popular_articles': popular_articles,
        #     'trending_news': trending_articles,
        # }
        context = {}
        return render(request, 'news/index.html', context)
