from django.urls import path
from main.views import show_app

app_name = 'main'

urlpatterns = [
    path('', show_app, name='show_app'),
]