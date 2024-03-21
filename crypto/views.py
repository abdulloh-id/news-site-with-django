from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class CryptoPageView(TemplateView):
	template_name = 'crypto.html'