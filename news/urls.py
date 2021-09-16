from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', index,name='home'),
    path('cat/<int:cat_id>/', get_category, name='category' ),
    path('news/<int:news_id>/', view_news, name='view_news' ),
    path('news/add_news/', add_news, name='add_news'),
path('register/', register, name='register'),
path('login/', user_login, name='login'),

]
