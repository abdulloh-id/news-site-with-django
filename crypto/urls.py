from django.urls import path
from .views import CryptoPageView

urlpatterns = [
	path('', CryptoPageView.as_view(), name='crypto'),
]