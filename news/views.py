from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
import requests
import environ

env = environ.Env()
environ.Env.read_env()


class HomepageView(View):
    def get(self, request):
        API_KEY = env('API_KEY')
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
            # if page_number is not an integer then assign the first page
            page_obj = p.page(1)
        except EmptyPage:
            # if page is empty then return last page
            page_obj = p.page(p.num_pages)

        context = {
            'news_articles': page_obj, 'page': page_obj,
            }
        return render(request, 'news/index.html', context)
