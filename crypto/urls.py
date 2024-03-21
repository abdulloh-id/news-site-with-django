from django.urls import path
from .views import CryptoPageView

urlpatterns = [
	path('crypto/', CryptoPageView.as_view(), name='crypto'),
]