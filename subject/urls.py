from django.urls import path
from .views import CryptoPageView, GazaPageView

urlpatterns = [
	path('crypto/', CryptoPageView.as_view(), name='crypto'),
	path('gaza/', GazaPageView.as_view(), name='gaza'),
]