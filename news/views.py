# from django.shortcuts import render
# from django.views.generic import ListView
# from .models import Post

from django.shortcuts import render
from django.views.generic import TemplateView
from newsapi import NewsApiClient
from dotenv import load_dotenv
import os
import datetime

load_dotenv()
API_KEY = os.getenv("API_KEY")

# Create your views here.
# class HomePageView(ListView):
# 	model = Post
# 	template_name = 'home.html'

class HomePageView(TemplateView):
	template_name = 'home.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		newsapi = NewsApiClient(api_key=API_KEY)

		top_headlines = newsapi.get_top_headlines(sources='bbc-news', language='en')

		context['top_headlines'] = top_headlines

		return context
