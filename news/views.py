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

        news_articles = data['articles'][:2]

        context = {'news_articles': news_articles}
        return render(request, 'news/index.html', context)
