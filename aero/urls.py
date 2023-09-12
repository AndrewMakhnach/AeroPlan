from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('price/', price, name='price'),
    path('book/', book, name='book'),
    path('schedule/', schedule, name='schedule'),
]