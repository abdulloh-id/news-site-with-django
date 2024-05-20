from django.shortcuts import render
from django.views.generic import TemplateView
from newsapi import NewsApiClient
from dotenv import load_dotenv
import os
import datetime

load_dotenv()
API_KEY = os.getenv("API_KEY")

# Create your views here.
class CryptoPageView(TemplateView):
	template_name = 'crypto.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		today = datetime.datetime.now().date()
		yesterday = today - datetime.timedelta(days=1)

		newsapi = NewsApiClient(api_key=API_KEY)

		# top_headlines = newsapi.get_top_headlines(
		# 										q='bitcoin',
		# 										language='en')
		
		all_articles = newsapi.get_everything(
											q='bitcoin',
											from_param=yesterday,
											to=today,
											language='en',
											sort_by='relevancy')

		#context['top_headlines'] = top_headlines
		context['all_articles'] = all_articles

		return context

# Create your views here.
class GazaPageView(TemplateView):
	template_name = 'gaza.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		today = datetime.datetime.now().date()
		yesterday = today - datetime.timedelta(days=1)

		newsapi = NewsApiClient(api_key=API_KEY)

		# top_headlines = newsapi.get_top_headlines(
		# 										q='bitcoin',
		# 										language='en')
		
		all_articles = newsapi.get_everything(
											q='gaza',
											from_param=yesterday,
											to=today,
											language='en',
											sort_by='relevancy')

		#context['top_headlines'] = top_headlines
		context['all_articles'] = all_articles
		print(context)

		return context



